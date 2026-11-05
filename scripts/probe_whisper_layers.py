"""What does each layer of Whisper's encoder know about *who* is speaking?

A small interpretability experiment on LibriSpeech test-clean, in three stages:

``extract``
    Run the Whisper encoder over a speaker-balanced subset of test-clean and
    save, for every 20 ms encoder frame, the hidden state after every block
    (plus the conv-stem output and the raw log-mel input), together with the
    frame's phone (from Montreal Forced Aligner TextGrids), speaker and gender.
    The same is done for a randomly initialised Whisper of the same shape as a
    control: whatever a probe finds there comes from the probe, not the model.

``probe``
    Train linear (softmax-regression) probes, written in NumPy, layer by layer:

    * phone identity (39 ARPAbet classes) -- speaker-disjoint split
    * speaker identity (40-way, closed set) -- utterance-disjoint split
    * speaker gender -- 5-fold speaker-disjoint cross-validation

``erase``
    A causal test at the encoder output (what the decoder cross-attends to).
    Fit LEACE (Belrose et al., 2023, closed form) to remove all *linearly*
    available speaker-identity information, then re-probe and re-transcribe.
    Controls: removing the same number of random directions, and removing
    gender only (rank 1).

Usage::

    python scripts/probe_whisper_layers.py all --model base.en \\
        --librispeech /path/LibriSpeech/test-clean \\
        --alignments /path/librispeech_alignments/test-clean \\
        --out results/probing/base.en

Requires ``openai-whisper`` and ``soundfile``. Phone alignments: Lugosch et al.,
"LibriSpeech Alignments", Zenodo record 2619474 (MFA TextGrids).
"""

from __future__ import annotations

import argparse
import json
import math
import re
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
import whisper
from whisper.normalizers import EnglishTextNormalizer

from aurora.speech import corpus_wer

SR = 16000
HOP = 320  # one encoder frame = 20 ms
PHONES = (
    "AA AE AH AO AW AY B CH D DH EH ER EY F G HH IH IY JH K L M N NG OW OY P R S SH "
    "T TH UH UW V W Y Z ZH"
).split()
PHONE_ID = {p: i for i, p in enumerate(PHONES)}
SIL = -1


# --------------------------------------------------------------------- data
def parse_textgrid(path: Path) -> dict[str, list[tuple[float, float, str]]]:
    tiers, name, cur = {}, None, None
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("name ="):
            name = line.split("=", 1)[1].strip().strip('"')
            tiers[name] = []
        elif line.startswith("xmin =") and name:
            cur = [float(line.split("=")[1])]
        elif line.startswith("xmax =") and cur is not None and len(cur) == 1:
            cur.append(float(line.split("=")[1]))
        elif line.startswith("text =") and cur is not None and len(cur) == 2:
            tiers[name].append(
                (cur[0], cur[1], line.split("=", 1)[1].strip().strip('"'))
            )
            cur = None
    return tiers


def frame_phones(phones: list[tuple[float, float, str]], n: int) -> np.ndarray:
    out = np.full(n, SIL, dtype=np.int16)
    t = (np.arange(n) + 0.5) * HOP / SR
    for a, b, p in phones:
        p = re.sub(r"\d", "", p.upper())
        if p in PHONE_ID:
            out[(t >= a) & (t < b)] = PHONE_ID[p]
    return out


def select_utterances(root: Path, align: Path, per_speaker: int):
    meta = root.parent / "SPEAKERS.TXT"
    gender = {}
    for line in meta.read_text().splitlines():
        if line.startswith(";"):
            continue
        f = [x.strip() for x in line.split("|")]
        if len(f) >= 3 and f[2] == "test-clean":
            gender[f[0]] = 0 if f[1] == "F" else 1
    trans = {}
    for t in root.rglob("*.trans.txt"):
        for line in t.read_text().splitlines():
            uid, txt = line.split(" ", 1)
            trans[uid] = txt
    utts = []
    for spk in sorted(gender, key=int):
        files = sorted((root / spk).rglob("*.flac"))
        picked = 0
        for f in files:
            tg = align / spk / f.parent.name / (f.stem + ".TextGrid")
            if not tg.exists():
                continue
            dur = sf.info(f).duration
            if dur > 29.5:
                continue
            utts.append(
                {
                    "id": f.stem,
                    "path": str(f),
                    "tg": str(tg),
                    "spk": spk,
                    "gender": gender[spk],
                    "text": trans[f.stem],
                    "dur": dur,
                }
            )
            picked += 1
            if picked == per_speaker:
                break
    return utts


# ------------------------------------------------------------------ extract
def encoder_states(model, mel: torch.Tensor) -> list[torch.Tensor]:
    """Hidden states: conv-stem output, after each block, after ln_post."""
    enc = model.encoder
    x = torch.nn.functional.gelu(enc.conv1(mel))
    x = torch.nn.functional.gelu(enc.conv2(x))
    x = x.permute(0, 2, 1)
    x = (x + enc.positional_embedding).to(x.dtype)
    states = [x]
    for block in enc.blocks:
        x = block(x)
        states.append(x)
    states.append(enc.ln_post(x))
    return states


def extract(args) -> None:
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    utts = select_utterances(
        Path(args.librispeech), Path(args.alignments), args.per_speaker
    )
    torch.manual_seed(0)
    model = whisper.load_model(args.model, device="cpu").eval()
    rand = (
        None if args.no_random else whisper.model.Whisper(model.dims).eval()
    )  # same shape, random weights
    n_layers = len(model.encoder.blocks)
    names = ["mel"] + ["conv"] + [f"L{i + 1}" for i in range(n_layers)] + ["out"]
    feats = {k: [] for k in names}
    rfeats = {k: [] for k in names[1:]}
    labels = {"phone": [], "spk": [], "gender": [], "utt": []}
    spk_index = {s: i for i, s in enumerate(sorted({u["spk"] for u in utts}, key=int))}
    t0 = time.time()
    for ui, u in enumerate(utts):
        audio, sr = sf.read(u["path"], dtype="float32")
        assert sr == SR
        n = min(1500, math.ceil(len(audio) / HOP))
        mel = whisper.log_mel_spectrogram(
            whisper.pad_or_trim(audio), n_mels=model.dims.n_mels
        )
        m = mel.numpy()[:, : 2 * n].T.reshape(n, -1)  # stack two 10 ms frames -> 20 ms
        feats["mel"].append(m.astype(np.float16))
        with torch.no_grad():
            for k, h in zip(names[1:], encoder_states(model, mel[None]), strict=True):
                feats[k].append(h[0, :n].numpy().astype(np.float16))
            if rand is not None:
                for k, h in zip(
                    names[1:], encoder_states(rand, mel[None]), strict=True
                ):
                    rfeats[k].append(h[0, :n].numpy().astype(np.float16))
        labels["phone"].append(frame_phones(parse_textgrid(Path(u["tg"]))["phones"], n))
        labels["spk"].append(np.full(n, spk_index[u["spk"]], np.int16))
        labels["gender"].append(np.full(n, u["gender"], np.int16))
        labels["utt"].append(np.full(n, ui, np.int16))
        if ui % 50 == 0:
            print(f"  {ui}/{len(utts)}  {time.time() - t0:.0f}s", flush=True)
    for k in list(feats):
        np.save(out / f"X_{k}.npy", np.concatenate(feats.pop(k)))
    for k in list(rfeats):
        if rfeats[k]:
            np.save(out / f"R_{k}.npy", np.concatenate(rfeats.pop(k)))
    for k, v in labels.items():
        np.save(out / f"y_{k}.npy", np.concatenate(v))
    (out / "utts.json").write_text(
        json.dumps({"layers": names, "utts": utts}, indent=1)
    )
    print(
        f"extracted {sum(len(x) for x in labels['utt'])} frames, {len(utts)} utterances"
    )


# -------------------------------------------------------------------- probe
def softmax_probe(
    Xtr, ytr, Xte, yte, k, epochs=12, lr=3e-3, wd=1e-4, batch=1024, seed=0
):
    """Multinomial logistic regression trained with Adam. Returns test accuracy."""
    rng = np.random.default_rng(seed)
    mu = Xtr.mean(0)
    sd = Xtr.std(0) + 1e-5
    Xtr = (Xtr - mu) / sd
    Xte = (Xte - mu) / sd
    d = Xtr.shape[1]
    W = np.zeros((d, k), np.float32)
    b = np.zeros(k, np.float32)
    mW, vW, mb, vb = (
        np.zeros_like(W),
        np.zeros_like(W),
        np.zeros_like(b),
        np.zeros_like(b),
    )
    step = 0
    for _ in range(epochs):
        order = rng.permutation(len(Xtr))
        for s in range(0, len(order), batch):
            idx = order[s : s + batch]
            x, y = Xtr[idx], ytr[idx]
            z = x @ W + b
            z -= z.max(1, keepdims=True)
            p = np.exp(z)
            p /= p.sum(1, keepdims=True)
            p[np.arange(len(y)), y] -= 1
            p /= len(y)
            gW = x.T @ p + wd * W
            gb = p.sum(0)
            step += 1
            for g, m, v, prm in ((gW, mW, vW, W), (gb, mb, vb, b)):
                m *= 0.9
                m += 0.1 * g
                v *= 0.999
                v += 0.001 * g * g
                prm -= (
                    lr * (m / (1 - 0.9**step)) / (np.sqrt(v / (1 - 0.999**step)) + 1e-8)
                )
    return float(((Xte @ W + b).argmax(1) == yte).mean())


def splits(out: Path):
    y = {
        k: np.load(out / f"y_{k}.npy").astype(np.int64)
        for k in ("phone", "spk", "gender", "utt")
    }
    meta = json.loads((out / "utts.json").read_text())
    speech = y["phone"] >= 0
    # speaker-disjoint test speakers for the phone probe: 4 F + 4 M, fixed
    g_of = {}
    for s, g in zip(y["spk"], y["gender"], strict=True):
        g_of[int(s)] = int(g)
    f_spk = [s for s in sorted(g_of) if g_of[s] == 0][::5][:4]
    m_spk = [s for s in sorted(g_of) if g_of[s] == 1][::5][:4]
    test_spk = np.isin(y["spk"], f_spk + m_spk)
    # speaker ID is utterance-disjoint: each speaker's last 3 utterances are test
    rank = {}
    per = {}
    for ui, u in enumerate(meta["utts"]):
        per.setdefault(u["spk"], []).append(ui)
    for ids in per.values():
        for r, ui in enumerate(ids):
            rank[ui] = r
    n_per = min(len(v) for v in per.values())
    utt_rank = np.array([rank[int(u)] for u in y["utt"]])
    spk_test = utt_rank >= n_per - 3
    # 5 speaker-disjoint folds for gender, each with 4 F + 4 M speakers
    fem = [s for s in sorted(g_of) if g_of[s] == 0]
    mal = [s for s in sorted(g_of) if g_of[s] == 1]
    folds = [fem[i::5] + mal[i::5] for i in range(5)]
    return y, speech, test_spk, spk_test, folds


def run_probes(Xget, y, speech, test_spk, spk_test, folds, sub=2):
    X = Xget()
    res = {}
    tr = speech & ~test_spk
    te = speech & test_spk
    tri = np.where(tr)[0][::sub]
    res["phone"] = softmax_probe(
        X[tri], y["phone"][tri], X[te], y["phone"][te], len(PHONES)
    )
    tr = speech & ~spk_test
    te = speech & spk_test
    tri = np.where(tr)[0][::sub]
    res["speaker"] = softmax_probe(X[tri], y["spk"][tri], X[te], y["spk"][te], 40)
    accs = []
    for f in folds:
        te = speech & np.isin(y["spk"], f)
        tri = np.where(speech & ~np.isin(y["spk"], f))[0][:: sub * 2]
        accs.append(
            softmax_probe(X[tri], y["gender"][tri], X[te], y["gender"][te], 2, epochs=6)
        )
    res["gender"] = float(np.mean(accs))
    res["gender_folds"] = accs
    return res


def chance(y, speech, test_spk, spk_test):
    def maj(tr, te, key):
        vals = np.bincount(y[key][tr])
        return float((y[key][te] == vals.argmax()).mean())

    return {
        "phone": maj(speech & ~test_spk, speech & test_spk, "phone"),
        "speaker": maj(speech & ~spk_test, speech & spk_test, "spk"),
        "gender": 0.5,
    }


def probe(args) -> None:
    out = Path(args.out)
    y, speech, test_spk, spk_test, folds = splits(out)
    layers = json.loads((out / "utts.json").read_text())["layers"]
    result = {
        "layers": layers,
        "chance": chance(y, speech, test_spk, spk_test),
        "n_frames": int(len(speech)),
        "n_speech_frames": int(speech.sum()),
        "trained": {},
        "random_init": {},
    }
    for L in layers:
        t0 = time.time()
        r = run_probes(
            lambda L=L: np.load(out / f"X_{L}.npy").astype(np.float32),
            y,
            speech,
            test_spk,
            spk_test,
            folds,
        )
        result["trained"][L] = r
        if L != "mel" and (out / f"R_{L}.npy").exists():
            result["random_init"][L] = run_probes(
                lambda L=L: np.load(out / f"R_{L}.npy").astype(np.float32),
                y,
                speech,
                test_spk,
                spk_test,
                folds,
            )
        print(
            f"  {L:>5}  phone {r['phone']:.3f}  speaker {r['speaker']:.3f}  "
            f"gender {r['gender']:.3f}   ({time.time() - t0:.0f}s)",
            flush=True,
        )
        (out / "probe.json").write_text(json.dumps(result, indent=1))


# -------------------------------------------------------------------- erase
class Eraser:
    """LEACE: x -> x - W^+ P W (x - mu); W = Sigma^{-1/2}, P onto col(W Sigma_xz)."""

    def __init__(
        self,
        X: np.ndarray,
        Z: np.ndarray | None = None,
        rank: int | None = None,
        seed: int = 0,
    ):
        X = X.astype(np.float64)
        self.mu = X.mean(0)
        Xc = X - self.mu
        S = Xc.T @ Xc / len(X)
        ev, V = np.linalg.eigh(S)
        keep = ev > ev.max() * 1e-8
        ev, V = ev[keep], V[:, keep]
        self.W = (V / np.sqrt(ev)) @ V.T
        self.Wp = (V * np.sqrt(ev)) @ V.T
        if Z is not None:
            Zc = Z - Z.mean(0)
            U, s, _ = np.linalg.svd(self.W @ (Xc.T @ Zc / len(X)), full_matrices=False)
            U = U[:, s > s.max() * 1e-6]
        else:  # control: the same number of random directions in whitened space
            rng = np.random.default_rng(seed)
            U, _ = np.linalg.qr(rng.standard_normal((X.shape[1], rank)))
        self.rank = U.shape[1]
        self.M = self.Wp @ U @ U.T @ self.W  # x -> x - (x - mu) @ M.T

    def __call__(self, X):
        Xd = X.astype(np.float64)
        return (Xd - (Xd - self.mu) @ self.M.T).astype(np.float32)


def erase(args) -> None:
    out = Path(args.out)
    y, speech, test_spk, spk_test, folds = splits(out)
    meta = json.loads((out / "utts.json").read_text())
    X = np.load(out / "X_out.npy").astype(np.float32)
    fit = speech & ~spk_test  # fit erasers on training utterances only
    Zs = np.eye(40)[y["spk"][fit]]
    Zg = np.eye(2)[y["gender"][fit]]
    erasers = {
        "none": None,
        "speaker_leace": Eraser(X[fit], Zs),
        "gender_leace": Eraser(X[fit], Zg),
    }
    erasers["random_same_rank"] = Eraser(
        X[fit], None, rank=erasers["speaker_leace"].rank
    )
    res = {
        "ranks": {k: (e.rank if e else 0) for k, e in erasers.items()},
        "probes": {},
        "wer": {},
    }
    for k, e in erasers.items():
        Xe = X if e is None else e(X)
        res["probes"][k] = run_probes(
            lambda Xe=Xe: Xe, y, speech, test_spk, spk_test, folds
        )
        print(f"  {k:>18}  rank {res['ranks'][k]:>3}  {res['probes'][k]}", flush=True)
        (out / "erase.json").write_text(json.dumps(res, indent=1))

    # transcription with the eraser applied to the encoder output
    model = whisper.load_model(args.model, device="cpu").eval()
    norm = EnglishTextNormalizer()
    opts = whisper.DecodingOptions(language="en", without_timestamps=True, fp16=False)
    n_per = min(
        sum(1 for u in meta["utts"] if u["spk"] == s)
        for s in {u["spk"] for u in meta["utts"]}
    )
    by_spk = {}
    for ui, u in enumerate(meta["utts"]):
        by_spk.setdefault(u["spk"], []).append(ui)
    test_utts = [ui for ids in by_spk.values() for ui in ids[n_per - 3 : n_per]]
    state = {"n": 0, "e": None}

    def hook(_m, _i, o):
        if state["e"] is None:
            return o
        o = o.clone()
        o[0, : state["n"]] = torch.from_numpy(state["e"](o[0, : state["n"]].numpy()))
        return o

    model.encoder.ln_post.register_forward_hook(hook)
    refs = [norm(meta["utts"][ui]["text"]) for ui in test_utts]
    for k, e in erasers.items():
        hyps = []
        t0 = time.time()
        for ui in test_utts:
            u = meta["utts"][ui]
            audio, _ = sf.read(u["path"], dtype="float32")
            state["n"] = min(1500, math.ceil(len(audio) / HOP))
            state["e"] = e
            mel = whisper.log_mel_spectrogram(
                whisper.pad_or_trim(audio), n_mels=model.dims.n_mels
            )
            with torch.no_grad():
                hyps.append(norm(whisper.decode(model, mel, opts).text))
        res["wer"][k] = float(corpus_wer(refs, hyps))
        res.setdefault("examples", {})[k] = hyps[:3]
        print(
            f"  WER {k:>18}: {res['wer'][k] * 100:.2f} %  ({time.time() - t0:.0f}s)",
            flush=True,
        )
        (out / "erase.json").write_text(json.dumps(res, indent=1))
    res["n_wer_utts"] = len(test_utts)
    res["refs_examples"] = refs[:3]
    (out / "erase.json").write_text(json.dumps(res, indent=1))


def erase_cv(args) -> None:
    """Gender erasure that respects the speaker-disjoint folds.

    The eraser for each fold is fitted on that fold's training speakers only,
    so the held-out speakers are unseen by both the eraser and the probe.
    """
    out = Path(args.out)
    y, speech, *_rest, folds = splits(out)
    X = np.load(out / "X_out.npy").astype(np.float32)
    res = {"gender_leace_cv": [], "speaker_leace_cv": [], "none": []}
    for f in folds:
        held = np.isin(y["spk"], f)
        fit = speech & ~held
        te = speech & held
        tri = np.where(fit)[0][::4]
        res["none"].append(
            softmax_probe(X[tri], y["gender"][tri], X[te], y["gender"][te], 2, epochs=6)
        )
        for key, Z in (
            ("gender_leace_cv", np.eye(2)[y["gender"][fit]]),
            ("speaker_leace_cv", np.eye(40)[y["spk"][fit]]),
        ):
            e = Eraser(X[fit], Z)
            Xe = e(X)
            res[key].append(
                softmax_probe(
                    Xe[tri], y["gender"][tri], Xe[te], y["gender"][te], 2, epochs=6
                )
            )
    res = {k: {"mean": float(np.mean(v)), "folds": v} for k, v in res.items()}
    (out / "erase_cv.json").write_text(json.dumps(res, indent=1))
    print(json.dumps({k: round(v["mean"], 4) for k, v in res.items()}))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("stage", choices=["extract", "probe", "erase", "erase_cv", "all"])
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--librispeech", required=True)
    ap.add_argument("--alignments", required=True)
    ap.add_argument("--per-speaker", type=int, default=10)
    ap.add_argument("--out", required=True)
    ap.add_argument(
        "--no-random", action="store_true", help="skip the random-init control"
    )
    args = ap.parse_args()
    for stage in ("extract", "probe", "erase", "erase_cv"):
        if args.stage in (stage, "all"):
            print(f"== {stage}", flush=True)
            globals()[stage](args)


if __name__ == "__main__":
    main()

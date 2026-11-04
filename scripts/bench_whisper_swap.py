"""Swap Aurora's hand-written front end into Whisper and measure WER.

For each LibriSpeech utterance we decode the *same* Whisper model twice:
once on Whisper's own ``log_mel_spectrogram`` (torch STFT + librosa mel) and
once on ``aurora.audio.log_mel_whisper`` (Aurora framing, window, DFT, mel).
If the DSP is right, the two transcripts should agree and the corpus WER
should match. Results go to ``results/whisper_swap.{md,json,csv}``.

Usage::

    python scripts/bench_whisper_swap.py --librispeech LibriSpeech/test-clean \
        --model base.en --n-utts 200

Requires ``pip install openai-whisper soundfile``. CPU is fine but slow.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
import whisper
from whisper.normalizers import EnglishTextNormalizer

from aurora.audio import log_mel_whisper
from aurora.speech import corpus_wer, wer


def load_utterances(root: Path, limit: int, max_seconds: float = 30.0):
    """Yield ``(utt_id, audio, reference)`` from LibriSpeech's trans.txt files."""
    utts = []
    for trans in sorted(root.rglob("*.trans.txt")):
        for line in trans.read_text().splitlines():
            utt_id, text = line.split(" ", 1)
            utts.append((utt_id, trans.parent / f"{utt_id}.flac", text))
    utts.sort()
    out = []
    for utt_id, path, text in utts:
        audio, sr = sf.read(path, dtype="float32")
        assert sr == 16000
        if len(audio) / sr > max_seconds:
            continue
        out.append((utt_id, audio, text))
        if len(out) >= limit:
            break
    return out


def decode(model, mel: np.ndarray, options) -> str:
    mel_t = torch.from_numpy(np.ascontiguousarray(mel, dtype=np.float32)).to(
        model.device
    )
    return whisper.decode(model, mel_t, options).text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--librispeech", required=True)
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--n-utts", type=int, default=200)
    ap.add_argument("--out", default="results")
    args = ap.parse_args()

    torch.set_num_threads(max(1, torch.get_num_threads()))
    model = whisper.load_model(args.model, device="cpu")
    options = whisper.DecodingOptions(
        language="en", without_timestamps=True, fp16=False
    )
    norm = EnglishTextNormalizer()
    n_mels = model.dims.n_mels

    utts = load_utterances(Path(args.librispeech), args.n_utts)
    print(f"{len(utts)} utterances, model={args.model}, n_mels={n_mels}")

    rows = []
    t0 = time.time()
    for i, (utt_id, audio, ref) in enumerate(utts, 1):
        padded = whisper.pad_or_trim(audio)
        mel_ref = whisper.log_mel_spectrogram(padded, n_mels=n_mels).numpy()
        mel_aur = log_mel_whisper(audio.astype(np.float64), n_mels=n_mels)
        feat_err = float(np.max(np.abs(mel_ref - mel_aur)))

        hyp_ref = decode(model, mel_ref, options)
        hyp_aur = decode(model, mel_aur, options)

        r, h1, h2 = norm(ref), norm(hyp_ref), norm(hyp_aur)
        rows.append(
            {
                "utt_id": utt_id,
                "seconds": round(len(audio) / 16000, 2),
                "feat_max_abs_err": feat_err,
                "ref": r,
                "hyp_whisper": h1,
                "hyp_aurora": h2,
                "wer_whisper": wer(r, h1),
                "wer_aurora": wer(r, h2),
                "identical": h1 == h2,
            }
        )
        if i % 10 == 0 or i == len(utts):
            el = time.time() - t0
            print(
                f"[{i}/{len(utts)}] {el:.0f}s elapsed, ~{el / i * (len(utts) - i):.0f}s left",
                flush=True,
            )

    out = Path(args.out)
    out.mkdir(exist_ok=True)
    with (out / "whisper_swap.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    refs = [r["ref"] for r in rows]
    summary = {
        "model": args.model,
        "n_utts": len(rows),
        "total_seconds": round(sum(r["seconds"] for r in rows), 1),
        "corpus_wer_whisper_frontend": corpus_wer(
            refs, [r["hyp_whisper"] for r in rows]
        ),
        "corpus_wer_aurora_frontend": corpus_wer(refs, [r["hyp_aurora"] for r in rows]),
        "transcripts_identical": sum(r["identical"] for r in rows),
        "feature_max_abs_err": max(r["feat_max_abs_err"] for r in rows),
        "feature_mean_max_abs_err": float(
            np.mean([r["feat_max_abs_err"] for r in rows])
        ),
    }
    (out / "whisper_swap.json").write_text(json.dumps(summary, indent=2))

    md = [
        f"Model: `{args.model}` · {summary['n_utts']} LibriSpeech test-clean utterances "
        f"({summary['total_seconds']:.0f} s of audio), greedy decoding, CPU.",
        "",
        "| Front end | Corpus WER |",
        "|---|---|",
        "| Whisper's own (`torch.stft` + librosa mel) | "
        f"{summary['corpus_wer_whisper_frontend'] * 100:.2f} % |",
        "| Aurora (`aurora.audio.log_mel_whisper`) | "
        f"{summary['corpus_wer_aurora_frontend'] * 100:.2f} % |",
        "",
        f"Identical transcripts: {summary['transcripts_identical']} / {summary['n_utts']}. "
        f"Max feature error across all utterances: {summary['feature_max_abs_err']:.2e} "
        f"(mean of per-utterance max: {summary['feature_mean_max_abs_err']:.2e}).",
    ]
    (out / "whisper_swap.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()

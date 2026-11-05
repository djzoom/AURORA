"""Numerical alignment of Aurora's hand-written DSP against reference libraries.

Runs on real LibriSpeech audio and reports, per primitive, the maximum absolute
and relative error between Aurora and librosa / numpy / whisper. Writes a
Markdown table to ``results/alignment.md`` and raw numbers to
``results/alignment.json``.

Usage::

    python scripts/bench_alignment.py --librispeech /path/to/LibriSpeech/test-clean

Requires the optional stacks: ``pip install librosa openai-whisper soundfile``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import whisper

from aurora.audio import (
    dct_ii,
    log_mel_whisper,
    mel_filterbank,
    mel_spectrogram,
    mfcc,
    power_to_db,
    rfft,
    stft,
    whisper_mel_filterbank,
)


def _err(a: np.ndarray, b: np.ndarray) -> dict:
    a = np.asarray(a)
    b = np.asarray(b)
    if not (np.iscomplexobj(a) or np.iscomplexobj(b)):
        a, b = a.astype(np.float64), b.astype(np.float64)
    abs_err = np.max(np.abs(a - b))
    rel_err = abs_err / max(np.max(np.abs(b)), 1e-300)
    return {
        "max_abs": float(abs_err),
        "max_rel": float(rel_err),
        "shape": list(a.shape),
    }


def iter_flacs(root: Path, limit: int):
    files = sorted(root.rglob("*.flac"))[:limit]
    for f in files:
        audio, sr = sf.read(f, dtype="float32")
        assert sr == 16000, f
        yield f, audio.astype(np.float64)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--librispeech", required=True)
    ap.add_argument("--n-files", type=int, default=20)
    ap.add_argument("--out", default="results")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(exist_ok=True)
    rows: dict[str, list[dict]] = {}

    def add(name: str, e: dict):
        rows.setdefault(name, []).append(e)

    # --- filterbanks (data-independent) ------------------------------------
    fb_htk = mel_filterbank(80, 1024, 16000)
    fb_htk_ref = librosa.filters.mel(
        sr=16000, n_fft=1024, n_mels=80, htk=True, norm=None
    )
    add("mel_filterbank (HTK, norm=None) vs librosa", _err(fb_htk, fb_htk_ref))

    fb_sl = mel_filterbank(80, 400, 16000, htk=False, norm="slaney")
    fb_sl_ref = librosa.filters.mel(sr=16000, n_fft=400, n_mels=80)
    add("mel_filterbank (Slaney) vs librosa", _err(fb_sl, fb_sl_ref))

    whisper_fb = whisper.audio.mel_filters("cpu", 80).numpy()
    add(
        "whisper_mel_filterbank vs whisper mel_filters.npz",
        _err(whisper_mel_filterbank(80), whisper_fb),
    )

    # --- per-file primitives --------------------------------------------------
    n = 0
    for _, x in iter_flacs(Path(args.librispeech), args.n_files):
        n += 1
        # FFT on one 1024-sample frame
        frame = x[:1024]
        add("rfft (1024) vs numpy.fft.rfft", _err(rfft(frame), np.fft.rfft(frame)))

        # STFT magnitude (n_fft=1024, hop=256, periodic hann, center/reflect)
        S = np.abs(stft(x, n_fft=1024, hop_length=256)).T
        # librosa >= 0.10 zero-pads at the edges by default; Aurora (like Whisper)
        # reflect-pads, so ask librosa for the same convention.
        S_ref = np.abs(
            librosa.stft(
                x,
                n_fft=1024,
                hop_length=256,
                window="hann",
                center=True,
                pad_mode="reflect",
            )
        )
        add("|STFT| (1024/256) vs librosa.stft", _err(S, S_ref))

        # Mel spectrogram (HTK, unit-peak) — librosa with matching options
        M = mel_spectrogram(x, 16000, n_fft=1024, hop_length=256, n_mels=80).T
        M_ref = librosa.feature.melspectrogram(
            y=x,
            sr=16000,
            n_fft=1024,
            hop_length=256,
            n_mels=80,
            htk=True,
            norm=None,
            power=2.0,
            pad_mode="reflect",
        )
        add("mel_spectrogram (HTK) vs librosa.melspectrogram", _err(M, M_ref))

        # MFCC: both from the same log-mel definition (10*log10, no top_db) + ortho DCT-II
        C = mfcc(x, 16000, n_mfcc=13, n_fft=1024, hop_length=256, n_mels=80).T
        C_ref = librosa.feature.mfcc(
            S=librosa.power_to_db(M_ref, top_db=None),
            n_mfcc=13,
            dct_type=2,
            norm="ortho",
        )
        add("mfcc (13) vs librosa.mfcc", _err(C, C_ref))

        # DCT-II alone
        add(
            "dct_ii (ortho) vs scipy via librosa",
            _err(dct_ii(power_to_db(M.T, top_db=None))[:, :13], C_ref.T),
        )

        # Whisper front end, end to end (float32 reference)
        W = log_mel_whisper(x)
        W_ref = whisper.log_mel_spectrogram(
            whisper.pad_or_trim(x.astype(np.float32)), n_mels=80
        ).numpy()
        add("log_mel_whisper vs whisper.log_mel_spectrogram", _err(W, W_ref))

    # --- aggregate --------------------------------------------------------------
    table = []
    for name, es in rows.items():
        table.append(
            {
                "primitive": name,
                "n": len(es),
                "max_abs": max(e["max_abs"] for e in es),
                "max_rel": max(e["max_rel"] for e in es),
                "shape": es[0]["shape"],
            }
        )
    (out / "alignment.json").write_text(json.dumps(table, indent=2))

    md = [
        "| Primitive | Files | Max abs error | Max rel error |",
        "|---|---|---|---|",
    ]
    for r in table:
        md.append(
            f"| `{r['primitive']}` | {r['n']} | {r['max_abs']:.2e} | {r['max_rel']:.2e} |"
        )
    (out / "alignment.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    print(f"\n{n} LibriSpeech files checked. Written to {out}/alignment.{{md,json}}")


if __name__ == "__main__":
    main()

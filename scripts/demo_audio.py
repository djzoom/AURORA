#!/usr/bin/env python3
"""Audio Core demo: generate a chirp, extract features, print a tiny ASCII
spectrogram — all using Aurora's from-scratch DSP.

Run:
    python scripts/demo_audio.py
"""

from __future__ import annotations

import numpy as np

from aurora.audio import (
    chirp,
    magnitude_spectrogram,
    mel_spectrogram,
    mfcc,
    power_to_db,
)

SR = 16000


def ascii_spectrogram(db: np.ndarray, width: int = 60, height: int = 16) -> str:
    """Render a (frames, freq) dB spectrogram as ASCII art."""
    ramp = " .:-=+*#%@"
    # Downsample to the terminal box.
    f_idx = np.linspace(0, db.shape[0] - 1, width).astype(int)
    b_idx = np.linspace(0, db.shape[1] - 1, height).astype(int)
    grid = db[np.ix_(f_idx, b_idx)].T[::-1]  # low freq at bottom
    lo, hi = grid.min(), grid.max()
    norm = (grid - lo) / (hi - lo + 1e-9)
    levels = (norm * (len(ramp) - 1)).astype(int)
    return "\n".join("".join(ramp[v] for v in row) for row in levels)


def main() -> None:
    print("Aurora Audio Core demo\n" + "=" * 40)
    x = chirp(f0=200.0, f1=6000.0, duration=2.0, sample_rate=SR)
    print(f"signal:            {x.shape[0]} samples @ {SR} Hz "
          f"({x.shape[0] / SR:.1f}s linear chirp 200->6000 Hz)")

    mag = magnitude_spectrogram(x, n_fft=1024, hop_length=256)
    print(f"magnitude STFT:    {mag.shape}  (frames, freq bins)")

    mel = mel_spectrogram(x, SR, n_fft=1024, hop_length=256, n_mels=80)
    print(f"mel spectrogram:   {mel.shape}  (frames, mels)")

    coeffs = mfcc(x, SR, n_mfcc=13, n_fft=1024, hop_length=256)
    print(f"MFCC:              {coeffs.shape}  (frames, coeffs)")

    print("\nASCII spectrogram (the sweep should rise left→right):\n")
    print(ascii_spectrogram(power_to_db(mag**2)))


if __name__ == "__main__":
    main()

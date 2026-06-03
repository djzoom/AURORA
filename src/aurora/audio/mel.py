"""Mel scale, mel filterbank, and mel spectrogram — from scratch.

The mel scale warps frequency to better match human pitch perception. We build
the triangular filterbank by hand rather than calling ``librosa.filters.mel``
so the math is fully visible.

We use the HTK mel formula by default:

    mel(f) = 2595 * log10(1 + f / 700)
"""

from __future__ import annotations

import numpy as np

from .stft import power_spectrogram
from .transforms import fft_frequencies

__all__ = [
    "hz_to_mel",
    "mel_to_hz",
    "mel_filterbank",
    "mel_spectrogram",
    "power_to_db",
]


def hz_to_mel(freq: np.ndarray | float) -> np.ndarray | float:
    """Convert frequency in Hz to the HTK mel scale."""
    return 2595.0 * np.log10(1.0 + np.asarray(freq, dtype=np.float64) / 700.0)


def mel_to_hz(mel: np.ndarray | float) -> np.ndarray | float:
    """Convert HTK mel values back to Hz."""
    return 700.0 * (10.0 ** (np.asarray(mel, dtype=np.float64) / 2595.0) - 1.0)


def mel_filterbank(
    n_mels: int,
    n_fft: int,
    sample_rate: int,
    fmin: float = 0.0,
    fmax: float | None = None,
) -> np.ndarray:
    """Construct an ``(n_mels, n_fft // 2 + 1)`` triangular mel filterbank.

    Each filter is a triangle in the frequency domain whose peak sits at one
    of ``n_mels`` points equally spaced on the mel scale between ``fmin`` and
    ``fmax``. The filterbank maps a linear-frequency power spectrum onto mel
    bands by a single matrix multiply.
    """
    if fmax is None:
        fmax = sample_rate / 2.0

    # n_mels + 2 mel points => n_mels triangles sharing edges.
    mel_min, mel_max = hz_to_mel(fmin), hz_to_mel(fmax)
    mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
    hz_points = mel_to_hz(mel_points)

    bin_freqs = fft_frequencies(sample_rate, n_fft)  # (n_fft//2 + 1,)
    fb = np.zeros((n_mels, bin_freqs.shape[0]))

    for m in range(n_mels):
        left, center, right = hz_points[m], hz_points[m + 1], hz_points[m + 2]
        # Rising edge from left -> center.
        rising = (bin_freqs - left) / (center - left)
        # Falling edge from center -> right.
        falling = (right - bin_freqs) / (right - center)
        fb[m] = np.clip(np.minimum(rising, falling), 0.0, None)
    return fb


def mel_spectrogram(
    signal: np.ndarray,
    sample_rate: int,
    n_fft: int = 1024,
    hop_length: int | None = None,
    n_mels: int = 80,
    fmin: float = 0.0,
    fmax: float | None = None,
    **stft_kwargs,
) -> np.ndarray:
    """Mel spectrogram of shape ``(n_frames, n_mels)``."""
    power = power_spectrogram(
        signal, n_fft=n_fft, hop_length=hop_length, **stft_kwargs
    )  # (n_frames, n_fft//2 + 1)
    fb = mel_filterbank(n_mels, n_fft, sample_rate, fmin, fmax)
    return power @ fb.T


def power_to_db(
    spectrogram: np.ndarray, ref: float = 1.0, top_db: float | None = 80.0
) -> np.ndarray:
    """Convert a power spectrogram to decibels (10 * log10), with a floor."""
    spectrogram = np.asarray(spectrogram, dtype=np.float64)
    amin = 1e-10
    db = 10.0 * np.log10(np.maximum(amin, spectrogram))
    db -= 10.0 * np.log10(np.maximum(amin, ref))
    if top_db is not None:
        db = np.maximum(db, db.max() - top_db)
    return db

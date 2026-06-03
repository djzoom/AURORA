"""Mel-Frequency Cepstral Coefficients and the DCT they rely on.

MFCCs are the classic compact representation of timbre used by speech and
music systems. We compute them as

    MFCC = DCT-II( log( mel_spectrogram ) )

and we implement the orthonormal DCT-II from its definition rather than
importing ``scipy.fftpack.dct``.
"""

from __future__ import annotations

import numpy as np

from .mel import mel_spectrogram, power_to_db

__all__ = ["dct_ii", "mfcc"]


def dct_ii(x: np.ndarray, norm: str = "ortho") -> np.ndarray:
    """Type-II DCT along the last axis.

        y[k] = sum_{n} x[n] * cos(pi/N * (n + 1/2) * k)

    With ``norm="ortho"`` the transform is scaled to be orthonormal, matching
    ``scipy.fftpack.dct(..., type=2, norm="ortho")``.
    """
    x = np.asarray(x, dtype=np.float64)
    n = x.shape[-1]
    k = np.arange(n)
    # Basis[k, m] = cos(pi/N * (m + 1/2) * k).
    basis = np.cos(np.pi / n * np.outer(k, k + 0.5))
    y = x @ basis.T

    if norm == "ortho":
        scale = np.full(n, np.sqrt(2.0 / n))
        scale[0] = np.sqrt(1.0 / n)
        y = y * scale
    return y


def mfcc(
    signal: np.ndarray,
    sample_rate: int,
    n_mfcc: int = 13,
    n_fft: int = 1024,
    hop_length: int | None = None,
    n_mels: int = 80,
    fmin: float = 0.0,
    fmax: float | None = None,
    **stft_kwargs,
) -> np.ndarray:
    """Compute ``n_mfcc`` MFCCs per frame -> shape ``(n_frames, n_mfcc)``."""
    mel = mel_spectrogram(
        signal,
        sample_rate,
        n_fft=n_fft,
        hop_length=hop_length,
        n_mels=n_mels,
        fmin=fmin,
        fmax=fmax,
        **stft_kwargs,
    )
    log_mel = power_to_db(mel, top_db=None)
    coeffs = dct_ii(log_mel, norm="ortho")
    return coeffs[:, :n_mfcc]

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


# Slaney's Auditory Toolbox mel scale: linear below 1 kHz, logarithmic above.
# This is the scale librosa uses by default (``htk=False``) and therefore the
# one baked into Whisper's ``mel_filters.npz``. Constants follow Slaney (1998).
_SLANEY_F_SP = 200.0 / 3.0  # Hz per mel in the linear region
_SLANEY_MIN_LOG_HZ = 1000.0  # where the log region starts
_SLANEY_MIN_LOG_MEL = _SLANEY_MIN_LOG_HZ / _SLANEY_F_SP
_SLANEY_LOGSTEP = np.log(6.4) / 27.0  # 27 mels span 1 kHz -> 6.4 kHz


def hz_to_mel_slaney(freq: np.ndarray | float) -> np.ndarray | float:
    """Convert Hz to the Slaney mel scale (linear < 1 kHz, log above)."""
    f = np.asarray(freq, dtype=np.float64)
    mels = f / _SLANEY_F_SP
    log_region = f >= _SLANEY_MIN_LOG_HZ
    safe = np.where(log_region, f, _SLANEY_MIN_LOG_HZ)
    mels = np.where(
        log_region,
        _SLANEY_MIN_LOG_MEL + np.log(safe / _SLANEY_MIN_LOG_HZ) / _SLANEY_LOGSTEP,
        mels,
    )
    return mels


def mel_to_hz_slaney(mel: np.ndarray | float) -> np.ndarray | float:
    """Convert Slaney mel values back to Hz."""
    m = np.asarray(mel, dtype=np.float64)
    freqs = _SLANEY_F_SP * m
    log_region = m >= _SLANEY_MIN_LOG_MEL
    freqs = np.where(
        log_region,
        _SLANEY_MIN_LOG_HZ * np.exp(_SLANEY_LOGSTEP * (m - _SLANEY_MIN_LOG_MEL)),
        freqs,
    )
    return freqs


def mel_filterbank(
    n_mels: int,
    n_fft: int,
    sample_rate: int,
    fmin: float = 0.0,
    fmax: float | None = None,
    htk: bool = True,
    norm: str | None = None,
) -> np.ndarray:
    """Construct an ``(n_mels, n_fft // 2 + 1)`` triangular mel filterbank.

    Each filter is a triangle in the frequency domain whose peak sits at one
    of ``n_mels`` points equally spaced on the mel scale between ``fmin`` and
    ``fmax``. The filterbank maps a linear-frequency power spectrum onto mel
    bands by a single matrix multiply.

    Parameters
    ----------
    htk : use the HTK mel formula (Aurora's default). ``False`` selects the
        Slaney scale used by librosa and Whisper.
    norm : ``None`` for unit-peak triangles, or ``"slaney"`` to scale each
        triangle to unit area (librosa's default). ``htk=False, norm="slaney"``
        reproduces ``librosa.filters.mel`` and Whisper's filterbank exactly.
    """
    if fmax is None:
        fmax = sample_rate / 2.0

    to_mel, to_hz = (
        (hz_to_mel, mel_to_hz) if htk else (hz_to_mel_slaney, mel_to_hz_slaney)
    )

    # n_mels + 2 mel points => n_mels triangles sharing edges.
    mel_min, mel_max = to_mel(fmin), to_mel(fmax)
    mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
    hz_points = to_hz(mel_points)

    bin_freqs = fft_frequencies(sample_rate, n_fft)  # (n_fft//2 + 1,)
    fb = np.zeros((n_mels, bin_freqs.shape[0]))

    for m in range(n_mels):
        left, center, right = hz_points[m], hz_points[m + 1], hz_points[m + 2]
        # Rising edge from left -> center.
        rising = (bin_freqs - left) / (center - left)
        # Falling edge from center -> right.
        falling = (right - bin_freqs) / (right - center)
        fb[m] = np.clip(np.minimum(rising, falling), 0.0, None)

    if norm == "slaney":
        # Unit-area normalisation: 2 / (bandwidth of each triangle in Hz).
        enorm = 2.0 / (hz_points[2 : n_mels + 2] - hz_points[:n_mels])
        fb *= enorm[:, None]
    elif norm is not None:
        raise ValueError(f"unknown norm {norm!r}; use None or 'slaney'")
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
    )  # (n_frames, fft_len//2 + 1)
    # The STFT zero-pads non-power-of-two n_fft up to the next power of two
    # (our radix-2 FFT requires it), so derive the actual FFT grid from the
    # spectrogram itself; e.g. Whisper's n_fft=400 is computed on a 512 grid.
    fft_len = 2 * (power.shape[1] - 1)
    fb = mel_filterbank(n_mels, fft_len, sample_rate, fmin, fmax)
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

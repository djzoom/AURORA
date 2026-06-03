"""Window functions implemented from scratch.

Windowing tapers each STFT frame to reduce spectral leakage. We implement the
cosine-sum windows directly from their definitions instead of importing
``scipy.signal.get_window`` so the Audio Core has no DSP dependencies.

The ``periodic`` flag (a.k.a. "DFT-even") follows the same convention as
NumPy/SciPy: a periodic window of length N is the first N samples of the
symmetric window of length N+1, which is the correct choice for spectral
analysis (STFT) because it makes the window seamlessly tile.
"""

from __future__ import annotations

import numpy as np

__all__ = ["hann", "hamming", "blackman", "get_window"]


def _cosine_sum(coeffs: list[float], length: int, periodic: bool) -> np.ndarray:
    """Generic generalized-cosine window: sum_k (-1)^k a_k cos(2*pi*k*n/M)."""
    if length <= 0:
        return np.zeros(0)
    if length == 1:
        return np.ones(1)
    denom = length if periodic else length - 1
    n = np.arange(length)
    w = np.zeros(length)
    for k, a in enumerate(coeffs):
        w += ((-1) ** k) * a * np.cos(2 * np.pi * k * n / denom)
    return w


def hann(length: int, periodic: bool = True) -> np.ndarray:
    """Hann window: 0.5 - 0.5*cos(2*pi*n/M)."""
    return _cosine_sum([0.5, 0.5], length, periodic)


def hamming(length: int, periodic: bool = True) -> np.ndarray:
    """Hamming window: 0.54 - 0.46*cos(2*pi*n/M)."""
    return _cosine_sum([0.54, 0.46], length, periodic)


def blackman(length: int, periodic: bool = True) -> np.ndarray:
    """Blackman window (classic 0.42/0.5/0.08 three-term cosine sum)."""
    return _cosine_sum([0.42, 0.5, 0.08], length, periodic)


_WINDOWS = {"hann": hann, "hamming": hamming, "blackman": blackman}


def get_window(name: str, length: int, periodic: bool = True) -> np.ndarray:
    """Look up a window by name (``"hann"``, ``"hamming"``, ``"blackman"``)."""
    try:
        return _WINDOWS[name](length, periodic)
    except KeyError as exc:
        raise ValueError(
            f"unknown window {name!r}; choose from {sorted(_WINDOWS)}"
        ) from exc

"""Short-Time Fourier Transform and spectrograms, built on our own FFT.

The STFT slides a window across the signal, takes the FFT of each frame, and
stacks the results into a time-frequency matrix. Everything here is built on
:mod:`aurora.audio.transforms` and :mod:`aurora.audio.windows` — no SciPy,
no librosa.
"""

from __future__ import annotations

import numpy as np

from .transforms import next_power_of_two, rfft
from .windows import get_window

__all__ = ["frame_signal", "stft", "magnitude_spectrogram", "power_spectrogram"]


def frame_signal(
    signal: np.ndarray,
    frame_length: int,
    hop_length: int,
    center: bool = True,
) -> np.ndarray:
    """Slice ``signal`` into overlapping frames.

    Parameters
    ----------
    signal : 1-D array
    frame_length : samples per frame
    hop_length : samples between successive frame starts
    center : if True, reflect-pad the signal by ``frame_length // 2`` on both
        ends so frame ``t`` is centered at sample ``t * hop_length`` (the
        librosa convention).

    Returns
    -------
    frames : array of shape ``(n_frames, frame_length)``.
    """
    signal = np.asarray(signal, dtype=np.float64)
    if center:
        pad = frame_length // 2
        signal = np.pad(signal, pad, mode="reflect")

    if signal.shape[0] < frame_length:
        signal = np.pad(signal, (0, frame_length - signal.shape[0]))

    n_frames = 1 + (signal.shape[0] - frame_length) // hop_length
    # Build the frame matrix with stride tricks to avoid a Python loop.
    idx = np.arange(frame_length)[None, :] + hop_length * np.arange(n_frames)[:, None]
    return signal[idx]


def stft(
    signal: np.ndarray,
    n_fft: int = 1024,
    hop_length: int | None = None,
    window: str = "hann",
    center: bool = True,
) -> np.ndarray:
    """Short-Time Fourier Transform.

    Returns a complex array of shape ``(n_frames, n_fft // 2 + 1)`` — one
    ``rfft`` per windowed frame.
    """
    if hop_length is None:
        hop_length = n_fft // 4

    win = get_window(window, n_fft, periodic=True)
    frames = frame_signal(signal, n_fft, hop_length, center=center) * win

    # rfft requires a power-of-two length; n_fft normally is, but guard anyway.
    target = next_power_of_two(n_fft)
    spectra = []
    for frame in frames:
        if target != n_fft:
            frame = np.pad(frame, (0, target - n_fft))
        spectra.append(rfft(frame))
    return np.asarray(spectra)


def magnitude_spectrogram(signal: np.ndarray, **kwargs) -> np.ndarray:
    """Magnitude (|STFT|) spectrogram."""
    return np.abs(stft(signal, **kwargs))


def power_spectrogram(signal: np.ndarray, **kwargs) -> np.ndarray:
    """Power (|STFT|^2) spectrogram."""
    return np.abs(stft(signal, **kwargs)) ** 2

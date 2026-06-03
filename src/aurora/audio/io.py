"""Minimal WAV reader/writer and test-signal generators.

We parse the RIFF/WAVE container by hand with :mod:`struct` so the Audio Core
can load audio without ``soundfile`` or ``scipy.io.wavfile``. Only
uncompressed PCM (8/16/24/32-bit int and 32-bit float) is supported, which
covers essentially every dataset we care about (LibriSpeech, etc.).
"""

from __future__ import annotations

import wave

import numpy as np

__all__ = ["read_wav", "write_wav", "sine", "chirp"]


def read_wav(path: str) -> tuple[np.ndarray, int]:
    """Read a PCM WAV file into ``(samples, sample_rate)``.

    Returns float64 samples in ``[-1, 1]``. Multi-channel audio is downmixed
    to mono by averaging channels.
    """
    with wave.open(path, "rb") as wf:
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        sample_rate = wf.getframerate()
        raw = wf.readframes(wf.getnframes())

    dtype_map = {1: np.uint8, 2: np.int16, 4: np.int32}
    if sample_width not in dtype_map:
        raise ValueError(f"unsupported sample width: {sample_width} bytes")

    data = np.frombuffer(raw, dtype=dtype_map[sample_width]).astype(np.float64)
    if sample_width == 1:  # 8-bit PCM is unsigned, centered at 128.
        data = (data - 128.0) / 128.0
    else:
        data = data / float(2 ** (8 * sample_width - 1))

    if n_channels > 1:
        data = data.reshape(-1, n_channels).mean(axis=1)
    return data, sample_rate


def write_wav(path: str, samples: np.ndarray, sample_rate: int) -> None:
    """Write float samples in ``[-1, 1]`` to a 16-bit PCM mono WAV file."""
    samples = np.asarray(samples, dtype=np.float64)
    clipped = np.clip(samples, -1.0, 1.0)
    pcm = (clipped * 32767.0).astype("<i2")  # little-endian int16
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm.tobytes())


def sine(
    freq: float, duration: float, sample_rate: int = 16000, amplitude: float = 1.0
) -> np.ndarray:
    """Generate a pure sine tone."""
    t = np.arange(int(duration * sample_rate)) / sample_rate
    return amplitude * np.sin(2 * np.pi * freq * t)


def chirp(
    f0: float,
    f1: float,
    duration: float,
    sample_rate: int = 16000,
    amplitude: float = 1.0,
) -> np.ndarray:
    """Generate a linear chirp sweeping from ``f0`` to ``f1`` Hz."""
    t = np.arange(int(duration * sample_rate)) / sample_rate
    k = (f1 - f0) / duration
    phase = 2 * np.pi * (f0 * t + 0.5 * k * t * t)
    return amplitude * np.sin(phase)

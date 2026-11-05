"""Whisper's log-mel front end, rebuilt from Aurora's own primitives.

OpenAI's Whisper turns audio into an ``(n_mels, 3000)`` log-mel matrix with a
very specific recipe (``whisper/audio.py``):

1. pad/trim the waveform to exactly 30 s at 16 kHz (480 000 samples);
2. STFT with a 400-sample periodic Hann window, hop 160, centred with
   reflect padding — a *400-point* FFT, not a power of two;
3. drop the last frame, square the magnitudes;
4. multiply by librosa's Slaney-scale, area-normalised mel filterbank;
5. ``log10(max(x, 1e-10))``, clamp to ``max - 8``, then ``(x + 4) / 4``.

Every step below uses Aurora's framing, window, DFT and mel code — no torch,
no librosa — so that the hand-written DSP can be dropped into a real model and
judged by word error rate rather than by unit tests alone. The 400-point
transform is the plain DFT definition applied to every frame as one matrix
multiply, because Aurora's radix-2 FFT needs a power-of-two length and
zero-padding to 512 would change the frequency grid Whisper was trained on.
"""

from __future__ import annotations

import numpy as np

from .mel import mel_filterbank
from .stft import frame_signal
from .windows import hann

__all__ = ["log_mel_whisper", "whisper_mel_filterbank", "rdft_frames"]

SAMPLE_RATE = 16_000
N_FFT = 400
HOP_LENGTH = 160
CHUNK_LENGTH = 30
N_SAMPLES = CHUNK_LENGTH * SAMPLE_RATE  # 480 000
N_FRAMES = N_SAMPLES // HOP_LENGTH  # 3000


def rdft_frames(frames: np.ndarray) -> np.ndarray:
    """Real DFT of every row of ``frames`` straight from the definition.

    ``X[k] = sum_n x[n] exp(-2j pi k n / N)`` for ``k = 0 .. N//2``, computed
    as ``frames @ basis`` with a precomputed ``(N, N//2 + 1)`` complex basis.
    Returns an array of shape ``(n_frames, N//2 + 1)``.
    """
    frames = np.asarray(frames, dtype=np.float64)
    n = frames.shape[-1]
    k = np.arange(n // 2 + 1)
    t = np.arange(n)
    basis = np.exp(-2j * np.pi * np.outer(t, k) / n)  # (N, N//2 + 1)
    return frames @ basis


def whisper_mel_filterbank(n_mels: int = 80) -> np.ndarray:
    """The ``(n_mels, 201)`` filterbank Whisper ships in ``mel_filters.npz``."""
    return mel_filterbank(
        n_mels,
        N_FFT,
        SAMPLE_RATE,
        fmin=0.0,
        fmax=SAMPLE_RATE / 2,
        htk=False,
        norm="slaney",
    )


def pad_or_trim(audio: np.ndarray, length: int = N_SAMPLES) -> np.ndarray:
    """Zero-pad or cut a 1-D waveform to ``length`` samples."""
    audio = np.asarray(audio, dtype=np.float64)
    if audio.shape[0] >= length:
        return audio[:length]
    return np.pad(audio, (0, length - audio.shape[0]))


def log_mel_whisper(
    audio: np.ndarray, n_mels: int = 80, pad: bool = True
) -> np.ndarray:
    """Whisper-compatible log-mel features of shape ``(n_mels, n_frames)``.

    With ``pad=True`` (the default, matching ``whisper.transcribe``) the
    waveform is padded/trimmed to 30 s first, giving exactly 3000 frames.
    """
    if pad:
        audio = pad_or_trim(audio)
    frames = frame_signal(audio, N_FFT, HOP_LENGTH, center=True)
    frames = frames * hann(N_FFT, periodic=True)
    spectra = rdft_frames(frames)[:-1]  # drop last frame, as Whisper does
    power = np.abs(spectra) ** 2  # (n_frames, 201)

    mel = power @ whisper_mel_filterbank(n_mels).T  # (n_frames, n_mels)
    log_spec = np.log10(np.maximum(mel, 1e-10))
    log_spec = np.maximum(log_spec, log_spec.max() - 8.0)
    log_spec = (log_spec + 4.0) / 4.0
    return log_spec.T

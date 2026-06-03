"""Aurora Audio Core — DSP primitives implemented from scratch.

This package is the foundation of the whole system. Everything here is written
from first principles (FFT, STFT, mel filterbank, MFCC, WAV I/O) and validated
against reference implementations in the test suite. No librosa, no SciPy DSP,
no black boxes.

Quick start
-----------
>>> from aurora.audio import sine, mfcc
>>> x = sine(440.0, duration=1.0, sample_rate=16000)
>>> features = mfcc(x, sample_rate=16000, n_mfcc=13)
>>> features.shape  # (n_frames, 13)
"""

from .io import chirp, read_wav, sine, write_wav
from .mel import hz_to_mel, mel_filterbank, mel_spectrogram, mel_to_hz, power_to_db
from .mfcc import dct_ii, mfcc
from .stft import (
    frame_signal,
    magnitude_spectrogram,
    power_spectrogram,
    stft,
)
from .transforms import (
    dft,
    fft,
    fft_frequencies,
    idft,
    ifft,
    irfft,
    rfft,
)
from .windows import blackman, get_window, hamming, hann

__all__ = [
    # io
    "read_wav",
    "write_wav",
    "sine",
    "chirp",
    # transforms
    "dft",
    "idft",
    "fft",
    "ifft",
    "rfft",
    "irfft",
    "fft_frequencies",
    # windows
    "hann",
    "hamming",
    "blackman",
    "get_window",
    # stft
    "frame_signal",
    "stft",
    "magnitude_spectrogram",
    "power_spectrogram",
    # mel
    "hz_to_mel",
    "mel_to_hz",
    "mel_filterbank",
    "mel_spectrogram",
    "power_to_db",
    # mfcc
    "dct_ii",
    "mfcc",
]

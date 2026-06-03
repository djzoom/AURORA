"""Tests for windows, STFT, mel filterbank, MFCC and WAV I/O."""

import os
import tempfile

import numpy as np

from aurora.audio import (
    chirp,
    dct_ii,
    frame_signal,
    hamming,
    hann,
    hz_to_mel,
    mel_filterbank,
    mel_spectrogram,
    mel_to_hz,
    mfcc,
    read_wav,
    sine,
    stft,
    write_wav,
)


# ---------------------------------------------------------------- windows ----
def test_hann_matches_numpy():
    # NumPy's hanning is the *symmetric* window; ours with periodic=False too.
    np.testing.assert_allclose(hann(64, periodic=False), np.hanning(64), atol=1e-12)


def test_hamming_matches_numpy():
    # NumPy's hamming is the *symmetric* window; ours with periodic=False too.
    np.testing.assert_allclose(hamming(32, periodic=False), np.hamming(32), atol=1e-12)


def test_degenerate_window_length():
    np.testing.assert_allclose(hann(1, periodic=True), np.ones(1))


def test_periodic_window_is_symmetric_minus_one():
    # Periodic length-N window == symmetric length-(N+1) window without its last point.
    per = hann(8, periodic=True)
    sym = hann(9, periodic=False)
    np.testing.assert_allclose(per, sym[:-1], atol=1e-12)


# ------------------------------------------------------------------ stft ----
def test_frame_signal_shapes():
    x = np.arange(100, dtype=float)
    frames = frame_signal(x, frame_length=16, hop_length=8, center=False)
    assert frames.shape[1] == 16
    assert frames.shape[0] == 1 + (100 - 16) // 8


def test_stft_shape():
    x = sine(440.0, 0.5, 16000)
    S = stft(x, n_fft=512, hop_length=128)
    assert S.shape[1] == 512 // 2 + 1
    assert np.iscomplexobj(S)


def test_stft_peak_at_input_frequency():
    sr, f = 16000, 1000.0
    x = sine(f, 1.0, sr)
    S = np.abs(stft(x, n_fft=2048, hop_length=512))
    # Average magnitude per bin; peak bin should map to ~1000 Hz.
    avg = S.mean(axis=0)
    peak_bin = int(np.argmax(avg))
    peak_hz = peak_bin * sr / 2048
    assert abs(peak_hz - f) < sr / 2048  # within one bin


# ------------------------------------------------------------------- mel ----
def test_mel_roundtrip():
    freqs = np.array([0.0, 100.0, 440.0, 1000.0, 8000.0])
    np.testing.assert_allclose(mel_to_hz(hz_to_mel(freqs)), freqs, atol=1e-6)


def test_mel_filterbank_shape_and_nonneg():
    fb = mel_filterbank(n_mels=40, n_fft=1024, sample_rate=16000)
    assert fb.shape == (40, 513)
    assert np.all(fb >= 0.0)
    # Each triangular filter should have a positive peak.
    assert np.all(fb.max(axis=1) > 0.0)


def test_mel_spectrogram_shape():
    x = chirp(200.0, 4000.0, 1.0, 16000)
    M = mel_spectrogram(x, 16000, n_fft=1024, hop_length=256, n_mels=80)
    assert M.shape[1] == 80
    assert np.all(M >= 0.0)


# ------------------------------------------------------------------ mfcc ----
def test_dct_matches_scipy_formula():
    # Compare against the explicit orthonormal DCT-II reference.
    x = np.array([1.0, 2.0, 3.0, 4.0])
    n = len(x)
    k = np.arange(n)
    basis = np.cos(np.pi / n * np.outer(k, k + 0.5))
    ref = x @ basis.T
    scale = np.full(n, np.sqrt(2.0 / n))
    scale[0] = np.sqrt(1.0 / n)
    ref = ref * scale
    np.testing.assert_allclose(dct_ii(x), ref, atol=1e-12)


def test_mfcc_shape():
    x = sine(440.0, 1.0, 16000)
    C = mfcc(x, 16000, n_mfcc=13, n_fft=1024, hop_length=256)
    assert C.shape[1] == 13


# -------------------------------------------------------------------- io ----
def test_wav_roundtrip():
    sr = 16000
    x = sine(440.0, 0.25, sr)
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "t.wav")
        write_wav(path, x, sr)
        y, sr2 = read_wav(path)
    assert sr2 == sr
    assert len(y) == len(x)
    # 16-bit quantization error is small.
    assert np.max(np.abs(y - x)) < 1e-3

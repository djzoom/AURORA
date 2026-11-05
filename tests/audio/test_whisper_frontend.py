"""Pin the Whisper front end to an independent NumPy reference.

These tests re-derive each stage with ``numpy.fft`` and closed-form formulas,
so the hand-written path is checked without importing torch, librosa or
whisper. Bit-level agreement with the real Whisper is checked in
``scripts/bench_alignment.py`` (needs the optional stacks).
"""

import numpy as np

from aurora.audio import (
    hz_to_mel_slaney,
    log_mel_whisper,
    mel_filterbank,
    mel_to_hz_slaney,
    sine,
    whisper_mel_filterbank,
)
from aurora.audio.whisper_frontend import N_FRAMES, rdft_frames


def test_rdft_frames_matches_numpy_rfft():
    rng = np.random.default_rng(0)
    frames = rng.standard_normal((7, 400))
    np.testing.assert_allclose(
        rdft_frames(frames), np.fft.rfft(frames, axis=-1), atol=1e-9
    )


def test_slaney_scale_round_trip_and_knee():
    f = np.array([0.0, 500.0, 1000.0, 4000.0, 8000.0])
    np.testing.assert_allclose(mel_to_hz_slaney(hz_to_mel_slaney(f)), f, rtol=1e-12)
    # Linear region: 1000 Hz == 15 mel exactly.
    np.testing.assert_allclose(hz_to_mel_slaney(1000.0), 15.0)
    # Log region: 6400 Hz is 27 mel above 1 kHz by construction.
    np.testing.assert_allclose(hz_to_mel_slaney(6400.0), 42.0)


def test_slaney_filterbank_has_unit_area():
    fb = mel_filterbank(80, 400, 16000, htk=False, norm="slaney")
    assert fb.shape == (80, 201)
    # Each triangle integrates (over Hz) to ~1 up to bin quantisation.
    df = 16000 / 400
    areas = fb.sum(axis=1) * df
    assert np.all(areas > 0.5) and np.all(areas < 1.5)
    np.testing.assert_array_equal(fb, whisper_mel_filterbank(80))


def test_log_mel_whisper_shape_and_range():
    x = sine(440.0, duration=2.0, sample_rate=16000)
    feats = log_mel_whisper(x)
    assert feats.shape == (80, N_FRAMES)
    # After (x + 4) / 4 with an 8 dB-decade clamp, values live in [max-2, max].
    assert feats.max() - feats.min() <= 2.0 + 1e-9


def test_log_mel_whisper_no_pad_frame_count():
    x = sine(440.0, duration=1.0, sample_rate=16000)  # 16000 samples
    feats = log_mel_whisper(x, pad=False)
    assert feats.shape == (80, 16000 // 160)  # 1 + 16000//160 frames, last dropped

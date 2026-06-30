"""Tests for aurora.music.features."""
import numpy as np
from aurora.music.features import (
    chromagram, chroma_vector, rms_envelope, zero_crossing_rate, onset_envelope, beat_track
)


SR = 8000
DURATION = 1.0
N_SAMPLES = int(SR * DURATION)


def make_sine(freq=440.0, sr=SR, duration=DURATION):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)


def test_chroma_vector_shape():
    sig = make_sine()
    n_fft = 2048
    power_spec = np.abs(np.fft.rfft(sig, n=n_fft)) ** 2
    cv = chroma_vector(power_spec, sample_rate=SR, n_fft=n_fft)
    assert cv.shape == (12,), f"Expected (12,), got {cv.shape}"


def test_chroma_vector_nonneg():
    sig = make_sine()
    n_fft = 2048
    power_spec = np.abs(np.fft.rfft(sig, n=n_fft)) ** 2
    cv = chroma_vector(power_spec, sample_rate=SR, n_fft=n_fft)
    assert np.all(cv >= 0), "chroma_vector should be non-negative"


def test_chromagram_shape():
    sig = make_sine()
    cg = chromagram(sig, sample_rate=SR)
    assert cg.ndim == 2
    # aurora chromagram returns (n_frames, 12): 12 pitch classes per frame
    assert cg.shape[-1] == 12, f"Expected 12 pitch classes, got {cg.shape}"
    assert cg.shape[0] > 0, "Should have at least one frame"


def test_chromagram_nonneg():
    sig = make_sine()
    cg = chromagram(sig, sample_rate=SR)
    assert np.all(cg >= 0)


def test_rms_envelope_shape():
    sig = make_sine()
    rms = rms_envelope(sig)
    assert rms.ndim == 1
    assert rms.shape[0] > 0


def test_rms_envelope_nonneg():
    sig = make_sine()
    rms = rms_envelope(sig)
    assert np.all(rms >= 0)


def test_rms_silence_is_zero():
    silence = np.zeros(N_SAMPLES)
    rms = rms_envelope(silence)
    assert np.all(rms < 1e-9), "Silence should have near-zero RMS"


def test_zero_crossing_rate_shape():
    sig = make_sine()
    zcr = zero_crossing_rate(sig)
    assert zcr.ndim == 1
    assert zcr.shape[0] > 0


def test_zcr_sine_positive():
    sig = make_sine(440.0)
    zcr = zero_crossing_rate(sig)
    assert np.mean(zcr) > 0, "A sine wave should have positive ZCR"


def test_onset_envelope_shape():
    sig = make_sine()
    env = onset_envelope(sig, sample_rate=SR)
    assert env.ndim == 1
    assert env.shape[0] > 0


def test_onset_envelope_nonneg():
    sig = make_sine()
    env = onset_envelope(sig, sample_rate=SR)
    assert np.all(env >= 0)


def make_pulse(bpm=120.0, sr=SR, duration=4.0):
    """Impulse train at a known BPM — gives beat_track a clean ground truth."""
    n = int(sr * duration)
    sig = np.zeros(n, dtype=np.float64)
    beat_interval = int(sr * 60.0 / bpm)
    for i in range(0, n, beat_interval):
        if i < n:
            sig[i] = 1.0
    return sig


def test_beat_track_known_bpm():
    target_bpm = 120.0
    sig = make_pulse(bpm=target_bpm, sr=SR, duration=4.0)
    bpm, beat_times = beat_track(sig, sample_rate=SR)
    assert abs(bpm - target_bpm) / target_bpm < 0.10, (
        f"beat_track returned {bpm:.1f} BPM, expected {target_bpm} ± 10%"
    )
    assert len(beat_times) >= 4, "Should detect at least 4 beats in 4-second signal"


def test_beat_track_returns_tuple():
    sig = make_sine(440.0)
    result = beat_track(sig, sample_rate=SR)
    assert isinstance(result, tuple) and len(result) == 2
    bpm, beat_times = result
    assert bpm > 0
    assert isinstance(beat_times, np.ndarray)

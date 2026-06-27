"""aurora.music.features — music feature extraction from scratch using aurora.audio primitives."""
import numpy as np
from aurora.audio.stft import stft

MIDI_A4 = 69
FREQ_A4 = 440.0
PITCH_CLASSES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def hz_to_midi(freq: np.ndarray) -> np.ndarray:
    """Frequency in Hz → fractional MIDI note number. A4=440Hz=MIDI69."""
    return 12.0 * np.log2(np.maximum(freq, 1e-8) / FREQ_A4) + MIDI_A4


def chroma_vector(power_spectrum: np.ndarray, sample_rate: int, n_fft: int = 2048) -> np.ndarray:
    """12-bin chroma vector from a single power spectrum frame.

    Maps each FFT bin to its nearest MIDI pitch, accumulates energy into the
    corresponding pitch class (chroma = MIDI mod 12), then L1-normalises.

    Args:
        power_spectrum: (n_bins,) magnitude² array (one STFT frame).
        sample_rate: audio sample rate in Hz.
        n_fft: FFT size used to compute power_spectrum.

    Returns:
        (12,) float64 chroma vector, L1-normalised.
    """
    n_bins = power_spectrum.shape[0]
    freqs = np.fft.rfftfreq(n_fft, d=1.0 / sample_rate)[:n_bins]
    chroma = np.zeros(12)
    for f, energy in zip(freqs, power_spectrum):
        if f <= 0:
            continue
        midi = hz_to_midi(np.array([f]))[0]
        pitch_class = int(round(midi)) % 12
        chroma[pitch_class] += energy
    total = chroma.sum()
    if total > 0:
        chroma /= total
    return chroma


def chromagram(
    signal: np.ndarray,
    sample_rate: int,
    n_fft: int = 2048,
    hop_length: int = 512,
) -> np.ndarray:
    """Time-varying chromagram via STFT.

    Returns:
        (n_frames, 12) float64 array.
    """
    S = stft(signal, n_fft=n_fft, hop_length=hop_length)  # (n_frames, n_freqs)
    power = np.abs(S) ** 2
    return np.array([chroma_vector(frame, sample_rate, n_fft) for frame in power])


def rms_envelope(signal: np.ndarray, frame_len: int = 2048, hop: int = 512) -> np.ndarray:
    """Root-mean-square energy per frame.

    Returns:
        (n_frames,) float64 array.
    """
    n_frames = max(1, (len(signal) - frame_len) // hop + 1)
    frames = np.stack([signal[i * hop : i * hop + frame_len] for i in range(n_frames)])
    return np.sqrt(np.mean(frames**2, axis=1))


def zero_crossing_rate(signal: np.ndarray, frame_len: int = 2048, hop: int = 512) -> np.ndarray:
    """Zero-crossing rate per frame (fraction of samples where sign changes).

    Returns:
        (n_frames,) float64 array.
    """
    n_frames = max(1, (len(signal) - frame_len) // hop + 1)
    zcr = np.zeros(n_frames)
    for i in range(n_frames):
        frame = signal[i * hop : i * hop + frame_len]
        zcr[i] = np.mean(np.abs(np.diff(np.sign(frame))) / 2)
    return zcr


def onset_envelope(
    signal: np.ndarray,
    sample_rate: int,
    n_fft: int = 2048,
    hop_length: int = 512,
) -> np.ndarray:
    """Spectral flux onset envelope: sum of positive first differences of magnitude spectra.

    Returns:
        (n_frames - 1,) float64 array.
    """
    S = stft(signal, n_fft=n_fft, hop_length=hop_length)  # (n_frames, n_freqs)
    mag = np.abs(S)
    flux = np.maximum(0.0, np.diff(mag, axis=0))  # half-wave rectified flux
    return flux.sum(axis=1)


def beat_track(
    signal: np.ndarray,
    sample_rate: int,
    hop_length: int = 512,
) -> tuple:
    """Estimate BPM and beat times via autocorrelation of onset envelope.

    Uses the onset envelope's autocorrelation to find the dominant periodicity
    in the range 40-240 BPM, then places beat markers at that period.

    Returns:
        (bpm, beat_times_seconds) where beat_times is a 1D float64 array.
    """
    env = onset_envelope(signal, sample_rate, hop_length=hop_length)
    fps = sample_rate / hop_length

    min_lag = max(1, int(fps * 60 / 240))
    max_lag = min(len(env) - 1, int(fps * 60 / 40))

    if min_lag >= max_lag or len(env) < 4:
        return 120.0, np.array([0.0])

    lags = np.arange(min_lag, max_lag + 1)
    # autocorrelation at each lag: dot product of env with itself shifted by lag
    ac = np.array([float(np.dot(env[: len(env) - lag], env[lag:])) for lag in lags])
    best_lag = lags[int(np.argmax(ac))]
    bpm = fps * 60.0 / best_lag

    beat_times = []
    pos = int(np.argmax(env[:best_lag]))
    while pos < len(env):
        beat_times.append(pos / fps)
        pos += best_lag

    return float(bpm), np.array(beat_times)

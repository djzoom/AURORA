"""Validate the hand-written Fourier transforms against NumPy's FFT.

NumPy's FFT is the ground truth here. Our job is to prove the from-scratch
Cooley-Tukey implementation produces the same numbers.
"""

import numpy as np
import pytest

from aurora.audio import transforms as T


@pytest.fixture
def rng():
    return np.random.default_rng(0)


@pytest.mark.parametrize("n", [1, 2, 4, 8, 16, 64, 256, 1024])
def test_fft_matches_numpy(rng, n):
    x = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    np.testing.assert_allclose(T.fft(x), np.fft.fft(x), atol=1e-9)


@pytest.mark.parametrize("n", [2, 8, 32, 128])
def test_dft_matches_numpy(rng, n):
    x = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    np.testing.assert_allclose(T.dft(x), np.fft.fft(x), atol=1e-9)


def test_fft_agrees_with_dft(rng):
    x = rng.standard_normal(64)
    np.testing.assert_allclose(T.fft(x), T.dft(x), atol=1e-9)


@pytest.mark.parametrize("n", [4, 16, 256])
def test_ifft_inverts_fft(rng, n):
    x = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    np.testing.assert_allclose(T.ifft(T.fft(x)), x, atol=1e-9)


def test_fft_rejects_non_power_of_two():
    with pytest.raises(ValueError):
        T.fft(np.zeros(3))


@pytest.mark.parametrize("n", [8, 64, 512])
def test_rfft_matches_numpy(rng, n):
    x = rng.standard_normal(n)
    np.testing.assert_allclose(T.rfft(x), np.fft.rfft(x), atol=1e-9)


@pytest.mark.parametrize("n", [8, 64, 512])
def test_irfft_inverts_rfft(rng, n):
    x = rng.standard_normal(n)
    np.testing.assert_allclose(T.irfft(T.rfft(x), n), x, atol=1e-9)


def test_next_power_of_two():
    assert T.next_power_of_two(1) == 1
    assert T.next_power_of_two(5) == 8
    assert T.next_power_of_two(1024) == 1024
    assert T.next_power_of_two(1025) == 2048


def test_fft_frequencies():
    freqs = T.fft_frequencies(16000, 1024)
    assert freqs.shape == (513,)
    assert freqs[0] == 0.0
    assert freqs[-1] == pytest.approx(8000.0)

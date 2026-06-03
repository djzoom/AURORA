"""Fourier transforms implemented from scratch.

This module is deliberately *not* a wrapper around ``numpy.fft``. The whole
point of Aurora's Audio Core is to demonstrate first-principles understanding
of the Discrete Fourier Transform and the Cooley-Tukey Fast Fourier Transform.

We use NumPy strictly as a numerical array container and for elementwise
complex arithmetic — never for the transform algorithms themselves. Every
function here is validated against ``numpy.fft`` in the test suite so we know
the hand-written math is correct.

References
----------
- Cooley, J. W. & Tukey, J. W. (1965). "An Algorithm for the Machine
  Calculation of Complex Fourier Series." Math. Comp. 19, 297-301.
- Oppenheim & Schafer, "Discrete-Time Signal Processing", 3rd ed.
"""

from __future__ import annotations

import numpy as np

__all__ = [
    "dft",
    "idft",
    "fft",
    "ifft",
    "rfft",
    "irfft",
    "fft_frequencies",
    "is_power_of_two",
    "next_power_of_two",
]


def is_power_of_two(n: int) -> bool:
    """Return ``True`` if ``n`` is a positive power of two."""
    return n > 0 and (n & (n - 1)) == 0


def next_power_of_two(n: int) -> int:
    """Return the smallest power of two greater than or equal to ``n``."""
    if n <= 1:
        return 1
    return 1 << (n - 1).bit_length()


def dft(x: np.ndarray) -> np.ndarray:
    """Naive O(N^2) Discrete Fourier Transform.

    Computed directly from the definition

        X[k] = sum_{n=0}^{N-1} x[n] * exp(-2j*pi*k*n/N)

    This is intentionally the textbook double-loop expressed as a single
    matrix multiply. It is slow but unambiguous, and serves as the ground
    truth the FFT is validated against.
    """
    x = np.asarray(x, dtype=np.complex128)
    n = x.shape[-1]
    k = np.arange(n)
    # Twiddle matrix W[k, m] = exp(-2j*pi*k*m/N).
    twiddle = np.exp(-2j * np.pi * np.outer(k, k) / n)
    return twiddle @ x


def idft(x: np.ndarray) -> np.ndarray:
    """Naive inverse DFT (the conjugate-twiddle, 1/N-scaled DFT)."""
    x = np.asarray(x, dtype=np.complex128)
    n = x.shape[-1]
    k = np.arange(n)
    twiddle = np.exp(2j * np.pi * np.outer(k, k) / n)
    return (twiddle @ x) / n


def _bit_reverse_permutation(x: np.ndarray) -> np.ndarray:
    """Reorder ``x`` (length a power of two) into bit-reversed index order."""
    n = x.shape[-1]
    bits = n.bit_length() - 1
    indices = np.arange(n)
    rev = np.zeros(n, dtype=np.intp)
    for i in range(bits):
        # Move bit i of the original index to bit (bits-1-i) of the result.
        rev |= ((indices >> i) & 1) << (bits - 1 - i)
    return x[rev]


def fft(x: np.ndarray) -> np.ndarray:
    """Iterative radix-2 Cooley-Tukey FFT.

    Input length must be a power of two. For arbitrary lengths, zero-pad to
    :func:`next_power_of_two` (this is what :func:`aurora.audio.stft` does) or
    fall back to :func:`dft`.

    The algorithm:

    1. Permute the input into bit-reversed order (decimation-in-time).
    2. Iteratively combine butterflies of size 2, 4, 8, ... N, reusing the
       twiddle factors at each stage.

    This runs in O(N log N) and allocates only O(N) extra memory.
    """
    x = np.asarray(x, dtype=np.complex128)
    n = x.shape[-1]
    if n == 0:
        return x.copy()
    if not is_power_of_two(n):
        raise ValueError(
            f"fft() requires a power-of-two length, got {n}. "
            "Zero-pad with next_power_of_two() or use dft()."
        )

    a = _bit_reverse_permutation(x).astype(np.complex128)

    size = 2
    while size <= n:
        half = size // 2
        # Twiddle factors for this stage: exp(-2j*pi*j/size), j in [0, half).
        twiddle = np.exp(-2j * np.pi * np.arange(half) / size)
        for start in range(0, n, size):
            # Copy the even half: the first assignment below mutates ``a`` in
            # place, and ``even`` would otherwise alias that same memory.
            even = a[start : start + half].copy()
            odd = a[start + half : start + size] * twiddle
            a[start : start + half] = even + odd
            a[start + half : start + size] = even - odd
        size *= 2
    return a


def ifft(x: np.ndarray) -> np.ndarray:
    """Inverse FFT via the conjugation trick: ifft(X) = conj(fft(conj(X)))/N."""
    x = np.asarray(x, dtype=np.complex128)
    n = x.shape[-1]
    if n == 0:
        return x.copy()
    return np.conj(fft(np.conj(x))) / n


def rfft(x: np.ndarray) -> np.ndarray:
    """FFT of a real signal, returning the non-redundant ``N//2 + 1`` bins.

    For real input the spectrum is conjugate-symmetric, so only the first
    half (plus DC and Nyquist) carries information. This mirrors the contract
    of ``numpy.fft.rfft``.
    """
    x = np.asarray(x, dtype=np.float64)
    n = x.shape[-1]
    spectrum = fft(x.astype(np.complex128))
    return spectrum[: n // 2 + 1]


def irfft(x: np.ndarray, n: int) -> np.ndarray:
    """Inverse of :func:`rfft`, reconstructing a length-``n`` real signal."""
    x = np.asarray(x, dtype=np.complex128)
    full = np.zeros(n, dtype=np.complex128)
    half = n // 2 + 1
    full[:half] = x[:half]
    # Rebuild the conjugate-symmetric upper half.
    if n % 2 == 0:
        full[half:] = np.conj(x[1 : half - 1][::-1])
    else:
        full[half:] = np.conj(x[1:half][::-1])
    return np.real(ifft(full))


def fft_frequencies(sample_rate: float, n_fft: int) -> np.ndarray:
    """Center frequency (Hz) of each ``rfft`` bin for a length-``n_fft`` frame."""
    return np.linspace(0.0, sample_rate / 2.0, n_fft // 2 + 1)

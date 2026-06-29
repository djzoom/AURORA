# Writing the FFT from scratch (and proving it's correct)

*Aurora dev log #1 — Audio Core*

Aurora's one rule is "no API wrappers," and the Audio Core is where that rule
bites first. The entire speech/music front-end — `audio → frames → window →
FFT → |·|² → mel → log → DCT → MFCC` — rests on the Fourier transform. So we
write the FFT ourselves.

## From the definition to O(N log N)

The DFT is one line:

```
X[k] = Σ_n x[n] · exp(-2πi·k·n / N)
```

Written as a twiddle matrix times a vector, that's `dft()` — O(N²), our ground
truth. The FFT (Cooley-Tukey, 1965) gets to O(N log N) by exploiting the
structure of those twiddles: split into even/odd indices recursively, and the
sub-transforms share work. We implement the *iterative* radix-2 version:

1. Permute the input into **bit-reversed** order.
2. Combine butterflies of size 2, 4, 8, …, N, reusing each stage's twiddles.

The whole thing is ~30 lines and allocates O(N) scratch.

## The bug that every from-scratch FFT hits

The butterfly reads the "even" half and the "odd" half, then writes
`even + odd` and `even - odd` back. If `even` is a *view* into the working
buffer, the first write corrupts it before the second read:

```python
even = a[start:start+half]          # view — aliases `a`
a[start:start+half]      = even + odd   # mutates the memory `even` points at
a[start+half:start+size] = even - odd   # `even` is now wrong
```

One `.copy()` fixes it. The test suite caught this immediately, which is the
whole point of the next section.

## Proving it

Correctness isn't a vibe; it's a test. We pin the implementation to NumPy's FFT
across power-of-two sizes, and cross-check the FFT against the naive DFT:

```python
@pytest.mark.parametrize("n", [1, 2, 4, 8, 16, 64, 256, 1024])
def test_fft_matches_numpy(rng, n):
    x = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    np.testing.assert_allclose(T.fft(x), np.fft.fft(x), atol=1e-9)
```

`rfft`/`irfft` round-trip, and the STFT built on top of it peaks at the right
frequency for a known sine. 38 tests, all green.

## Next

STFT, mel filterbank, and MFCC — all on this FFT — then PyTorch warm-ups before
the Speech Core. The running artifact is the *Audio Analysis Engine*; the demo
already renders a chirp's spectrogram as ASCII straight from our own DSP.

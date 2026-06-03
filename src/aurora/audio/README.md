# Audio Core

The DSP foundation of Aurora — **implemented**, not wrapped. NumPy is used only
as an array container; every transform is hand-written and pinned to a
reference in `tests/audio/`.

## Modules

| Module | Contents |
|---|---|
| `transforms.py` | naive `dft`/`idft`; iterative radix-2 Cooley-Tukey `fft`/`ifft`; `rfft`/`irfft`; bin frequencies |
| `windows.py` | `hann`, `hamming`, `blackman` (periodic & symmetric), `get_window` |
| `stft.py` | `frame_signal`, `stft`, `magnitude_spectrogram`, `power_spectrogram` |
| `mel.py` | `hz_to_mel`/`mel_to_hz` (HTK), `mel_filterbank`, `mel_spectrogram`, `power_to_db` |
| `mfcc.py` | orthonormal `dct_ii`, `mfcc` |
| `io.py` | `read_wav`/`write_wav` (PCM, from scratch), `sine`, `chirp` |

## Why from scratch

The pipeline `audio → frames → window → FFT → |·|² → mel filterbank → log →
DCT → MFCC` is the canonical front-end of nearly every speech and music model.
Implementing it by hand is what separates a research engineer from an API
caller, and it is a near-guaranteed interview topic at Spotify / Apple / Google
audio teams.

## Validation

`tests/audio/test_transforms.py` checks the FFT against `numpy.fft` across
power-of-two sizes (and the FFT against the naive DFT). The feature tests pin
windows to `numpy.hanning`/`numpy.hamming`, verify the STFT peaks at a known
input frequency, the mel round-trip, the DCT formula, and lossy WAV
round-tripping.

```bash
pytest tests/audio -q
python scripts/demo_audio.py
```

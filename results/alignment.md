| Primitive | Files | Max abs error | Max rel error |
|---|---|---|---|
| `mel_filterbank (HTK, norm=None) vs librosa` | 1 | 2.97e-08 | 2.98e-08 |
| `mel_filterbank (Slaney) vs librosa` | 1 | 1.33e-09 | 5.15e-08 |
| `whisper_mel_filterbank vs whisper mel_filters.npz` | 1 | 1.33e-09 | 5.15e-08 |
| `rfft (1024) vs numpy.fft.rfft` | 20 | 3.33e-16 | 3.47e-16 |
| `|STFT| (1024/256) vs librosa.stft` | 20 | 1.59e-14 | 3.99e-16 |
| `mel_spectrogram (HTK) vs librosa.melspectrogram` | 20 | 6.86e-05 | 2.84e-08 |
| `mfcc (13) vs librosa.mfcc` | 20 | 2.81e-07 | 7.79e-10 |
| `dct_ii (ortho) vs scipy via librosa` | 20 | 2.81e-07 | 7.79e-10 |
| `log_mel_whisper vs whisper.log_mel_spectrogram` | 20 | 2.70e-05 | 2.23e-05 |

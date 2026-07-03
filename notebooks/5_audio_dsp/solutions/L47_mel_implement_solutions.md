# 参考实现 — L47_mel_implement

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
import numpy as np
from aurora.audio.stft import stft
from aurora.audio.mel import mel_filterbank


def log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256):
    S = stft(x, n_fft=win_len, hop_length=hop)   # (n_frames, win_len//2+1)
    power = np.abs(S) ** 2                       # 功率谱，shape 同上
    fb = mel_filterbank(n_mels, win_len, sr)
    mel_energy = power @ fb.T
    return np.log(mel_energy + 1e-8)
```

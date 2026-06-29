# 参考实现 — L50_mfcc

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_mfcc(x, sr, n_mfcc=13, n_mels=40, win_len=1024, hop=256):
    from aurora.audio.mel import mel_spectrogram, power_to_db
    from aurora.audio.mfcc import dct_ii
    mel = mel_spectrogram(x, sr, n_fft=win_len, hop_length=hop, n_mels=n_mels)
    log_mel = power_to_db(mel, top_db=None)
    coeffs = dct_ii(log_mel, norm="ortho")
    return coeffs[:, :n_mfcc]
```


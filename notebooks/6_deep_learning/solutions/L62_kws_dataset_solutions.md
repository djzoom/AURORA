# 参考实现 — L62_kws_dataset

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def extract_features(
    wav_path: str,
    sr: int = 16000,
    n_mels: int = 40,
) -> torch.Tensor:
    x, file_sr = read_wav(wav_path)
    assert file_sr == sr, f"期望 {sr} Hz，实际 {file_sr} Hz"
    x = x.astype(np.float32)
    if x.ndim == 2:          # 立体声 → 单声道
        x = x.mean(axis=1)
    x = pad_or_truncate(x, sr)                        # (16000,)
    mel = mel_spectrogram(x, sample_rate=sr, n_mels=n_mels, n_fft=2048, hop_length=512)    # (T, n_mels)
    mel = mel.T                                        # (n_mels, T)
    mel = normalize(mel)                               # per-sample 归一化
    return torch.from_numpy(mel).float()
```


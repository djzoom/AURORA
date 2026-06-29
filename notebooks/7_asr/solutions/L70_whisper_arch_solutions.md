# 参考实现 — L70_whisper_arch

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def whisper_preprocess(wav: np.ndarray, sr: int = 16000) -> "torch.Tensor":
    # 1. mel 特征，aurora 输出 (n_frames, n_mels)
    mel = mel_spectrogram(wav, sr, n_fft=400, hop_length=160, n_mels=80)
    mel = mel.T  # → (80, n_frames)

    # 2. log 归一化（Whisper 风格）
    log_mel = np.log10(np.maximum(mel, 1e-10))
    log_mel = np.maximum(log_mel, log_mel.max() - 8.0)
    log_mel = (log_mel + 4.0) / 4.0

    # 3. pad / truncate 到 3000 帧
    n_frames = log_mel.shape[1]
    if n_frames < 3000:
        pad = np.zeros((80, 3000 - n_frames), dtype=log_mel.dtype)
        log_mel = np.concatenate([log_mel, pad], axis=1)
    else:
        log_mel = log_mel[:, :3000]

    # 4. 转 tensor，加 batch 维
    return torch.tensor(log_mel, dtype=torch.float32).unsqueeze(0)
```


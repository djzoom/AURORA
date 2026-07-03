# 参考实现 — L62_kws_dataset

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def extract_features(
    wav_path: str,
    sr: int = 16000,
    n_mels: int = 40,
) -> torch.Tensor:
    """加载 WAV → pad/truncate → mel 频谱 → dB 转换 → 归一化 → torch.Tensor (n_mels, T)。"""
    from aurora.audio.mel import mel_spectrogram, power_to_db

    x, file_sr = read_wav(wav_path)                    # 1. 读取（多声道自动混单声道）
    assert file_sr == sr, f"期望 {sr} Hz，实际 {file_sr} Hz"  # 2. 断言采样率
    x = x.astype(np.float32)
    x = pad_or_truncate(x, sr)                          # 3. (16000,)
    mel = mel_spectrogram(
        x, sample_rate=sr, n_mels=n_mels, n_fft=2048, hop_length=512
    )                                                   # 4. (T, n_mels) = (32, 40)
    mel = power_to_db(mel)                              # 4b. dB 量纲
    mel = mel.T                                         # 5. (n_mels, T)
    mel = normalize(mel)                                # 6. per-sample 归一化
    return torch.from_numpy(mel).float()
```

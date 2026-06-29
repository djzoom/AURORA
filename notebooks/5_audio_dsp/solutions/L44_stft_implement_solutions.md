# 参考实现 — L44_stft_implement

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_stft(x, win_len=2048, hop=512, window="hann"):
    from aurora.audio.windows import get_window
    from aurora.audio.stft import frame_signal

    win = get_window(window, win_len, periodic=True)      # (win_len,)
    frames = frame_signal(x, win_len, hop, center=True)  # (n_frames, win_len)
    windowed = frames * win                               # 广播乘窗

    n_bins = win_len // 2 + 1
    spectra = [np.fft.fft(f)[:n_bins] for f in windowed]
    return np.stack(spectra)                              # (n_frames, n_bins)
```


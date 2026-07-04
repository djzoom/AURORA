# 参考实现 — L44_stft_implement

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_stft(x, win_len=2048, hop=512, window="hann"):
    from aurora.audio.windows import get_window
    from aurora.audio.stft import frame_signal
    from aurora.audio.transforms import fft as aurora_fft  # L37-39 手写 Cooley-Tukey FFT

    win = get_window(window, win_len, periodic=True)      # (win_len,)
    frames = frame_signal(x, win_len, hop, center=True)  # (n_frames, win_len)
    windowed = frames * win                               # 广播乘窗

    # 铁律：引擎走从零实现的 aurora fft（win_len=2048 是 2 的幂，
    # Cooley-Tukey 可用）；np.fft 只在演示/对照格里出现，不当引擎。
    n_bins = win_len // 2 + 1
    spectra = [aurora_fft(f)[:n_bins] for f in windowed]
    return np.stack(spectra)                              # (n_frames, n_bins)
```


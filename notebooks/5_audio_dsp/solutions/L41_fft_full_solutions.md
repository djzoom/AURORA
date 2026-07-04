# 参考实现 — L41_fft_full

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
from aurora.audio.transforms import fft as aurora_fft  # L37-39 手写的 Cooley-Tukey FFT


def windowed_fft(x: np.ndarray, window_type: str = "hann") -> np.ndarray:
    N = len(x)
    if window_type == "hann":
        window = hann(N)
    elif window_type == "hamming":
        window = hamming(N)
    elif window_type == "rectangular":
        window = np.ones(N)
    else:
        raise ValueError(f"未知窗类型：{window_type}")
    x_win = x * window
    # 铁律：真正的引擎是从零实现的 aurora.audio.transforms.fft
    # （基-2 Cooley-Tukey，要求 N 为 2 的幂；本课 N=16/64/128/256 均满足）。
    # np.fft.fft 只在检查格里作交叉验证，不当引擎。
    return aurora_fft(x_win)
```


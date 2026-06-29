# 参考实现 — L41_fft_full

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
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
    return np.fft.fft(x_win)
```


# 参考实现 — L43_stft

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def frame_signal(x: np.ndarray, win_len: int, hop: int) -> np.ndarray:
    """把 1D 信号切成重叠帧，返回 shape (n_frames, win_len)。"""
    n_frames = 1 + (len(x) - win_len) // hop
    # sliding_window_view 零拷贝；[::hop] 按 hop 取行
    frames = np.lib.stride_tricks.sliding_window_view(x, win_len)[::hop]
    return frames[:n_frames].copy()  # 确保可写，截断到精确帧数
```


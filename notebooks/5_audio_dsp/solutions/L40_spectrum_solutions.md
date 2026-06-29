# 参考实现 — L40_spectrum

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def frequency_bins(N: int, sr: int) -> np.ndarray:
    freqs_full = np.arange(N) * sr / N
    return freqs_full[:N // 2 + 1]
```


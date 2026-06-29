# 参考实现 — L49_dct

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def dct_ii(x: np.ndarray) -> np.ndarray:
    N = len(x)
    k = np.arange(N)
    n = np.arange(N)
    M = np.cos(np.pi * np.outer(k, 2 * n + 1) / (2 * N))
    scale = np.full(N, np.sqrt(2.0 / N))
    scale[0] = np.sqrt(1.0 / N)
    return (M @ x) * scale
```


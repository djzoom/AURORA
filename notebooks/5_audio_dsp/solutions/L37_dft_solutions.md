# 参考实现 — L37_dft

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def naive_dft(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=complex)
    N = len(x)
    X = np.zeros(N, dtype=complex)
    n = np.arange(N)
    for k in range(N):
        twiddles = np.exp(-2j * np.pi * k * n / N)
        X[k] = np.dot(x, twiddles)
    return X
```


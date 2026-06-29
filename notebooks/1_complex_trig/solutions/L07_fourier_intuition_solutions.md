# 参考实现 — L07_fourier_intuition

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def square_approx(t, n):
    result = np.zeros_like(t)
    for k in range(1, 2*n, 2):
        result += np.sin(2 * np.pi * k * t) / k
    return result
```


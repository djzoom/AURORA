# 参考实现 — L35_euler_fft

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def euler(theta):
    return np.cos(theta) + 1j * np.sin(theta)
```

## 参考实现 2

```python
def twiddle(k, n, N):
    return euler(-2 * np.pi * k * n / N)
```


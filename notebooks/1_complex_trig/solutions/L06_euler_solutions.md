# 参考实现 — L06_euler

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def twiddle(k, n, N):
    return np.exp(-2j * np.pi * k * n / N)
    # 等价写法（手动拼）：
    # theta = -2 * np.pi * k * n / N
    # return np.cos(theta) + 1j * np.sin(theta)
```


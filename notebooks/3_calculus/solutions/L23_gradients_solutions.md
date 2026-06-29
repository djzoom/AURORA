# 参考实现 — L23_gradients

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def gradient(f, point, h=1e-5):
    point = np.asarray(point, dtype=float)
    grad = np.zeros_like(point)
    for i in range(len(point)):
        e = np.zeros_like(point)
        e[i] = h
        grad[i] = (f(point + e) - f(point - e)) / (2 * h)
    return grad
```


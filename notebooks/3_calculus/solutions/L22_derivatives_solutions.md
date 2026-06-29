# 参考实现 — L22_derivatives

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def numeric_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
```


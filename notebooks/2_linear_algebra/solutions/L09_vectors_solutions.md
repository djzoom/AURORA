# 参考实现 — L09_vectors

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def scale(v, c):
    return c * v
```

## 参考实现 2

```python
def add_signals(a, b):
    return a + b
```

## 参考实现 3

```python
def linear_combination(coeffs, vecs):
    result = coeffs[0] * vecs[0]
    for c, v in zip(coeffs[1:], vecs[1:]):
        result = result + c * v
    return result
```

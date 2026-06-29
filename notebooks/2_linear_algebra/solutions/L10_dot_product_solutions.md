# 参考实现 — L10_dot_product

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```


# 参考实现 — L10_dot_product

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def cosine_similarity(a, b):
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        raise ValueError("零向量没有方向，无法计算余弦相似度")
    return np.dot(a, b) / (na * nb)
```

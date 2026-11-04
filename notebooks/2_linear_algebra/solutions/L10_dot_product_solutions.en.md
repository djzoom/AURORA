# Reference implementation — L10_dot_product

> ⚠️ Please finish the exercises on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def cosine_similarity(a, b):
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        raise ValueError("The zero vector has no direction, so cosine similarity cannot be computed")
    return np.dot(a, b) / (na * nb)
```

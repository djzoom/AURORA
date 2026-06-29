# 参考实现 — L13_special_matrices

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def is_orthogonal(Q):
    n = len(Q)
    return bool(np.allclose(Q.T @ Q, np.eye(n)))
```


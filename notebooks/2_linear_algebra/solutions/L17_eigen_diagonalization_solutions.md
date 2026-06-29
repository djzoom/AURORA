# 参考实现 — L17_eigen_diagonalization

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def char_poly(A, lam):
    A = np.asarray(A, float)
    return np.linalg.det(A - lam * np.eye(len(A)))
```


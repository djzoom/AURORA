# 参考实现 — L18_invertibility

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — extract_null_vector

```python
def extract_null_vector(B):
    """返回矩阵 B 的（最小奇异值对应）零空间向量 v。"""
    B = np.asarray(B, float)
    # SVD：B = U · diag(s) · Vt，最小奇异值对应 Vt 的最后一行
    U, s, Vt = np.linalg.svd(B)
    return Vt[-1]
```

## 参考实现 2 — is_sdd

```python
def is_sdd(A):
    A = np.asarray(A, float)
    n = len(A)
    return all(abs(A[i, i]) > np.sum(np.abs(A[i])) - abs(A[i, i]) for i in range(n))

# 向量化等价写法：
# diag = np.abs(np.diag(A))
# off  = np.sum(np.abs(A), axis=1) - diag
# return bool(np.all(diag > off))
```

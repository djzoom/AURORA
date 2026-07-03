# 参考实现 — L12_matrices

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def matvec(A, x):
    out = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        out[i] = np.dot(A[i], x)
    return out
```

## 参考实现 2

```python
def matmul(A, B):
    """矩阵 × 矩阵：对 B 的每一列调用 matvec(A, col)，再横向拼接。"""
    return np.column_stack([matvec(A, B[:, j]) for j in range(B.shape[1])])
```


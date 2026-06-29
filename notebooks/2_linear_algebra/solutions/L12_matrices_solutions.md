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


# 参考实现 — L18_invertibility

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

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


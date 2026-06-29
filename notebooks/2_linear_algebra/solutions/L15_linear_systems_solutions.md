# 参考实现 — L15_linear_systems

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def classify_system(A, b):
    A = np.asarray(A, float); b = np.asarray(b, float)
    rA  = np.linalg.matrix_rank(A)
    rAb = np.linalg.matrix_rank(np.column_stack([A, b]))
    n   = A.shape[1]
    if rA < rAb:
        return 'none'
    elif rA == n:
        return 'unique'
    else:
        return 'many'
```


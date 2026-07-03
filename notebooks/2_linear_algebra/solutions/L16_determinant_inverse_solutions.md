# 参考实现 — L16_determinant_inverse

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def det_2x2(M):
    a, b = M[0]
    c, d = M[1]
    return a*d - b*c

def inv_2x2(M):
    a, b = M[0]
    c, d = M[1]
    det = a*d - b*c
    if det == 0:
        return None
    return (1/det) * np.array([[d, -b], [-c, a]])
```

## 参考实现 2

```python
def det_3x3(M):
    M = np.asarray(M, float)
    d = 0.0
    for j in range(3):                       # 按第一行余子式展开
        minor = M[1:, [k for k in range(3) if k != j]]
        d += ((-1)**j) * M[0, j] * det_2x2(minor)
    return d

def inv_3x3(M):
    M = np.asarray(M, float)
    det = det_3x3(M)
    if det == 0:
        return None
    cof = np.zeros((3, 3))                    # 代数余子式矩阵
    for i in range(3):
        for j in range(3):
            minor = M[[r for r in range(3) if r != i]][:, [c for c in range(3) if c != j]]
            cof[i, j] = ((-1)**(i+j)) * det_2x2(minor)
    return cof.T / det                        # A⁻¹ = adj(A)/det = cofᵀ/det
```


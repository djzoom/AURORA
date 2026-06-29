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


# 参考实现 — L11_norms

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def normalize(v):
    n = np.linalg.norm(v)
    if n == 0:
        return v          # 零向量没有方向，返回全零，避免除零产生 nan
    return v / n
```

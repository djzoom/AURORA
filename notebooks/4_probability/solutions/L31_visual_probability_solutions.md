# 参考实现 — L31_visual_probability

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def shannon_entropy(p: np.ndarray) -> float:
    """计算离散概率分布 p 的 Shannon 熵（单位：bit）。"""
    p = np.asarray(p, dtype=float)
    nz = p[p > 0]                       # 跳过 p=0 项（约定 0·log0 = 0）
    return float(-np.sum(nz * np.log2(nz)))
```

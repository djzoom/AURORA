# 参考实现 — L20_visual_factorizations

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — rank_from_svd

```python
def rank_from_svd(A, threshold=1e-10):
    """用 SVD 计算矩阵数值秩（不调用 np.linalg.matrix_rank）"""
    A = np.asarray(A, float)
    # 只需奇异值：数值秩 = 显著奇异值（> threshold · 最大奇异值）的个数
    s = np.linalg.svd(A, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > threshold * s[0]))
```

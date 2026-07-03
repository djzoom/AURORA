# 参考实现 — L14_eigen_svd

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def low_rank_approx(A, k):
    """返回 A 的秩-k 近似矩阵（shape 与 A 相同）。

    参数
    ----
    A : np.ndarray, shape (m, n)
    k : int, 保留的奇异值数量，1 <= k <= min(m, n)
    """
    U, S, Vt = np.linalg.svd(A)           # A = U diag(S) Vt
    # 取前 k 个方向：U 的前 k 列 · diag(前 k 个奇异值) · Vt 的前 k 行
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
```

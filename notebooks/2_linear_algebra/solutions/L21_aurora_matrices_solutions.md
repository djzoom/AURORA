# 参考实现 — L21_aurora_matrices

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — build_dft_matrix

```python
def build_dft_matrix(N: int) -> np.ndarray:
    """返回 N×N DFT 矩阵 W，满足 W @ x == np.fft.fft(x)。"""
    n = np.arange(N)
    # W[k, n] = exp(-2πi·k·n/N)：np.outer(n, n) 一次生成所有 k·n 组合
    return np.exp(-2j * np.pi * np.outer(n, n) / N)
```

## 参考实现 2 — build_simple_mel_matrix

```python
def build_simple_mel_matrix(n_mels: int, n_fft: int) -> np.ndarray:
    """返回 (n_mels, n_fft//2+1) 的线性刻度三角形滤波器矩阵。"""
    bins = np.arange(n_fft // 2 + 1, dtype=float)
    # n_mels+2 个等距端点（含边界 0 和 n_fft//2）；
    # 滤波器 m 的 lo/cen/hi 取相邻三元组 (centers[m], centers[m+1], centers[m+2])
    centers = np.linspace(0, n_fft // 2, n_mels + 2)
    M = np.zeros((n_mels, len(bins)))
    for m in range(n_mels):
        lo, cen, hi = centers[m], centers[m + 1], centers[m + 2]
        # 上升沿 (bins-lo)/(cen-lo)，下降沿 (hi-bins)/(hi-cen)，负值截为 0
        M[m] = np.clip(np.where(bins <= cen,
                                (bins - lo) / (cen - lo + 1e-9),
                                (hi - bins) / (hi - cen + 1e-9)), 0, 1)
    return M
```

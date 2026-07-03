# 参考实现 — L38_fft_butterfly

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def butterfly(E: np.ndarray, O: np.ndarray) -> np.ndarray:
    """单层蝶形合并：两个 N/2 点 DFT → 一个 N 点 DFT。"""
    half = len(E)
    N = half * 2
    twiddles = np.exp(-2j * np.pi * np.arange(half) / N)  # 旋转因子 W_N^k
    top    = E + twiddles * O   # 上半频谱 X[0..N/2-1]
    bottom = E - twiddles * O   # 下半频谱 X[N/2..N-1]
    return np.concatenate([top, bottom])
```

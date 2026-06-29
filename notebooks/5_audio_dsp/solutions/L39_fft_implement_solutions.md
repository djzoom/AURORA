# 参考实现 — L39_fft_implement

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_fft(x: np.ndarray) -> np.ndarray:
    N = len(x)
    if N == 1:
        return x.astype(complex)
    E = my_fft(x[::2])            # 偶数下标子问题
    O = my_fft(x[1::2])           # 奇数下标子问题
    k = np.arange(N // 2)
    twiddle = np.exp(-2j * np.pi * k / N)  # 旋转因子
    top    = E + twiddle * O
    bottom = E - twiddle * O
    return np.concatenate([top, bottom])
```


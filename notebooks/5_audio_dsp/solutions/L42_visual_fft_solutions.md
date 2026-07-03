# 参考实现 — L42_visual_fft

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_fft_n8(x):
    """手工实现 N=8 的迭代式 Cooley-Tukey FFT（不调用任何 FFT 库）。"""
    N = 8
    assert len(x) == N, f"需要 N=8 输入，实际 N={len(x)}"

    # Step 1 — bit-reversal 置换
    bit_rev = [int(f'{i:03b}'[::-1], 2) for i in range(N)]
    X = np.array([x[bit_rev[i]] for i in range(N)], dtype=complex)

    # Step 2 — 三层蝶形迭代
    for s in range(3):
        half = 2 ** s
        group = 2 * half
        for g in range(N // group):
            for b in range(half):
                top = g * group + b
                bot = top + half
                W_k = np.exp(-2j * np.pi * b / group)  # 旋转因子
                t = X[top] + W_k * X[bot]
                X[bot] = X[top] - W_k * X[bot]
                X[top] = t
    return X
```

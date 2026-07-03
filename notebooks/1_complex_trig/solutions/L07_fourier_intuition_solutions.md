# 参考实现 — L07_fourier_intuition

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def square_approx(t, n):
    result = np.zeros_like(t)
    for k in range(1, 2*n, 2):
        result += (4 / (np.pi * k)) * np.sin(2 * np.pi * k * t)
    return result
```

> 注意系数 `4/(πk)`：少了 4/π，叠加结果只会收敛到 ±π/4 ≈ ±0.785，
> 而不是方波的 ±1（白板挑战对答案格会检查这一点）。


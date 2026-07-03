# 参考实现 — L05_complex_numbers

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def magnitude_phase(z):
    # 按练习要求：仅用 z.real, z.imag, np.sqrt, np.arctan2，不直接调 abs/np.angle
    mag = np.sqrt(z.real**2 + z.imag**2)   # |z| = √(a²+b²)
    phase = np.arctan2(z.imag, z.real)     # atan2 覆盖四象限，返回 (-π, π]
    return mag, phase
```


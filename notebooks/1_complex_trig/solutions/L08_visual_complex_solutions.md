# 参考实现 — L08_visual_complex

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def plot_conjugate(z):
    """在同一坐标轴上画出 z 和 z̄，图标题显示两者的模。"""
    import numpy as np
    import matplotlib.pyplot as plt

    z_conj = z.real - 1j * z.imag          # 共轭：虚部取反（关于实轴镜像）
    mag = np.sqrt(z.real**2 + z.imag**2)   # |z| = |z̄|

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    # z（箭头）
    ax.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1,
              color='#2A9D8F', label=f'z = {z.real:+.2f}{z.imag:+.2f}j')
    # z̄（箭头）
    ax.quiver(0, 0, z_conj.real, z_conj.imag, angles='xy', scale_units='xy', scale=1,
              color='#E76F51', label=f'z̄ = {z_conj.real:+.2f}{z_conj.imag:+.2f}j')

    lim = mag * 1.3 + 0.5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.legend(loc='lower right', fontsize=9)
    ax.set_title(f'|z| = {mag:.2f}')
    plt.tight_layout()
    plt.show()
    return fig, ax
```

**要点**
- 共轭只翻转虚部符号：`z̄ = a − bj`，几何上是关于实轴的镜像反射。
- 模不变：`|z| = |z̄| = √(a²+b²)`，两个箭头等长。
- `z · z̄ = a² + b² = |z|²` 为纯实数，所以断言 `(z * z̄).imag ≈ 0` 成立。

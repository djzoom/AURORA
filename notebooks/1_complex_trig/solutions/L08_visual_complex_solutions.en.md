# Reference implementation — L08_visual_complex

> ⚠️ Work through the exercise on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def plot_conjugate(z):
    """Draw z and z̄ on the same axes; the plot title shows their magnitude."""
    import numpy as np
    import matplotlib.pyplot as plt

    z_conj = z.real - 1j * z.imag          # conjugate: flip the imaginary part (mirror across the real axis)
    mag = np.sqrt(z.real**2 + z.imag**2)   # |z| = |z̄|

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    # z (arrow)
    ax.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1,
              color='#2A9D8F', label=f'z = {z.real:+.2f}{z.imag:+.2f}j')
    # z̄ (arrow)
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

**Key points**
- The conjugate only flips the sign of the imaginary part: `z̄ = a − bj`; geometrically, a mirror reflection across the real axis.
- The magnitude is unchanged: `|z| = |z̄| = √(a²+b²)`, so the two arrows have the same length.
- `z · z̄ = a² + b² = |z|²` is purely real, so the assert `(z * z̄).imag ≈ 0` holds.

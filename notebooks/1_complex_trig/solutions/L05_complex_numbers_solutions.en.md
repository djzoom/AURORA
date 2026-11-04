# Reference implementation — L05_complex_numbers

> ⚠️ Please complete the exercise on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def magnitude_phase(z):
    # As the exercise requires: only z.real, z.imag, np.sqrt, np.arctan2 — no direct abs/np.angle
    mag = np.sqrt(z.real**2 + z.imag**2)   # |z| = √(a²+b²)
    phase = np.arctan2(z.imag, z.real)     # atan2 covers all four quadrants, returns (-π, π]
    return mag, phase
```


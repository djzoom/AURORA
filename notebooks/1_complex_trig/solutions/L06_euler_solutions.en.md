# Reference implementation — L06_euler

> ⚠️ Please complete the exercise on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def twiddle(k, n, N):
    return np.exp(-2j * np.pi * k * n / N)
    # Equivalent form (assembled by hand):
    # theta = -2 * np.pi * k * n / N
    # return np.cos(theta) + 1j * np.sin(theta)
```


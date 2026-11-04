# Reference implementation — L07_fourier_intuition

> ⚠️ Work through the exercise on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def square_approx(t, n):
    result = np.zeros_like(t)
    for k in range(1, 2*n, 2):
        result += (4 / (np.pi * k)) * np.sin(2 * np.pi * k * t)
    return result
```

> Mind the coefficient `4/(πk)`: leave out the 4/π and the sum only converges to ±π/4 ≈ ±0.785,
> not the square wave's ±1 (the whiteboard challenge's answer-check cell checks this).

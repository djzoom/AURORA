# Reference implementation — L09_vectors

> ⚠️ Please finish the exercises on your own first, then look at the reference implementation.

## Reference implementation 1

```python
def scale(v, c):
    return c * v
```

## Reference implementation 2

```python
def add_signals(a, b):
    return a + b
```

## Reference implementation 3

```python
def linear_combination(coeffs, vecs):
    result = coeffs[0] * vecs[0]
    for c, v in zip(coeffs[1:], vecs[1:]):
        result = result + c * v
    return result
```

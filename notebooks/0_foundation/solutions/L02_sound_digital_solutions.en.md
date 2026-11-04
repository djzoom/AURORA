# Reference implementations — L02_sound_digital

> ⚠️ Work through the exercises on your own first, then look at the reference implementations.

## Reference implementation 1

`samples_count`: N = round(duration × sample_rate).

```python
def samples_count(duration, sample_rate):
    """Return the total number of samples N for a given duration and sample rate."""
    return round(duration * sample_rate)
```

## Reference implementation 2

`make_time_axis`: compute N first, then `np.arange(N) / sample_rate` (the first element is 0, the last is < duration).

```python
def make_time_axis(duration, sample_rate):
    N = samples_count(duration, sample_rate)
    return np.arange(N) / sample_rate
```

## Reference implementation 3

`make_sine`: `x(t) = amplitude · sin(2π · frequency · t)`.

```python
def make_sine(duration, sample_rate, frequency, amplitude=1.0):
    t = make_time_axis(duration, sample_rate)
    return amplitude * np.sin(2 * np.pi * frequency * t)
```

## Reference implementation 4

`signal_summary`: return length / shape / max_abs / mean / rms (RMS = √(mean(x²))).

```python
def signal_summary(x):
    return {
        'length':  len(x),
        'shape':   x.shape,
        'max_abs': float(np.max(np.abs(x))),
        'mean':    float(np.mean(x)),
        'rms':     float(np.sqrt(np.mean(x ** 2))),
    }
```

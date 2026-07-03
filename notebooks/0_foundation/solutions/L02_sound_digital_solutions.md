# 参考实现 — L02_sound_digital

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

`samples_count`：N = round(duration × sample_rate)。

```python
def samples_count(duration, sample_rate):
    """返回给定时长和采样率下的采样点总数 N。"""
    return round(duration * sample_rate)
```

## 参考实现 2

`make_time_axis`：先算 N，再 `np.arange(N) / sample_rate`（第一个元素为 0，末点 < duration）。

```python
def make_time_axis(duration, sample_rate):
    N = samples_count(duration, sample_rate)
    return np.arange(N) / sample_rate
```

## 参考实现 3

`make_sine`：`x(t) = amplitude · sin(2π · frequency · t)`。

```python
def make_sine(duration, sample_rate, frequency, amplitude=1.0):
    t = make_time_axis(duration, sample_rate)
    return amplitude * np.sin(2 * np.pi * frequency * t)
```

## 参考实现 4

`signal_summary`：返回 length / shape / max_abs / mean / rms（RMS = √(mean(x²))）。

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

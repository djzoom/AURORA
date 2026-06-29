# 参考实现 — L33_sine_wave

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_sine(freq, duration, sample_rate, amplitude=1.0):
    N = round(duration * sample_rate)
    n = np.arange(N)
    angle = 2 * np.pi * freq * n / sample_rate
    return amplitude * np.sin(angle)
```


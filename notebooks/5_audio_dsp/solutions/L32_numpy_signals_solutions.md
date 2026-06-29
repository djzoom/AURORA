# 参考实现 — L32_numpy_signals

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def time_axis(duration, sample_rate):
    N = round(duration * sample_rate)
    n = np.arange(N)
    return n / sample_rate
```


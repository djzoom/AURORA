# 参考实现 — L34_aliasing

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def predict_alias_freq(freq, sample_rate):
    k = round(freq / sample_rate)
    return abs(freq - k * sample_rate)
```


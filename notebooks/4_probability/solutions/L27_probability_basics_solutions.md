# 参考实现 — L27_probability_basics

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def estimate_prob_six(n, seed=0):
    rng = np.random.default_rng(seed)
    rolls = rng.integers(1, 7, size=n)
    return np.mean(rolls == 6)
```


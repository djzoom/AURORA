# 参考实现 — L29_distributions

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def gaussian_pdf(x, mu, sigma):
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    normalization = sigma * np.sqrt(2 * np.pi)
    return np.exp(exponent) / normalization
```


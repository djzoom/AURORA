# 参考实现 — L83_transformer

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.shape[-1]
    # (B, seq_q, seq_k)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(d_k)
    if mask is not None:
        scores = scores.copy()
        scores[mask] = -np.inf
    # softmax along seq_k axis
    scores -= scores.max(axis=-1, keepdims=True)  # 数值稳定（Numerical Stability）
    weights = np.exp(scores)
    weights /= weights.sum(axis=-1, keepdims=True)
    return weights @ V
```


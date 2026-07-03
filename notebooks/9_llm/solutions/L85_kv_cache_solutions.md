# 参考实现 — L85_kv_cache

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def scaled_dot_product_attention(Q, K, V, mask=None):
    """Scaled dot-product attention，纯 NumPy。

    Args:
        Q: (n_heads, seq_q, head_dim)
        K: (n_heads, seq_k, head_dim)
        V: (n_heads, seq_k, head_dim)
        mask: optional (seq_q, seq_k) bool mask，True=mask out

    Returns:
        (n_heads, seq_q, head_dim)
    """
    head_dim = Q.shape[-1]
    # 1) 打分：(n_heads, seq_q, seq_k)
    scores = Q @ K.swapaxes(-1, -2) / np.sqrt(head_dim)
    # 2) 因果掩码：屏蔽未来位置
    if mask is not None:
        scores = scores.copy()
        scores[..., mask] = -np.inf
    # 3) softmax（数值稳定：先减去每行最大值）
    scores -= scores.max(axis=-1, keepdims=True)
    weights = np.exp(scores)
    weights /= weights.sum(axis=-1, keepdims=True)
    # 4) 加权求和
    return weights @ V
```

## 参考实现 2

```python
    def update(self, layer, new_k, new_v):
        """Append 新 K/V 并返回完整缓存。new_k/new_v: (n_heads, 1, head_dim)"""
        if layer not in self._k:            # 首次调用：直接赋值
            self._k[layer] = new_k
            self._v[layer] = new_v
        else:                               # 后续调用：沿 seq 轴拼接
            self._k[layer] = np.concatenate([self._k[layer], new_k], axis=1)
            self._v[layer] = np.concatenate([self._v[layer], new_v], axis=1)
        return self._k[layer], self._v[layer]
```

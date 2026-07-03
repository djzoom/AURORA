# 参考实现 — L86_sampling

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — 任务 1：Top-k 采样

```python
def top_k_sample(logits, k=10, temperature=1.0):
    """从前 k 个 logit 最大的 token 中采样。"""
    logits = np.asarray(logits, dtype=np.float64)
    k = max(1, min(k, len(logits)))
    # 1) 找到 top-k 索引（argpartition 只保证第 -k 个位置是分界，速度 O(n)）
    top_idx = np.argpartition(logits, -k)[-k:]
    # 2) 其余 token 设为 -inf（softmax 后概率为 0）
    masked = np.full_like(logits, -np.inf)
    masked[top_idx] = logits[top_idx]
    # 3) softmax + 采样
    probs = softmax(masked, temperature)
    return int(np.random.choice(len(probs), p=probs))
```

## 参考实现 2 — 任务 2：Top-p（Nucleus）采样

```python
def top_p_sample(logits, p=0.9, temperature=1.0):
    """从累积概率 >= p 的最小 token 集中采样。"""
    logits = np.asarray(logits, dtype=np.float64)
    probs = softmax(logits, temperature)
    sorted_idx = np.argsort(probs)[::-1]
    sorted_probs = probs[sorted_idx]
    # 1) 累积概率
    cumulative = np.cumsum(sorted_probs)
    # 2) 找第一个使 cumsum >= p 的位置；+1 把它本身纳入 nucleus
    cutoff = int(np.searchsorted(cumulative, p)) + 1
    cutoff = max(1, min(cutoff, len(sorted_idx)))
    # 3) nucleus 内重归一化后采样
    nucleus_idx = sorted_idx[:cutoff]
    nucleus_probs = probs[nucleus_idx]
    nucleus_probs = nucleus_probs / nucleus_probs.sum()
    return int(np.random.choice(nucleus_idx, p=nucleus_probs))
```

## 闭卷推导参考答案 — top-p Nucleus（logits = [2.0, 1.0, 0.5, 0.1, -1.0]，p = 0.9）

1. **Softmax（数值稳定）**：先减去 max（=2.0）再取指数。
   - shifted = [0.0, -1.0, -1.5, -1.9, -3.0]
   - exp     = [1.000, 0.368, 0.223, 0.150, 0.050]
   - 归一化分母 ≈ 1.790
   - probs ≈ [0.559, 0.205, 0.125, 0.084, 0.028]

2. **按概率降序 + 累积概率**：

| 排名 | token index | prob  | cumsum |
|------|-------------|-------|--------|
| 1    | 0           | 0.559 | 0.559  |
| 2    | 1           | 0.205 | 0.764  |
| 3    | 2           | 0.125 | 0.889  |
| 4    | 3           | 0.084 | 0.972  |
| 5    | 4           | 0.028 | 1.000  |

3. **p = 0.9 的 nucleus**：cumsum 第一个 ≥ 0.9 的位置是排名 4（cumsum=0.972），
   所以 nucleus = 排名 1~4 的 token = **{0, 1, 2, 3}**（排除 token 4）。
</content>
</invoke>

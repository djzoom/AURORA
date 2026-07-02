# 参考实现 — L69_ctc_forward

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def log_softmax(logits, axis=-1):
    m = logits.max(axis=axis, keepdims=True)
    shifted = logits - m
    return shifted - np.log(np.exp(shifted).sum(axis=axis, keepdims=True))


def ctc_forward(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
    T, V = log_probs.shape
    lprime = [blank]
    for c in labels:
        lprime.append(c)
        lprime.append(blank)
    S = len(lprime)

    NEG_INF = -1e30
    alpha = np.full((T, S), NEG_INF)
    alpha[0, 0] = log_probs[0, lprime[0]]
    if S > 1:
        alpha[0, 1] = log_probs[0, lprime[1]]

    for t in range(1, T):
        for s in range(S):
            val = alpha[t - 1, s]
            if s > 0:
                val = np.logaddexp(val, alpha[t - 1, s - 1])
            if s > 1 and lprime[s] != lprime[s - 2]:
                val = np.logaddexp(val, alpha[t - 1, s - 2])
            alpha[t, s] = val + log_probs[t, lprime[s]]

    return float(np.logaddexp(alpha[-1, -1], alpha[-1, -2]))


def ctc_forward_brute_force(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
    from itertools import product

    T, V = log_probs.shape

    def collapse(path):
        result, prev = [], None
        for c in path:
            if c == blank:
                prev = None
            elif c != prev:
                result.append(c)
                prev = c
        return result

    log_p_list = []
    for path in product(range(V), repeat=T):
        if collapse(list(path)) == list(labels):
            lp = sum(log_probs[t, path[t]] for t in range(T))
            log_p_list.append(lp)

    if not log_p_list:
        return -1e30

    arr = np.array(log_p_list)
    m = arr.max()
    return float(m + np.log(np.exp(arr - m).sum()))
```
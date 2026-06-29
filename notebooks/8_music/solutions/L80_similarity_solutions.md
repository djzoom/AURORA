# 参考实现 — L80_similarity

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def find_similar(
    query_emb: np.ndarray,
    library_embs: np.ndarray,
    top_k: int = 5,
) -> tuple[np.ndarray, np.ndarray]:
    # L2 归一化
    q = query_emb / (np.linalg.norm(query_emb) + 1e-12)
    norms = np.linalg.norm(library_embs, axis=1, keepdims=True) + 1e-12
    L = library_embs / norms
    # 余弦相似度 = 内积（归一化后）
    scores = L @ q
    # top-k via argpartition
    top_k = min(top_k, len(scores))
    part_idx = np.argpartition(scores, -top_k)[-top_k:]
    # 对 top-k 内部排序（降序）
    order = np.argsort(scores[part_idx])[::-1]
    indices = part_idx[order]
    return indices, scores[indices]
```


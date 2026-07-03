# 参考实现 — L81_recommendation

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def recommend(
    user_history_ids: list[int],
    all_embs: np.ndarray,
    top_k: int = 10,
) -> np.ndarray:
    """基于 mean-embedding user profile 的余弦 k-NN 推荐。

    Args:
        user_history_ids: 用户喜欢的歌曲 id 列表；空列表触发冷启动
        all_embs:         (N, d) L2 归一化的歌曲 embedding
        top_k:            返回条数
    Returns:
        (top_k,) np.ndarray[int]，推荐歌曲 id，按相似度降序
    """
    # 步骤1：冷启动 — history 为空则用全库均值（几何中心）作中性出发点
    if len(user_history_ids) == 0:
        user_emb = all_embs.mean(axis=0)
    else:
        # 步骤2：user profile = 历史歌曲 embedding 的均值
        user_emb = all_embs[user_history_ids].mean(axis=0)

    # L2 归一化，使内积等价于余弦相似度
    user_emb = user_emb / (np.linalg.norm(user_emb) + 1e-8)

    # 步骤3：余弦相似度（embedding 已归一化，内积即余弦）
    scores = all_embs @ user_emb

    # 步骤4：过滤历史 — 置为 -inf 使其排到末尾，argsort 降序取 top_k
    scores = scores.copy()
    if len(user_history_ids) > 0:
        scores[user_history_ids] = -np.inf
    ranked = np.argsort(scores)[::-1]
    return ranked[:top_k]
```


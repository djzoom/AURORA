# 参考实现 — L91_visual_llm

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def find_top_pairs(A: np.ndarray, tokens: list, k: int = 3) -> list:
    """从注意力权重矩阵提取最强 token 关联对。

    Returns
    -------
    list of (query_token: str, key_token: str, weight: float)
        按 weight 降序，长度为 k。
    """
    # 步骤 1：展开所有 (i, j) 对及其权重
    pairs = [
        (tokens[i], tokens[j], float(A[i, j]))
        for i, j in np.ndindex(A.shape)
    ]
    # 步骤 2：按权重降序排序
    pairs.sort(key=lambda x: -x[2])
    # 步骤 3：取前 k 个
    return pairs[:k]
```

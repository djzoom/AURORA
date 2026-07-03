# 参考实现 — L67_edit_distance

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 · 字符级编辑距离 `edit_distance`

```python
def edit_distance(a, b) -> int:
    """字符级别 Levenshtein 编辑距离，纯 Python 动态规划。

    同样接受词列表（任何可索引序列），因此词级别 WER 也可复用此函数。
    dp[i][j] = 将 a[:i] 变成 b[:j] 的最小编辑次数
      边界：dp[i][0] = i（删除 a 前 i 个），dp[0][j] = j（插入 b 前 j 个）
      递推：a[i-1]==b[j-1] → dp[i-1][j-1]
             否则 → 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i          # 删除 a 的前 i 个字符
    for j in range(n + 1):
        dp[0][j] = j          # 插入 b 的前 j 个字符
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]          # 字符相同，免操作
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # 删除 a[i-1]
                    dp[i][j - 1],      # 插入 b[j-1]
                    dp[i - 1][j - 1],  # 替换
                )
    return dp[m][n]
```

## 参考实现 2 · 词级别 WER `wer`

```python
def wer(reference: str, hypothesis: str) -> float:
    """Word Error Rate = 词级别编辑距离 / 参考词数。

    关键设计：edit_distance 接受任意可索引序列，词列表同样适用；
    直接复用，无需重写 DP 循环——这是正确的代码抽象。
    """
    ref_words = reference.lower().split()
    hyp_words = hypothesis.lower().split()
    if len(ref_words) == 0:
        return 0.0 if len(hyp_words) == 0 else float('inf')
    # 复用 edit_distance：字符级和词级共用同一 DP 骨架，只换输入序列类型
    return edit_distance(ref_words, hyp_words) / len(ref_words)
```

## 参考答案 · 闭卷推导检查格（"cat" → "cut"）

**1. 递推公式**

```
边界： dp[i][0] = i,  dp[0][j] = j
递推： a[i-1] == b[j-1]  → dp[i][j] = dp[i-1][j-1]
       否则             → dp[i][j] = 1 + min(dp[i-1][j],    # 删除
                                             dp[i][j-1],    # 插入
                                             dp[i-1][j-1])  # 替换
```

**2. 完整 DP 表格（行=cat，列=cut）**

|   |   | c | u | t |
|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 |
| c | 1 | 0 | 1 | 2 |
| a | 2 | 1 | 1 | 2 |
| t | 3 | 2 | 2 | 1 |

- `dp[1][1]`：`c==c` → 取左上 `dp[0][0]=0`。
- `dp[2][2]`：`a≠u` → `1 + min(dp[1][2]=1, dp[2][1]=1, dp[1][1]=0) = 1`。
- `dp[3][3]`：`t==t` → 取左上 `dp[2][2]=1`。
- **编辑距离 = dp[3][3] = 1**。

**3. 一条最短编辑路径（从 dp[3][3] 回溯到 dp[0][0]）**

```
dp[3][3] (t==t, 匹配)  ← dp[2][2]
dp[2][2] (a→u, 替换)   ← dp[1][1]
dp[1][1] (c==c, 匹配)  ← dp[0][0]

对齐： c a t
       | S |
       c u t
路径：Match(c) → Sub(a→u) → Match(t)   共 1 次替换，距离 = 1
```

## 自评格参考填写（`l67_review`）

全部独立完成并通过后，5 项均填 `True`：

```python
l67_review = {
    "levenshtein_dp_memorized":  True,   # 能默写 DP 转移方程
    "edit_distance_impl":        True,   # edit_distance() 5 个断言全通过
    "wer_impl":                  True,   # wer() 复用 edit_distance
    "dp_table_traced":           True,   # 手推 "cat"→"cut" 4×4 DP 表
    "whiteboard_passed":         True,   # 白板推导格通关
}
```

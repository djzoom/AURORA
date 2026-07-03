---
tags: [aurora, concept, asr, interview]
aliases: [Edit Distance, 编辑距离, Levenshtein, 莱文斯坦距离, Levenshtein Distance]
domain: asr
whiteboard: ★★★★★
first_seen: L66
mastered: L67
---

# Edit-Distance · 编辑距离（Levenshtein Distance）

[[_lifecycle|← 生命周期总表]] · [[../domains/asr|← ASR 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把一个词改成另一个词，最少要几步"插入 / 删除 / 替换"——这个最少步数就是编辑距离，也是衡量"听错了多少"的尺子。

---

## 📖 定义
编辑距离（Levenshtein 距离）是**把字符串 A 变成字符串 B 所需的最少编辑操作数**，允许三种操作：**插入（Insertion）、删除（Deletion）、替换（Substitution）**，每种记 1 分。用动态规划求解：`dp[i][j]` 表示 A 前 i 个与 B 前 j 个的编辑距离，`dp[i][j] = dp[i-1][j-1]`（字符相同）或 `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`（分别对应删/插/替）。复杂度 `O(m×n)`。回溯对齐路径即可分出 S/D/I 各多少。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 判断识别结果对不对，不能只看"完全一致"——差一个字也要能量化差多少。
- **它解决了什么真实问题？** 给两个不等长的序列一个"相似度分数"，是 [[WER|词错误率]] 的数学地基，也是拼写纠错、DNA 比对的基础。
- Aurora 里 L67 从零写出 DP 表，L73 直接拿它算 WER 并分解 S/D/I。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L66  ASR 全览：如何量化"听错了多少"
拆解原理     L67  三种操作 + O(m×n) DP 表
真正掌握     L67  ★ 从零手写 DP 并回溯 S/D/I 对齐
再次使用     L73  WER = (S+D+I)/N 的核心计算
再次使用     L74  ASR 错误分析，逐词定位错因
最终应用     L72  Whisper 微调后的评估反馈信号
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学编辑距离之前你得先会
```
Edit-Distance
 ├─ 需要 → [[Dynamic-Programming|动态规划]]   (dp 表 + 状态转移)
 └─ 需要 → [[Recursion|递归]]/表格填充思维     (自底向上填表)
被谁依赖 → [[WER|词错误率]] → ASR 评估 / 错误分析
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[WER|词错误率]]** | 评估指标 | WER = 编辑距离 **÷ 参考词数**，编辑距离是它的分子 |
| **Hamming 距离** | 等长逐位比 | Hamming 只数替换、要求等长；编辑距离允许插/删、可不等长 |
| **[[CTC]] 前向对齐** | 概率求和 | CTC 对所有对齐**求概率和**；编辑距离求**最小操作数** |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — LeetCode 经典 + ASR 必考，必须做到：
- ✅ 闭卷写出状态转移 `dp[i][j]` 与边界 `dp[i][0]=i, dp[0][j]=j`
- ✅ 手写 O(m×n) DP，说清替换 / 插入 / 删除对应哪个前驱
- ✅ 回溯对齐路径，分出 S / D / I 三类操作数

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#ElevenLabs` `#ASR` `#Algorithm`
> 既是算法题（LeetCode 72）又是语音评估基石，双重高频。

## 🌍 现实系统里它在哪发挥作用
ASR 的 WER 评测 · 拼写检查 / 自动纠错 · 搜索的模糊匹配 · 生物信息学序列比对 · diff 工具

## 📚 出现于（反查）
[[../lessons/L66]] · **[[../lessons/L67]]** · [[../lessons/L72]] · [[../lessons/L73]] · [[../lessons/L74]]

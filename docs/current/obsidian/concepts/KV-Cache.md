---
tags: [aurora, concept, llm, interview]
aliases: [KV-Cache, 键值缓存, KV 缓存, Key-Value Cache]
domain: llm
whiteboard: ★★★★★
first_seen: L85
mastered: L85
---

# KV-Cache · 键值缓存（Key-Value Cache）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：自回归生成时把每个已算过词的 K、V 存起来，生成下一个词就不用把整段历史重算一遍——总计算量从 O(seq²) 降到 O(seq)。

---

## 📖 定义
KV-Cache 是 [[Transformer]] 解码器**推理阶段**的加速技巧。自回归生成时，每步只新增一个 token，但注意力需要它去看**全部历史**的键 K 和值 V。这些历史 K/V 不随新 token 改变，于是把每层、每个头算过的 K、V **缓存**下来；下一步只需为新 token 计算它自己的 q、k、v，把新 k/v 追加进缓存，再对整个缓存做注意力。省掉的是历史 token 的**投影与重算**代价。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 每生成一个词都要把前面所有词的 K/V 从头重算，第 t 步做 O(t) 工作，整段生成 O(seq²)，越写越慢、显卡空转。
- **它解决了什么真实问题？** 这正是"为什么 ChatGPT 每次回复越答越快"的答案——缓存让每步降到 O(1) 新增计算，总成本 O(seq)，长对话才跑得动。
- **代价是显存**：缓存大小 = `T × n_layers × n_heads × head_dim`，长序列显存吃紧——这就是 vLLM、PagedAttention 要精细管理这块内存的原因。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
前置铺垫     L83  注意力的 K/V 从哪来（投影矩阵）
正式动机     L85  自回归重算 → O(seq²) 越答越慢
拆解原理     L85  缓存历史 K/V，新 token 只算自己
真正掌握     L85  ★ 从零实现 KVCache，实测提速
再次使用     L86  采样解码循环里每步复用缓存
再次使用     L87  本地推理：缓存 + 量化一起省显存
最终应用          vLLM / PagedAttention 的核心数据结构
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 KV-Cache 之前你得先会
```
KV-Cache
 ├─ 需要 → [[Self-Attention|注意力的 K/V]]      (L83)
 ├─ 需要 → [[Transformer|自回归解码器]]         (L83)
 └─ 需要 → 复杂度分析 O(seq) vs O(seq²)
被谁依赖 → [[Sampling|采样解码]] · 本地/服务端 LLM 推理 · vLLM
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **省投影 vs 省注意力** | 缓存省重算 K/V vs 注意力仍要算 | KV-Cache 省的是**投影**，新 token 对全缓存的注意力仍是 O(t) |
| **训练 vs 推理** | 只在推理用 | 训练是并行 teacher-forcing，不需要逐步缓存 |
| **KV-Cache vs 量化** | 省重复计算 vs 省存储位宽 | 一个砍时间、一个砍显存，常一起用 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷推导：无缓存 O(seq²) vs 有缓存 O(seq) 的来历
- ✅ 说清缓存的正是**注意力的 K 和 V**，Q 每步新算
- ✅ 算出显存代价 `T×n_layers×n_heads×head_dim`，点出长序列瓶颈

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#NVIDIA` `#Meta` `#Google-DeepMind` `#LLM-Infra`
> LLM 推理优化岗必问，紧跟着就是 PagedAttention / 连续批处理。

## 🌍 现实系统里它在哪发挥作用
ChatGPT / Claude 逐字流式输出 · vLLM · TensorRT-LLM · llama.cpp · 所有生产级 LLM 推理服务

## 📚 出现于（反查）
**[[../lessons/L85]]** · [[../lessons/L86]] · [[../lessons/L87]]

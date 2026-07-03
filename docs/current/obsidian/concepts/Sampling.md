---
tags: [aurora, concept, llm, interview]
aliases: [Sampling, 采样策略, 解码采样, temperature, 温度, top-k, top-p, Nucleus Sampling, 核采样]
domain: llm
whiteboard: ★★★★★
first_seen: L71
mastered: L86
---

# Sampling · 采样策略（Temperature / Top-k / Top-p 解码）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：生成下一个词时不总是挑概率最高的那个——用 temperature 调随机程度、用 top-k/top-p 圈定候选范围，让输出既通顺又不呆板重复。

---

## 📖 定义
自回归模型每步输出一个词表上的概率分布，采样决定"怎么从中选下一个词"。
- **Temperature T**：把 logits 除以 T 再 softmax。`T<1` 更尖锐（更保守），`T>1` 更平坦（更随机），`T→0` 退化成贪婪。
- **Top-k**：只保留概率最高的 k 个词，重新归一化后再采样。
- **Top-p（Nucleus/核采样）**：按概率从高到低累加，取累计概率刚超过 p 的最小词集再采样——候选池大小随分布自适应。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 永远选最高概率（贪婪解码）会陷入死循环、重复啰嗦，"一本正经地说废话"；纯随机采样又会蹦出离谱的词。
- **它解决了什么真实问题？** 用温度控制"任性程度"，用 top-k/top-p 砍掉长尾垃圾词——在**通顺**和**多样**之间找到平衡，让 AI 说话像人。
- **温度的数学早学过**：就是 softmax 加了个缩放旋钮，和 L30 的 softmax 一脉相承。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L71  Whisper 解码：贪婪解码 vs beam search
正式动机     L86  贪婪会重复、纯随机会离谱
拆解原理     L86  temperature 缩放 → top-k 截断 → top-p 核
真正掌握     L86  ★ 纯 NumPy 手写 top-k / top-p，闭卷推导 nucleus
再次使用     L87  本地推理时调温度/采样参数
最终应用          聊天机器人、创意写作、代码生成的解码控制
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学采样之前你得先会
```
Sampling
 ├─ 需要 → [[Softmax]]（logits→概率）          (L30)
 ├─ 需要 → [[Probability-Distribution|概率分布]] (L29)
 ├─ 需要 → [[Transformer|自回归解码器]]         (L83)
 └─ 依赖搭档 → [[KV-Cache]]（每步复用缓存）      (L85)
被谁依赖 → 本地/服务端 LLM 推理 · 对话/写作/代码生成
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **Top-k vs Top-p** | 固定 k 个 vs 自适应累计到 p | top-p 候选池随分布确定度伸缩，通常比固定 k 更稳 |
| **Temperature vs Top-p** | 调分布形状 vs 裁候选集 | 温度改概率斜率，top-p 直接砍长尾，可叠加使用 |
| **贪婪/Beam vs 采样** | 找最可能 vs 有控制随机 | 贪婪/beam 求"最优"，采样求"自然多样" |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷写出 temperature 缩放式与 top-p 的"累计概率取最小集"推导
- ✅ 解释贪婪解码为何重复、温度如何缓解
- ✅ 说清 top-k 与 top-p 的区别与各自失效场景

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#Meta` `#ElevenLabs` `#NVIDIA` `#LLM`
> "解码策略怎么选" 是 LLM 岗必问，紧接 KV-Cache 一起考。

## 🌍 现实系统里它在哪发挥作用
ChatGPT / Claude 的 temperature/top_p 参数 · 代码补全（低温）· 创意写作（高温）· API 采样控制

## 📚 出现于（反查）
[[../lessons/L71]] · **[[../lessons/L86]]** · [[../lessons/L87]]

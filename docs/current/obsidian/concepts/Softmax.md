---
tags: [aurora, concept, probability, interview]
aliases: [Softmax, softmax, 软最大, 归一化指数, softmax(z)]
domain: probability
whiteboard: ★★★★
first_seen: L29
mastered: L30
---

# Softmax · 软最大（Softmax）

[[_lifecycle|← 生命周期总表]] · [[../domains/probability|← Probability 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把模型吐出的一排任意分数（可以是负数、加起来不为 1）压成一个合法概率分布——每项都在 0~1 之间、加起来正好等于 1。

---

## 📖 定义
Softmax 把 logits 向量 `z` 变成概率分布：`softmax(z)_i = e^{z_i} / Σ_j e^{z_j}`。指数保证每项为正，除以总和保证加和为 1。**数值稳定版**先减去最大值 `z − max(z)` 再取指数——结果不变（分子分母同除 `e^{max}`），但避免 `exp` 溢出（z>709 → inf）。它光滑可导，因此损失能一路反传到每个 logit。

## 🤔 为什么工程师要发明它（Layer 9）
> 复用自 L30「为什么工程师要发明它？」：

- **不用它会怎样？** 模型最后一层吐出的是 `[2.0, 1.0, 0.1]` 这种任意实数（logits），可能为负、加和不为 1，没法当"我有多确定"来读，也没法跟标签比对算损失。
- **它解决了什么真实问题？** softmax 把这排分数压成一个合法概率分布（每项 ∈ (0,1)、加和为 1），再配合交叉熵变成可求导的标量损失。
- **后面哪里还会再用到？** 几乎每个分类网络的最后两行——KWS（L63/L64）、ASR 解码、LLM 预测下一个 token。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L29  分布里概率要"加和为 1"的直觉
正式动机     L30  logits 不是概率，需要一层转换
真正掌握     L30  ★ 手写数值稳定 softmax + 手推梯度 dL/dz = p − y
再次使用     L64  KWS 分类器输出层 + argmax 预测
再次使用     L68/L69  CTC 每帧对齐概率
再次使用     L71  Whisper 解码取 token 概率
再次使用     L83  Transformer 注意力权重 = softmax(QKᵀ/√d)
最终应用     L86  LLM 采样：温度缩放后的 softmax
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 softmax 之前你得先会
```
Softmax
 ├─ 需要 → [[Probability-Distribution|概率分布]]  (L29)
 ├─ 需要 → exp / 指数函数
 └─ 需要 → 数值稳定（减 max 防溢出）              (L30)
被谁依赖 → [[Cross-Entropy|交叉熵]] → [[Self-Attention|注意力]] → LLM 采样
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **归一化（normalize）** | 除以总和 | softmax 先**取指数**再归一化，放大差距且恒为正 |
| **argmax** | 取最大那格 | softmax 是**软**的、可导；argmax 是硬的、不可导 |
| **sigmoid** | 单个值→(0,1) | softmax 是**多类**版，整排一起归一 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 分类/注意力/LLM 都用，必须做到：
- ✅ 写出 `softmax(z)_i = e^{z_i}/Σe^{z_j}`，并解释为何**先减 max**
- ✅ 手推与交叉熵合起来的梯度 `dL/dz_i = p_i − y_i`
- ✅ 说清"软最大 vs argmax"的可导性区别

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#ElevenLabs` `#NVIDIA` `#ML-Fundamentals`
> 数值稳定性（减 max）是经典 follow-up。

## 🌍 现实系统里它在哪发挥作用
每个分类器输出层 · Transformer 注意力 · LLM 下一 token 分布 · Whisper 解码 · CTC 对齐

## 📚 出现于（反查）
[[../lessons/L29]] · **[[../lessons/L30]]** · [[../lessons/L64]] · [[../lessons/L68]] · [[../lessons/L69]] · [[../lessons/L71]] · [[../lessons/L83]] · [[../lessons/L86]]

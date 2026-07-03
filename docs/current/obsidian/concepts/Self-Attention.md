---
tags: [aurora, concept, llm, interview]
aliases: [Attention, Self-Attention, 注意力, 自注意力, Scaled Dot-Product Attention, 交叉注意力, Cross-Attention]
domain: llm
whiteboard: ★★★★★
first_seen: L70
mastered: L83
---

# Self-Attention · 注意力（Attention / Self-Attention）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：让句子里每个词一步之内直接"看到"全句任意词，用相似度决定该关注谁——这就是大模型能读懂上下文的核心机制。

---

## 📖 定义
注意力是一种**加权求和**机制：每个词发出一个查询向量 **Q**，和所有词的键向量 **K** 做点积算相似度，除以 `√d_k` 缩放后过 **softmax** 变成权重，再对值向量 **V** 加权求和。公式 `Attention(Q,K,V) = softmax(QKᵀ/√d_k)·V`。当 Q、K、V 都来自同一句话时叫**自注意力**；Q 来自解码器、K/V 来自编码器时叫**交叉注意力**。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** RNN 逐词串行读句子，读到句尾时开头的词早被反复稀释，翻译长句频频"忘词"，而且必须一个词一个词地算，没法并行加速。
- **它解决了什么真实问题？** attention 让每个词在一步之内直接"看到"全句任意词，用相似度决定该看谁——长程依赖 + 并行训练一次解决。
- **后面哪里还会再用到？** LoRA 就贴在注意力的投影矩阵旁、KV-Cache 缓存的正是注意力的 K/V、agent 靠它推理、可视化课把注意力权重画成热力图。它是后面所有大模型课的同一块地基。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L70  Whisper 解码器的交叉注意力（听声音→写字）
正式动机     L83  RNN 串行会忘词，attention 一步看全句
拆解原理     L83  Q·Kᵀ → 缩放 → softmax → 加权 V
真正掌握     L83  ★ 从零手写 scaled dot-product attention
再次使用     L84  LoRA 贴在 Q/K/V/O 投影矩阵旁
再次使用     L85  KV-Cache 缓存的正是 K/V
再次使用     L90  agent 推理循环
最终应用     L91  把注意力权重画成热力图（闭卷推导注意力数学）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学注意力之前你得先会
```
Self-Attention
 ├─ 需要 → [[Dot-Product|点积]]（算相似度）      (L10)
 ├─ 需要 → [[Softmax]]（分数变权重）             (L30)
 ├─ 需要 → [[Matrix|矩阵乘法]]                   (L12)
 └─ 需要 → [[Embedding|词向量]]                  (L79)
被谁依赖 → [[Transformer]] → [[KV-Cache]] / [[LoRA]] → [[RAG]] / agent
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **Self vs Cross Attention** | Q/K/V 同源 vs Q 与 K/V 异源 | 自注意力"句内互看"，交叉注意力"解码器看编码器" |
| **Attention vs 全连接层** | 权重由数据算 vs 权重是固定参数 | 注意力权重**随输入现算**，全连接权重训练完就冻住 |
| **Attention ≠ 玄乎的加权平均** | ❌ | 权重完全由 **Q·Kᵀ** 相似度经 softmax 决定，没有魔法 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷写出 `softmax(QKᵀ/√d_k)·V` 并讲清每一步维度
- ✅ 解释为何要除以 `√d_k`（防止点积过大导致 softmax 饱和）
- ✅ 说清 self / cross / multi-head 的区别

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#Google-DeepMind` `#Meta` `#ElevenLabs` `#NVIDIA` `#LLM`
> 大模型岗第一白板题，几乎必考。

## 🌍 现实系统里它在哪发挥作用
GPT / Claude / Gemini · Whisper · Stable Diffusion（cross-attention）· BERT 检索 · 几乎所有现代 LLM 与多模态模型

## 📚 出现于（反查）
[[../lessons/L70]] · **[[../lessons/L83]]** · [[../lessons/L84]] · [[../lessons/L85]] · [[../lessons/L90]] · [[../lessons/L91]]

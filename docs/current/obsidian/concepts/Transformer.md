---
tags: [aurora, concept, llm, interview]
aliases: [Transformer, 变换器, Encoder-Decoder, 自回归 Transformer]
domain: llm
whiteboard: ★★★★★
first_seen: L70
mastered: L83
---

# Transformer · 变换器（Transformer）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：一种完全靠注意力、彻底扔掉 RNN 的网络架构——能并行读整句话，是今天所有大模型（GPT、Claude、Whisper）的共同骨架。

---

## 📖 定义
Transformer 是 2017 年《Attention Is All You Need》提出的架构，用**堆叠的相同模块**处理序列。每个模块 = **多头自注意力（[[Self-Attention|注意力]]）+ 前馈网络（FFN）**，外加**残差连接**和 **LayerNorm**。位置信息靠**位置编码**注入。分编码器（双向看全句）和解码器（自回归、带因果掩码只能看左边）两类，可单用也可组合成 Encoder-Decoder。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** RNN/LSTM 逐词串行，长句训练慢又健忘；卷积只能看局部窗口。
- **它解决了什么真实问题？** 用注意力让任意两个词一步互通，**训练可完全并行**——这才让"喂海量数据、堆到千亿参数"变得现实，直接催生了 GPT 时代。
- **后面哪里还会再用到？** LoRA 微调它、KV-Cache 加速它的推理、RAG/agent 把它当生成引擎。它是整个 LLM 单元的地基。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L70  Whisper = Conv1D×2 → Transformer 编码器 + 解码器
再次露面     L71  自回归解码（贪婪 / beam）跑的就是它
正式动机     L83  RNN 会忘词、没法并行 → 注意力堆叠
拆解原理     L83  多头注意力 + FFN + 残差 + LayerNorm
真正掌握     L83  ★ 从零搭一个 Transformer block
再次使用     L84  LoRA 只微调它的投影矩阵
再次使用     L85  KV-Cache 加速它的自回归推理
最终应用     L90  agent 用它做推理引擎 / L91 可视化内部
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 Transformer 之前你得先会
```
Transformer
 ├─ 需要 → [[Self-Attention|注意力]]（核心积木）   (L83)
 ├─ 需要 → [[Softmax]] + [[Cross-Entropy|交叉熵]]  (L30)
 ├─ 需要 → [[MLP|前馈网络]] + [[Backpropagation|反向传播]] (L57)
 └─ 需要 → [[LayerNorm|层归一化]] / [[Residual|残差]]
被谁依赖 → [[LoRA]] · [[KV-Cache]] · [[Sampling|采样]] · [[RAG]] · Whisper · agent
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **Transformer vs Attention** | 整栋楼 vs 一块砖 | 注意力是模块，Transformer 是把它堆起来的完整架构 |
| **Encoder vs Decoder** | 双向看全句 vs 自回归只看左 | 编码器理解（BERT/Whisper-enc），解码器生成（GPT） |
| **Transformer vs RNN** | 并行 + 全局 vs 串行 + 健忘 | Transformer 一步连通全句，RNN 得一个词一个词传 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷画出一个 Transformer block 的数据流（Attn→Add&Norm→FFN→Add&Norm）
- ✅ 讲清残差、LayerNorm、位置编码各自解决什么问题
- ✅ 说清 encoder-only / decoder-only / enc-dec 三种形态与代表模型

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#Google-DeepMind` `#Meta` `#NVIDIA` `#ElevenLabs` `#LLM`
> 大模型/多模态岗必考架构题。

## 🌍 现实系统里它在哪发挥作用
GPT-4 / Claude / Gemini / Llama · Whisper · ViT · Stable Diffusion · AlphaFold · 几乎所有前沿 AI 模型

## 📚 出现于（反查）
[[../lessons/L70]] · [[../lessons/L71]] · **[[../lessons/L83]]** · [[../lessons/L84]] · [[../lessons/L85]] · [[../lessons/L90]] · [[../lessons/L91]]

---
tags: [aurora, concept, llm, interview]
aliases: [Quantization, 量化, INT8, INT8 量化, INT4, 低精度推理]
domain: llm
whiteboard: ★★★★
first_seen: L87
mastered: L87
---

# Quantization · 量化（INT8 Quantization）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把模型权重从 32 位小数压成 8 位整数，体积和显存直接缩到 1/4，而精度几乎不掉——这就是 7B 大模型能塞进笔记本的原因。

---

## 📖 定义
量化把高精度浮点权重映射到低位宽整数。对称 INT8 量化：`scale = max|W| / 127`，`W_int8 = round(W / scale)`（截断到 [-127,127]）；用时反量化 `W ≈ scale · W_int8`。32-bit → 8-bit 存储缩 4 倍，误差来自舍入（量化步长 = scale）。位宽越低误差越大：INT4 只有 16 个格子，误差约为 INT8 的 16 倍，需要特殊校正。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 一个 7B 模型 FP32 要 28 GB 显存，普通笔记本、手机根本装不下，更别说实时推理。
- **它解决了什么真实问题？** 8-bit 让同一个模型显存/体积砍到 1/4，配合 KV-Cache 就能在消费级硬件甚至端侧本地跑——隐私、离线、低延迟一次到位。
- **代价是精度**：舍入引入量化误差，但权重分布集中、模型有冗余，INT8 通常几乎无损，INT4 才需要分组/校正技巧。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
正式动机     L87  7B 模型为什么能跑在笔记本上
拆解原理     L87  scale=max|W|/127，round 到 INT8
真正掌握     L87  ★ 手写 quantize，画 bits→误差曲线
再次使用     L87  连接 HuggingFace 本地 INT8 推理
最终应用     L94  demo 里用量化模型做端侧推理
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学量化之前你得先会
```
Quantization
 ├─ 需要 → [[Rounding|舍入与相对误差]]
 ├─ 需要 → [[Matrix|权重矩阵]]              (L12)
 └─ 需要 → 浮点 vs 整数表示
被谁依赖 → 本地/端侧 LLM 推理 · QLoRA · 边缘部署
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **量化 vs 剪枝** | 降位宽 vs 删权重 | 量化让每个数更省位，剪枝直接扔掉一些权重 |
| **量化 vs 蒸馏** | 压缩表示 vs 换小模型 | 量化不改结构，蒸馏训练一个更小的新模型 |
| **INT8 vs INT4** | 256 格 vs 16 格 | 位越低越省但误差涨约 16 倍，INT4 要校正 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★（高）** — 必须做到：
- ✅ 闭卷写出 `scale = max|W|/127`、`W_int8 = round(W/scale)`、反量化式
- ✅ 算显存/体积压缩比（FP32→INT8 = 4×）
- ✅ 说清位宽降低与量化误差的关系（步长 ∝ 1/2^bits）

## 💼 面试标签（Layer 7）
`#interview` `#NVIDIA` `#Apple` `#Qualcomm` `#Meta` `#OpenAI` `#LLM-Infra` `#Edge-AI`
> 端侧/推理优化岗高频，常和 KV-Cache、LoRA 一起考。

## 🌍 现实系统里它在哪发挥作用
llama.cpp / GGUF · bitsandbytes INT8 · QLoRA · Apple Neural Engine · 手机端 Whisper/LLM · TensorRT

## 📚 出现于（反查）
**[[../lessons/L87]]** · [[../lessons/L94]]

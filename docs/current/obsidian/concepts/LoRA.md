---
tags: [aurora, concept, llm, interview]
aliases: [LoRA, 低秩适配, Low-Rank Adaptation, 低秩分解微调]
domain: llm
whiteboard: ★★★★★
first_seen: L72
mastered: L84
---

# LoRA · 低秩适配（Low-Rank Adaptation）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：微调大模型时不去改那张巨大的原权重，只在旁边贴一对小小的低秩矩阵 `B·A` 来学新东西——可训练参数省掉 97~99%。

---

## 📖 定义
LoRA 假设"微调带来的权重改变量 **ΔW** 其实是低秩的"，于是把 `ΔW` 分解成两个瘦长矩阵之积：`ΔW = B·A`，其中 `A∈ℝ^{r×d}`、`B∈ℝ^{d×r}`，秩 `r≪d`。前向传播变成 `h = Wx + (B·A)x`，**原权重 W 冻结不动**，只训练 A、B。初始化时 `B=0`（保证起步 `ΔW=0`、无扰动启动），`A~N(0,0.01)`（打破对称性）。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 全参数微调一个 7B 模型要更新 70 亿参数，显存爆炸、每个任务都存一整份权重，个人根本玩不起。
- **它解决了什么真实问题？** 只训练 0.1% 的参数就能改变模型的"性格"，一张消费级显卡即可微调，每个任务只存几 MB 的 A/B 便利贴，随插随换。
- **依赖的数学早就学过**：低秩分解就是 SVD 那套"任何矩阵 ≈ 少数几个秩一矩阵之和"的思想（L14）。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
数学种子     L14  SVD：低秩 = 压缩，一把打开低秩世界的钥匙
第一次露面   L72  微调 Whisper 时提出用 LoRA 省参数
正式动机     L84  全参微调太贵 → 只学低秩增量 ΔW
拆解原理     L84  ΔW=B·A，B=0 起步、A 高斯破对称
真正掌握     L84  ★ 从零实现 LoRALinear，验证参数量 ↓97%
再次使用     L91  画出 LoRA 低秩结构图（B·A 的形状）
最终应用          领域微调 / 多任务热插拔适配器
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 LoRA 之前你得先会
```
LoRA
 ├─ 需要 → [[SVD|奇异值分解 / 低秩]]       (L14)
 ├─ 需要 → [[Matrix|矩阵乘法与秩]]         (L12/L13)
 ├─ 需要 → [[Self-Attention|注意力投影矩阵]] (L83, LoRA 贴在这)
 └─ 需要 → [[Backpropagation|反向传播]]     (L56)
被谁依赖 → 参数高效微调（PEFT）· 领域适配 · 多适配器路由
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **LoRA vs 全参微调** | 只训 B·A vs 训全部权重 | LoRA 冻结 W，只学低秩增量，省 97%+ 参数 |
| **LoRA vs 量化(QLoRA)** | 省训练参数 vs 省存储位宽 | 二者正交，QLoRA = 4-bit 量化底模 + LoRA 微调 |
| **秩 r 的作用** | 容量旋钮 | r 越大越能拟合但越贵；太小欠拟合，需实验取舍 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷推导参数量：全参 `d×d` vs LoRA `2×r×d`，算出压缩比
- ✅ 解释为何 `B=0` 初始化（无扰动启动，保留预训练知识）
- ✅ 说清 LoRA 贴在 Transformer 的哪些矩阵（Q/K/V/O 投影）

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#Meta` `#HuggingFace` `#ElevenLabs` `#NVIDIA` `#LLM`
> "如何低成本微调大模型" 的标准答案，PEFT 必问。

## 🌍 现实系统里它在哪发挥作用
HuggingFace PEFT · Stable Diffusion 的画风 LoRA · 语音克隆微调 · 企业私有领域适配 · QLoRA 单卡微调

## 📚 出现于（反查）
[[../lessons/L14]] · [[../lessons/L72]] · **[[../lessons/L84]]** · [[../lessons/L91]]

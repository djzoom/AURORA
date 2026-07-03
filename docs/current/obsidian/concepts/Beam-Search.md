---
tags: [aurora, concept, asr, interview]
aliases: [Beam Search, 集束搜索, 束搜索, beam width, 贪婪解码, greedy decoding]
domain: asr
whiteboard: ★★★★
first_seen: L66
mastered: L71
---

# Beam-Search · 集束搜索（Beam Search）

[[_lifecycle|← 生命周期总表]] · [[../domains/asr|← ASR 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：每步只留下最好的 K 条候选句子继续往下扩展——比"每步都选最高分"更聪明，又比"枚举所有可能"便宜得多。

---

## 📖 定义
集束搜索是**序列解码的近似最优搜索算法**。自回归模型每步都对下一个 token 给出概率分布；beam search 维护 **beam width = K** 条得分最高的部分序列（beam），每步把每条 beam 扩展所有候选、按累计对数概率排序、只保留 top-K，直到遇到结束符。K=1 时退化成**贪婪解码（greedy）**；K→∞ 时逼近穷举最优。它在"贪婪的短视"和"穷举的爆炸"之间取折中。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 贪婪解码每步只挑当前最高分，一步走错就再也回不了头，容易输出局部最优的烂句子。
- **它解决了什么真实问题？** 用可控的 K 保留多条候选，显著提升整句概率（尤其对 ASR / 翻译这种全局连贯很重要的任务）。
- Aurora 里 L71 用它让 Whisper "开口说话"：对比贪婪与 width=2 的 beam，看输出质量差异。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L66  ASR 全览：解码器怎么把概率变成文字
正式动机     L71  贪婪解码的短视问题
拆解原理     L71  维护 K 条 beam，累计 log-prob 剪枝
真正掌握     L71  ★ 手写 width=2 beam search
再次使用     L72  Whisper 微调后的解码
对比出现     L86  LLM 采样（temperature/top-k/top-p）另一条路线
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 beam search 之前你得先会
```
Beam-Search
 ├─ 需要 → [[Softmax]]                     (每步 token 概率)
 ├─ 需要 → [[Log-Probability|对数概率]]     (累计得分, 防下溢)
 └─ 需要 → 自回归解码（AR）                 (L71, 逐 token 生成)
被谁依赖 → [[Whisper]] 解码 · 神经机器翻译 · 语音合成对齐
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **贪婪解码 greedy** | K=1 特例 | beam search 保留 **K 条**，greedy 只留 1 条 |
| **采样 sampling** | 按概率随机抽 | beam 追求**高概率/确定性**，采样追求**多样性** (L86) |
| **[[CTC]] 前向** | 训练时求和 | CTC 对齐求**概率和**；beam search 解码时求**最优序列** |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 常见算法面试，必须做到：
- ✅ 讲清 beam width 的作用与 greedy(K=1)/穷举(K=∞) 两个极端
- ✅ 手写维护 top-K beam 的扩展—打分—剪枝循环
- ✅ 说明为什么用**累计对数概率**（防浮点下溢）与长度惩罚

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Google` `#Meta` `#ElevenLabs` `#ASR` `#NLP`
> ASR / 机器翻译 / TTS 解码的通用工具，能手写是加分。

## 🌍 现实系统里它在哪发挥作用
Whisper / Google Speech 解码 · 神经机器翻译（Transformer NMT）· 语音合成对齐 · 早期 GPT 生成

## 📚 出现于（反查）
[[../lessons/L66]] · [[../lessons/L68]] · [[../lessons/L70]] · **[[../lessons/L71]]** · [[../lessons/L72]]

---
tags: [aurora, concept, asr, interview]
aliases: [WER, 词错误率, Word Error Rate, S/D/I]
domain: asr
whiteboard: ★★★
first_seen: L66
mastered: L73
---

# WER · 词错误率（Word Error Rate）

[[_lifecycle|← 生命周期总表]] · [[../domains/asr|← ASR 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把语音识别结果和标准答案对齐，数出替换、删除、插入几个词，除以标准答案的词数——这就是衡量 ASR 好坏的头号指标。

---

## 📖 定义
词错误率是**语音识别质量的标准评估指标**：`WER = (S + D + I) / N`，其中 S=替换（Substitution）、D=删除（Deletion）、I=插入（Insertion）、N=参考文本的总词数。S/D/I 通过对参考串与识别串做 [[Edit-Distance|词级编辑距离]] 得到。WER 可以 >100%（插入过多时）。它诊断的是"错在哪一类"——替换多说明声学模型弱，插入/删除多常与解码或对齐有关。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** "识别得挺准"是主观感受，没法比较两个模型、没法追踪训练是否进步。
- **它解决了什么真实问题？** 给 ASR 一个客观、可复现、可分解的数字，让"病因诊断"成为可能——同样 15% 错误率，替换多还是删除多，修复路线完全不同（L73）。
- Aurora 里 L73 产出 `analyze_errors()`，为 Whisper 微调循环提供量化反馈。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L66  ASR 全览：怎么衡量识别系统好坏
正式动机     L67  编辑距离搭好数学地基（WER 的分子）
拆解原理     L73  按 S/D/I 分解、逐句长尾分析
真正掌握     L73  ★ 手算 WER 并分类三种错误
再次使用     L74  错误分析：从 WER 数字到修复路线
再次使用     L72  Whisper 微调前后的效果对比
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 WER 之前你得先会
```
WER
 ├─ 需要 → [[Edit-Distance|编辑距离]]     (S/D/I 来源, L67)
 └─ 需要 → 词级对齐/回溯                    (分类三种错误)
被谁依赖 → ASR 错误分析 · 微调评估 · 模型选型
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[Edit-Distance|编辑距离]]** | 原始操作数 | WER = 编辑距离 **÷ N**，是归一化后的比率 |
| **CER（字错误率）** | 字符级 | 同一公式，粒度换成字符/汉字；中文常用 CER |
| **accuracy** | 分类准确率 | WER 处理**不等长序列对齐**，不是简单逐位比对 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★（理解 + 应用）** — 必须做到：
- ✅ 写出公式 `WER = (S+D+I)/N` 并解释每个符号
- ✅ 给一对句子，手动对齐并数出 S/D/I、算出 WER
- ✅ 说明为什么 WER 可能 >100%，以及 S/D/I 各自暗示的病因

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Google` `#ElevenLabs` `#Meta` `#ASR`
> 语音岗必问的"你怎么评估模型"，答得出 S/D/I 分解是加分项。

## 🌍 现实系统里它在哪发挥作用
Whisper / Google Speech / 讯飞等所有 ASR 的官方 benchmark · 语音助手上线前的验收指标 · 数据集排行榜（LibriSpeech WER）

## 📚 出现于（反查）
[[../lessons/L66]] · [[../lessons/L67]] · [[../lessons/L72]] · **[[../lessons/L73]]** · [[../lessons/L74]]

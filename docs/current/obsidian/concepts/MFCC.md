---
tags: [aurora, concept, audio-dsp, interview]
aliases: [MFCC, 梅尔倒谱系数, Mel-Frequency Cepstral Coefficients, MFCC-13]
domain: audio-dsp
whiteboard: ★★★★★
first_seen: L50
mastered: L50
---

# MFCC · 梅尔频率倒谱系数（Mel-Frequency Cepstral Coefficients）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把一帧声音浓缩成十几个数字，既保留"这是什么音"的关键信息，又扔掉重复和噪声——经典语音特征。

---

## 📖 定义
MFCC 是一条串起所有 DSP 步骤的特征流水线：

```
音频 →(切帧+加窗) [[STFT]] →(|·|²) 功率谱 →([[Mel]]滤波器组) Mel谱 →(log) log-Mel →([[DCT]]) MFCC
```

对每一帧，最后一步 [[DCT]] 把 40 维高度相关的 log-Mel 去相关、压到前几维；截取前 13 维即经典 **MFCC-13**。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 直接用几百维频谱又大又相关，早期 GMM-HMM 模型吃不消，也塞满了重复信息。
- **它解决了什么真实问题？** MFCC 用一套固定流程把一帧声音压成十几个近乎独立的数字：Mel 贴合人耳、log 压缩动态范围、DCT 去相关降维。低阶系数对应声道形状（元音），高阶对应细节（声门激励），截断即降维又去噪。
- **它在哪：** 这套特征是 Month 2 关键词识别分类器的标准输入，也是深度学习时代之前所有语音识别系统的地基。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L01  课程蓝图：MFCC 是终点目标之一
拆解前置     L44  STFT / L47 Mel / L49 DCT 各自打好基础
真正掌握     L50  ★ 串联完整流水线，手写 mfcc()，对齐参考实现
再次使用     L51  真实录音 → MFCC 特征
再次使用     L53  MFCC 可视化（倒谱系数热图）
再次使用     L62  关键词识别数据集特征
最终应用     L66  ASR 概览：MFCC 作为经典特征基线
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 MFCC 之前你得先会
```
MFCC
 ├─ 需要 → [[STFT]]                    (L44)
 ├─ 需要 → [[Mel]] 滤波器组             (L47)
 ├─ 需要 → log 压缩                    (L50)
 └─ 需要 → [[DCT]]（DCT-II）           (L49)
被谁依赖 → 关键词识别 / 经典 ASR 基线
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **log-Mel 谱** | MFCC 的上一步 | MFCC = log-Mel 再做 [[DCT]]；深度学习里常直接用 log-Mel |
| **[[Mel]] 滤波器组** | 一个组件 | Mel 只是 MFCC 五步里的一步 |
| **"倒谱 cepstrum"** | 频谱的频谱 | MFCC 是 Mel 域上的倒谱，DCT 相当于取对数谱的"频率" |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高，L50 闭卷推导课）** — 必须做到：
- ✅ 闭卷默画完整五步流水线 STFT→|·|²→Mel→log→DCT
- ✅ 说清每步动机（人耳 / 动态范围 / 去相关）
- ✅ 解释 `n_mfcc=13` 的来历、`n_mfcc ≤ n_mels`

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#ElevenLabs` `#Apple-Audio` `#NVIDIA` `#ASR`
> "手画一遍 MFCC 提取流程"是语音岗白板经典题。

## 🌍 现实系统里它在哪发挥作用
经典语音识别（Kaldi / GMM-HMM）· 说话人识别 · 关键词唤醒 · 音频分类基线；现代端到端模型多改用 log-Mel，但 MFCC 仍是理解特征工程的必修课。

## 📚 出现于（反查）
[[../lessons/L01]] · **[[../lessons/L50]]** · [[../lessons/L51]] · [[../lessons/L53]] · [[../lessons/L62]] · [[../lessons/L66]]

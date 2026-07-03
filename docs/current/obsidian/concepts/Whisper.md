---
tags: [aurora, concept, asr, interview]
aliases: [Whisper, OpenAI Whisper, log-Mel encoder-decoder, 多任务语音识别]
domain: asr
whiteboard: ★★★★
first_seen: L01
mastered: L70
---

# Whisper · OpenAI 语音识别模型（Whisper）

[[_lifecycle|← 生命周期总表]] · [[../domains/asr|← ASR 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把声音变成 log-Mel 频谱图，喂进一个 Transformer 编码器—解码器，用特殊 token 一次搞定"识别 / 翻译 / 语种检测"多种任务——这就是能听懂 99 种语言的 Whisper。

---

## 📖 定义
Whisper 是 OpenAI 提出的**弱监督多任务语音模型**，架构是 **log-Mel 输入 → 卷积前端 → Transformer Encoder-Decoder → 多任务解码头**。输入是 80 维 log-Mel 频谱（25 ms 窗 / 10 ms 帧移）；编码器把音频编成隐表示，解码器以自回归方式生成 token；通过特殊 token（`<|transcribe|>`、`<|translate|>`、`<|zh|>`、时间戳）在一个模型里统一完成转写、翻译、语种识别、加时间戳。它用 68 万小时弱标注数据训练，鲁棒性强。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 经典 ASR 要拼声学模型 + 语言模型 + 发音词典 + 解码器，多个组件各自训练、难维护、跨语言差。
- **它解决了什么真实问题？** 用一个端到端 seq2seq 模型 + 海量弱标注数据，做到开箱即用、多语言、抗噪声，还能顺手翻译。
- Aurora 全程的终极目标（L01"亲手造出 Whisper"）：从正弦波、FFT、Mel 一路搭到这里，L70 拆开它的每个设计选择与前面 DSP 基础一一对应。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L01  远征目标：6 个月亲手造出 Whisper
正式动机     L66  ASR 全览：端到端 seq2seq vs 经典流水线
拆解原理     L70  ★ 架构精读：log-Mel → Encoder-Decoder → 多任务头
再次使用     L71  解码策略：贪婪 vs beam search
再次使用     L72  LoRA 微调，教它你的方言
再次使用     L73  微调后用 WER 评估
最终应用     L92  集成进 aurora 端到端 pipeline / L94 demo
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 Whisper 之前你得先会
```
Whisper
 ├─ 需要 → [[Mel]]（80-dim log-Mel）        (L46/L47, 输入特征)
 ├─ 需要 → [[Transformer]] / [[Self-Attention]]   (L83, 编解码骨架)
 ├─ 需要 → [[CNN]]（conv stem）              (L63/L70, 前端下采样)
 ├─ 需要 → [[Beam-Search|集束搜索]]          (L71, 解码)
 └─ 需要 → [[LoRA]]                           (L72, 微调)
被谁依赖 → aurora.speech 端到端语音 pipeline
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[CTC]] 模型** | 帧级对齐损失 | Whisper 是 **seq2seq + 注意力解码**，不用 CTC |
| **经典流水线 ASR** | AM+LM+词典 | Whisper 一个模型端到端，多任务用特殊 token 切换 |
| **wav2vec2** | 自监督声学表示 | Whisper 是**弱监督有标注**训练，直接出文本 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 系统设计高频，必须做到：
- ✅ 闭卷画出数据流：`音频 → log-Mel(80) → conv → Encoder → Decoder → token`
- ✅ 说清各部件对应 Aurora 哪节（Mel=L47、Attention=L83）
- ✅ 讲清多任务 token 体系（转写/翻译/语种/时间戳）与自回归解码

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Google` `#Meta` `#ElevenLabs` `#Apple-Audio` `#ASR`
> 语音岗几乎必聊的现代 ASR 标杆，能对应到 DSP 基础是深度信号。

## 🌍 现实系统里它在哪发挥作用
OpenAI Whisper API · GPT-4o 语音前端 · 会议转录 / 字幕生成 · 播客搜索 · 各类离线语音助手

## 📚 出现于（反查）
[[../lessons/L01]] · [[../lessons/L66]] · **[[../lessons/L70]]** · [[../lessons/L71]] · [[../lessons/L72]] · [[../lessons/L73]]

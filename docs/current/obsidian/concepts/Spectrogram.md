---
tags: [aurora, concept, audio-dsp, interview]
aliases: [Spectrogram, 声谱图, 谱图, 频谱图, 语谱图]
domain: audio-dsp
whiteboard: ★★★★
first_seen: L03
mastered: L45
---

# Spectrogram · 声谱图（Spectrogram）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：给声音拍一张"X 光片"——横轴是时间、纵轴是频率、颜色越亮代表那一刻那个频率能量越强，一眼看出声音怎么随时间变化。

---

## 📖 定义
声谱图是**信号的时频能量图**。把信号切成一帧帧、每帧做一次 [[STFT]] 得到复数矩阵 `S`（形状 `(n_frames, n_fft//2+1)`），丢掉相位只留幅度，取功率再压成 dB：`mag = |S|`，`pow = |S|²`，`dB = 10·log₁₀(pow + ε)`。把这张 `(时间, 频率)` 的 dB 矩阵用热力图画出来，就是声谱图。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 光看波形（振幅 vs 时间）根本看不出"哪个频率在响"——一段和弦、一句人声在波形上都是一团乱麻。
- **它解决了什么真实问题？** 医生用 X 光把身体摊成"时间×部位×密度"，声谱图把声音摊成"时间×频率×能量"，让人和机器都能**一眼读出**共振峰、谐波、节奏。
- **为什么取 dB？** 声音动态范围高达 120 dB（比值 10¹²），线性尺度下轻声几乎不可见；dB 是对数尺度，正好贴合人耳的对数感知，弱音强音都清晰。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L03  先读图后学 FFT，练"看见声音"的眼睛
正式动机     L40  有了单帧频谱，缺一根时间轴
拆解原理     L44  手写 STFT → 得到复数矩阵 S
真正掌握     L45  ★ |STFT|² → dB 热力图，手写 plot_spectrogram
再次使用     L46  Mel 谱：把频率轴换成 Mel 刻度
再次使用     L50  MFCC 完整流水线的中间产物
再次使用     L62  KWS 数据集：声谱图当作模型输入
最终应用     L70  Whisper 的输入就是 log-Mel 声谱图
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学声谱图之前你得先会
```
Spectrogram
 ├─ 需要 → [[STFT]]                 (L43/L44)
 ├─ 需要 → [[FFT|快速傅里叶变换]]    (L38/L39)
 ├─ 需要 → 幅度/功率/dB             (L45)
 └─ 需要 → 时频分辨率权衡 win/hop   (L45)
被谁依赖 → [[Mel]] → [[MFCC]] → [[Whisper]] · KWS 模型
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **STFT** | 复数时频矩阵 | 声谱图 = **取 STFT 的幅度平方再 dB**，扔掉相位 |
| **Mel 声谱图** | 频率轴换成 Mel 刻度 | 普通声谱图是**线性频率轴**，Mel 是感知加权后的 |
| **波形（waveform）** | 振幅 vs 时间 | 波形只有 1 根轴信息，声谱图多了**频率维** |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — L45 有白板挑战，必须做到：
- ✅ 说清 `幅度谱 → 功率谱 → dB 谱` 的三步与单位
- ✅ 手算时间轴 `t = m·hop/sr`、频率轴 `f = k·sr/n_fft`
- ✅ 讲明 win_len / hop 的时频分辨率权衡（测不准原理）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#OpenAI` `#ElevenLabs` `#Apple-Audio` `#NVIDIA` `#DSP`
> 音频岗基础题：让你在白板上从波形一路推到 log-Mel 声谱图。

## 🌍 现实系统里它在哪发挥作用
Whisper · GPT-4o Voice · Google Speech · Shazam · 各类声纹/说话人识别 · 生物声学与故障诊断

## 📚 出现于（反查）
[[../lessons/L03]] · [[../lessons/L40]] · [[../lessons/L44]] · **[[../lessons/L45]]** · [[../lessons/L46]] · [[../lessons/L50]] · [[../lessons/L62]] · [[../lessons/L70]]

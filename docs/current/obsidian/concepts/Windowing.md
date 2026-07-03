---
tags: [aurora, concept, audio-dsp, interview]
aliases: [windowing, 窗函数, 加窗, window function, Hann, Hamming, Blackman, 频谱泄漏, spectral leakage]
domain: audio-dsp
whiteboard: ★★★★
first_seen: L36
mastered: L36
---

# Windowing · 窗函数与加窗（Window Function）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：给截取的一段信号做"淡入淡出"，让两端平滑归零，FFT 就不会把突兀的切口误当成高频噪声。

---

## 📖 定义
窗函数是一串与信号等长的权重 `w[n]`，两端接近 0、中间接近 1；把信号逐点乘上它（加窗）再做 [[FFT]]，可压制**频谱泄漏（spectral leakage）**。常见窗与旁瓣抑制：

| 窗 | 公式核心 | 旁瓣抑制 | 主瓣宽度 |
|---|---|---|---|
| 矩形 Rectangular | w=1 | 差 (−13 dB) | 最窄 |
| **Hann** | 0.5·(1−cos(2πn/(N−1))) | 好 (−31 dB) | 中 |
| Hamming | 0.54−0.46·cos(...) | 较好 (−41 dB) | 中 |
| Blackman | 0.42−0.5·cos+0.08·cos(2·) | 很好 (−58 dB) | 最宽 |

Aurora 的 [[STFT]] 每一帧都乘 Hann 窗（`src/aurora/audio/windows.py`）。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 直接截取一段信号，边缘幅值会突然跳到 0——相当于乘了一个矩形函数。FFT 不知道"这是截取边界"，会把这个跳变当成真实高频成分，在频谱上产生**旁瓣污染**。
- **它解决了什么真实问题？** 混音师给录音做"淡入淡出"不只是审美，更是数学必要性。窗函数把信号两端温柔压低，FFT 看到的是平滑过渡而非突变，泄漏大大减少。
- **代价与权衡：** 旁瓣压得越狠（Blackman），主瓣越宽、频率分辨率越差——没有免费午餐。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L32  numpy 信号处理里初见"窗"概念
真正掌握     L36  ★ 对比 4 种窗，手写 describe_window，理解泄漏来源
再次使用     L43  STFT 每帧加窗
再次使用     L44  手写 stft() 时把 Hann 窗乘进每帧
再次使用     L50  MFCC 流水线的切帧步骤
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学窗函数之前你得先会
```
Windowing
 ├─ 需要 → 正弦 / 余弦                  (L04)
 ├─ 需要 → 逐元素乘法                   (L32)
 └─ 关联 → [[FFT]] 旁瓣 / sinc          (L39)
被谁依赖 → [[STFT]] → [[Mel]] → [[MFCC]]
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **频谱泄漏 vs [[Aliasing|混叠]]** | 两种失真 | 泄漏来自**截断边缘**（加窗解决）；混叠来自**采样率不够**（提高 sr 解决） |
| **主瓣 vs 旁瓣** | 峰 vs 裙边 | 主瓣宽=频率分辨率差；旁瓣高=泄漏严重，二者此消彼长 |
| **窗长 vs hop** | 帧长 vs 步长 | 窗决定每帧看多长信号；hop 决定帧与帧的重叠 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 必须做到：
- ✅ 写出 Hann 窗公式，手算 N=4 的 w[0..3]
- ✅ 解释矩形截断 → sinc 旁瓣 → 泄漏，平滑窗如何压制
- ✅ 说清"旁瓣抑制↔主瓣宽度"的权衡

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Apple-Audio` `#ElevenLabs` `#NVIDIA` `#DSP` `#ASR`
> "为什么 STFT 每帧要加窗"是时频分析常见追问。

## 🌍 现实系统里它在哪发挥作用
所有 STFT / 声谱图前端（Whisper、语音识别、TTS）· 音频编解码器 · 频谱分析仪 · 通信系统的 OFDM。

## 📚 出现于（反查）
[[../lessons/L32]] · **[[../lessons/L36]]** · [[../lessons/L43]] · [[../lessons/L44]] · [[../lessons/L50]]

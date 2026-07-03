---
tags: [aurora, concept, audio-dsp, interview]
aliases: [FFT, 快速傅里叶变换, Fast Fourier Transform]
domain: audio-dsp
whiteboard: ★★★★★
first_seen: L35
mastered: L39
---

# FFT · 快速傅里叶变换（Fast Fourier Transform）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把一个信号"拆成一堆正弦波"，本来要算 N² 次，FFT 用分治只要 N·log N 次——快到能实时处理声音。

---

## 📖 定义
快速傅里叶变换是**离散傅里叶变换（[[DFT]]）的快速算法**。它利用 DFT 里旋转因子 `e^{-2πikn/N}` 的对称性，把长度 N 的变换**对半拆成两个 N/2 的子问题**（偶数点 + 奇数点），递归下去，把复杂度从 `O(N²)` 降到 `O(N log N)`。结果和 DFT **完全一样**，只是算得快。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 一秒 16000 个采样点，直接算 DFT 是 16000² ≈ 2.5 亿次乘法/帧——实时语音、音乐、通信全都卡死。
- **它解决了什么真实问题？** 让"把声音拆成频率"这件事**快到可以实时**，是整个数字信号处理的地基。
- 1965 年 Cooley & Tukey 发表后，直接催生了现代音频/通信/图像处理。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L35  欧拉公式遇见 FFT（旋转因子登场）
正式动机     L37  暴力 DFT O(N²)，先感受慢
拆解原理     L38  蝶形分治 8→4+4→2+2+2+2→1
真正掌握     L39  ★ 从零递归手写，误差 < 1e-10
再次使用     L44  STFT：每一帧都调用你写的 FFT
再次使用     L47  log-Mel：STFT → 功率谱
再次使用     L50  MFCC 完整流水线
最终应用     L70  Whisper 的输入特征（log-Mel）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 FFT 之前你得先会
```
FFT
 ├─ 需要 → [[complex number|复数]]        (L05)
 ├─ 需要 → [[Euler formula|欧拉公式]]      (L06)
 ├─ 需要 → [[twiddle factor|旋转因子]]     (L35)
 ├─ 需要 → [[divide and conquer|分治]]     (L38)
 └─ 需要 → [[recursion|递归]]              (程序结构)
被谁依赖 → [[STFT]] → [[Mel]] → [[MFCC]] → [[Whisper]]
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **DFT** | 定义/公式，O(N²) | FFT 是 DFT 的**快速算法**，结果一样 |
| **STFT** | 加时间轴的 FFT | STFT = 把信号切帧，**每帧做一次 FFT** |
| **FFT vs "一种新数学"** | ❌ | FFT **不是新数学**，就是把同一个 DFT 更聪明地算 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷推导 蝶形递推 `X[k] = E[k] + W_N^k·O[k]`
- ✅ 手写代码（Cooley-Tukey 递归）
- ✅ 讲清复杂度 `O(N²) → O(N log N)` 的来历

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#ElevenLabs` `#Apple-Audio` `#NVIDIA` `#DSP`
> 音频/语音岗几乎必问的白板题之一。

## 🌍 现实系统里它在哪发挥作用
Whisper · GPT-4o Voice · Google Speech · ElevenLabs · Shazam · 几乎所有音频编解码器（MP3/AAC）

## 📚 出现于（反查）
[[../lessons/L35]] · [[../lessons/L37]] · [[../lessons/L38]] · **[[../lessons/L39]]** · [[../lessons/L44]] · [[../lessons/L47]] · [[../lessons/L50]] · [[../lessons/L70]]

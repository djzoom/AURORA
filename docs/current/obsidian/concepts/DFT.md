---
tags: [aurora, concept, audio-dsp, interview]
aliases: [DFT, 离散傅里叶变换, Discrete Fourier Transform, naive DFT]
domain: audio-dsp
whiteboard: ★★★★★
first_seen: L35
mastered: L37
---

# DFT · 离散傅里叶变换（Discrete Fourier Transform）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：一个频率一个频率地"审问"信号——问它"你里面有多少这个频率的成分"，把时间信号翻译成频率清单。

---

## 📖 定义
离散傅里叶变换把长度 N 的时域序列 `x[n]` 变成 N 个频率分量 `X[k]`：

$$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-2\pi i k n / N}$$

第 `k` 个输出，就是信号 `x[n]` 与第 k 个频率基向量（一串[[twiddle factor|旋转因子]]）的**点积**。它是**定义**，不是算法——直接按公式算是双循环 `O(N²)`；[[FFT]] 是它的快速算法，结果完全相同。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 你只能在时间轴上看到一堆起伏的采样点，完全不知道里面藏着哪些音高、哪些频率。
- **它解决了什么真实问题？** 想知道一段音乐里有哪些音符，最朴素的办法就是"逐一扫频"：对每个可能的频率，问"信号里有多少这个成分"。DFT 把这个"扫频"写成了精确的求和公式——这是频率世界的入口。
- **代价**：N 个频点 × 每点 N 次点积 = `O(N²)`，N 翻倍时间变 4 倍，慢到无法实时——这个痛点直接催生了 [[FFT]]。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L35  旋转因子登场，DFT 公式第一次现身
正式动机     L37  暴力扫频：X[k] = 信号与频率基的点积
真正掌握     L37  ★ 手写 naive_dft(x)，与 numpy.fft 逐点对齐
拆解加速     L38  蝶形分治：把 DFT 对半拆成 FFT
再次使用     L44  STFT：每一帧都做一次（快速版）DFT
再次使用     L49  DCT：DFT 的"纯实数余弦"表亲
最终应用     L50  MFCC / L70 Whisper 输入特征的地基
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 DFT 之前你得先会
```
DFT
 ├─ 需要 → [[Euler formula|欧拉公式]]      (L06/L35)
 ├─ 需要 → [[twiddle factor|旋转因子]]     (L35)
 ├─ 需要 → [[Dot Product|点积]]            (L10)
 └─ 需要 → [[complex number|复数]]         (L05)
被谁依赖 → [[FFT]] → [[STFT]] → [[Mel]] → [[MFCC]] → [[DCT]]
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[FFT]]** | 快速算法，O(N log N) | DFT 是**定义/公式**，FFT 是把它算快，结果一样 |
| **[[STFT]]** | 加时间轴 | STFT = 切帧后**每帧做一次 DFT** |
| **[[DCT]]** | 纯实数余弦变换 | DFT 用复指数（正弦+余弦），DCT 只用余弦、输出实数 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷写出 `X[k] = Σ x[n]·e^{-2πikn/N}` 并解释"点积=投影"
- ✅ 手算 4 点 DFT（如 `x=[1,0,-1,0]`）
- ✅ 讲清复杂度 `O(N²)` 的来历，以及为何要过渡到 FFT

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#ElevenLabs` `#Apple-Audio` `#NVIDIA` `#DSP`
> "DFT 和 FFT 有什么区别"是音频/语音岗的开场白级问题。

## 🌍 现实系统里它在哪发挥作用
所有频谱分析的数学定义层：Whisper / Google Speech 的特征前端、音频编解码器、频谱可视化工具，底层都是这条求和公式（只是用 FFT 加速执行）。

## 📚 出现于（反查）
[[../lessons/L35]] · **[[../lessons/L37]]** · [[../lessons/L38]] · [[../lessons/L39]] · [[../lessons/L44]] · [[../lessons/L49]] · [[../lessons/L50]]

---
tags: [aurora, concept, audio-dsp, interview]
aliases: [STFT, 短时傅里叶变换, Short-Time Fourier Transform, 时频分析]
domain: audio-dsp
whiteboard: ★★★★★
first_seen: L43
mastered: L44
---

# STFT · 短时傅里叶变换（Short-Time Fourier Transform）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把长声音切成一帧一帧的小片，每片单独做一次 [[FFT]]，就得到"什么频率、在第几秒出现"的时频图。

---

## 📖 定义
短时傅里叶变换 = **切帧 + 加窗 + 逐帧 [[FFT]]**。对信号每隔 `hop` 个点取一段长 `n_fft` 的短窗 `x[t·hop : t·hop+n_fft]`，乘上一个[[Windowing|窗函数]]，再做 FFT：

$$\text{STFT}[t,k] = \sum_{n=0}^{N-1} x[t\cdot\text{hop}+n]\,w[n]\,e^{-2\pi i k n/N}$$

输出是一张 `(帧数 × 频率bin)` 的复数时频矩阵。取模平方即声谱图（spectrogram）。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 对整段音频只做**一次** FFT，你只知道"出现过哪些频率"，却不知道它们"在第几秒出现"——鸟鸣的啁啾、辅音的爆破、乐曲的转调，全被压平成一条平均频谱。
- **它解决了什么真实问题？** 把长信号切成一帧一帧的短窗、逐帧做 FFT，就给每个频率贴上了时间戳。这就是"滑窗"的意义：**一个 FFT 给不出时间轴，一串滑动的 FFT 才能画出时频图**。
- **后面哪里还会再用到？** L44 亲手组装 `stft()`、L45 声谱图、L46–L50 的 Mel / MFCC 全流水线，都站在这张时频矩阵之上。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L43  滑窗直觉：一个 FFT 给不出时间轴
真正掌握     L44  ★ 亲手组装 stft()，切帧+加窗+逐帧 FFT
再次使用     L45  取模平方 → 声谱图
再次使用     L47  Mel 滤波器组作用在每一帧功率谱上
再次使用     L50  MFCC 完整流水线的第一步
再次使用     L62  关键词识别数据集的特征前端
最终应用     L70  Whisper 输入 = log-Mel 声谱图（STFT 打底）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 STFT 之前你得先会
```
STFT
 ├─ 需要 → [[FFT]]                     (L39)
 ├─ 需要 → [[Windowing|窗函数]]         (L36)
 └─ 需要 → 切帧 / hop / 重叠            (L43)
被谁依赖 → [[Mel]] → [[MFCC]] → [[Whisper]]
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[FFT]]** | 单次频率变换 | STFT = 把信号切帧，**每帧做一次 FFT** |
| **声谱图 spectrogram** | STFT 的模平方 | STFT 是**复数**矩阵，声谱图是它的**能量**（丢了相位） |
| **[[Mel]] 谱** | 频率轴压缩后的 STFT | Mel 谱 = STFT 功率谱 × Mel 滤波器组 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高，L44 闭卷推导课）** — 必须做到：
- ✅ 闭卷写出 STFT 三步：切帧 → 加窗 → 逐帧 FFT
- ✅ 讲清 `n_fft`、`hop`、重叠率与时间/频率分辨率的权衡
- ✅ 手写 `stft()`，能算出输出矩阵 shape `(1 + (len-n_fft)//hop, n_fft//2+1)`

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Google` `#Meta` `#ElevenLabs` `#Apple-Audio` `#NVIDIA` `#DSP` `#ASR`
> "为什么不直接对整段做 FFT" 是时频分析的必答题。

## 🌍 现实系统里它在哪发挥作用
Whisper · GPT-4o Voice · Google Speech · ElevenLabs TTS · Shazam · 所有声谱图可视化与音乐分析工具。

## 📚 出现于（反查）
[[../lessons/L43]] · **[[../lessons/L44]]** · [[../lessons/L45]] · [[../lessons/L47]] · [[../lessons/L50]] · [[../lessons/L62]] · [[../lessons/L70]]

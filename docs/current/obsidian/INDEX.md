---
tags: [aurora, glossary, index, navigation]
created: 2026-06-27
---

# Aurora Course Glossary — Master Index

> Bilingual (中/英) glossary for the Aurora audio-AI course.
> 11 modules · 99 lessons · ~462 unique terms across 9 domains.


## 🕸️ Knowledge Graph（进行中 · v1）

从"术语表"升级为"知识中枢"。已建成的自动派生层（`scripts/build_knowledge_graph.py` 可重跑刷新）：

- **[[concepts/_lifecycle|术语生命周期总表]]** — 每个术语「第一次出现 → 一路复现 → 最终应用」的时间线（Layer 2/10）。*今天难，是因为以后它还会出现很多次。*
- **`lessons/L01.md … L99.md`** — 按课反查：本课「首次引入 / 前置术语 / 后续再用」（Layer 1/3）。例：[[lessons/L39]]。
- **`concepts/`** — 一个术语一页（原子化），含全部 10 层（一句话 / 定义 / 为什么发明 / 生命周期 / 依赖 / 易混淆 / 白板要求 / 面试标签 / 现实系统 / 反查）。**已建 41 个「白板/面试核心」概念页**，例：[[concepts/FFT]] · [[concepts/Backpropagation]] · [[concepts/Self-Attention]] · [[concepts/CTC]] · [[concepts/Mel]] · [[concepts/SVD]] · [[concepts/LoRA]] · [[concepts/RAG]]。
  - 白板 ★★★★★ 术语（面试必推导）：DFT / STFT / Mel / MFCC / DCT / Chain-Rule / Backpropagation / Autograd / CTC / Edit-Distance / Self-Attention / Transformer / LoRA / KV-Cache / RAG / Sampling。

- **[[interview/Audio-AI|🎧 面试冲刺图]]** — 按白板★优先级排的面试清单(★★★★★ 先啃),含一句话+相关公司;另有 [[interview/By-Company|按公司分组]](OpenAI 33 / ElevenLabs 20 …)。**自动生成自 concept 页**(Layer 7)。

> **待建（v2，需策展/agent 批量写）**：其余 ~420 个冷门 concept 页、`roadmaps/`（Speech AI / DSP / LLM / Music 技术主线）。concept 页里指向未建术语的 `[[…]]` 是 Obsidian 的"待创建"链接（正常，随图谱生长自动补齐）。
> 设计理念：**大量原子化概念页 + 双向链接 + MOC（Map of Content）索引**，而不是单一大词典。
> Annotation coverage: 795 applied in earlier rounds + ~92 more in the 2026-07-03 pass.
> Of the audit's 460 tracked term-slots, 430 are now glossed inline; the remaining ~30
> are **intentional skips** — 量化 in its "quantified" sense (L98/L99), terms that appear
> only in code cells or H1 titles, and substring-only occurrences (e.g. 偏导 inside 偏导数)
> that would mis-split if annotated. Not genuine gaps.

## Course Structure

| Module | Domain | Lessons | Term Count | Notes |
|--------|--------|---------|-----------|-------|
| 0 Foundation | Mixed | L01–L03 | 37 | Motivation survey |
| 1 Complex & Trig | Audio DSP | L04–L08 | 37 | Complex numbers, Euler |
| 2 Linear Algebra | Linear Algebra | L09–L21 | 60 | Vectors → SVD |
| 3 Calculus | Calculus | L22–L26 | 35 | Derivatives → Adam |
| 4 Probability | Probability | L27–L31 | 35 | Distributions → softmax |
| 5 Audio DSP | Audio DSP | L32–L53 | 55 | FFT → MFCC from scratch |
| 6 Deep Learning | Deep Learning | L54–L65 | 60 | Autograd → KWS |
| 7 ASR | ASR | L66–L75 | 50 | CTC → Whisper |
| 8 Music | Music | L76–L82 | 35 | Chroma → embeddings |
| 9 LLM | LLM | L83–L91 | 45 | Transformer → RAG |
| 10 Integration | Systems | L92–L99 | 50 | Pipeline → interview |

## Annotation Audit Summary

| Domain | Total Terms | ✅ Annotated | ⚠️ Partial | ❌ Missing |
|--------|------------|------------|-----------|----------|
| Audio DSP (M0+M1+M5) | 92 | 12 | 14 | 66 |
| Linear Algebra (M2) | 60 | 7 | 5 | 48 |
| Calculus (M3) | 35 | 0 | 9 | 26 |
| Probability (M4) | 35 | 1 | 5 | 29 |
| Deep Learning (M6) | 60 | 5 | 4 | 51 |
| ASR (M7) | 50 | 10 | 2 | 38 |
| Music (M8) | 35 | 7 | 9 | 19 |
| LLM (M9) | 45 | 10 | 2 | 33 |
| Integration (M10) | 50 | 8 | 2 | 40 |
| **Total** | **462** | **60** | **52** | **350** |

See [[annotation-audit]] for the full per-notebook breakdown.

---

## Domain Pages

- [[domains/audio-dsp]] — DFT, FFT, STFT, Mel scale, MFCC, DCT, windows, aliasing, cepstrum
- [[domains/linear-algebra]] — vectors, matrices, eigenvalues, SVD, LU/QR decompositions
- [[domains/calculus]] — derivatives, gradients, chain rule, gradient descent, Adam
- [[domains/probability]] — distributions, entropy, Bayes, cross-entropy, softmax
- [[domains/deep-learning]] — autograd, backprop, CNN, KWS training loop
- [[domains/asr]] — CTC, WER, Whisper, LoRA, beam search, edit distance
- [[domains/music]] — chroma, beat tracking, onset, embeddings, contrastive learning
- [[domains/llm]] — attention, KV cache, LoRA, RAG, nucleus sampling

---

## Quick Lookup A–Z

### A
- 模数转换器 ADC → [[domains/audio-dsp#模数转换器 (Analog-to-Digital Converter / ADC)]]
- 混叠 Aliasing → [[domains/audio-dsp#混叠 (Aliasing)]]
- 振幅 Amplitude → [[domains/audio-dsp#振幅 (Amplitude)]]
- 近似最近邻 ANN → [[domains/music#近似最近邻 (Approximate Nearest Neighbor / ANN)]]
- 语音识别 ASR → [[domains/asr#语音识别 (Automatic Speech Recognition / ASR)]]
- 注意力机制 Attention → [[domains/llm#缩放点积注意力 (Scaled Dot-Product Attention / SDPA)]]
- 自动微分 Autograd → [[domains/deep-learning#自动微分 (Automatic Differentiation / autograd)]]
- 自回归 Autoregressive → [[domains/asr#自回归 (Autoregressive / AR)]]

### B
- 反向传播 Backprop → [[domains/deep-learning#反向传播 (Backpropagation / backprop)]]
- 节拍检测 Beat Tracking → [[domains/music#节拍检测 (Beat Tracking / BPM)]]
- 伯努利分布 Bernoulli → [[domains/probability#伯努利分布 (Bernoulli Distribution)]]
- 位反转 Bit Reversal → [[domains/audio-dsp#位反转 (Bit Reversal)]]
- 蝶形运算 Butterfly → [[domains/audio-dsp#蝶形运算 (Butterfly Operation)]]

### C
- 倒谱 Cepstrum → [[domains/audio-dsp#倒谱 (Cepstrum)]]
- 链式法则 Chain Rule → [[domains/calculus#链式法则 (Chain Rule)]]
- 色度 Chroma → [[domains/music#色度 (Chroma)]]
- CTC → [[domains/asr#CTC (Connectionist Temporal Classification)]]
- 复数 Complex Number → [[domains/audio-dsp#复数 (Complex Number)]]
- 共轭对称 Conjugate Symmetry → [[domains/audio-dsp#共轭对称 (Conjugate Symmetry)]]
- 余弦相似度 Cosine Similarity → [[domains/linear-algebra#余弦相似度 (Cosine Similarity)]]
- 交叉注意力 Cross-Attention → [[domains/asr#交叉注意力 (Cross-Attention)]]
- 交叉熵 Cross Entropy → [[domains/probability#交叉熵 (Cross Entropy / CE)]]

### D
- DAG → [[domains/deep-learning#有向无环图 (Directed Acyclic Graph / DAG)]]
- DCT → [[domains/audio-dsp#离散余弦变换 (Discrete Cosine Transform / DCT)]]
- 去相关 Decorrelation → [[domains/audio-dsp#去相关 (Decorrelation)]]
- 导数 Derivative → [[domains/calculus#导数 (Derivative)]]
- DFT → [[domains/audio-dsp#离散傅里叶变换 (Discrete Fourier Transform / DFT)]]
- 对角化 Diagonalization → [[domains/linear-algebra#对角化 (Diagonalization)]]
- 动态规划 Dynamic Programming → [[domains/asr#动态规划 (Dynamic Programming / DP)]]

### E
- 编辑距离 Edit Distance → [[domains/asr#编辑距离 (Edit Distance / Levenshtein)]]
- 特征分解 Eigendecomposition → [[domains/linear-algebra#特征分解 (Eigendecomposition)]]
- 特征值 Eigenvalue → [[domains/linear-algebra#特征值 (Eigenvalue)]]
- 嵌入向量 Embedding → [[domains/music#嵌入向量 (Embedding)]]
- 欧拉公式 Euler's Formula → [[domains/audio-dsp#欧拉公式 (Euler's Formula)]]

### F
- FFT → [[domains/audio-dsp#快速傅里叶变换 (Fast Fourier Transform / FFT)]]
- 前向算法 Forward Algorithm → [[domains/asr#前向算法 (Forward Algorithm)]]
- 帧移 Hop Length → [[domains/audio-dsp#帧移 (Hop Length)]]
- 基频 Fundamental Frequency → [[domains/audio-dsp#基频 (Fundamental Frequency / F0)]]

### G
- 高斯消元 Gaussian Elimination → [[domains/linear-algebra#高斯消元 (Gaussian Elimination)]]
- 吉布斯现象 Gibbs Phenomenon → [[domains/audio-dsp#吉布斯现象 (Gibbs Phenomenon)]]
- 梯度 Gradient → [[domains/calculus#梯度 (Gradient / grad)]]
- 梯度下降 Gradient Descent → [[domains/calculus#梯度下降 (Gradient Descent / GD)]]
- 梯度检验 Gradient Check → [[domains/calculus#梯度检验 (Gradient Check)]]

### H
- 谐波 Harmonics → [[domains/audio-dsp#谐波 (Harmonics)]]
- 幻觉词 Hallucination → [[domains/asr#幻觉词 (Hallucination)]]
- 热力图 Heatmap → [[domains/asr#热力图 (Heatmap)]]

### K
- KL散度 KL Divergence → [[domains/probability#KL散度 (KL Divergence / KL)]]
- KV缓存 KV-Cache → [[domains/llm#键值缓存 (Key-Value Cache / KV-Cache)]]
- 关键词识别 KWS → [[domains/deep-learning#关键词识别 (Keyword Spotting / KWS)]]

### L
- 损失函数 Loss Function → [[domains/deep-learning#损失函数 (Loss Function)]]
- LoRA → [[domains/llm#低秩适配 (Low-Rank Adaptation / LoRA)]]
- 低秩近似 Low-Rank Approx → [[domains/linear-algebra#低秩近似 (Low-Rank Approximation)]]

### M
- mel滤波器组 Mel Filterbank → [[domains/audio-dsp#三角滤波器组 (Triangular Filter Bank / Mel Filterbank)]]
- Mel标度 Mel Scale → [[domains/audio-dsp#Mel 标度 (Mel Scale)]]
- MFCC → [[domains/audio-dsp#梅尔频率倒谱系数 (MFCC)]]
- 多头注意力 MHA → [[domains/llm#多头注意力 (Multi-Head Attention / MHA)]]

### N
- 奈奎斯特频率 Nyquist → [[domains/audio-dsp#奈奎斯特频率 (Nyquist Frequency)]]
- 归一化 Normalization → [[domains/linear-algebra#归一化 (Normalization)]]

### O
- 音符起点 Onset → [[domains/music#音符起点 (Onset)]]
- 过拟合 Overfitting → [[domains/deep-learning#过拟合 (Overfitting)]]

### P
- 偏导 Partial Derivative → [[domains/calculus#偏导 (Partial Derivative)]]
- PCA → [[domains/linear-algebra#主成分分析 (PCA)]]
- 音高 Pitch → [[domains/audio-dsp#音高 (Pitch)]]
- 正定 Positive Definite → [[domains/linear-algebra#正定 (Positive Definite / PD)]]
- 概率分布 Probability Distribution → [[domains/probability#概率分布 (Probability Distribution)]]

### Q
- 量化 Quantization → [[domains/llm#量化 (Quantization)]]

### R
- RAG → [[domains/llm#检索增强生成 (Retrieval-Augmented Generation / RAG)]]
- 残差连接 Residual Connection → [[domains/deep-learning#残差连接 (Residual Connection)]]
- 旋转矩阵 Rotation Matrix → [[domains/linear-algebra#旋转矩阵 (Rotation Matrix)]]

### S
- 采样率 Sample Rate → [[domains/audio-dsp#采样率 (Sample Rate / sr)]]
- 频谱泄漏 Spectral Leakage → [[domains/audio-dsp#频谱泄漏 (Spectral Leakage)]]
- 声谱图 Spectrogram → [[domains/audio-dsp#声谱图 (Spectrogram)]]
- STFT → [[domains/audio-dsp#短时傅里叶变换 (Short-Time Fourier Transform / STFT)]]
- SVD → [[domains/linear-algebra#奇异值分解 (Singular Value Decomposition / SVD)]]

### T
- 张量 Tensor → [[domains/deep-learning#张量 (Tensor)]]
- 旋转因子 Twiddle Factor → [[domains/audio-dsp#旋转因子 (Twiddle Factor / W)]]

### V
- 向量 Vector → [[domains/linear-algebra#向量 (Vector)]]

### W
- WER → [[domains/asr#词错率 (Word Error Rate / WER)]]
- 白噪声 White Noise → [[domains/audio-dsp#白噪声 (White Noise)]]
- 窗函数 Window Function → [[domains/audio-dsp#窗函数 (Window Function)]]

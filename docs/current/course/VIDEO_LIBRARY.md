# 🎬 AURORA 补充视频资料库 · Video Library

> **从正弦波到 Whisper，全程有名师陪你手写。**
> A curated, phase-by-phase catalog of the best YouTube courses & lectures — from famous teachers and top universities — that supplement AURORA's 99-lesson from-scratch course.

这是一份为**自习者**准备的、对齐 AURORA 课程 **L01–L99** 每一个阶段的 YouTube 补充片单。收录标准与 AURORA「**从零手写 · 拒绝 API wrapper · 第一性原理**」的理念一致：优先能让你**自己重新推导 / 亲手写出算法**的资源（Karpathy、3Blue1Brown、Valerio Velardo、Umar Jamil、Meinard Müller、李宏毅……），辅以名校完整课程做严谨对照。

- **规模**：约 **95 条**精选资源，覆盖 LLM · ML/DL · TTS · STT · DSP · 音乐 MIR · RAG/Agent · MLOps 全栈。
- **用法**：在 notebook 里遇到 `✏️ TODO` 卡住、或想先建立直觉时，按课号 `L__` 回到本库对应阶段找视频。**先看直觉课 → 再看手写实现课 → 最后回 notebook 自己写一遍。**
- **打卡**：交互版（随 Aurora Quest 部署的 `video-library.html`）支持逐条**打卡**——进度条、连续打卡天数、阶段通关和 🥉🥈🥇💎👑 里程碑奖章都记在本机浏览器里（localStorage），鼓励全刷一遍；「清空打卡」两点确认后即可重新开始。
- **图例**：难度 `入门 / 进阶 / 高级`；语言 `英文 / 中文 / 中英字幕`；`⚠️` = 直链未能逐一核实，请以「频道 + 搜索关键词」为准（详见文末[核实说明](#核实说明)）。

---

## 目录 Contents

- [速查表：阶段 → 首选视频](#速查表阶段--首选视频)
- [名师名校索引](#名师名校索引)
- [三条学习路径](#三条学习路径)
- [Phase 0–1 · 数学与信号直觉基础（L01–L08）](#phase-01--数学与信号直觉基础l01l08)
- [Phase 2 · 线性代数（L09–L21）](#phase-2--线性代数l09l21)
- [Phase 3 · 微积分（L22–L26）](#phase-3--微积分l22l26)
- [Phase 4 · 概率统计（L27–L31）](#phase-4--概率统计l27l31)
- [Phase 5 · Audio DSP 音频信号处理（L32–L53）](#phase-5--audio-dsp-音频信号处理l32l53)
- [Phase 6 · 机器学习 / 深度学习基础（L54–L65）](#phase-6--机器学习--深度学习基础l54l65)
- [Phase 7 · 语音识别 ASR / STT（L66–L75）](#phase-7--语音识别-asr--stt-l66l75)
- [Phase 8 · 音乐智能 / MIR（L76–L82）](#phase-8--音乐智能--mir-l76l82)
- [Phase 9 · LLM / RAG / Agent（L83–L91）](#phase-9--llm--rag--agent-l83l91)
- [Phase 10 · 系统集成 / MLOps / 面试（L92–L99）](#phase-10--系统集成--mlops--面试l92l99)
- [aurora.tts · 语音合成 TTS（延期模块，专项补充）](#auroratts--语音合成-tts延期模块专项补充)
- [核实说明](#核实说明)

---

## 速查表：阶段 → 首选视频

| 阶段 · 课号 | 主题 | 🥇 首选补充视频（一句话） |
| --- | --- | --- |
| **Phase 0–1** · L01–L08 | 声音数字化 · 复数三角 · 傅里叶直觉 | 3Blue1Brown《傅里叶变换 / 级数》+《欧拉公式》——把「复指数 = 旋转」讲到看得见 |
| **Phase 2** · L09–L21 | 线性代数 | 3B1B《线性代数的本质》建直觉 → MIT 18.06 Gilbert Strang 补严谨手写 |
| **Phase 3** · L22–L26 | 微积分 | 3B1B《微积分的本质》+《反向传播微积分》 |
| **Phase 4** · L27–L31 | 概率统计 | StatQuest 统计基础 + Harvard Stat 110；softmax/交叉熵看 StatQuest 导数精讲 |
| **Phase 5** · L32–L53 | Audio DSP | **Valerio Velardo《Audio Signal Processing for ML》——与本阶段几乎逐课对应，必看** |
| **Phase 6** · L54–L65 | 深度学习 | **Karpathy《Neural Networks: Zero to Hero》(micrograd)——从零手写反向传播** |
| **Phase 7** · L66–L75 | ASR / STT | 李宏毅 DLHLP 语音识别系列（中文）+ CMU 11-785 CTC 前向算法 |
| **Phase 8** · L76–L82 | 音乐 / MIR | Meinard Müller (FMP) chroma/beat + Valerio ASP 特征地基 |
| **Phase 9** · L83–L91 | LLM / RAG / Agent | **Karpathy《Let's build GPT》+ Umar Jamil 从零编码 KV-Cache/LoRA/量化/RAG** |
| **Phase 10** · L92–L99 | 集成 / MLOps / 面试 | Full Stack Deep Learning + Made With ML + W&B 官方 |
| **aurora.tts** | 语音合成（延期模块） | 李宏毅 語音合成 (Tacotron) + Valerio《TTS & Voice Cloning》 |

---

## 名师名校索引

按在本库出现频率与权威度排列，帮你认清「谁是谁、为什么值得跟」。

| 讲师 / 机构 | 身份 | 招牌内容 | 与 AURORA 的关系 |
| --- | --- | --- | --- |
| **Andrej Karpathy** | 前 OpenAI 创始成员 / 前 Tesla AI 总监 | Neural Networks: Zero to Hero（micrograd → GPT → tokenizer） | 「从零手写」理念的**头号对标**，L54–L58 与 L83–L87 的直接教材原型 |
| **3Blue1Brown**（Grant Sanderson） | 顶级数学可视化作者 | 线代 / 微积分 / 傅里叶 / 神经网络 / Transformer 直觉 | 每个「本质系列」都是先建直觉、零黑箱 |
| **Valerio Velardo**（The Sound of AI） | 音频 AI 教育社区头部 | ASP for ML、Deep Learning for Audio、TTS & Voice Cloning、PyTorch for Audio | **音频主线几乎逐课对应**，横跨 DSP/DL/音乐/TTS |
| **李宏毅 Hung-yi Lee**（台大 NTU） | 华语区顶尖 ML 名师 | ML2021、DLHLP（深度学习与人类语言处理） | **中文主线**，语音/自注意力/TTS 的最佳母语入口 |
| **Umar Jamil** | ML 工程师 | 从零 PyTorch 编码 Transformer/LLaMA/LoRA/量化/RAG | L84–L90 的逐行实现蓝本 |
| **Steve Brunton**（UW） | 华盛顿大学教授 | Data-Driven Science：Fourier/FFT/SVD | 每概念配 Python/MATLAB 手写代码 |
| **Meinard Müller**（AudioLabs Erlangen） | 《Fundamentals of Music Processing》作者 | chroma / onset / beat + FMP Notebooks | MIR 领域权威，代码级手写对照 |
| **StatQuest**（Josh Starmer） | UNC 统计学者 | 「逐步拆解」统计与 ML | softmax/交叉熵/反向传播导数手推 |
| **Gilbert Strang / Joe Blitzstein / Alan Oppenheim / Denis Auroux** | MIT · Harvard 名教授 | 18.06 线代 · Stat 110 概率 · 信号与系统 · 18.02 微积分 | 名校严谨理论底座 |
| **Yannic Kilcher** | ML 研究者 | 论文逐段精读 | Attention / wav2vec / VALL-E / SimCLR |
| **李沐 (Mu Li)** | Amazon 资深首席科学家 | 论文精读方法论（中文） | L95 研究技能中文首选 |
| **Full Stack Deep Learning · Made With ML · Weights & Biases** | 产业级 MLOps 课程 | 从 demo 到产品、实验跟踪、CI/CD | L92–L94 工程落地蓝本 |

---

## 三条学习路径

自习者可按自己的风格挑一条主线，其余作补充：

1. **🎨 直觉派**（先看得见，再动手）：3Blue1Brown → StatQuest → Serrano.Academy → 回 notebook。适合数学基础较弱、需要先建立几何直觉的人。
2. **⌨️ 硬核手写派**（边看边敲，与 AURORA 同频）：Karpathy → Umar Jamil → Valerio Velardo → Steve Brunton。看一段就暂停，自己用 NumPy 复刻，再对齐参考实现（正是 AURORA 的工作流）。
3. **🀄 中文母语派**：李宏毅（ML/语音/TTS）→ 李沐（论文精读）→ 可汗学院简体中文（数学）。用母语打通概念，再回英文正课深化。

> **时间预算**：数学与信号基础（Phase 0–4）建议每课配 1 段直觉视频（10–30 分钟）即可；Audio DSP / DL / LLM 三大手写阶段值得把对应的 Karpathy/Velardo/Umar Jamil 长视频**完整跟写一遍**（单条 2–4 小时，物有所值）。

---

## Phase 0–1 · 数学与信号直觉基础（L01–L08）

> 复数三角与傅里叶直觉是整个音频 AI 的第一把钥匙。先在这里把「复数乘法 = 旋转 + 缩放」「方波 = 正弦叠加」看透，后面手写 DFT/FFT 才不会是死公式。

### 线性代数的本质 Essence of Linear Algebra
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **类型**: 播放列表（16 集） · **难度**: 入门 · **语言**: 英文（社区中文字幕可选；B 站有官方双语搬运） · **时长**: 约 3 小时
- **覆盖**: 向量/线性组合/张成空间、矩阵=线性变换、矩阵乘法=变换复合、行列式、逆矩阵/列空间/零空间、点积与叉积、特征值与特征向量、基变换、抽象向量空间
- **对齐 Aurora**: L05–L21（复数几何延伸到线代）
- **为何契合**: 核心命题「矩阵就是线性变换」正是 AURORA「矩阵即滤波（DFT/Mel 矩阵）」思想源头；纯几何推导、零黑箱。**Phase 1–2 的直觉总纲。**

### 微积分的本质 Essence of Calculus
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- **类型**: 播放列表（12 集） · **难度**: 入门 · **语言**: 英文（社区中文字幕可选） · **时长**: 约 3 小时
- **覆盖**: 导数的几何本质、切线、幂/指数/三角函数求导、链式法则与乘积法则（可视化）、隐函数求导、极限、积分与微积分基本定理、泰勒级数
- **对齐 Aurora**: L22–L26（微积分）
- **为何契合**: 第 4 集「可视化链式法则」是 AURORA 反向传播（L24–L25）的直觉基石；强调「让你觉得自己本可以发明微积分」，与第一性原理精神一致。

### 傅里叶变换 & 傅里叶级数（两集可视化直觉）
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: 傅里叶变换 https://www.youtube.com/watch?v=spUNpyF58BY ｜ 傅里叶级数 https://www.youtube.com/watch?v=r6sGWTCMz2k
- **类型**: 单视频 ×2 · **难度**: 入门 → 进阶 · **语言**: 英文（社区中文字幕可选） · **时长**: 约 21 分 + 25 分
- **覆盖**: 把信号「绕在圆上」求质心 → 频域分解的几何本质；旋转向量（复指数）叠加逼近任意波形/方波，即「方波 = 正弦叠加」
- **对齐 Aurora**: L07–L08（傅里叶直觉），并在 L35–L42 手写 DFT/FFT 时复看
- **为何契合**: 用旋转向量把「复指数 e^{iθ} + 叠加 = 频谱」讲透，直接对应 AURORA 手写 DFT 前必须建立的直觉；比任何公式推导都更「可复现」。

### 欧拉公式（群论视角）Euler's Formula via Group Theory
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: https://www.youtube.com/watch?v=mvmuCPvRoWQ
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文（社区中文字幕可选） · **时长**: 约 24 分钟
- **覆盖**: 把「数」看作「作用（旋转/缩放）」，理解 e^{iθ} 为何是绕单位圆旋转、e^{iπ}=−1 的几何含义
- **对齐 Aurora**: L05–L06（复数几何=旋转+缩放、欧拉公式）
- **为何契合**: 直击 AURORA 复数模块核心命题「复数乘法 = 旋转 + 缩放」；用「作用」而非死记公式来理解欧拉公式，第一性原理典范。

### 可汗学院（简体中文）Khan Academy Mandarin
- **讲师/机构**: Khan Academy 简体中文组
- **链接**: https://www.youtube.com/user/KhanAcademyMandarin （配套习题站 https://zh.khanacademy.org/math/linear-algebra ）
- **类型**: 频道 / 完整课程 · **难度**: 入门 · **语言**: 中文（简体配音/字幕） · **时长**: 单集 5–15 分钟，成体系
- **覆盖**: 向量与线性组合、矩阵与线性方程、点积与投影、零空间/列空间、秩、特征值特征向量、正交化；另有微积分/概率分册
- **对齐 Aurora**: L09–L21（线代）、部分 L22–L31
- **为何契合**: 满足「中文入门梯度」需求；小步骤讲解 + 习题，适合先用母语打通概念再回 3B1B/MIT 深化。

---

## Phase 2 · 线性代数（L09–L21）

> AURORA 要手写高斯消元、LU/QR/SVD、特征分解——先用 3B1B 建直觉，再用 MIT 18.06 补严谨，最后用 Brunton 落到能跑的代码。

### MIT 18.06 线性代数（Gilbert Strang 完整课程）
- **讲师/机构**: Prof. Gilbert Strang, MIT OpenCourseWare
- **链接**: https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C （18.06SC, Fall 2011）
- **类型**: 完整课程（约 35+ 讲，含习题精讲） · **难度**: 进阶 · **语言**: 英文（YouTube 字幕） · **时长**: 约 35–40 小时
- **覆盖**: 高斯消元、A=LU、列空间/零空间/秩、正交性与投影、Gram-Schmidt/QR、行列式、特征值与对角化 A=PDP⁻¹、对称/正定矩阵、SVD、线性变换
- **对齐 Aurora**: L09–L21（线性代数）
- **为何契合**: AURORA 手写高斯消元、LU/QR/SVD、特征分解的**权威严谨对照**；Strang 边推导边讲「为什么」，是把 3B1B 直觉落到可手写实现的桥梁。

### 奇异值分解 SVD（Data-Driven Science & Engineering）
- **讲师/机构**: Prof. Steve Brunton, University of Washington
- **链接**: https://www.youtube.com/playlist?list=PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv
- **类型**: 播放列表（约 7 小时） · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 约 7 小时
- **覆盖**: SVD 数学概览、矩阵低秩逼近、主导相关性、图像压缩（手写代码）、矩阵补全、PCA 与 SVD 关系、随机化 SVD
- **对齐 Aurora**: L18–L21（特征值/SVD、矩阵分解）
- **为何契合**: 每个概念都配 Python/MATLAB **手撕代码**，与 AURORA「NumPy 手写并对齐参考实现」的工作流几乎一模一样。

### Serrano.Academy（机器学习数学直觉）
- **讲师/机构**: Dr. Luis Serrano（前 Google/Apple/Udacity/Cohere，数学博士）
- **链接**: https://www.youtube.com/channel/UCgBncpylJ1kiVaPyP-PZauQ
- **类型**: 频道（含 SVD/PCA、概率、softmax、Bayes 等播放列表） · **难度**: 入门 → 进阶 · **语言**: 英文（另有西语频道） · **时长**: 单集 10–30 分钟
- **覆盖**: 奇异值分解与图像压缩、主成分分析、点积与投影、概率与贝叶斯、softmax/交叉熵、余弦相似度
- **对齐 Aurora**: L11–L21（线代）、L27–L31（概率统计）
- **为何契合**: 擅长用类比/图示把 SVD、softmax 讲到「能自己重写一遍」，是 3B1B 与名校课之间的难度衔接层。

---

## Phase 3 · 微积分（L22–L26）

> 梯度就是反向传播的方向盘。这里把「链式法则 → 反向传播」看透，Phase 6 手写训练循环就水到渠成。

### 神经网络如何学习：梯度下降 + 反向传播直觉
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: 梯度下降 https://www.youtube.com/watch?v=IHZwWFHWa-w ｜ 反向传播微积分 https://www.youtube.com/watch?v=tIeHLnjs5U8
- **类型**: 单视频 ×2（隶属 Neural Networks 系列） · **难度**: 进阶 · **语言**: 英文（官方多语字幕，含简体中文） · **时长**: 约 21 分 + 14 分
- **覆盖**: 代价函数曲面、梯度=最速下降方向、梯度下降迭代；反向传播如何按链式法则高效计算梯度
- **对齐 Aurora**: L24–L25（链式法则 / 梯度下降），延伸 L54–L57
- **为何契合**: 把「链式法则 → 反向传播」的可视化讲到极致，是 AURORA 手写训练循环前的必看直觉课。

### MIT 18.02 多元微积分（梯度与偏导）
- **讲师/机构**: Prof. Denis Auroux, MIT OpenCourseWare (Fall 2007)
- **链接**: https://www.youtube.com/playlist?list=PLEAYkSg4uSQ2dvsWLz9X6ANX_U-cwtOaX
- **类型**: 完整课程（35 讲） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 30 小时
- **覆盖**: 偏导数、梯度与方向导数、多元链式法则、拉格朗日乘子、二重/三重积分、向量微积分
- **对齐 Aurora**: L23（梯度/偏导），支撑 L24–L25
- **为何契合**: 为 AURORA 梯度下降与反向传播提供**多元微积分的严谨底座**；Auroux 的偏导/梯度两讲是把 3B1B 直觉补成可推导实现的关键。

---

## Phase 4 · 概率统计（L27–L31）

### StatQuest 统计基础 Statistics Fundamentals
- **讲师/机构**: Josh Starmer (StatQuest)
- **链接**: https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9
- **类型**: 播放列表（约 60 集） · **难度**: 入门 · **语言**: 英文（清晰口语 + 字幕） · **时长**: 约 10–15 小时
- **覆盖**: 直方图/分布、均值/方差/标准差、正态分布、采样与总体参数、协方差与相关、中心极限定理、标准误、概率 vs 似然、最大似然估计、期望值、z-score
- **对齐 Aurora**: L27–L31（概率统计）
- **为何契合**: 「把每个方法拆成最小步骤」的教学法与 AURORA 手写实现同频；均值/方差/z-score/分布采样（L28–L30）用它打底最省力。

### Harvard Stat 110: Probability（Joe Blitzstein 完整课程）
- **讲师/机构**: Prof. Joe Blitzstein, Harvard University
- **链接**: https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo
- **类型**: 完整课程（34 讲） · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 约 28 小时
- **覆盖**: 概率与计数、条件概率/独立性、随机变量与分布（伯努利/二项/几何/泊松/均匀/正态/指数）、期望与线性性、方差/协方差、条件期望、不等式、大数定律与中心极限定理
- **对齐 Aurora**: L27–L31（概率统计）
- **为何契合**: 条件概率/独立性/大数定律（L27）的黄金标准课；Blitzstein 坚持「从定义一步步推、拒绝套公式」。

### StatQuest 神经网络 / 深度学习（含 Softmax 与交叉熵导数）
- **讲师/机构**: Josh Starmer (StatQuest)
- **链接**: https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1
- **类型**: 播放列表 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 6–8 小时
- **覆盖**: ArgMax/SoftMax、SoftMax 导数逐步推导、交叉熵、交叉熵导数与反向传播、神经网络基础到 Transformer
- **对齐 Aurora**: L30–L31（softmax 与交叉熵），延伸 L55–L58
- **为何契合**: 把 softmax 与交叉熵的**导数一步步手推**，正好对齐 AURORA 手写并验证梯度的要求。

---

## Phase 5 · Audio DSP 音频信号处理（L32–L53）

> **本阶段是 AURORA 的音频核心，也是全库对齐最紧的一段。** 采样→窗→DFT/FFT→STFT→Mel→MFCC，一路手写不用 librosa/scipy。首选 Valerio Velardo，几乎逐课对应。

### 🥇 Audio Signal Processing for Machine Learning（必看 · 置顶）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0
- **类型**: 播放列表（约 24 讲） · **难度**: 入门 → 进阶 · **语言**: 英文（自带英文字幕） · **时长**: 累计约 12 小时
- **覆盖**: 声波与波形、时域/频域特征（RMS、过零率、频谱质心）、傅里叶变换与 STFT、频谱图、Mel 频率尺度与三角滤波器组、Mel 频谱、MFCC 完整流水线；每讲「直觉 + 数学 + Python 实现」三段式，配 GitHub 代码
- **对齐 Aurora**: L32–L53（Audio DSP 全阶段）
- **为何契合**: 与本阶段几乎逐课对应，全网最贴合 AURORA 音频核心的系列；FFT/STFT/Mel/MFCC 全部亲手实现、不套黑箱，是「第一性原理手写」的范本。

### The Sound of AI 频道（Mel 谱 / MFCC 单课深挖）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ
- **类型**: 频道（含多支独立长视频） · **难度**: 进阶 · **语言**: 英文 · **时长**: 单课 40–60 分钟
- **覆盖**: 单独成篇的 Mel 频谱、Cepstrum 倒谱、MFCC 逐步推导与可视化，及声道/语音生成物理解释
- **对齐 Aurora**: L46–L53（Mel / MFCC）
- **为何契合**: 讲 MFCC 时把「信号→STFT→Mel→log→DCT」每一环拆开手算，直接支撑 L49–L53。⚠️ 单课直链未逐一核实，在该频道搜 "Mel-Frequency Cepstral Coefficients Explained Easily"。

### But what is the Fourier Transform? / Fourier series（可视化直觉）
- **讲师/机构**: 3Blue1Brown (Grant Sanderson)
- **链接**: 变换 https://www.youtube.com/watch?v=spUNpyF58BY ｜ 级数 https://www.youtube.com/watch?v=r6sGWTCMz2k （另见 [Phase 0–1](#phase-01--数学与信号直觉基础l01l08)）
- **类型**: 单视频 ×2 · **难度**: 入门 · **语言**: 英文（含社区中文字幕） · **时长**: 约 20 分 + 25 分
- **覆盖**: 旋转因子 e^{-2πift} 的几何意义、复指数求和逼近周期函数
- **对齐 Aurora**: L35, L37–L42
- **为何契合**: 动手写 DFT 前建立「旋转因子/复指数」几何直觉，让 L35 欧拉公式与 L37 暴力 DFT 的求和不再是死公式。

### Fourier Analysis [Data-Driven Science and Engineering]
- **讲师/机构**: Steve Brunton — University of Washington
- **链接**: https://www.youtube.com/playlist?list=PLMrJAkhIeNNT_Xh3Oy0Y4LTj0Oxo8GqsC
- **类型**: 播放列表（完整课程） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 8 小时 / 40+ 讲
- **覆盖**: 傅里叶级数、复数傅里叶级数、傅里叶变换、DFT、FFT 算法、Gabor 变换/声谱图、小波；含 MATLAB + Python 实操（去噪、求导、解 PDE）
- **对齐 Aurora**: L35–L48
- **为何契合**: 名校教授系统串讲 DFT→FFT 的数学与代码，DFT 矩阵分解视角直接指导 L37 O(N²) 暴力法与 L38–L42 蝶形分治的手写实现。

### The Fast Fourier Transform: Most Ingenious Algorithm Ever?
- **讲师/机构**: Reducible
- **链接**: https://www.youtube.com/watch?v=h7apO7q16V0
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 28 分钟
- **覆盖**: 从多项式乘法引入，讲 N 次单位根、分治递归、Cooley-Tukey 蝶形结构与 IFFT，动画拆解 O(N log N)
- **对齐 Aurora**: L38–L42
- **为何契合**: 全网讲「为什么 FFT 能分治」最清晰的动画，直接对标 L39–L40「从零手写 FFT」，递归结构可照着改写成 NumPy。

### Denoising Data with FFT [Python]
- **讲师/机构**: Steve Brunton — University of Washington
- **链接**: https://www.youtube.com/watch?v=s2K1JfNR7Sc
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 11 分钟
- **覆盖**: 用 Python/NumPy 对含噪信号做 FFT、看幅度谱、按功率阈值滤波再逆变换的完整代码演示
- **对齐 Aurora**: L40–L42（频谱分析实战）
- **为何契合**: 一支端到端的「手写 FFT 频谱分析 + 幅度谱/功率谱」实操，可作为 AURORA 手写 FFT 后的验证案例。

### How the Cooley-Tukey FFT Algorithm Works（逐步手推 FFT）
- **讲师/机构**: Mark Newman — Mark Newman Education
- **链接**: https://www.youtube.com/c/MarkNewmanEducation ⚠️（系列单视频直链未核实；频道已核实，配套图文见 dsprelated.com 同名 Part 1–4）
- **类型**: 频道 / 多集系列 · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 分 4 部分
- **覆盖**: 用归并排序类比讲奇偶分解，2 点 DFT 化为加减、bit-reversal 重排、twiddle factor 推导，直至可手写实现的蝶形图
- **对齐 Aurora**: L38–L42
- **为何契合**: 把 FFT 拆到「能照着敲代码」的颗粒度，最契合从零实现 FFT（搜 "Mark Newman Cooley-Tukey FFT"）。

### MIT RES.6.007 Signals and Systems（信号与系统全课）
- **讲师/机构**: Alan V. Oppenheim — MIT OpenCourseWare
- **链接**: https://www.youtube.com/playlist?list=PL41692B571DD0AF9B
- **类型**: 完整课程（约 30 讲） · **难度**: 高级 · **语言**: 英文 · **时长**: 每讲约 50 分钟
- **覆盖**: 连续/离散时间信号与系统、傅里叶级数/变换、采样与重建、Laplace/Z 变换
- **对齐 Aurora**: L32–L48
- **为何契合**: DSP 泰斗、经典教材作者亲授，为 AURORA 的傅里叶与采样章节提供最权威的理论地基与符号规范。

### MIT RES.6.007 — Lecture 16: Sampling（采样 / Nyquist / 混叠）
- **讲师/机构**: Alan V. Oppenheim — MIT OpenCourseWare
- **链接**: https://www.youtube.com/watch?v=P3eLer1edx8
- **类型**: 单视频（课程第 16 讲） · **难度**: 高级 · **语言**: 英文 · **时长**: 约 50 分钟
- **覆盖**: 冲激采样、频谱周期化、Nyquist 采样定理证明、混叠成因与频域图解、重建条件
- **对齐 Aurora**: L33–L34（Nyquist 与混叠）
- **为何契合**: 权威推导 Nyquist 定理与混叠，正是 L34 aliasing 一课的理论出处。

### 深度学习与人类语言处理 DLHLP（2020，含语音特征）
- **讲师/机构**: 李宏毅 Hung-yi Lee — 台湾大学 NTU
- **链接**: https://www.youtube.com/playlist?list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG
- **类型**: 完整课程 · **难度**: 进阶 · **语言**: 中文（国语讲授，含中文字幕） · **时长**: 每讲约 1 小时
- **覆盖**: 语音识别总览中的声学特征（MFCC/滤波器组）、frame 切分与特征提取，及后续 LAS/CTC/RNN-T 语音模型
- **对齐 Aurora**: L49–L53（特征工程的中文对应）
- **为何契合**: 顶尖华语名师，用中文把「波形→帧→MFCC/filter bank 特征」讲清，补齐双语课程的中文侧。

---

## Phase 6 · 机器学习 / 深度学习基础（L54–L65）

> 从标量自动微分（micrograd）到 PyTorch，再到音频 CNN 分类。**首选 Karpathy「Zero to Hero」——与 L54–L58 逐课对应，是全网从零手写反向传播的黄金对标。**

### 🥇 Neural Networks: Zero to Hero（完整课程）
- **讲师/机构**: Andrej Karpathy（前 OpenAI / 前 Tesla AI 总监）
- **链接**: https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- **类型**: 播放列表（8 讲） · **难度**: 入门 → 高级 · **语言**: 英文（自动中英字幕） · **时长**: 约 15+ 小时
- **覆盖**: micrograd 标量自动微分引擎、反向传播、makemore（bigram→MLP→BatchNorm→手推反向 "Backprop Ninja"→WaveNet）、Let's build GPT
- **对齐 Aurora**: L54–L58（深度学习），并延伸 L83（LLM）
- **为何契合**: AURORA「第一性原理/手写实现」的黄金对标——全程从零手写节点、前向反向、训练循环，不用任何 wrapper。**本主题必收核心。**

### The spelled-out intro to neural networks and backpropagation: building micrograd
- **讲师/机构**: Andrej Karpathy
- **链接**: https://youtu.be/VMj-3S1tku0 （配套：makemore Part 2 (MLP) https://youtu.be/TCH_1BHY58I ｜"Backprop Ninja" https://youtu.be/q8SA3rM6ckI ）
- **类型**: 单视频 · **难度**: 入门 · **语言**: 英文（中英字幕） · **时长**: 2 小时 25 分
- **覆盖**: 手写 Value 节点（add/mul/pow/tanh/exp）、构建动态计算图 DAG、链式法则逐层反向、手推梯度、在 micrograd 上搭 MLP 并训练
- **对齐 Aurora**: L54–L56（Value 计算图、算子补全、反向传播手推）
- **为何契合**: 与 L54–L56 几乎逐点对应，最详尽的 "spelled-out" 反向传播讲解；配套 makemore Part 2 对齐 L57（MLP），"Backprop Ninja" 对齐 L55（手推反向）。

### Neural Networks（可视化系列）
- **讲师/机构**: Grant Sanderson (3Blue1Brown)
- **链接**: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
- **类型**: 播放列表（核心 4 集） · **难度**: 入门 · **语言**: 英文（官方多语字幕，含简体中文） · **时长**: 约 1.5 小时
- **覆盖**: 什么是神经网络、梯度下降如何学习、反向传播直觉、反向传播微积分（链式法则）
- **对齐 Aurora**: L55–L57
- **为何契合**: 用顶级动画把链式法则/反向传播的几何直觉讲透，是 L55 手推反向前的最佳直觉铺垫，与 Karpathy 的代码实现互补。

### Neural Networks / Deep Learning
- **讲师/机构**: StatQuest with Josh Starmer
- **链接**: https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1
- **类型**: 播放列表 · **难度**: 入门 · **语言**: 英文（中英字幕） · **时长**: 约 5–6 小时（多为 10–20 分钟短集）
- **覆盖**: 神经网络基础、反向传播主线思想、逐参数优化的链式法则、ReLU、CNN 图像分类
- **对齐 Aurora**: L55–L58、L64
- **为何契合**: "Backpropagation Details Pt.1/Pt.2" 把 L55 手推反向拆成最小步骤；CNN 集对齐 L64 音频分类的卷积直觉。

### MIT 6.S191: Introduction to Deep Learning
- **讲师/机构**: MIT（Alexander Amini / Ava Soleimany）
- **链接**: https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI （课程主页 https://introtodeeplearning.com/ ）
- **类型**: 完整课程（每年更新） · **难度**: 入门 → 进阶 · **语言**: 英文（中英字幕） · **时长**: 约 10 讲，每讲 45–60 分钟
- **覆盖**: 感知机与 MLP、反向传播、训练技巧（正则化/过拟合诊断）、CNN、RNN/Transformer，含 TensorFlow/PyTorch 实验
- **对齐 Aurora**: L54–L65（整体概览）
- **为何契合**: 名校顶配、每年刷新的系统课，给 L54–L65 提供从 MLP 到 CNN、过拟合诊断的权威主线框架。

### 🥇 PyTorch for Audio + Music Processing
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/playlist?list=PL-wATfeyAMNoirN4idjev6aRu8ISZYVWm （代码 https://github.com/musikalkemist/pytorchforaudio ；示例 "Training a Sound Classifier with PyTorch" https://www.youtube.com/watch?v=MMkeLjcBTcI ）
- **类型**: 播放列表 · **难度**: 进阶 · **语言**: 英文（中英字幕） · **时长**: 约 3–4 小时
- **覆盖**: 用 torchaudio 自定义音频 Dataset（__getitem__）、DataLoader 批量加载、提取 Mel 频谱、重采样/mixdown、搭 CNN 在 UrbanSound8K 上训练声音分类器、train loop
- **对齐 Aurora**: L62–L65
- **为何契合**: 与 L62–L65 高度重合——自定义 Dataset/DataLoader + Mel 特征 + CNN 音频分类 + 训练闭环，几乎就是 AURORA 关键词识别任务的 PyTorch 蓝本。

### Learn PyTorch for Deep Learning – Full Course
- **讲师/机构**: Daniel Bourke（freeCodeCamp.org 出品）
- **链接**: https://www.youtube.com/watch?v=V_xro1bcAuA （配套 https://www.learnpytorch.io/ ｜代码 https://github.com/mrdbourke/pytorch-deep-learning ）
- **类型**: 单视频（约 25 小时）/ 完整课程 · **难度**: 入门 → 进阶 · **语言**: 英文（中英字幕） · **时长**: 约 25 小时
- **覆盖**: PyTorch Tensor、autograd 与 requires_grad、nn.Module/Linear/Sequential、训练循环、自定义 Dataset、CNN、模型保存/加载
- **对齐 Aurora**: L59–L65
- **为何契合**: 覆盖 L59–L65 全部 PyTorch 主题，可作为 PyTorch 段的系统主教程。

### PyTorch Tutorials — Complete Beginner Course
- **讲师/机构**: Patrick Loeber（现 Google DeepMind DevRel）
- **链接**: https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4 （代码 https://github.com/patrickloeber/pytorchTutorial ）
- **类型**: 播放列表 · **难度**: 入门 · **语言**: 英文（中英字幕） · **时长**: 约 4–5 小时
- **覆盖**: Tensor 基础与 NumPy 互转、autograd 机制、backward 与梯度、手写线性/逻辑回归训练、nn.Module、Dataset & DataLoader、激活函数
- **对齐 Aurora**: L59–L62
- **为何契合**: 短小精悍、逐个概念拆解，先手写训练循环再用 nn 封装，契合「先第一性原理后封装」的节奏。

### Deep Learning (For Audio) With Python
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: 频道 https://www.youtube.com/@ValerioVelardoTheSoundofAI （代码 https://github.com/musikalkemist/DeepLearningForAudioWithPython ）⚠️ 播放列表直链未逐一核实，从频道 "Playlists" 进入 "Deep Learning (For Audio) With Python"
- **类型**: 播放列表 · **难度**: 入门 → 进阶 · **语言**: 英文（中英字幕） · **时长**: 约 5–6 小时
- **覆盖**: 从零手写神经元与反向传播 → 声音/波形/傅里叶/STFT/Mel 谱/MFCC → MLP/CNN/RNN-LSTM 音乐流派分类
- **对齐 Aurora**: L54–L55、L63–L64
- **为何契合**: 前几集从零手写神经元+反向传播（呼应 L54–L55），后半系统讲 Mel/MFCC 与 CNN 分类（呼应 L63–L64），把手写 ML 与音频 AI 打通。

### Practical Deep Learning for Coders 2022
- **讲师/机构**: Jeremy Howard（fast.ai）
- **链接**: https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU （课程主页 https://course.fast.ai/ ）
- **类型**: 完整课程（9 讲） · **难度**: 入门 → 进阶 · **语言**: 英文（中英字幕） · **时长**: 每讲约 90 分钟
- **覆盖**: 训练与部署模型、从零实现 MLP 与反向传播（"从矩阵乘法搭起"）、SGD 训练循环、CNN、过拟合诊断
- **对齐 Aurora**: L57–L65
- **为何契合**: 以「先能跑通再拆内部」的工程视角补充 Karpathy；从零实现神经网络与训练循环，对齐 L57–L58 并延伸完整训练评估闭环。

### 機器學習 / 深度學習（Machine Learning, NTU 2021）
- **讲师/机构**: 李宏毅 Hung-yi Lee（台湾大学）
- **链接**: https://www.youtube.com/playlist?list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49 （课程主页 https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html ）
- **类型**: 完整课程 · **难度**: 入门 → 高级 · **语言**: 中文（国语讲授，中文投影片） · **时长**: 数十小时
- **覆盖**: 反向传播、梯度下降与优化、MLP/CNN、训练技巧（过拟合/正则化/批归一化）、深度学习理论
- **对齐 Aurora**: L54–L65
- **为何契合**: 华语圈公认最佳中文深度学习课，反向传播与优化章节直接支撑 L55–L58，可作中文学习者主线。

### Machine Learning Specialization / DeepLearning.AI
- **讲师/机构**: Andrew Ng（斯坦福 / DeepLearning.AI）
- **链接**: https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI （频道 https://www.youtube.com/c/deeplearningai ）
- **类型**: 播放列表 / 完整课程 · **难度**: 入门 · **语言**: 英文（中英字幕） · **时长**: 数十小时
- **覆盖**: 神经网络与深度学习基础、前向/反向传播、逻辑回归到深层网络、梯度下降、超参数与正则化
- **对齐 Aurora**: L54–L58
- **为何契合**: 最经典的入门权威，把 MLP、前向反向、训练收敛讲得极稳，适合作为 Karpathy 手写实现的理论对照。

---

## Phase 7 · 语音识别 ASR / STT（L66–L75）

> 从编辑距离/WER，到 CTC 前向算法，再到 Whisper 架构与 beam search。**中文主线首选李宏毅 DLHLP；CTC 前向算法数学推导首选 CMU 11-785。**

### 🥇 李宏毅 DLHLP 2020 — Speech Recognition 系列（LAS / CTC / RNN-T / HMM）
- **讲师/机构**: 李宏毅 Hung-yi Lee（台大 NTU）
- **链接**: 课程页 https://speech.ee.ntu.edu.tw/~hylee/dlhlp/2020-spring.php ｜频道 https://www.youtube.com/@HungyiLeeNTU
- **类型**: 完整课程（内含 "Speech Recognition" 7 讲子系列） · **难度**: 入门 → 进阶 · **语言**: 中文（国语讲授） · **时长**: 语音识别部分约 3–4 小时
- **覆盖**: 端到端 ASR 全景；Listen-Attend-Spell、CTC、RNN-T、HMM 对齐、beam search 解码直觉
- **对齐 Aurora**: L66–L75
- **为何契合**: 全网最好的中文语音识别原理课，把 CTC / seq2seq / HMM→E2E 讲成直觉故事，和 AURORA「第一性原理」完全同频。**中文置顶首选。**

### CMU 11-785 Introduction to Deep Learning — CTC / Seq2Seq
- **讲师/机构**: Bhiksha Raj、Rita Singh（卡内基梅隆 CMU）
- **链接**: 频道 https://www.youtube.com/channel/UC8hYZGEkI2dDO8scT8C5UQA ｜课程页 https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/ ｜CTC 讲座 https://www.youtube.com/watch?v=5Rj0J9AuGw0
- **类型**: 完整课程中的专题讲座 · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 单讲约 80 分钟
- **覆盖**: CTC 前向-后向算法逐步推导、blank 符号、路径求和、CTC beam search；seq2seq/attention 对齐
- **对齐 Aurora**: L67–L69（CTC 对齐 + 前向算法）
- **为何契合**: 名校课程里对 CTC 前向算法数学推导最扎实的一档，正对 AURORA「纯 NumPy 手写 CTC 前向」的目标，可直接照着实现。

### Whisper Paper Explained — Robust Speech Recognition via Large-Scale Weak Supervision
- **讲师/机构**: Aladdin Persson（以「从零实现」著称）
- **链接**: 频道 https://www.youtube.com/@AladdinPersson ｜搜索："Aladdin Persson Whisper Paper Explained" ⚠️ 单视频精确 URL 未核实（约 33 分钟）
- **类型**: 单视频（论文精读） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 33 分钟
- **覆盖**: Whisper 架构（log-Mel + conv + encoder-decoder）、68 万小时弱监督数据、zero-shot 评测、长音频转写
- **对齐 Aurora**: L70–L71（Whisper 架构 + 解码）
- **为何契合**: 「from scratch」教育风格作者，讲论文紧扣工程实现取舍，是理解 Whisper 设计动机的高性价比入口。

### Whisper 解码器复用：Let's build GPT（Karpathy）
- **讲师/机构**: Andrej Karpathy
- **链接**: https://www.youtube.com/watch?v=kCc8FmEb1nY （配套代码 https://github.com/karpathy/build-nanogpt ；完整介绍见 [Phase 9](#phase-9--llm--rag--agent-l83l91)）
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 1 小时 56 分
- **覆盖**: 从零手写 Transformer 解码器（self-attention、causal mask、自回归生成）
- **对齐 Aurora**: L70（Whisper 解码器部分）
- **为何契合**: Whisper 是 encoder-decoder Transformer，其 GPT 式解码器可直接复用本课手写实现，再叠加音频 encoder 与 cross-attention。

### wav2vec 2.0 论文精读
- **讲师/机构**: Yannic Kilcher
- **链接**: https://www.youtube.com/watch?v=aUSXvoWfy3w （标题已核实 "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations"；频道 https://www.youtube.com/c/YannicKilcher ）
- **类型**: 单视频（论文逐段精读） · **难度**: 高级 · **语言**: 英文 · **时长**: 约 50 分钟
- **覆盖**: 自监督语音表征、latent masking、contrastive loss、product quantization、微调后超越半监督
- **对齐 Aurora**: L72（进阶：wav2vec 2.0）
- **为何契合**: Yannic 的招牌逐段读论文，把自监督预训练直觉讲透，是进阶章节 wav2vec 2.0 的权威精读。

### Hugging Face Audio Course + Fine-Tune Whisper 实战
- **讲师/机构**: Hugging Face（Sanchit Gandhi 等）
- **链接**: 课程 https://huggingface.co/learn/audio-course ｜CTC 章节 https://huggingface.co/learn/audio-course/chapter3/ctc ｜Whisper 微调 https://huggingface.co/blog/fine-tune-whisper
- **类型**: 完整课程 + 动手 Notebook（**官方免费课程，非 YouTube**） · **难度**: 入门 → 进阶 · **语言**: 英文（社区多语翻译） · **时长**: 自定进度
- **覆盖**: CTC 架构（Wav2Vec2/HuBERT）、Whisper encoder-decoder、在 Common Voice/LibriSpeech 上微调 whisper-small、WER 评测
- **对齐 Aurora**: L69、L72（Whisper-small 微调）
- **为何契合**: 直接对齐 L72「Whisper-small 微调」；CTC 章节讲清 encoder-only+CTC 与 Whisper 端到端两条路线的差异，最贴近实操。

### Stanford CS224S — Spoken Language Processing
- **讲师/机构**: Stanford（Dan Jurafsky 传统 + 近年 LLM-speech 客座）
- **链接**: 课程页 https://web.stanford.edu/class/cs224s/ ｜Stanford Online https://online.stanford.edu/courses/cs224s-spoken-language-processing ｜端到端语音讲座（含 CTC）https://www.youtube.com/watch?v=3MjIkWxXigM
- **类型**: 完整课程（部分公开讲座 + 讲义） · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 一学期
- **覆盖**: WER 评估、HMM-GMM、CTC/attention 端到端、解码策略、口语处理全景
- **对齐 Aurora**: L66–L75
- **为何契合**: 名校完整口语处理课，系统覆盖 WER→CTC→端到端，讲义可作全章脚手架（注：完整视频多在注册学生 Canvas 内，YouTube 仅部分公开讲座）。

### Valerio Velardo — Deep Learning for Audio / 构建 ASR 系统
- **讲师/机构**: Valerio Velardo（The Sound of AI）
- **链接**: 频道 https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ ｜Deep Learning (For Audio) with Python 播放列表 https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf
- **类型**: 播放列表 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 15–18 段
- **覆盖**: 音频特征（mel spectrogram/MFCC）、CNN/RNN 声学建模、从设计到部署搭建语音识别 app
- **对齐 Aurora**: L66、L73（音频前端 + 声学建模）
- **为何契合**: 「直觉+数学+代码」三段式，补齐 AURORA ASR 章节所需的音频前端第一性原理。

### University of Edinburgh — Automatic Speech Recognition (ASR)
- **讲师/机构**: Steve Renals、Hiroshi Shimodaira（爱丁堡大学 CSTR）
- **链接**: 课程页 https://www.inf.ed.ac.uk/teaching/courses/asr/ ｜HMM-GMM 讲义 https://www.inf.ed.ac.uk/teaching/courses/asr/2018-19/asr03-hmmgmm-handout.pdf
- **类型**: 完整课程（**公开讲义/PDF**；视频对注册学生开放） · **难度**: 高级 · **语言**: 英文 · **时长**: 18 讲
- **覆盖**: HMM-GMM 声学模型、维特比解码、WFST、DNN-HMM 混合、直至端到端（CTC/attention）的演变
- **对齐 Aurora**: L75（进阶：传统声学模型→端到端）
- **为何契合**: 讲传统 HMM-GMM→DNN-HMM→端到端演进最权威的公开材料，正对 AURORA「从 HMM-GMM 到端到端」进阶主题。

### AssemblyAI — 语音识别 / Whisper 直觉讲解
- **讲师/机构**: AssemblyAI（工业界语音 API 团队，教育向内容）
- **链接**: 频道 https://www.youtube.com/@assemblyai ｜搜索："AssemblyAI Whisper how it works"
- **类型**: 频道 / 系列短视频 · **难度**: 入门 · **语言**: 英文 · **时长**: 单集约 10–20 分钟
- **覆盖**: ASR 流程直觉、Whisper 工作原理、CTC vs seq2seq、实时/流式转写概念
- **对齐 Aurora**: L70、L74（入门 + 流式概念）
- **为何契合**: 轻量入门与全局直觉，适合作 L70 Whisper、L74 流式 ASR 的「预热」层，再进 CMU/李宏毅深水区。

> **关于 L66（编辑距离 / WER）**：Levenshtein DP 与 WER 是经典二维 DP，上述李宏毅、CS224S、HF Audio Course 均含 WER 评估讲解。若只需手写 DP，直接在 AURORA 内实现即可，无需外部视频。

---

## Phase 8 · 音乐智能 / MIR（L76–L82）

> chroma / onset / beat tracking / 音乐嵌入 / 相似检索。**权威首选 Meinard Müller (FMP)——附开源 Notebooks，正是「第一性原理手写」的黄金对照。**

### Audio Signal Processing for Machine Learning（特征地基）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0 （完整介绍见 [Phase 5](#phase-5--audio-dsp-音频信号处理l32l53)）
- **类型**: 播放列表 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 8–10 小时
- **对齐 Aurora**: L76–L78（特征地基）
- **为何契合**: chromagram/onset 之前必备的特征提取地基；与 AURORA「NumPy 手写音频特征」理念高度一致。

### 🥇 Music Processing using Chroma Features
- **讲师/机构**: Meinard Müller — AudioLabs Erlangen（FMP《Fundamentals of Music Processing》作者）
- **链接**: https://www.youtube.com/watch?v=PF05xP1NqUM （开源 FMP Notebooks https://www.audiolabs-erlangen.de/FMP ）
- **类型**: 单视频（FMP 配套导览） · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 短片
- **覆盖**: pitch class / 色度概念、从频谱到 chromagram 的映射、色度在和弦识别与音乐同步/对齐中的作用
- **对齐 Aurora**: L76–L77（chroma）
- **为何契合**: MIR 领域权威、FMP 教科书作者；强烈建议搭配其开源 **FMP Notebooks**（纯 Python/Jupyter 参考实现），正是 AURORA「第一性原理手写」的黄金对照。

### 🥇 Tempo and Beat Tracking
- **讲师/机构**: Meinard Müller — AudioLabs Erlangen
- **链接**: https://www.youtube.com/watch?v=FmwpkdcAXl0 （FMP C6 章节 Notebook）
- **类型**: 单视频（FMP 配套导览） · **难度**: 进阶 · **语言**: 英文 · **时长**: 短片
- **覆盖**: onset 检测与 spectral novelty（起音包络）、脉冲/周期性分析、tempo 估计与 beat tracking 的核心思路
- **对齐 Aurora**: L78（onset envelope + beat tracking）
- **为何契合**: 直接对应 L78，把「起音包络→自相关/新颖度→节拍」链路讲清，配 FMP C6 Notebook 可逐步手写复现。

### Learn Music Theory in Half an Hour（乐理速成）
- **讲师/机构**: Andrew Huang
- **链接**: https://www.youtube.com/watch?v=rgaTLrZGlk0
- **类型**: 单视频 · **难度**: 入门 · **语言**: 英文 · **时长**: 约 30 分钟
- **覆盖**: 音、八度、半音/全音、音阶与音程、和弦构成——十二平均律下的音高组织直觉
- **对齐 Aurora**: L76（pitch class / chroma wheel / MIDI↔Hz）
- **为何契合**: 为 L76 补齐乐理直觉，帮助纯工程背景者理解为何 chroma 要按 12 个 pitch class 折叠。

### Generating Sound with Neural Networks（VAE 生成声音）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/playlist?list=PL-wATfeyAMNpEyENTc-tVH5tfLGKtSWPp
- **类型**: 播放列表 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 5–6 小时
- **覆盖**: 自编码器→变分自编码器（VAE）原理与手写实现，在梅尔频谱域学习潜在表示（latent embedding）并重建/生成音频
- **对齐 Aurora**: L79（音乐嵌入模型）
- **为何契合**: MusicEncoder 的本质就是把音频压进 embedding 空间；本系列逐行实现 VAE 编码器/解码器与潜空间，是理解「音乐嵌入」最贴近手写的桥梁。

### C4W4L04 Triplet Loss
- **讲师/机构**: Andrew Ng — DeepLearning.AI
- **链接**: https://www.youtube.com/watch?v=d2XB5-tuCWU
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 15 分钟
- **覆盖**: anchor/positive/negative 三元组、margin、把同类拉近异类推远的 embedding 学习目标（FaceNet 思路）
- **对齐 Aurora**: L79（triplet loss）
- **为何契合**: 权威名师对 triplet loss 的经典讲解；损失函数与 AURORA MusicEncoder 的 triplet 训练完全通用，公式可直接迁移到 NumPy 手写。

### SimCLR Explained（NT-Xent 对比学习）
- **讲师/机构**: Yannic Kilcher
- **链接**: https://www.youtube.com/watch?v=7Id8SPH31UE
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 14–16 分钟
- **覆盖**: 正/负样本对、数据增强、NT-Xent（温度缩放的归一化交叉熵）损失、batch 内负样本机制
- **对齐 Aurora**: L79（NT-Xent 对比学习）
- **为何契合**: 直接对应 L79 的 NT-Xent，把 SimCLR 对比目标拆到公式级，帮助理解音乐嵌入的对比学习分支如何手写。

### 【機器學習 2022】語音與影像上的自督導式學習
- **讲师/机构**: 李宏毅 Hung-yi Lee — 台湾大学（NTU）
- **链接**: https://www.youtube.com/watch?v=lMIN1iKYNmA
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 中文（国语讲授，繁体字幕） · **时长**: 约 35 分钟
- **覆盖**: 语音/音频上的自监督与对比式表示学习（CPC、wav2vec 类思路）、正负样本与预测式目标
- **对齐 Aurora**: L79（对比学习音频嵌入）
- **为何契合**: 少有的高质量中文资源，把「音频如何在无标签下学表示」讲得系统清晰，为 L79 提供中文视角理论补充。

### Recommendation Systems using Nearest Neighbors（kNN 推荐）
- **讲师/机构**: Krish Naik
- **链接**: https://www.youtube.com/watch?v=kccT0FVK6OY
- **类型**: 单视频（教程） · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 20 分钟
- **覆盖**: 基于最近邻的相似度检索、用户/物品相似度、用 kNN 做 top-k 推荐的实现流程
- **对齐 Aurora**: L80–L81（相似度检索 + 推荐）
- **为何契合**: 直接对应 L80–L81「纯 kNN 相似度检索 + 推荐」，可对照 AURORA 用 NumPy 手写余弦相似度 + top-k（注：社区教程，作实操参考）。

### MusicGen Paper Explained（Meta 音乐生成）
- **讲师/机构**: AI Bites
- **链接**: https://www.youtube.com/watch?v=cbAa7kart-4
- **类型**: 单视频（论文精讲） · **难度**: 高级 · **语言**: 英文 · **时长**: 约 13 分钟
- **覆盖**: EnCodec 编解码、残差向量量化（RVQ）、codebook 交织模式、文本/旋律条件生成、单一语言模型架构
- **对齐 Aurora**: 进阶（MusicGen 音乐生成）
- **为何契合**: 把「音频→离散 token→语言模型生成」核心机制讲清，是理解现代音乐生成范式的高性价比入口。

### How Shazam Works (Probably!)（音频指纹）
- **讲师/机构**: David Domminney Fowler — Computerphile
- **链接**: https://www.youtube.com/watch?v=RRsq9apr5QY
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 14 分钟
- **覆盖**: FFT/频谱图峰值提取、星座图（constellation map）、峰值配对哈希生成指纹、数据库匹配检索
- **对齐 Aurora**: 进阶（音频指纹 / 精确检索）
- **为何契合**: 把 Shazam 指纹算法讲到可复现的程度，是相似度检索之外的另一条「精确检索」思路。

> **MIR 代码级主参考**：Meinard Müller 的 [FMP Notebooks](https://www.audiolabs-erlangen.de/FMP) 与 [ISMIR 2019 FMP 教程](https://www.audiolabs-erlangen.de/resources/MIR/2019_TutorialFMP_ISMIR/)（chroma/onset/beat/结构分析全套 Jupyter）建议作为 L77–L78 的代码级主参考，与上面视频配套。

---

## Phase 9 · LLM / RAG / Agent（L83–L91）

> Transformer → LoRA → KV-Cache → 采样 → 量化 → TF-IDF/RAG → Agent。**首选 Karpathy《Let's build GPT》建全局，Umar Jamil 从零 PyTorch 编码 KV-Cache/LoRA/量化/RAG 逐行落地。**

### 🥇 Let's build GPT: from scratch, in code, spelled out
- **讲师/机构**: Andrej Karpathy
- **链接**: 单视频 https://www.youtube.com/watch?v=kCc8FmEb1nY ｜全课播放列表 https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- **类型**: 单视频（含所属完整课程） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 1h56m
- **覆盖**: 从零逐行手写并训练一个 Transformer（bigram baseline → 自注意力 → 多头 → 位置编码 → 残差/LayerNorm/FFN），最终得到 nanoGPT 核心
- **对齐 Aurora**: L83–L84
- **为何契合**: 全网最经典的「从空文件手写 GPT」，每一步矩阵运算讲透，与 AURORA「不用 wrapper、手写注意力」完全一致。**必收第一顺位。**

### Let's reproduce GPT-2 (124M)
- **讲师/机构**: Andrej Karpathy
- **链接**: https://www.youtube.com/watch?v=l8pRSuU81PU
- **类型**: 单视频 · **难度**: 高级 · **语言**: 英文 · **时长**: 约 4 小时
- **覆盖**: 从空文件复现 GPT-2：搭网络 → 权重加载 → 训练优化（混合精度、梯度累积、学习率调度）→ 采样/评测
- **对齐 Aurora**: L83–L87
- **为何契合**: 把 L83 手写 Transformer 拉通到真实预训练与推理采样，是 L85–L86 KV/采样与 L87 推理的工业级参照。

### Let's build the GPT Tokenizer
- **讲师/机构**: Andrej Karpathy
- **链接**: https://www.youtube.com/watch?v=zduSFxRajkE
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 2h13m
- **覆盖**: 从零实现 BPE（Byte Pair Encoding）分词器：Unicode/字节编码、训练、encode/decode、正则切分
- **对齐 Aurora**: L87（本地推理前的输入处理）
- **为何契合**: 分词是 LLM 独立且易被忽视的一环，纯手写 BPE 完全契合「第一性原理」。

### Deep Dive into LLMs like ChatGPT
- **讲师/机构**: Andrej Karpathy
- **链接**: https://www.youtube.com/watch?v=7xTGNNLPyMI
- **类型**: 单视频 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 3h31m
- **覆盖**: LLM 完整训练栈心智模型：预训练/分词/架构 → SFT → RLHF，含幻觉、工具调用、知识表示
- **对齐 Aurora**: L83–L91（全链路）
- **为何契合**: 少公式、重全局，帮学员在动手手写各模块前后建立端到端认知，串起 L83–L91（含 RAG/Agent 动机）。

### Neural Networks · Chapter 5–7（Transformers / Attention 可视化）
- **讲师/机构**: 3Blue1Brown（Grant Sanderson）
- **链接**: 播放列表 https://www.youtube.com/playlist?list=PLZZWrBYkx7Otcjr3eCLZDCgfpqnxMY29s ｜Ch5 Transformers https://www.youtube.com/watch?v=wjZofJX0v4M ｜Ch6 Attention https://www.youtube.com/watch?v=eMlx5fFNoYc
- **类型**: 播放列表（单集可独立看） · **难度**: 入门 → 进阶 · **语言**: 英文（官方多语字幕，含中文） · **时长**: 每集约 26–27 分钟
- **覆盖**: 词嵌入与 Transformer 数据流（Ch5）、注意力/QKV 逐步可视化（Ch6）、MLP/事实存储章节
- **对齐 Aurora**: L83
- **为何契合**: 全网最清晰的注意力几何直觉可视化，先建直觉再手写 NumPy，L83 自注意力/多头的「看得见」版。

### 🥇 Coding a Transformer from scratch on PyTorch
- **讲师/机构**: Umar Jamil
- **链接**: https://www.youtube.com/watch?v=ISNdQcPhsts ｜频道 https://www.youtube.com/@umarjamilai
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 3 小时
- **覆盖**: 逐层手写完整 encoder-decoder Transformer（输入嵌入、位置编码、多头自注意力、投影层）+ 翻译任务训练 + 注意力可视化
- **对齐 Aurora**: L83–L84
- **为何契合**: 「从零编码」路线标杆，逐行 PyTorch 对照论文，与 AURORA 手写哲学高度契合（其整条 from-scratch 系列见频道）。

### LoRA: Low-Rank Adaptation — 讲解 + PyTorch 从零实现
- **讲师/机构**: Umar Jamil
- **链接**: https://www.youtube.com/watch?v=PXWYUTMt-AU
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 26 分钟
- **覆盖**: LoRA 数学原理（冻结原权重 + 低秩 B·A 增量）+ MNIST 上从零 PyTorch 实现
- **对齐 Aurora**: L84（LoRA 低秩适配）
- **为何契合**: 直接命中 L84，先讲低秩分解直觉再手写，便于用 NumPy 复刻。

### Coding LLaMA 2 from scratch（KV-Cache / RoPE / GQA / RMSNorm）
- **讲师/机构**: Umar Jamil
- **链接**: https://www.youtube.com/watch?v=oM4VmoabDAI
- **类型**: 单视频 · **难度**: 高级 · **语言**: 英文 · **时长**: 约 3 小时
- **覆盖**: 从零手写 LLaMA 2：KV-Cache、旋转位置编码、Grouped-Query Attention、RMSNorm、SwiGLU，并覆盖采样策略（greedy/beam/temperature/top-k/top-p）
- **对齐 Aurora**: L85–L86（KV-Cache + 采样策略）
- **为何契合**: L85 KV-Cache + L86 采样策略的最佳单一来源，逐行实现让 NumPy 版 KV-Cache 有清晰蓝本。

### Quantization explained with PyTorch（PTQ / QAT）
- **讲师/机构**: Umar Jamil
- **链接**: https://www.youtube.com/watch?v=0VdNflU08yA
- **类型**: 单视频 · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 约 1h39m
- **覆盖**: 整数/浮点数值表示、对称/非对称量化、量化范围与粒度、动态/静态量化、PTQ 与 QAT、GPU MAC 硬件加速
- **对齐 Aurora**: L87（INT8 量化从零）
- **为何契合**: L87 的理论+实现底座，把「缩放/零点/取整」讲到硬件层，支撑手写量化内核。

### Retrieval Augmented Generation (RAG) Explained
- **讲师/机构**: Umar Jamil
- **链接**: https://www.youtube.com/watch?v=rhZgXNdhWDY
- **类型**: 单视频 · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 35 分钟
- **覆盖**: RAG 全管线：嵌入、Sentence-BERT、向量数据库与 HNSW 近邻检索、检索拼 prompt 生成
- **对齐 Aurora**: L88–L90
- **为何契合**: 系统讲透 RAG 每一环（chunk→索引→检索→拼 prompt→生成）；学员可将其向量检索替换为 AURORA 的手写 TF-IDF/余弦，理解原理映射。

### Transformers & Attention, Clearly Explained
- **讲师/机构**: StatQuest with Josh Starmer
- **链接**: Transformer https://www.youtube.com/watch?v=zxQyTK8quyY ｜Attention https://www.youtube.com/watch?v=PSs6nxngL6k
- **类型**: 单视频（同频道成系列） · **难度**: 入门 · **语言**: 英文 · **时长**: 约 36 分 / 16 分
- **覆盖**: 词嵌入、位置编码、自注意力、encoder-decoder 与并行计算，及注意力机制单独精讲
- **对齐 Aurora**: L83
- **为何契合**: 极慢极清晰的入门首选，为 L83 手写前打好零基础直觉，配合 Karpathy 形成「直觉→实现」梯度。

### 注意力机制数学原理（Serrano.Academy）
- **讲师/机构**: Luis Serrano（前 Google/Apple、Udacity ML 负责人）
- **链接**: 播放列表 https://www.youtube.com/@SerranoAcademy/playlists ｜数学精讲 https://www.youtube.com/watch?v=g2BRIuln4uc
- **类型**: 播放列表（三部曲） · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 单集约 20–38 分钟
- **覆盖**: 嵌入、相似度、Keys/Queries/Values 矩阵与注意力的数学推导，三部曲递进到 Transformer
- **对齐 Aurora**: L83
- **为何契合**: 用类比+图解把 QKV 的线性代数讲透，衔接 3B1B 直觉与手写实现之间的数学台阶。

### The Narrated Transformer Language Model
- **讲师/机构**: Jay Alammar（"The Illustrated Transformer" 作者，Cohere）
- **链接**: https://www.youtube.com/watch?v=sMPq4cVS4kg
- **类型**: 单视频 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 30 分钟
- **覆盖**: Transformer 语言模型组件的可视化叙述：分词、嵌入、自注意力、前馈网络、输出投影
- **对齐 Aurora**: L83
- **为何契合**: Illustrated Transformer 的视频版讲演，图解直观，是 L83 架构总览的经典补充。

### Attention Is All You Need（论文精读）
- **讲师/机构**: Yannic Kilcher
- **链接**: https://www.youtube.com/watch?v=iDulhoQ2pro
- **类型**: 单视频 · **难度**: 高级 · **语言**: 英文 · **时长**: 约 27 分钟
- **覆盖**: 逐节精读 Vaswani et al. 2017 原论文：纯注意力架构、位置编码、多头注意力、去 RNN/CNN 的动机与实验
- **对齐 Aurora**: L83
- **为何契合**: 回到第一性来源——原始论文，帮学员用原文校准手写实现的每个设计决策。

### 【機器學習2021】自注意力機制 Self-attention & Transformer（中文）
- **讲师/机构**: 李宏毅 Hung-yi Lee（台大 NTU）
- **链接**: Self-attention(上) https://www.youtube.com/watch?v=hYdO9CscNes ｜(下) https://www.youtube.com/watch?v=gmsMY5kc-zw ｜Transformer(上) https://www.youtube.com/watch?v=n9TlOhRjYoc
- **类型**: 单视频（属 ML2021 完整课程） · **难度**: 入门 → 进阶 · **语言**: 中文（国语讲解，含中文字幕） · **时长**: 每集约 28–60 分钟
- **覆盖**: 自注意力动机与 QKV 计算、多头、位置编码，Transformer 的 seq2seq/encoder-decoder 与训练
- **对齐 Aurora**: L83–L84
- **为何契合**: 华语区公认最佳中文 Transformer 讲解，为中文学员提供母语原理入口。

---

## Phase 10 · 系统集成 / MLOps / 面试（L92–L99）

> 从 mic→ASR→LLM 端到端管线，到 W&B/Docker/CI-CD，再到「从 demo 到产品」的证据链与研究工程面试。**首选 Full Stack Deep Learning + Made With ML + W&B 官方。**

### 🥇 Full Stack Deep Learning — 2022 完整课程
- **讲师/机构**: Josh Tobin、Sergey Karayev、Charles Frye（UC Berkeley 背景，FSDL）
- **链接**: https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur （主页 https://fullstackdeeplearning.com/course/2022/ ）
- **类型**: 完整课程（12 讲 + Labs） · **难度**: 进阶 · **语言**: 英文 · **时长**: 15–20 小时
- **覆盖**: DL 产品全栈——训练基础设施与工具、数据管理/版本化、模型部署为 Web 服务、监控、ML 团队与项目管理、「从 demo 到产品」
- **对齐 Aurora**: L92–L94（整门课即 Aurora v1 capstone 方法论蓝本）
- **为何契合**: 全网公认「从模型到产品」的权威课程，直接对应 L94「Aurora v1 demo + 证据链」与云部署 live demo。**必收第一条。**

### Made With ML — MLOps Course
- **讲师/机构**: Goku Mohandas（Made With ML / Anyscale）
- **链接**: https://madewithml.com/courses/mlops/ （代码 https://github.com/GokuMohandas/mlops-course ｜视频 https://www.youtube.com/playlist?list=PLqy_sIcckLC2jrxQhyqWDhL_9Uwxz8UFq ）
- **类型**: 完整课程（网站 + GitHub + YouTube） · **难度**: 进阶 · **语言**: 英文 · **时长**: 自定进度
- **覆盖**: 生产级 ML 设计→数据→模型（训练/追踪/调优/评估/serving）→测试（代码/数据/模型）→复现与版本化→CI/CD→监控
- **对齐 Aurora**: L93–L94
- **为何契合**: GitHub 顶流 MLOps 开源课，把「第一性原理手写系统」落到工程规范（测试、CI/CD、监控），补足 FSDL 之外的可复制代码骨架。

### Weights & Biases — 官方频道与课程
- **讲师/机构**: Weights & Biases 官方
- **链接**: 频道 https://www.youtube.com/channel/UCBp3w4DCEC64FZr4k9ROxig ｜官方课程 https://wandb.ai/site/courses/
- **类型**: 频道 + 完整课程 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 单集 5–30 分钟
- **覆盖**: 实验跟踪、指标/模型日志、数据集版本化、超参 sweeps、模型评估与协作复现
- **对齐 Aurora**: L93（MLOps 实验跟踪）
- **为何契合**: L93 明确点名 W&B；官方一手教程，把 Aurora 训练实验的可追溯/可复现做扎实，直接支撑 L94 证据链。

### Build a Fully Local AI Voice Assistant (STT + LLM + TTS)
- **讲师/机构**: 独立教程（⚠️ 频道名未核实，标题与内容已核实）
- **链接**: https://www.youtube.com/watch?v=2IffgzB8USw （备用检索："fully local AI voice assistant Whisper TTS"）
- **类型**: 单视频 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 30–60 分钟
- **覆盖**: 纯本地、无云 API 的语音助手——Whisper STT + 本地 LLM + TTS，Python orchestrator 串起 mic→ASR→LLM→TTS 循环，含延迟讨论
- **对齐 Aurora**: aurora.realtime（mic→ASR→LLM→TTS 实时管线）、L92
- **为何契合**: 与 L92/aurora.realtime 目标同构的最小可跑实现，天然「不用 wrapper」路线；可作为 <500ms 目标的起点基线去逐层砍延迟。

### freeCodeCamp — Docker Tutorial for Beginners
- **讲师/机构**: freeCodeCamp.org
- **链接**: https://www.youtube.com/watch?v=fqMOX6JJhGo
- **类型**: 单视频（完整课程） · **难度**: 入门 · **语言**: 英文 · **时长**: 约 2 小时
- **覆盖**: 容器 vs 虚机、Dockerfile 与镜像构建、Docker Hub、网络与存储卷、Docker Compose 多容器编排
- **对齐 Aurora**: L93（Docker 容器化）
- **为何契合**: 为 Aurora 把 realtime/serving 组件打包成可复现镜像、进而上云 GPU 铺路。

### MLOps Tutorial #1 — CI/CD for ML Pipelines with GitHub Actions
- **讲师/机构**: DVCorg / Iterative（DVC 团队）
- **链接**: https://www.youtube.com/watch?v=9I8X-3HIErc
- **类型**: 单视频（系列第一集） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 20–40 分钟
- **覆盖**: 用 GitHub Actions 为 ML 管线做持续集成——PR 触发测试、自动跑训练/评估、把 metrics 回贴 PR，合并后触发部署
- **对齐 Aurora**: L93（CI/CD）
- **为何契合**: 聚焦 ML 的 CI/CD 实战（非泛 DevOps），把 Made With ML 的概念落到 GitHub Actions 具体 workflow。

### A Practical Tutorial on Building ML Demos with Gradio
- **讲师/机构**: Abubakar Abid（Gradio 创始人 / Hugging Face）
- **链接**: https://www.youtube.com/watch?v=97KxA1r184o
- **类型**: 单视频 · **难度**: 入门 · **语言**: 英文 · **时长**: 约 1 小时
- **覆盖**: 用纯 Python 快速搭交互式 demo 与 Web 界面，音频/文本输入组件、分享链接、托管到 Spaces
- **对齐 Aurora**: L94（live demo）
- **为何契合**: 一手创始人讲解，是 L94「Aurora v1 live demo URL」最省力路径；原生支持麦克风/音频，可直接包住 aurora.realtime 管线。

### How to Deploy ML Models with FastAPI, Docker & Fly.io
- **讲师/机构**: 独立教程
- **链接**: https://www.youtube.com/watch?v=jzGzw98Eikk
- **类型**: 单视频（端到端） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 30–50 分钟
- **覆盖**: 把模型封装为 FastAPI 推理服务、容器化、部署到 Fly.io 拿到公网 URL 的完整链路
- **对齐 Aurora**: L93–L94、aurora.realtime 服务化
- **为何契合**: 直接产出 L94 需要的「云上 live demo URL」；FastAPI + Docker 是 realtime 后端 serving 的主流栈。

### Enable Model Quantization for ONNX and TensorRT
- **讲师/机构**: Nicolai Nielsen
- **链接**: https://www.youtube.com/watch?v=phmFvMOHt4I ⚠️（标题经搜索核实，未逐帧核对）
- **类型**: 单视频 · **难度**: 高级 · **语言**: 英文 · **时长**: 约 15–30 分钟
- **覆盖**: 训练模型→导出 ONNX→TensorRT 引擎构建与 INT8/FP8 量化标定，GPU 低延迟高吞吐推理
- **对齐 Aurora**: L94（部署优化）、aurora.realtime（<500ms 延迟预算）
- **为何契合**: aurora.realtime 要压到 <500ms，量化 + ONNX/TensorRT 是把 ASR/TTS 模型提速的关键工程手段。

### Machine Learning System Design Interview — Hello Interview
- **讲师/机构**: Hello Interview（FAANG 资深工程师/招聘经理）
- **链接**: 频道 https://www.youtube.com/@hello_interview ｜指南 https://www.hellointerview.com/learn/ml-system-design
- **类型**: 频道 + 配套课程 · **难度**: 进阶 → 高级 · **语言**: 英文 · **时长**: 单集 20–60 分钟
- **覆盖**: ML 系统设计框架、推荐/检索/排序经典题、真人 mock 与反馈、把业务问题翻译成 ML 方案
- **对齐 Aurora**: L95–L99（ML/系统设计面试）
- **为何契合**: L96–L98 面试准备核心；「框架化 + mock + 反馈」正对研究工程师岗的 ML System Design 环节，可拿 Aurora 项目做 design 素材。

### NeetCode — 编程/白板面试频道 + Roadmap
- **讲师/机构**: Navdeep Singh（前 Google/Amazon 工程师）
- **链接**: 频道 https://www.youtube.com/c/neetcode ｜路线图 https://neetcode.io/roadmap
- **类型**: 频道 + 结构化 roadmap · **难度**: 入门 → 高级 · **语言**: 英文 · **时长**: 410+ 视频
- **覆盖**: NeetCode 150 / Blind 75 按模式（双指针、滑窗、树、图、DP…）递进，每题干净的思路 + 编码讲解
- **对齐 Aurora**: L95–L99（白板/coding 面试）
- **为何契合**: 算法/白板面试事实标准，直接支撑 L96–L98 的 coding 环节与刷题复盘。

### 跟李沐学AI — 论文精读系列（研究技能）
- **讲师/机构**: 李沐（Amazon 资深首席科学家，d2l 作者）
- **链接**: 汇总仓库 https://github.com/mli/paper-reading ｜"如何读论文" https://www.bilibili.com/video/BV1H44y1t75x/ （B 站主页「跟李沐学AI」，YouTube 有同名镜像）
- **类型**: 播放列表/系列 · **难度**: 进阶 → 高级 · **语言**: 中文 · **时长**: 数十集
- **覆盖**: 逐段精读 Transformer/BERT/ViT/ResNet/GAN/InstructGPT 等，并示范「如何读论文」方法论
- **对齐 Aurora**: L95–L99（研究技能、复盘）
- **为何契合**: L95「研究技能」中文首选；示范研究工程师如何拆解论文、提炼贡献与证据链，与 AURORA「第一性原理复现」气质一致。

---

## aurora.tts · 语音合成 TTS（延期模块，专项补充）

> TTS 是 AURORA 路线图中的**延期模块**（六个月内不做深度训练），但你明确要求补充 TTS 学习资料。TTS 领域缺乏成体系的高质量视频课，以下以「中文系统课（李宏毅）+ 英文系统课（Valerio）+ 论文精读 + 前端基础 + DSP 衔接」搭配。**声学模型输出的 Mel 谱正是 AURORA 已实现的 DSP 表示，学 TTS 是 aurora.audio 的自然延伸。**

### 🥇 李宏毅 DLHLP 2020 — 語音合成 (1/2)：Tacotron
- **讲师/机构**: 李宏毅 Hung-yi Lee / 台大 (NTU)
- **链接**: https://www.youtube.com/watch?v=DMxKeHW8KdM
- **类型**: 单视频（属 DLHLP 2020） · **难度**: 入门 → 进阶 · **语言**: 中文（繁体投影片，中英术语） · **时长**: 约 50 分钟
- **覆盖**: TTS 总体流水线、深度学习前的做法、端到端思路，Tacotron 的 seq2seq + attention 架构、CBHG、吐出 mel/线性谱、Griffin-Lim
- **对齐 Aurora**: aurora.tts（声学模型）
- **为何契合**: 华语圈最权威的语音深度学习课，从第一性原理讲清「文本→谱」为什么这么设计，是理解声学模型的最佳起点。

### 李宏毅 DLHLP 2020 — 語音合成 (2/2)：More than Tacotron
- **讲师/机构**: 李宏毅 Hung-yi Lee / 台大 (NTU)
- **链接**: https://www.youtube.com/watch?v=Eau1Fr2x86Y
- **类型**: 单视频（续集） · **难度**: 进阶 · **语言**: 中文 · **时长**: 约 50 分钟
- **覆盖**: Tacotron 痛点与改良、Tacotron2 + WaveNet 声码器、非自回归 FastSpeech、可控合成（speaker/prosody）、对齐与 attention 失败模式
- **对齐 Aurora**: aurora.tts（声学模型 + 声码器衔接）
- **为何契合**: 承接上集，把「为什么要非自回归、为什么要独立声码器」讲透，对应路线图里 FastSpeech/HiFi-GAN 方向的动机。

### 🥇 Text-to-Speech & Voice Cloning Course（完整课程）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: 课程首集 https://www.youtube.com/watch?v=_MFrEYPdEn8 ｜频道全部视频 https://www.youtube.com/c/ValerioVelardoTheSoundofAI/videos
- **类型**: 完整课程（分集连载，持续更新） · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 单集约 30–45 分钟
- **覆盖**: concatenative→neural 演进、双阶段流水线（声学模型 + 声码器）、mel 谱作桥梁、WaveNet/WaveGlow/HiFi-GAN 声码器、FastSpeech/Glow-TTS 并行架构、VALL-E/AudioLM/SPEAR-TTS 等 codec 生成、声音克隆
- **对齐 Aurora**: aurora.tts（全流水线）
- **为何契合**: 目前 YouTube 上体系最完整的英文 TTS 课，讲解偏「理解内部机制」而非调 API，可作 aurora.tts 主线英文教材。

### The Neural TTS Revolution（单集精华总览）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/watch?v=4Lbox-d0UcE
- **类型**: 单视频 · **难度**: 入门 → 进阶 · **语言**: 英文 · **时长**: 约 41 分钟
- **覆盖**: 2016 WaveNet/Tacotron 起点、双阶段流水线、mel 谱桥梁、各类声码器、并行架构、codec 生成
- **对齐 Aurora**: aurora.tts（概念地图）
- **为何契合**: 一集把整个神经 TTS 版图串成时间线，适合作 aurora.tts 的「导航图」，看完再深入各论文不会迷路。

### End-to-End Adversarial Text-to-Speech (EATS) — Paper Explained
- **讲师/机构**: Yannic Kilcher
- **链接**: https://www.youtube.com/watch?v=WTB2p4bqtXU
- **类型**: 单视频（论文精读） · **难度**: 高级 · **语言**: 英文 · **时长**: 约 41 分钟
- **覆盖**: 多阶段 TTS 流水线的问题、对抗训练、端到端训练、判别器/生成器结构、对齐问题与 aligner、谱预测损失、DTW
- **对齐 Aurora**: aurora.tts（端到端/对抗）
- **为何契合**: 把「对齐为何是 TTS 核心难点」讲到公式层面，是理解 VITS 等端到端对抗模型的前置精读。

### In-depth Review of VALL-E — Zero-Shot TTS
- **讲师/机构**: ⚠️ 出品频道未核实（视频标题与内容已核实指向 VALL-E 论文精读）
- **链接**: https://www.youtube.com/watch?v=fCtbnhR83UI ｜若失效搜："VALL-E paper explained neural codec language model zero-shot TTS"
- **类型**: 单视频（论文精读） · **难度**: 高级 · **语言**: 英文 · **时长**: 约 20–40 分钟
- **覆盖**: 把 TTS 当条件语言建模、EnCodec 离散音频码替代 mel 谱、自回归 + 非自回归两级解码、3 秒提示做 zero-shot 声音克隆
- **对齐 Aurora**: aurora.tts（zero-shot 声音克隆）
- **为何契合**: 对齐「VALL-E 思路 / zero-shot voice cloning」，讲清 codec-LM 范式与传统 mel 谱路线的分野；建议与论文 arXiv 2301.02111 对照。

### Text Processing for Speech Synthesis（TTS 前端 · G2P/正规化）
- **讲师/机构**: Prof. Simon King / University of Edinburgh (CSTR)，SPCC 2016
- **链接**: https://www.youtube.com/watch?v=6lMs1VcUrYc ｜同系列 HMM 合成 https://www.youtube.com/watch?v=3Ffd75PVjjc
- **类型**: 单视频（讲座系列） · **难度**: 进阶 · **语言**: 英文 · **时长**: 约 1 小时
- **覆盖**: 文本正规化、字素→音素 (G2P)、词典与发音、韵律/停顿标注，TTS 前端如何把文本变成模型输入
- **对齐 Aurora**: aurora.tts（前端 text→phoneme/G2P）
- **为何契合**: 神经 TTS 视频普遍跳过前端，而 aurora.tts 流水线第一环正是「文本→音素/G2P」；Edinburgh 语音合成组是该领域最权威学派。

### Audio Signal Processing for ML（DSP 衔接）
- **讲师/机构**: Valerio Velardo — The Sound of AI
- **链接**: https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0 （完整介绍见 [Phase 5](#phase-5--audio-dsp-音频信号处理l32l53)）
- **类型**: 播放列表 · **难度**: 入门 → 进阶 · **语言**: 英文
- **覆盖**: 从零推导 STFT→mel 谱，正是声学模型输出与声码器输入的公共表示
- **对齐 Aurora**: aurora.tts ↔ aurora.audio 衔接
- **为何契合**: 直接对接「TTS 与 AURORA 已实现的 DSP（Mel 谱/STFT）如何衔接」，是连接两模块的桥梁课。

### WaveNet by Google DeepMind | Two Minute Papers #93
- **讲师/机构**: Károly Zsolnai-Fehér — Two Minute Papers
- **链接**: https://www.youtube.com/watch?v=CqFIVCD1WWo
- **类型**: 单视频（概览） · **难度**: 入门 · **语言**: 英文 · **时长**: 约 4 分钟
- **覆盖**: WaveNet 直接建模原始波形、自回归生成、听感飞跃（概念层）
- **对齐 Aurora**: aurora.tts（声码器概览）
- **为何契合**: 神经声码器起点 WaveNet 的「为什么重要」引子，开课前快速建直觉；深入机制回到李宏毅第 2 集与 Valerio 课程。

> **VITS / HiFi-GAN / FastSpeech2 / Grad-TTS**：未找到出自名师名校、可核实的独立高质量视频（多为博客/文档/代码）。这些主题在李宏毅第 2 集与 Valerio 完整课程中均有覆盖，建议配合原论文精读：VITS `arXiv 2106.06103`、HiFi-GAN `2010.05646`、FastSpeech2 `2006.04558`、Grad-TTS `2105.06337`。

---

## 核实说明

- 本库链接主要通过 **YouTube 搜索结果与官方页面**核实存在并指向所述资源。由于 YouTube 为前端渲染（SPA）页面，抓取工具无法逐条回读播放列表内的视频清单，故：
  1. **优先给最稳定的播放列表 / 频道 / 官方课程 URL**；
  2. 标 **`⚠️`** 的条目为单视频直链未能逐一确认，请以其**频道 + 搜索关键词**为准；
  3. 少数条目为官方免费课程 / 讲义（**非 YouTube**，如 Hugging Face Audio Course、Edinburgh ASR 讲义、FMP Notebooks），已在「类型」中注明，作为高价值补充。
- 视频可能随时间**下架或改名**——若某条失效，用标题 / 频道名在 YouTube 重新搜索即可命中。
- **跨阶段复用**：Karpathy（micrograd/GPT）、Valerio Velardo（音频全线）、3B1B（数学/Transformer）、李宏毅（ML/语音/TTS）在多个阶段出现，本库在其「主场」阶段给完整条目，其它阶段用一句话交叉引用，避免重复。

---

*生成于 2026-07-12 · 对齐 AURORA `notebooks/README.md` 与 `ROADMAP.md` 的 L01–L99 课程结构 · 补充资料，与 `docs/current/video/`（Aurora 自制课程视频脚本）互不重叠。*

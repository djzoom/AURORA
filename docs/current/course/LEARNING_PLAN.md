# Aurora 学习计划（6 个月 · 全职 · 零基础起步）

> 这是一份**个人学习计划**，不是项目宣传文档。它诚实地按"完全不懂 + 全职
> 40h/周 + 有云 GPU 预算"的真实情况重排。配套的可追踪 checklist 见 `ROADMAP.md`，
> 每周的逐日打卡见 `docs/current/course/week-NN-checklist.md`。
> 补充视频片单见 [`VIDEO_LIBRARY.md`](VIDEO_LIBRARY.md)——92 条名师名校 YouTube
> 教程，逐条对齐 L01–L99，卡住时按课号回查。

## 0. 先校准预期（最重要的一节）

- **6 个月不会到 Senior Research Engineer 水平**——那是 3-5 年的积累。我们要造的
  是一条**证据链**，证明研究工程师的底层能力和学习曲线。
- 证据链的质量**不取决于数量指标**。重新校准：

  | 旧目标 | 真相 | 真正要追求的 |
  |---|---|---|
  | 10,000 commits | 灌水指标，一眼看穿 | 每天 2-5 个**有意义**的 commit，自然累积 |
  | 50 篇博客 | 数量没用，深度有用 | 每周 1-2 篇**短而准**的学习日志 |
  | 复现 24 篇论文 | 对新手不现实 | **真正吃透 3-5 篇**（如 Whisper） |
  | 100 个真实用户 | 只有 Month 6 才相关 | 不是核心信号 |

- **面试官真正看的**：能否推导核心数学？算法是**写的**还是 `import` 的？能否训练
  一个模型并解释它为什么 work？能否讲清 tradeoff？
- 一句话原则：**少量、正确、讲得清的深度作品 > 一大堆 API 拼装。**

## 1. 核心认知：仓库里的代码是"标准答案"

Audio Core（`src/aurora/audio/`）已经实现好了。对零基础的你，Month 1 不是"去造它"，
而是：**学数学和 DSP，直到你能把每一行都看懂、能从空白文件重写出来、能在白板上推导。**
代码当"已解出的答案"，你学到能独立复现、然后超越它（加新功能）。

## 2. 依赖链：为什么不能跳

```
数学(线代/复数) ─┐
                 ├─→ DSP ──→ 音频特征 ─┐
numpy 流畅度 ────┘                      ├─→ 音频深度学习 ──→ ASR/Music/TTS
                                        │
微积分/梯度 ──→ ML 基础 ──→ 深度学习 ──┘
```

前两个月是地基。跳过会让后面全部坍塌。

## 3. 6 个月重排（深度优先）

| 月 | 主题 | 交付物 | 通关标志 |
|---|---|---|---|
| **1** | 数学 + DSP 地基 | *Audio Analysis Engine* | 能从空白文件重写 FFT/STFT/mel/MFCC |
| **2** | ML / 深度学习地基 | 从零 autograd + 语音命令分类器 | 能手推反向传播；用自己的 mel 特征训出模型 |
| **3** | Speech Core (ASR) | 微调 Whisper-small + WER 评估 | 能转录真实音频并讲清 CTC/注意力 |
| **4** | Music Core（你的优势区） | 音乐 embedding + 相似推荐 | 歌→向量→推荐跑通 |
| **5** | LLM + RAG + Agent | Podcast 智能引擎 | 本地推理 + LoRA + RAG 跑通 |
| **6** | 整合 + 1 个 Demo + MLOps | Aurora v1 + 面试材料 | 一个打磨好的端到端 demo |

**诚实砍掉**（6 个月内做不到有质量，留到以后）：TTS 声音克隆训练、Realtime <500ms
全链路、24 篇论文复现。贪多 = 全是半成品 = 面试零分。

## 3.5 前导课程（代码优先）

所有前导课在 `notebooks/0_foundation/`–`notebooks/4_probability/`，带 ✏️ 填空与自动判卷，每课连到 Aurora 真实用途。

**⓪ 开场五课**（课程入口，先全部跑通）：

| 课程 | 内容 |
|---|---|
| `0_foundation/L01_motivation`    | Aurora 动机、11 模块路线图、月通关标志、`check_imports`、`environment_report` |
| `0_foundation/L02_sound_digital` | 声音数字表示、`samples_count`/`make_time_axis`/`make_sine`/`signal_summary`，先手算再验证 |
| `0_foundation/L03_spectrogram`   | 谱图直觉（纯音/和弦/扫频/噪声），不推公式，为 FFT 种下视觉印象 |
| `1_complex_trig/L04_trig`        | 正弦三要素 A·sin(2πft+φ)，实现 `sinusoid`，和弦叠加 demo |
| `1_complex_trig/L05_complex_numbers` | 复数模与相位，实现 `magnitude_phase`，FFT 输出复数预览 |

**① 数学地基**（四门，足以支撑 Aurora 全部核心数学）：

| 课程 | 内容 | 主要服务于 |
|---|---|---|
| `1_complex_trig/` L06–L08 | 欧拉公式、傅里叶直觉、可视化 | DSP / FFT |
| `2_linear_algebra/` L09–L21 | 向量、点积、矩阵、SVD | 几乎所有模块 |
| `3_calculus/` L22–L26 | 导数、梯度、链式、梯度下降 | 深度学习训练 |
| `4_probability/` L27–L31 | 随机、分布、softmax、交叉熵 | ML 损失与生成 |

**推荐顺序**：先过开场五课（L01–L05）→ `1_complex_trig` L06–L08 + `2_linear_algebra` L09–L21
→ 做 `5_audio_dsp` L32–L36 → 快进深度学习前再补 `3_calculus` + `4_probability`（L22–L31）。

## 4. Month 1 周计划（当前可执行）

逐日 checklist：`docs/current/course/week-01-checklist.md`（L32–L36）、`docs/current/course/week-02-checklist.md`（L37–L42）、
`docs/current/course/week-03-checklist.md`（L53–L58）、`docs/current/course/week-04-checklist.md`（L67–L71）。
后续阶段 checklist 还会继续按课程推进补齐。
对应课程 notebook 全部已建在 `notebooks/5_audio_dsp/`（L32–L53）。

- **L32–L36 — 信号、复数、numpy**：采样/Nyquist、欧拉公式 `e^{iθ}=cosθ+isinθ`、
  numpy 广播切片。亲眼看到混叠 aliasing。读懂 `io.py`/`windows.py`。
- **L37–L42 — 傅里叶（核心）**：DFT 定义、twiddle 矩阵、FFT 分治 + 位反转。
  **从空白文件重写 `transforms.py`** 让测试全绿。能白板默写 DFT。
- **L43–L48 — STFT/频谱图/Mel**：时频 tradeoff、加窗与频谱泄漏、mel 标度与人耳。
  重写 `stft.py`/`mel.py`，做一个真正的频谱热力图 CLI。
- **L49–L53 — MFCC/DCT + 接入真实音频**：倒谱、DCT-II；下载 LibriSpeech 音频算
  MFCC，用 librosa **当"对答案"工具**验证（只验证、不依赖）；给 Audio Core 加新特征。
  交付 *Audio Analysis Engine*。

## 5. Phase 2–6（课程 notebook 已全部建好，L01–L99）

- **L54–L65** (`notebooks/6_deep_learning/`)：从零 autograd（L54–L58）→ PyTorch 入门（L59–L61）→
  关键词识别分类器（L62–L64，用自己的 mel 特征）→ 训练可视化（L65）。
- **L66–L75** (`notebooks/7_asr/`)：Edit Distance → CTC 对齐 + 前向算法 → Whisper 架构 + 解码策略 → 云 GPU 微调 → WER 评估 → 错误分析 → 可视化。
- **L76–L82** (`notebooks/8_music/`)：音乐理论速成 → chroma/onset/beat 特征（aurora.music 从零实现）→ embedding → 纯 NumPy k-NN 相似搜索 → 推荐引擎 → 可视化。
- **L83–L91** (`notebooks/9_llm/`)：Transformer → LoRA → KV-Cache 从零实现 → 采样策略从零实现 → INT8 量化 → TF-IDF 检索从零实现（无 faiss）→ RAG 流水线 → Agent → 可视化。
- **L92–L99** (`notebooks/10_integration/`)：端到端流水线 → MLOps → Demo 打磨 → 论文精读 → 白板演练 → 面试材料 → 复盘 → 下一步规划。

## 6. 每日节奏（40h/周）

```
上午 (3h)  学理论：看书/课程/推导数学      —— 输入
下午 (3h)  写代码：实现 + 跑测试            —— 输出（每天 ≥1 个 commit）
傍晚 (1-2h) 写学习日志 / 整理博客           —— 内化（讲不清 = 没懂）
```

**铁律**：每天 `git commit`；每周末更新 `ROADMAP.md` 的 checkbox；学不会的逼自己
写成博客（费曼学习法）。

## 7. 资源清单（按出场顺序 · 免费 + 代码优先）

| 阶段 | 资源 | 为什么 |
|---|---|---|
| 数学直觉 | 3Blue1Brown「线性代数本质」+「傅里叶变换」 | 可视化，新手友好 |
| DSP | Allen Downey《Think DSP》/ Steven Smith《DSP Guide》 | 代码驱动，专为工程师 |
| Python/numpy | numpy 官方教程 | 够用即可 |
| ML/DL | Karpathy「Neural Networks: Zero to Hero」+ d2l.ai | 从零手写，契合 no-wrapper |
| 语音 | HuggingFace Audio Course + Jurafsky《SLP》 | ASR 入门最佳 |
| Transformer | Karpathy「Let's build GPT」+「The Annotated Transformer」 | 看懂注意力 |

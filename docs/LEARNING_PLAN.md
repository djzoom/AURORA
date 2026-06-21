# Aurora 学习计划（6 个月 · 全职 · 零基础起步）

> 这是一份**个人学习计划**，不是项目宣传文档。它诚实地按"完全不懂 + 全职
> 40h/周 + 有云 GPU 预算"的真实情况重排。配套的可追踪 checklist 见 `ROADMAP.md`，
> 每周的逐日打卡见 `docs/week-NN-checklist.md`。

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

## 3.5 前导课程：代码优先的线性代数（Month 1 之前）

在啃 Audio Core 之前，先用 numpy 把线代地基打好——见
`notebooks/prep_linear_algebra/`（p1 向量 → p6 SVD），每课都连到 Aurora 真实用途。

> **线代够不够撑起 Aurora 全部核心数学？不够。** 它是最大的支柱，但深度学习还需
> **微积分**（梯度/链式法则）和**概率统计**（损失/分布）；这两块采用 just-in-time
> 策略，进 Month 2 前再补。复数/三角已在 Week 1 Day 4 接触。

## 4. Month 1 周计划（当前可执行）

逐日 checklist 见 `docs/week-01-checklist.md`，后续每周到时再细化。

- **Week 1 — 信号、复数、numpy**：采样/Nyquist、欧拉公式 `e^{iθ}=cosθ+isinθ`、
  numpy 广播切片。亲眼看到混叠 aliasing。读懂 `io.py`/`windows.py`。
- **Week 2 — 傅里叶（核心）**：DFT 定义、twiddle 矩阵、FFT 分治 + 位反转。
  **从空白文件重写 `transforms.py`** 让测试全绿。能白板默写 DFT。
- **Week 3 — STFT/频谱图/Mel**：时频 tradeoff、加窗与频谱泄漏、mel 标度与人耳。
  重写 `stft.py`/`mel.py`，做一个真正的频谱热力图 CLI。
- **Week 4 — MFCC/DCT + 接入真实音频**：倒谱、DCT-II；下载 LibriSpeech 音频算
  MFCC，用 librosa **当"对答案"工具**验证（只验证、不依赖）；给 Audio Core 加新特征。
  交付 *Audio Analysis Engine*。

## 5. Month 2-6 粗粒度（到时再拆周）

- **M2**：跟 Karpathy「Zero to Hero」从零手写 autograd→MLP→反向传播→CNN/RNN→attention。
  用**自己的 mel 特征**训练 Speech Commands 分类器。
- **M3**：CTC 原理 + 云 GPU 微调 Whisper-small on LibriSpeech，WER 评估。
- **M4**：音乐 embedding + 相似推荐；有余力碰 MusicGen 微调。
- **M5**：本地跑 Qwen/Llama、LoRA、FAISS 搭 RAG、Podcast Agent。
- **M6**：挑一个最亮的 demo 打磨上线、Docker 化、接 W&B、整理面试材料。

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

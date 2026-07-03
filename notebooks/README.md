# notebooks/ — 99 节交互式音频 AI 课程

用 Jupyter 一格一格地学：左边读讲解、右边改代码、立刻看输出。

> 🔰 **完全零基础**（没装过 Python / 没用过终端）请先看
> [**新手上路指南**](../docs/current/course/GETTING_STARTED.md)——手把手装环境、跑通第一课。
> 下面是给已经熟悉终端的同学的速查版。

## 启动

```bash
cd AURORA
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,notebooks]"
python -m ipykernel install --user --name aurora --display-name "Python (AURORA)"
jupyter lab
```

打开 Notebook 后在右上角选内核 `Python (AURORA)`。如果内核列表里没有，先完成 L01。

## 用法

按 `Shift+Enter` 逐格运行。看到 **✏️ TODO** = 你要填的代码；填完运行，下面的检查格打 ✅ 或报错。

---

## 课程序列（L01 → L99）

### 🏁 Phase 0 · 基础前导  `0_foundation/`  L01–L03

| 课号 | 课程标题 |
|---|---|
| L01 | Aurora 是什么 — 从正弦波到 Whisper，6 个月路线图与核心动机 |
| L02 | 声音的数字表示 — 采样定理、PCM 数组、第一个可听正弦波 |
| L03 | 谱图直觉 — 在学 FFT 之前先读懂时频图的三个轴 |

---

### 📐 Phase 1 · 复数与三角  `1_complex_trig/`  L04–L08

| 课号 | 课程标题 |
|---|---|
| L04 | 正弦波三要素 — 频率决定音高、振幅决定响度、相位决定起点，亲手实现 |
| L05 | 复数几何本质 — 实部虚部 → 极坐标，复数乘法 = 旋转 + 缩放 |
| L06 | 欧拉公式 e^{iθ}=cosθ+isinθ — 旋转因子是 FFT 的命根子 |
| L07 | 万物皆正弦 — 用三角波叠加合成方波，傅里叶直觉一图彻底建立 |
| L08 🎨 | 复数平面可视化 — 单位圆旋转、共轭与相位，matplotlib 动态演示 |

---

### 🔢 Phase 2 · 线性代数  `2_linear_algebra/`  L09–L21

| 课号 | 课程标题 |
|---|---|
| L09 | 向量代数 — 加法、标量乘法与线性组合，NumPy 实现 + 几何意义 |
| L10 | 点积与投影 — a·b = \|a\|\|b\|cosθ，为什么相似度 = 点积 ÷ 积范数 |
| L11 | 向量范数 — L1 / L2 / ∞ 范数的计算、几何形状与正则化含义 |
| L12 | 矩阵乘法 — 矩阵 = 线性变换，乘法 = 函数复合，手推 2×2 例子 |
| L13 | 特殊矩阵 — 正交矩阵保长度、对称矩阵 = 镜子、正定的判定 |
| L14 | 特征值与 SVD — Ax=λx 的几何意义，SVD 作为万能分解工具 |
| L15 | 高斯消元 — 方程组 Ax=b 的消元过程，行阶梯形与解的存在性分类 |
| L16 | 行列式与逆矩阵 — det(A) 的几何含义（面积缩放），求逆与何时不可逆 |
| L17 | 特征分解 A=PDP⁻¹ — 换坐标系让矩阵乘法变成标量乘法 |
| L18 | 可逆性与秩 — 秩 = 信息量，零空间 = 被压缩的方向，奇异矩阵诊断 |
| L19 🎨 | 矩阵变换图解 — 旋转、缩放、剪切的动态视觉演示 |
| L20 🎨 | 分解图谱 — LU / QR / SVD 三种分解的几何意义对比 |
| L21 🎨 | 矩阵即滤波 — DFT 矩阵 / Mel 矩阵：音频处理 = 矩阵乘法 |

---

### ∂ Phase 3 · 微积分  `3_calculus/`  L22–L26

| 课号 | 课程标题 |
|---|---|
| L22 | 导数 — 切线斜率、极限定义、数值微分 vs 解析微分 |
| L23 | 梯度 — 多元函数的"最陡上坡"方向，偏导与梯度向量的计算 |
| L24 | 链式法则 — 函数套函数的求导，反向传播的数学基础 |
| L25 | 梯度下降 — 用一条直线拟合数据，从损失函数到权重更新公式 |
| L26 🎨 | 微积分可视化 — 切线、等高线与梯度下降轨迹动态演示 |

---

### 🎲 Phase 4 · 概率统计  `4_probability/`  L27–L31

| 课号 | 课程标题 |
|---|---|
| L27 | 概率基础 — 事件、条件概率、独立性与大数定律 |
| L28 | 均值方差标准化 — 描述性统计、z-score 标准化与分布比较 |
| L29 | 常见概率分布 — 均匀、高斯、伯努利：PDF / CDF 与采样 |
| L30 | Softmax 与交叉熵 — 分类模型的输出层与损失函数，手推梯度 |
| L31 🎨 | 概率分布可视化 — PDF、CDF 与交叉熵损失曲面动态演示 |

---

### 🔊 Phase 5 · Audio DSP  `5_audio_dsp/`  L32–L53

| 课号 | 课程标题 |
|---|---|
| L32 | NumPy 信号基础 — `np.arange` / `linspace`，生成 16kHz 一秒时间轴 |
| L33 | 正弦波生成 — `x[n]=A·sin(2πfn/sr)`，亲手实现并对齐 aurora.audio.sine |
| L34 | Nyquist 定理与混叠 — 6kHz 正弦波被 8kHz 采样后会变成什么 |
| L35 | 欧拉公式遇见 FFT — `e^{-2πikn/N}` 是什么，旋转因子可视化 |
| L36 | 窗函数原理 — 矩形窗的旁瓣泄漏，Hann / Hamming / Blackman 对比 |
| L37 | DFT 暴力实现 — `X[k]=Σ x[n]e^{-2πikn/N}`，O(N²) 双循环 + numpy 对齐验证 |
| L38 | FFT 蝶形分治 — 偶奇拆分、蝶形运算 `E[k]+W^k·O[k]`，O(N²)→O(N log N) |
| L39 | 从零手写 FFT — Cooley-Tukey 递归实现，与 numpy.fft 误差 < 1e-10 |
| L40 | 频谱分析实战 — 幅度谱 / 相位谱 / 频率分辨率，440Hz+880Hz 混合信号 |
| L41 | 加窗 FFT 完整流程 — 信号 → 加窗 → FFT → 幅度谱，一条管线跑通 |
| L42 🎨 | FFT 图形化 — 蝴蝶图 + 纯音 / 和弦 / 噪声的频谱形态对比 |
| L43 | STFT 原理 — 短时傅里叶变换：给信号加时间戳，时频分辨率 tradeoff |
| L44 | 亲手写 STFT — 分帧 + 加窗 + FFT，与 aurora.audio.stft 对齐验证 |
| L45 | 声谱图生成 — magnitude_spectrogram，pcolormesh 热力图，读懂时频图 |
| L46 | Mel 频率尺度 — 人耳对数感知，mel = 2595·log₁₀(1+f/700)，三角滤波器 |
| L47 | 亲手写 Mel 滤波器 — mel_filterbank 从公式到 NumPy，与仓库输出对齐 |
| L48 🎨 | 时频图解 — 线性谱 / Mel 谱 / 对数 Mel 谱三者视觉对比 |
| L49 | DCT-II 离散余弦变换 — 去相关原理，纯 NumPy 实现替代 scipy.fft.dct |
| L50 | MFCC 完整流水线 — 信号 → STFT → Mel → log → DCT，每步输出形状确认 |
| L51 | MFCC 工程实战 — 在真实 WAV 音频上提取特征，librosa 对答案 |
| L52 | Audio Core 完结 — 特征工程收口，38 个单元测试全绿，面试证据整理 |
| L53 🎨 | MFCC 图形化 — 波形 → 声谱图 → Mel 谱 → 倒谱系数，逐层图示 |

---

### 🧠 Phase 6 · 深度学习  `6_deep_learning/`  L54–L65

| 课号 | 课程标题 |
|---|---|
| L54 | Value 计算图 — 标量自动微分：前向值 + 反向梯度，手写 add / mul 节点 |
| L55 | Value 算子补全 — `__pow__`、relu、tanh、exp 节点实现，计算图完整展开 |
| L56 | 反向传播手推 — 链式法则逐层展开，梯度 = 局部梯度 × 上游梯度 |
| L57 | MLP 从零搭建 — 手写全连接层、激活函数、前向 / 反向完整实现 |
| L58 | 训练循环 — loss 计算、optimizer.step、收敛曲线，拟合 make_moons 数据集 |
| L59 | PyTorch Tensor 基础 — 与 NumPy 互转、device、requires_grad |
| L60 | autograd 机制 — grad_fn 计算图，backward()，retain_graph 原理 |
| L61 | nn.Module 实战 — Linear / ReLU / Sequential，参数管理与模型保存 |
| L62 | Dataset 与 DataLoader — 自定义 __getitem__，音频数据批量加载 |
| L63 | 音频分类模型 — CNN + Mel 特征，在 Speech Commands 上定义网络 |
| L64 | 训练评估闭环 — train loop + val loop，准确率 / 混淆矩阵 / 过拟合诊断 |
| L65 🎨 | 训练可视化 — Loss / Acc 曲线，梯度范数，权重分布直方图 |

---

### 🎙️ Phase 7 · 语音识别  `7_asr/`  L66–L75

| 课号 | 课程标题 |
|---|---|
| L66 | ASR 系统全览 — 声学模型 → 语言模型 → 解码器，端到端 vs 经典流水线 |
| L67 | Edit Distance 从零实现 — Levenshtein 动态规划，WER 的数学基础 |
| L68 | CTC 对齐原理 — blank 符号、单调路径与标签折叠 |
| L69 | CTC 前向算法 — 所有路径概率求和，O(T×2L) 纯 NumPy 实现 |
| L70 | Whisper 架构解析 — Log-Mel 输入、Transformer Encoder-Decoder、多任务头 |
| L71 | Whisper 解码策略 — 贪婪解码与 beam search 从原理到实现 |
| L72 | Whisper 微调 — LoRA 低秩注入 vs 全参数，中文 / 方言数据适配实战 |
| L73 | WER 评估 — 词错误率（插入 / 删除 / 替换），jiwer 对比逐句分析 |
| L74 | ASR 错误分析 — 替换/删除/插入模式，从 WER 到可改进方向 |
| L75 🎨 | ASR 流水线图形化 — 波形 → 声谱图 → token → 文字路径可视化 |

---

### 🎵 Phase 8 · 音乐理解  `8_music/`  L76–L82

| 课号 | 课程标题 |
|---|---|
| L76 | 音乐理论速成 — 音高、音程、色度轮与十二平均律 |
| L77 | 音乐特征工程 — chroma、RMS 能量、ZCR，调用 aurora.music 从零实现 |
| L78 | 节拍追踪从零实现 — onset 包络、自相关与 BPM 估计 |
| L79 | 音乐嵌入向量 — 对比学习：相似风格靠近，不同流派拉远 |
| L80 | 向量相似度检索 — 余弦相似度 vs 点积 vs L2，纯 NumPy k-NN 实现 |
| L81 | 音乐推荐系统 — 用户喜好 → 嵌入向量 → k-NN 邻居 → 推荐列表 |
| L82 🎨 | 音乐特征可视化 — 色度图、节拍图、相似度热力图动态展示 |

---

### 💬 Phase 9 · LLM + RAG  `9_llm/`  L83–L91

| 课号 | 课程标题 |
|---|---|
| L83 | Transformer 从零复现 — 多头注意力 + 位置编码 + Feed-Forward 完整实现 |
| L84 | LoRA 低秩适配 — W = W₀ + BA，用 0.1% 参数量精调 GPT-style 模型 |
| L85 | KV-Cache 从零实现 — 键值缓存矩阵更新，O(seq²)→O(seq) 加速 |
| L86 | 采样策略从零实现 — temperature / top-k / top-p，纯 NumPy |
| L87 | 量化与本地推理 — INT8 量化原理，连接 HuggingFace 轻量推理 |
| L88 | TF-IDF 检索从零实现 — 词频逆文档频率，纯 NumPy 向量检索 |
| L89 | RAG 完整流水线 — 文档切片 + TF-IDF 检索 + 提示词构建 + 生成 |
| L90 | 对话式 RAG 与工具调用 Agent（ReAct）— 会话记忆、来源归因 + Thought/Action/Observation 循环 |
| L91 🎨 | 注意力图解 — 多头注意力权重热力图，LoRA 低秩结构可视化 |

---

### 🚀 Phase 10 · 整合交付  `10_integration/`  L92–L99

| 课号 | 课程标题 |
|---|---|
| L92 | 端到端流水线 — 麦克风 → ASR → LLM → 文本回答，全链路组装 |
| L93 | MLOps 基础 — W&B 实验追踪、模型版本管理、Docker 打包与部署脚本 |
| L94 | Aurora v1 全景 Demo — 综合展示所有能力，面试材料与证据链整理 |
| L95 | 研究论文入门 — 三遍阅读法、论文结构写作、投稿流程与学术合作 |
| L96 | 白板演练 — DFT / FFT / 注意力机制口述推导，面试现场模拟 |
| L97 | 面试材料整理 — 30 秒 elevator pitch、GitHub 证据链、简历技术点对照 |
| L98 | 复盘 — 6 个月里程碑回顾，方法论总结，成长曲线量化 |
| L99 | 下一步 — 进阶路线规划：研究方向、开源贡献、下一个里程碑 |

---

## 配套文档

- 宏观路线：[`docs/current/course/LEARNING_PLAN.md`](../docs/current/course/LEARNING_PLAN.md)
- 里程碑追踪：[`ROADMAP.md`](../ROADMAP.md)
- 数学前导打卡：[`docs/current/course/prep-checklist.md`](../docs/current/course/prep-checklist.md)
- DSP 阶段打卡：[`docs/current/course/week-01-checklist.md`](../docs/current/course/week-01-checklist.md)（L32–L36）
- 逐课审计：[`docs/current/audit/INDEX.md`](../docs/current/audit/INDEX.md)

## 验收

所有 99 个 notebook 均通过机器验收：

```bash
python scripts/validate_pipeline.py   # JSON + 语法 + audio pipeline 全部 PASSED
```

> 🎨 标记的课程为图形化视觉课，无编码任务，通过参数实验建立直觉。

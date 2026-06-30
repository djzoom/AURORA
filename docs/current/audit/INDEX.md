# Aurora 课程审计报告索引

> 审计日期：2026-06-29 | 审计范围：L01–L99（99课）

## 主报告
- [00_教授总评.md](00_教授总评.md) — 课程整体评价、评级分布、Top 20 优先修复
- [01_逐课问题清单.md](01_逐课问题清单.md) — 全部问题按严重程度分类汇总
- [02_纵向分析.md](02_纵向分析.md) — 难度递进、前驱依赖、模块内聚性分析

## 统计摘要（2026-06-30 重新评级）
| 项目 | 数值 |
|------|------|
| 审查课节 | 99/99 |
| 🔴 Critical 问题（原始） | 119 |
| 🟠 Major 问题（原始） | 300 |
| 🟡 Minor 问题（原始） | 404 |
| A- | 1 课（L96）|
| B+ | 9 课 |
| B  | 47 课 |
| B- | 42 课 |
| C+ 及以下 | 0 课 |

> 重新评级日期：2026-06-30 · 评级方法：逐课读取 notebook，按统一 rubric 评分（NIE桩/真实Aurora连接/数值断言/推导深度）
> 上一版（2026-06-29）：A-×4，B+×3，B×68，B-×24
> 本版变化：升级 13 课，降级 29 课（发现系统性桩问题和幻影路径）


## 逐课报告（per_lesson/）

| 课节 | 标题 | 评级 |
|------|------|------|
| [L01.md](per_lesson/L01.md) | Aurora 是什么——从正弦波（sine wave）到 Whisper，6 个月的路线图 | B- |
| [L02.md](per_lesson/L02.md) | 声音的数字表示——采样、数组、第一个可听正弦波 | B- |
| [L03.md](per_lesson/L03.md) | 谱图（spectrogram）直觉——在学 FFT 之前先看结果 | B+ |
| [L04.md](per_lesson/L04.md) | 正弦波三要素 — 频率决定音高、振幅决定响度、相位决定起点，亲手实现 | B |
| [L05.md](per_lesson/L05.md) | 复数（complex number）几何本质——频谱（spectrum）分析语境版 | B |
| [L06.md](per_lesson/L06.md) | 欧拉公式 e^{iθ}=cosθ+isinθ — 旋转因子（twiddle factor）是 FFT 的命根子 | B- |
| [L07.md](per_lesson/L07.md) | 万物皆正弦 — 用三角波叠加合成方波，傅里叶直觉一图彻底建立 | B |
| [L08.md](per_lesson/L08.md) | 复数平面可视化 — 单位圆旋转、共轭与相位，matplotlib 动态演示 | B |
| [L09.md](per_lesson/L09.md) | 向量（vector）代数 — 加法、标量乘法与线性组合，NumPy 实现 + 几何意义 | B |
| [L10.md](per_lesson/L10.md) | 点积（dot product）与投影（projection） | B |
| [L11.md](per_lesson/L11.md) | 向量（vector）范数 — L1 / L2 / ∞ 范数的计算、几何形状与正则化含义 | B |
| [L12.md](per_lesson/L12.md) | 矩阵乘法 — 矩阵 = 线性变换，乘法 = 函数复合，手推 2×2 例子 | B |
| [L13.md](per_lesson/L13.md) | 特殊矩阵 — 正交矩阵保长度、对称矩阵 = 镜子、正定的判定 | B+ |
| [L14.md](per_lesson/L14.md) | 特征值（eigenvalue）与 SVD — Ax=λx 的几何意义，SVD 作为万能分解工具 | B |
| [L15.md](per_lesson/L15.md) | 高斯消元（Gaussian elimination） — 方程组 Ax=b 的消元过程，行阶梯形（REF）与解 | B |
| [L16.md](per_lesson/L16.md) | 行列式（determinant）与逆矩阵（inverse matrix）— det(A) 的几何含义（面积缩放 | B+ |
| [L17.md](per_lesson/L17.md) | 特征分解（eigendecomposition） A=PDP⁻¹ — 换坐标系让矩阵乘法变成标量乘法 | B- |
| [L18.md](per_lesson/L18.md) | 可逆性与秩（rank）— 秩 = 信息量，零空间（null space）= 被压缩的方向，奇异矩阵诊断 | B- |
| [L19.md](per_lesson/L19.md) | 矩阵变换图解 — 旋转、缩放、剪切的动态视觉演示 | B |
| [L20.md](per_lesson/L20.md) | 分解图谱 — LU / QR / SVD 三种分解的几何意义对比 | B |
| [L21.md](per_lesson/L21.md) | 矩阵即滤波 — DFT 矩阵 / Mel 矩阵：音频处理 = 矩阵乘法 | B- |
| [L22.md](per_lesson/L22.md) | 导数（derivative）— 切线斜率、极限定义、数值微分 vs 解析微分 | B- |
| [L23.md](per_lesson/L23.md) | 梯度（gradient） — 多元函数的"最陡上坡"方向，偏导与梯度向量的计算 | B- |
| [L24.md](per_lesson/L24.md) | 链式法则（chain rule） — 函数套函数的求导，反向传播（backpropagation，BP）的数学 | B- |
| [L25.md](per_lesson/L25.md) | 梯度下降 — 用一条直线拟合数据，从损失函数到权重更新公式 | B- |
| [L26.md](per_lesson/L26.md) | 微积分可视化 — 切线、等高线与梯度下降轨迹动态演示 | B |
| [L27.md](per_lesson/L27.md) | 概率基础 — 事件、条件概率、独立性与大数定律 | B |
| [L28.md](per_lesson/L28.md) | 均值方差标准化 — 描述性统计、z-score 标准化与分布比较 | B- |
| [L29.md](per_lesson/L29.md) | 常见概率分布（Probability Distribution） — 均匀（Uniform）、正态（Gauss | B |
| [L30.md](per_lesson/L30.md) | Softmax 与交叉熵（Cross Entropy，CE）— 分类模型的输出层与损失函数（Loss Func | B |
| [L31.md](per_lesson/L31.md) | 概率分布可视化 — PDF、CDF 与交叉熵损失曲面动态演示 | B |
| [L32.md](per_lesson/L32.md) | NumPy 信号基础 — `np.arange` / `linspace`，生成 16kHz 一秒时间轴 | B |
| [L33.md](per_lesson/L33.md) | 正弦波生成 — `x[n]=A·sin(2πfn/sr)`，亲手实现并对齐 aurora.audio.sine | B |
| [L34.md](per_lesson/L34.md) | Nyquist 定理与混叠（aliasing） — 6kHz 正弦波被 8kHz 采样后会变成什么 | B |
| [L35.md](per_lesson/L35.md) | 欧拉公式（Euler's formula）遇见 FFT — `e^{-2πikn/N}` 是什么，旋转因子可视 | B |
| [L36.md](per_lesson/L36.md) | 窗函数（window function）原理 — 矩形窗的旁瓣（sidelobe）泄漏，Hann / Hamm | B- |
| [L37.md](per_lesson/L37.md) | DFT 暴力实现 — `X[k]=Σ x[n]e^{-2πikn/N}`，O(N²) 双循环 + numpy  | B |
| [L38.md](per_lesson/L38.md) | FFT 蝶形分治 — 偶奇拆分、蝶形运算 `E[k]+W^k·O[k]`，O(N²)→O(N log N) | B+ |
| [L39.md](per_lesson/L39.md) | 从零手写 FFT — Cooley-Tukey 递归实现，与 numpy.fft 误差 < 1e-10 | B- |
| [L40.md](per_lesson/L40.md) | 频谱分析实战 — 幅度谱 / 相位谱 / 频率分辨率，440Hz+880Hz 混合信号 | B- |
| [L41.md](per_lesson/L41.md) | 加窗 FFT 完整流程 — 信号 → 加窗 → FFT → 幅度谱，一条管线跑通 | B |
| [L42.md](per_lesson/L42.md) | FFT 图形化 — 蝴蝶图 + 纯音 / 和弦 / 噪声的频谱形态对比 | B |
| [L43.md](per_lesson/L43.md) | STFT 原理 — 短时傅里叶变换：给信号加时间戳，时频分辨率 tradeoff | B- |
| [L44.md](per_lesson/L44.md) | 亲手写 STFT — 分帧（framing）+ 加窗（windowing）+ FFT，与 aurora.aud | B- |
| [L45.md](per_lesson/L45.md) | 声谱图（spectrogram）生成 — magnitude_spectrogram，pcolormesh 热 | B |
| [L46.md](per_lesson/L46.md) | Mel 频率尺度 — 人耳对数感知，mel = 2595·log₁₀(1+f/700)，三角滤波器 | B- |
| [L47.md](per_lesson/L47.md) | 亲手写 Mel 滤波器 — mel_filterbank 从公式到 NumPy，与仓库输出对齐 | B- |
| [L48.md](per_lesson/L48.md) | 时频图解 — 线性谱 / Mel 谱 / 对数 Mel 谱三者视觉对比 | B- |
| [L49.md](per_lesson/L49.md) | DCT-II 离散余弦变换 — 去相关原理，纯 NumPy 实现替代 scipy.fft.dct | B- |
| [L50.md](per_lesson/L50.md) | MFCC 完整流水线 — 信号 → STFT → Mel → log → DCT，每步输出形状确认 | B- |
| [L51.md](per_lesson/L51.md) | MFCC 工程实战 — 在真实 WAV 音频上提取特征，librosa 对答案 | B |
| [L52.md](per_lesson/L52.md) | Audio Core 完结 — 特征工程收口，38 个单元测试全绿，面试证据整理 | B |
| [L53.md](per_lesson/L53.md) | MFCC 图形化 — 波形 → 声谱图 → Mel 谱 → 倒谱系数，逐层图示 | B |
| [L54.md](per_lesson/L54.md) | Value 计算图 — 标量自动微分：前向值 + 反向梯度，手写 add / mul 节点 | B |
| [L55.md](per_lesson/L55.md) | 前向传播（forward pass）拆解 — 算子（operator）节点：`__pow__`、`relu`、 | B- |
| [L56.md](per_lesson/L56.md) | 反向传播（backpropagation）手推 — 链式法则（chain rule）逐层展开，梯度（gradi | B- |
| [L57.md](per_lesson/L57.md) | MLP 从零搭建 — 手写全连接层、激活函数、前向 / 反向完整实现 | B- |
| [L58.md](per_lesson/L58.md) | 训练循环（training loop） — loss 计算、optimizer.step、收敛曲线，拟合 ma | B- |
| [L59.md](per_lesson/L59.md) | PyTorch Tensor 基础 — 与 NumPy 互转、device、requires_grad | B- |
| [L60.md](per_lesson/L60.md) | autograd 机制 — grad_fn 计算图，backward()，retain_grad 与梯度累积 | B- |
| [L61.md](per_lesson/L61.md) | nn.Module 实战 — Linear / ReLU / Sequential，参数管理与模型保存 | B- |
| [L62.md](per_lesson/L62.md) | Dataset 与 DataLoader — 自定义 __getitem__，音频数据批量加载 | B |
| [L63.md](per_lesson/L63.md) | 音频分类模型 — CNN + Mel 特征，在 Speech Commands 上定义网络 | B |
| [L64.md](per_lesson/L64.md) | 训练评估闭环 — train loop + val loop，准确率 / 混淆矩阵 / 过拟合诊断 | B |
| [L65.md](per_lesson/L65.md) | 训练可视化 — Loss / Acc 曲线，梯度范数，权重分布直方图 | B |
| [L66.md](per_lesson/L66.md) | ASR 系统全览 — 声学模型 → 语言模型 → 解码器，端到端 vs 经典流水线 | B |
| [L67.md](per_lesson/L67.md) | Edit Distance 从零实现 — Levenshtein 动态规划，WER 的数学基础 | B+ |
| [L68.md](per_lesson/L68.md) | CTC 对齐原理 — blank 符号、单调路径与标签折叠 | B |
| [L69.md](per_lesson/L69.md) | CTC 前向算法 — 所有路径概率求和，O(T×2L) 纯 NumPy 实现 | B- |
| [L70.md](per_lesson/L70.md) | Whisper 架构解析 — Log-Mel 输入、Transformer Encoder-Decoder、多 | B+ |
| [L71.md](per_lesson/L71.md) | Whisper 解码策略 — 贪婪解码与 Beam Search 从原理到实现 | B |
| [L72.md](per_lesson/L72.md) | Whisper 微调（fine-tuning） — LoRA 低秩注入 vs 全参数，中文 / 方言数据适配实 | B- |
| [L73.md](per_lesson/L73.md) | WER 评估 — 词错误率（插入 / 删除 / 替换），jiwer 对比逐句分析 | B |
| [L74.md](per_lesson/L74.md) | ASR 错误分析 — 替换/删除/插入模式，从 WER 到可改进方向 | B |
| [L75.md](per_lesson/L75.md) | ASR 流水线图形化 — 波形 → 声谱图 → token → 文字路径可视化 | B- |
| [L76.md](per_lesson/L76.md) | 音乐理论速成 — 音高、音程、色度（chroma）轮与十二平均律 | B |
| [L77.md](per_lesson/L77.md) | 音乐特征工程 — chroma、RMS 能量、ZCR，调用 aurora.music 从零实现 | B |
| [L78.md](per_lesson/L78.md) | 节拍追踪从零实现 — onset 包络、自相关与 BPM 估计 | B |
| [L79.md](per_lesson/L79.md) | 音乐嵌入向量（embedding）— 对比学习（contrastive learning）：相似风格靠近，不同 | B+ |
| [L80.md](per_lesson/L80.md) | 向量相似度检索 — 余弦相似度 vs 点积 vs L2，纯 NumPy k-NN 实现 | B |
| [L81.md](per_lesson/L81.md) | 音乐推荐系统 — 用户喜好 → 嵌入向量 → k-NN 邻居 → 推荐列表 | B- |
| [L82.md](per_lesson/L82.md) | 音乐特征可视化 — 色度（chroma）图、节拍图、相似度热力图动态展示 | B- |
| [L83.md](per_lesson/L83.md) | Transformer 从零复现 — 多头注意力 + 位置编码 + Feed-Forward 完整实现 | B- |
| [L84.md](per_lesson/L84.md) | LoRA 低秩适配 — W = W₀ + BA，用 0.1% 参数量精调 GPT-style 模型 | B |
| [L85.md](per_lesson/L85.md) | KV-Cache 从零实现 — 键值缓存矩阵更新，O(seq²)→O(seq) 加速 | B+ |
| [L86.md](per_lesson/L86.md) | 采样策略从零实现 — temperature / top-k / top-p，纯 NumPy | B+ |
| [L87.md](per_lesson/L87.md) | 量化与本地推理 — INT8 量化原理，连接 HuggingFace 轻量推理 | B- |
| [L88.md](per_lesson/L88.md) | TF-IDF 检索从零实现 — 词频逆文档频率，纯 NumPy 向量检索 | B |
| [L89.md](per_lesson/L89.md) | RAG 完整流水线 — 文档切片（Document Chunking）+ TF-IDF 检索 + 提示词（Pr | B |
| [L90.md](per_lesson/L90.md) | 对话式 RAG — 会话记忆（Conversation Memory）、来源归因与 Podcast Q&A 流 | B- |
| [L91.md](per_lesson/L91.md) | 注意力图解 — 多头注意力权重热力图，LoRA 低秩结构可视化 | B- |
| [L92.md](per_lesson/L92.md) | 端到端流水线（pipeline） — 麦克风 → ASR → LLM → 文本回答，全链路组装 | B- |
| [L93.md](per_lesson/L93.md) | MLOps 基础 — W&B 实验追踪、模型版本管理、Docker 打包与部署脚本 | B- |
| [L94.md](per_lesson/L94.md) | Aurora v1 全景 Demo — 综合展示所有能力，面试材料与证据链整理 | B |
| [L95.md](per_lesson/L95.md) | 研究论文入门——阅读、写作、投稿与学术合作 | B- |
| [L96.md](per_lesson/L96.md) | 白板推导演练——FFT / CTC / 注意力机制（attention mechanism） | A- |
| [L97.md](per_lesson/L97.md) | 面试准备与技术沟通——如何讲清你做的每一件事 | B |
| [L98.md](per_lesson/L98.md) | 课程总结——做到了什么，还差什么 | B- |
| [L99.md](per_lesson/L99.md) | Aurora v2 与持续成长——6 个月之后怎么走 | B- |

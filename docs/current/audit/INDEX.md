# Aurora 课程审计报告索引

> 审计日期：2026-06-29 | 审计范围：L01–L99（99课）| 最后更新：2026-07-03（标题已更新为 Fable 5 重写版）

## 主报告
- [00_教授总评.md](00_教授总评.md) — 课程整体评价、评级分布、Top 20 优先修复
- [01_逐课问题清单.md](01_逐课问题清单.md) — 全部问题按严重程度分类汇总
- [02_纵向分析.md](02_纵向分析.md) — 难度递进、前驱依赖、模块内聚性分析

## 统计摘要（2026-07-01 第四轮科普升级后）
| 项目 | 数值 |
|------|------|
| 审查课节 | 99/99 |
| 🔴 Critical 问题（原始） | 119 |
| 🟠 Major 问题（原始） | 300 |
| 🟡 Minor 问题（原始） | 404 |
| A- | 79 课（全部内容课：科普引入+任务表+白板+自评）|
| B+ | 13 课（可视化课 🎨：NIE 桩+独立数学断言）|
| B  | 7 课（元认知/整合课，无代码练习，属设计如此）|
| B- | 0 课 |
| C+ 及以下 | 0 课 |

> 最新更新：2026-07-03（第六轮 Fable 5 独立复审 + 全课标题重写）
> 第六轮（2026-07-03，**Fable 5**）：独立第二模型两态静态复审 L01–L99，捕获 Opus 轮遗漏的
>   critical（L37 顺逆时针、L05 np.angle 描述、L34 markdown 藏 Python、多处 dead guard 导致
>   学生态崩溃、L94 证据链路径等）；并把全部 99 课标题重写为「感召力」科普风（保留 `第N课 ·` 前缀）。
>   随后 bridge 衔接语对齐新标题（只修真正描述错邻课的桥接）。
> 第五轮（2026-07-02，**Opus 4.8**）：P1–P4 两态执行验证 + 修复（KWS/ASR/音乐/LLM/整合收尾 +
>   36 门地基课两态验证）；补齐大量缺失 solutions；修复 execution_count 崩溃、np.trapz→trapezoid、
>   guard 方向、帧数硬编码等「上轮润色后仍存在」的 bug。全程 validate_pipeline + 82 pytest 全绿。
> 第四轮（2026-07-01）：科普升级，L01–L91 全部达到 A-/B+ 目标等级
> 第三轮（2026-06-30）：内容对齐、Aurora 连接、断言补充
> 第二轮（2026-06-30）：24 门 B- → B（NIE 桩修复 + 幻影路径修复）
> 第一轮（2026-06-30）：全课重新评级，统一 rubric（NIE/真实 Aurora 连接/数值断言/推导深度）


## 逐课报告（per_lesson/）

| 课节 | 标题 | 评级 |
|------|------|------|
| [L01.md](per_lesson/L01.md) | 拒绝黑盒——从一条正弦波（sine wave）亲手造出 Whisper 的 6 个月远征 | B+ |
| [L02.md](per_lesson/L02.md) | 把空气的颤抖装进数组——采样（sampling）与你的第一声可听正弦波（sine wave） | A- |
| [L03.md](per_lesson/L03.md) | 练出一双「看见」声音的眼睛——谱图（spectrogram）直觉，先读图后学 FFT | A- |
| [L04.md](per_lesson/L04.md) | 三个旋钮驯服一切声音——正弦波（sine wave）的频率、振幅（amplitude）与相位（phase，φ） | A- |
| [L05.md](per_lesson/L05.md) | 给每个频率发一张身份证——复数（complex number）的模与相位（phase），FFT 的母语 | A- |
| [L06.md](per_lesson/L06.md) | 最美公式为你转动——欧拉公式（Euler's formula）e^{iθ}=cosθ+isinθ 与 FFT 的旋转因子（twiddle factor） | A- |
| [L07.md](per_lesson/L07.md) | 万物皆正弦——亲手用正弦波叠出方波（square wave），推开傅里叶（Fourier）的大门 | A- |
| [L08.md](per_lesson/L08.md) | 🎨 让旋转看得见——复数平面（complex plane）上的单位圆（unit circle）、共轭（conjugate）与相位（phase） | B+ |
| [L09.md](per_lesson/L09.md) | 每一帧声音都是一支箭——向量（vector）加法、缩放与线性组合（linear combination） | A- |
| [L10.md](per_lesson/L10.md) | 一个数字量出“有多像”——点积（dot product）、余弦相似度与投影（projection） | A- |
| [L11.md](per_lesson/L11.md) | 三把尺子量一个向量——L1 / L2 / ∞ 范数（norm）与归一化的几何 | A- |
| [L12.md](per_lesson/L12.md) | 矩阵不是数字表格，是变换机器——矩阵乘法与线性变换（linear transformation） | A- |
| [L13.md](per_lesson/L13.md) | 三位“特殊能力”矩阵——正交（orthogonal）保长度、对称如镜、正定（PD）的能量判据 | A- |
| [L14.md](per_lesson/L14.md) | 找到矩阵偏爱的方向——特征值（eigenvalue）与 SVD，打开低秩世界的钥匙 | A- |
| [L15.md](per_lesson/L15.md) | 从结果倒推原因——高斯消元（Gaussian elimination）与 Ax=b 的三种命运 | A- |
| [L16.md](per_lesson/L16.md) | 这个变换能撤销吗？——行列式（determinant）判生死，逆矩阵（inverse matrix）来还原 | A- |
| [L17.md](per_lesson/L17.md) | 找到矩阵的"天然坐标系"——特征分解（eigendecomposition）A=PDP⁻¹，让矩阵乘法退化成数乘 | A- |
| [L18.md](per_lesson/L18.md) | 信息丢了还能还原吗？——可逆性与秩（rank）、零空间（null space）与奇异矩阵诊断 | A- |
| [L19.md](per_lesson/L19.md) | 🎨 亲眼看见矩阵搬动整个空间——旋转、缩放、剪切与「列的线性组合」图解 | B+ |
| [L20.md](per_lesson/L20.md) | 🎨 把复杂变换拆成几步简单动作——LU / QR / SVD 分解的几何图谱 | B+ |
| [L21.md](per_lesson/L21.md) | 🎨 你的耳机每秒都在做矩阵乘法——DFT 矩阵与 Mel 矩阵，音频即线代 | A- |
| [L22.md](per_lesson/L22.md) | 教计算机"感受变化"——导数（derivative）、切线斜率与数值微分的中心差分 | A- |
| [L23.md](per_lesson/L23.md) | 闭着眼也能找到最陡的上坡——梯度（gradient）与偏导（∂f/∂x）拼成的方向向量 | A- |
| [L24.md](per_lesson/L24.md) | 一条乘法链撑起整个深度学习——链式法则（chain rule），反向传播的种子 | A- |
| [L25.md](per_lesson/L25.md) | 蒙眼下山，沿负梯度走到谷底——梯度下降（gradient descent，GD）与权重更新公式 | A- |
| [L26.md](per_lesson/L26.md) | 🎨 亲眼看见「下山」— 切线（tangent line）、等高线（contour line）与梯度下降（gradient descent）轨迹 | B+ |
| [L27.md](per_lesson/L27.md) | 掷一万次，随机现出规律 — 条件概率（conditional probability）、独立性与大数定律（LLN） | A- |
| [L28.md](per_lesson/L28.md) | 让苹果和橘子可比 — 均值（mean）、方差（variance）与 z-score 标准化 | A- |
| [L29.md](per_lesson/L29.md) | 随机的三张面孔 — 均匀（uniform）、正态（Gaussian）、伯努利（Bernoulli）与 PDF / CDF | A- |
| [L30.md](per_lesson/L30.md) | 把分数变成信念 — Softmax 与交叉熵（cross entropy），手推梯度 p − y | A- |
| [L31.md](per_lesson/L31.md) | 🎨 随机留下的形状 — PDF、CDF 与交叉熵（cross entropy）损失全可视化 | B+ |
| [L32.md](per_lesson/L32.md) | 给声音标上时刻 — 用 np.arange 造出 16kHz 时间轴（time axis） | A- |
| [L33.md](per_lesson/L33.md) | 造出声音的原子 — 亲手实现正弦波（sine wave）x[n]=A·sin(2πfn/sr) | A- |
| [L34.md](per_lesson/L34.md) | 高频的伪装术 — Nyquist 定理与混叠（aliasing）：6kHz 如何冒充 2kHz | A- |
| [L35.md](per_lesson/L35.md) | 单位圆上的秒针——用欧拉公式（Euler's formula）亲手铸出 FFT 的旋转因子（twiddle factor） | A- |
| [L36.md](per_lesson/L36.md) | 先学会温柔，再学会分析——窗函数（window function）驯服频谱泄漏，Hann / Hamming / Blackman 对决 | A- |
| [L37.md](per_lesson/L37.md) | 一个频率一个频率地审问信号——O(N²) 双循环暴力 DFT，亲手算出你的第一张频谱 | A- |
| [L38.md](per_lesson/L38.md) | 把 N² 折成 N log N——蝶形（butterfly）分治，FFT 快 200 倍的全部秘密 | A- |
| [L39.md](per_lesson/L39.md) | 重写 1965 年改变世界的算法——从零递归实现 FFT（Cooley-Tukey），误差 < 1e-10 | A- |
| [L40.md](per_lesson/L40.md) | 打印声音的成分表——幅度谱 / 相位谱（magnitude / phase spectrum）与频率分辨率实战 | A- |
| [L41.md](per_lesson/L41.md) | 温柔地打开，清晰地看见——加窗（windowing）FFT 一条管线跑通，旁瓣应声而降 | A- |
| [L42.md](per_lesson/L42.md) | 🎨 看见 FFT 的心跳——蝴蝶图（butterfly）与纯音 / 和弦 / 噪声的频谱指纹 | B+ |
| [L43.md](per_lesson/L43.md) | 给声音装上时间轴——STFT（短时傅里叶变换）与时频分辨率的永恒取舍（tradeoff） | A- |
| [L44.md](per_lesson/L44.md) | 给声音装上时间轴——亲手写 STFT（分帧 + 加窗 + FFT），与 aurora 逐点对齐 | A- |
| [L45.md](per_lesson/L45.md) | 给声音拍一张 X 光片——声谱图（spectrogram）：从 |STFT|² 到 dB 热力图 | A- |
| [L46.md](per_lesson/L46.md) | 人耳是台对数机器——Mel 频率尺度与三角滤波器组（mel filterbank） | A- |
| [L47.md](per_lesson/L47.md) | 搭出 Whisper 的耳朵——log-Mel 流水线：STFT → 功率谱 → Mel → log 一气呵成 | A- |
| [L48.md](per_lesson/L48.md) | 🎨 一眼看穿时频世界——线性谱 / Mel 谱 / log-Mel 谱三图对照 | B+ |
| [L49.md](per_lesson/L49.md) | 把 40 个相关数字拧成 13 个独立系数——DCT-II（离散余弦变换）纯 NumPy 手写 | A- |
| [L50.md](per_lesson/L50.md) | 用 13 个数字听懂一帧声音——MFCC 完整流水线（STFT → Mel → log → DCT） | A- |
| [L51.md](per_lesson/L51.md) | 让特征遇见真实世界——WAV 语音上的 MFCC 工程实战（可选 librosa 对答案） | A- |
| [L52.md](per_lesson/L52.md) | 「给我看证据」——Audio Core 收官：测试全绿，从零 FFT→MFCC 的面试底气 | A- |
| [L53.md](per_lesson/L53.md) | 🎨 看见 MFCC 的诞生——波形 → 声谱图（spectrogram） → Mel 谱 → 倒谱系数逐层图解 | B+ |
| [L54.md](per_lesson/L54.md) | 亲手点燃自动微分（autograd）——用一个 Value 类造出计算图（computation graph）的心脏 | A- |
| [L55.md](per_lesson/L55.md) | 给计算图装上关节——`__pow__` / `relu` / `tanh`，前向传播（forward pass）算子集齐 | A- |
| [L56.md](per_lesson/L56.md) | 让梯度逆流而上——手推反向传播（backpropagation）：拓扑排序 × 链式法则（chain rule） | A- |
| [L57.md](per_lesson/L57.md) | 从一个神经元到一张网——MLP 从零搭建，41 个参数全由你亲手点亮 | A- |
| [L58.md](per_lesson/L58.md) | 见证机器学会的那一刻——训练循环（training loop）五步闭环，拟合双月牙 | A- |
| [L59.md](per_lesson/L59.md) | 拿到 GPU 世界的船票——PyTorch 张量（Tensor）、NumPy 互转与 requires_grad | A- |
| [L60.md](per_lesson/L60.md) | 与 PyTorch 对答案——autograd 的 grad_fn 计算图 vs 你手写的 Value 引擎 | A- |
| [L61.md](per_lesson/L61.md) | 给百万参数上户口——nn.Module 参数注册、Sequential 与模型保存 | A- |
| [L62.md](per_lesson/L62.md) | 教会 PyTorch「吃」声音——Dataset / DataLoader 把一秒语音喂成批量 Mel 特征 | A- |
| [L63.md](per_lesson/L63.md) | 用「看图」的方式听懂关键词——CNN 遇见 Mel 频谱，从零定义 KeywordCNN | A- |
| [L64.md](per_lesson/L64.md) | 亲手把 loss 压下去——训练评估闭环、混淆矩阵（confusion matrix）与过拟合诊断 | A- |
| [L65.md](per_lesson/L65.md) | 🎨 给训练过程拍 X 光——Loss 曲线、梯度范数（gradient norm）与权重直方图 | B+ |
| [L66.md](per_lesson/L66.md) | 从声波到文字的完整链路——ASR 系统全览：端到端（end-to-end） vs 经典流水线 | A- |
| [L67.md](per_lesson/L67.md) | 量化「听错了多少」——从零实现编辑距离（edit distance），WER 的数学地基 | A- |
| [L68.md](per_lesson/L68.md) | 100 帧如何吐出 5 个字——CTC 对齐：blank 符号与标签折叠（label collapse） | A- |
| [L69.md](per_lesson/L69.md) | 把指数级路径装进一张表——CTC 前向算法（forward algorithm），纯 NumPy 实现 | A- |
| [L70.md](per_lesson/L70.md) | 拆开能听懂 99 种语言的机器——Whisper 架构：log-Mel → Encoder-Decoder → 多任务头 | A- |
| [L71.md](per_lesson/L71.md) | 下一个词怎么选？——贪婪解码与集束搜索（beam search），让 Whisper 开口说话 | A- |
| [L72.md](per_lesson/L72.md) | 只动 0.5% 的参数，教会 Whisper 你的方言——LoRA 微调（fine-tuning）实战 | A- |
| [L73.md](per_lesson/L73.md) | 同样 15% 错误率，病因大不同——WER（词错误率）的 S/D/I 逐句诊断 | A- |
| [L74.md](per_lesson/L74.md) | 让每个错词供出线索——ASR 错误分析（error analysis），从 WER 数字到修复路线 | B+ |
| [L75.md](per_lesson/L75.md) | 🎨 看见语音变成文字的那条路——波形 → 声谱图 → token 对齐全程可视化 | B+ |
| [L76.md](per_lesson/L76.md) | 88 个琴键，其实只有 12 个音——音高、音程与色度轮（chroma wheel）里的十二平均律 | A- |
| [L77.md](per_lesson/L77.md) | 听出一首歌的"调性指纹"——从零实现 chroma、RMS 能量与过零率（ZCR） | A- |
| [L78.md](per_lesson/L78.md) | 教 AI 跟着音乐点头——onset 包络与自相关（autocorrelation），从零估出 BPM | A- |
| [L79.md](per_lesson/L79.md) | 让相似的歌在向量空间相遇——对比学习（contrastive learning）与音乐嵌入（embedding） | A- |
| [L80.md](per_lesson/L80.md) | 一亿首歌里找"知音"——余弦相似度（cosine similarity）与纯 NumPy k-NN 检索 | A- |
| [L81.md](per_lesson/L81.md) | 推荐系统竟是一道算术题——嵌入向量（embedding）均值 + k-NN，亲手写出懂你的歌单 | A- |
| [L82.md](per_lesson/L82.md) | 🎨 让音乐现出原形——色度（chroma）热力图、节拍网格与相似度矩阵 | B+ |
| [L83.md](per_lesson/L83.md) | 一个公式撑起大模型时代——从零复现 Transformer 与多头注意力（Multi-Head Attention） | A- |
| [L84.md](per_lesson/L84.md) | 给大模型贴便利贴——LoRA 低秩适配（Low-Rank Adaptation），0.1% 参数改写模型性格 | A- |
| [L85.md](per_lesson/L85.md) | ChatGPT 为什么越答越快——KV-Cache 键值缓存从零实现，O(seq²)→O(seq) | A- |
| [L86.md](per_lesson/L86.md) | 给 AI 一点"任性"——temperature / top-k / top-p 采样（sampling）纯 NumPy 从零实现 | A- |
| [L87.md](per_lesson/L87.md) | 把 7B 模型塞进笔记本——INT8 量化（quantization）原理与本地推理 | A- |
| [L88.md](per_lesson/L88.md) | 教机器大海捞针——TF-IDF（词频×逆文档频率）检索，纯 NumPy 从零写起 | A- |
| [L89.md](per_lesson/L89.md) | 给 LLM 一座图书馆——RAG 完整流水线：切片（Chunking）、检索、提示词（Prompt）、生成 | A- |
| [L90.md](per_lesson/L90.md) | 让机器记住对话、答有出处——对话式 RAG：会话记忆（Conversation Memory）与 Podcast 问答引擎 | A- |
| [L91.md](per_lesson/L91.md) | 看见模型在"看"哪里——Self-Attention 权重热力图（Heatmap）与 LoRA 低秩结构图解 | A- |
| [L92.md](per_lesson/L92.md) | 六个月的模块第一次合体——端到端流水线（pipeline）：麦克风 → ASR → LLM → 回答 | B |
| [L93.md](per_lesson/L93.md) | 让实验永不"失忆"——MLOps：W&B 实验追踪（experiment tracking）、模型版本管理与 Docker 打包 | B |
| [L94.md](per_lesson/L94.md) | 把六个月炼成五分钟——Aurora v1 全景 Demo 与面试证据链（evidence chain） | B |
| [L95.md](per_lesson/L95.md) | 从论文读者到作者——研究论文入门：三遍阅读法、写作、投稿与学术合作 | B |
| [L96.md](per_lesson/L96.md) | 白板见真章——合上电脑，亲手推导 FFT / CTC / 注意力机制（attention mechanism） | A- |
| [L97.md](per_lesson/L97.md) | 做得出，更要讲得清——面试（interview）黄金结构与 30 秒 / 3 分钟讲法 | B |
| [L98.md](per_lesson/L98.md) | 诚实的盘点——用数字复盘（retrospective）：做到了什么，还差什么 | B |
| [L99.md](per_lesson/L99.md) | 终点亦是起点——Aurora v2 与持续成长，下一段路，由你亲手书写 | B |

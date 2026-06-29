# Aurora 课程全量审计报告（历史快照，新一轮）

> 这是 2026-06-28 的原始审计记录，保留用于追溯。当前口径请看 `/Users/z/AURORA/docs/README.md` 或最新评审集。

**日期：2026-06-28 · 覆盖范围：L01–L99（99 个 notebook，当前工作区状态）**

---

## 一、总览统计

| 指标 | 数量 |
|------|------|
| 总课数 | 99 |
| 严重问题（Critical） | 29 |
| 重大问题（Major） | 143 |
| 次要问题（Minor） | 136 |
| 不能继续的课（cannot_proceed） | 67 |
| 标题与 README 不符 | 28 |
| 答案提前暴露（Solution Leak） | 68 课次（含多处泄漏） |
| 下一课预告错误 | 59 |
| 完全无问题的课 | **0** |

> **结论：当前工作区没有任何一门课可以不加修改地直接发布给学生。67 门课（68%）存在阻塞性问题，必须在发布前解决。**

---

## 二、严重问题（Critical — 立即修复）

### L01 · `notebooks/0_foundation/L01_motivation.ipynb`

**#1 — 标题与内容不符**
- 位置：Cell c0，H1 标题
- 问题：notebook 标题为「Aurora 是什么——从正弦波到 Whisper，6 个月的路线图」，但 README 将 L01 登记为「环境配置 — conda/venv、Jupyter 内核选择、import aurora 一次跑通」。
- 为何错：学生按目录找到 L01 期望学环境配置，实际看到的是动机/路线图内容。
- 修复：更新 notebooks/README.md 中 L01 条目为「动机与路线图 — Aurora 是什么、为什么从零写、6 个月路线图与 check_imports 环境验证」，或将环境配置内容移入本 notebook。

---

### L02 · `notebooks/0_foundation/L02_sound_digital.ipynb`

**#2 — 标题与内容不符**
- 位置：Cell c0，H1 标题
- 问题：notebook H1 描述「声音的数字表示——采样、数组、第一个可听正弦波」，但 README 登记 L02 为「NumPy 速成 — 数组、dtype、广播与切片，30 分钟能写信号处理代码」。
- 为何错：两者描述完全不同的学习目标，标题契约破裂。
- 修复：确认哪份文档为权威来源，然后统一另一份（更新 README 或重写 notebook 内容）。

**#3 — 下一课预告与实际不符（Critical）**
- 位置：Cell c21，「下一课 L03」section
- 问题：预告说 L03 是「谱图直觉——在学 FFT 之前先看结果」，但官方 L03 标题是「全课程地图 — 从正弦波到 Transformer，99 课能力路径」。
- 修复：将预告文字替换为「下一课 L03：全课程地图——从正弦波到 Transformer，99 课能力路径与面试证据链对照」。

**#4 — 验证断言容差错误（Critical）**
- 位置：Cell c20，`signal_summary` 验证断言
- 问题：`assert abs(s.get('max_abs', 0) - 1.0) < 1e-6`，但 `make_sine(1.0, 64, 3.0)` 在 N=64 采样点上最大值约 0.9952，与 1.0 相差 ~0.005，远超 1e-6。
- 为何错：正确实现会通过不了断言，产生假阴性。
- 修复：将断言改为 `assert abs(s.get('max_abs', 0) - 1.0) < 0.02`。

---

### L03 · `notebooks/0_foundation/L03_spectrogram.ipynb`

**#5 — 课程编号/内容身份错误**
- 位置：Cell c0，H1 标题；文件名 L03_spectrogram.ipynb
- 问题：notebook 内容是「谱图直觉」，但 README 登记 L03 为「全课程地图」，原来的 L03_course_map.ipynb 已被删除（git status 显示 D）。
- 为何错：学生和课程索引都期望 L03 是课程地图，谱图课占用了错误的编号槽位，破坏了其他课程的交叉引用（如 L09 引用「L03 课程地图」）。
- 修复：（a）将本文件改编号到合适位置（如 Module 5 内），并在 L03 恢复课程地图 notebook；或（b）更新 README.md L03 条目为「谱图（Spectrogram）直觉——在学 FFT 之前先看结果」并删除对 L03_course_map.ipynb 的引用。

---

### L09 · `notebooks/2_linear_algebra/L09_vectors.ipynb`

**#6 — 关键依赖库缺失（ModuleNotFoundError）**
- 位置：Cell 4a525441
- 问题：`from laviz import style, arrows2d` — laviz 未安装，运行时抛出 ModuleNotFoundError，notebook 执行中断。
- 修复：在 pyproject.toml 的 [notebooks] 可选依赖组中添加 laviz，或用 matplotlib 替代并删除该 import。

---

### L12 · `notebooks/2_linear_algebra/L12_matrices.ipynb`

**#7 — TODO 桩函数返回 None 导致 TypeError 崩溃**
- 位置：Cell 64236d6c（matvec 桩）+ Cell 17e52ba7（验证断言）
- 问题：桩函数无条件返回 `None`，导致 `np.allclose(None, A @ x)` 抛出 TypeError，而不是有提示性的 AssertionError。
- 修复：将桩函数末行从 `return None` 改为 `pass`（保留零数组 `out`），或改为 `raise NotImplementedError('TODO')`。

---

### L14 · `notebooks/2_linear_algebra/L14_eigen_svd.ipynb`

**#8 — laviz 依赖缺失**
- 位置：Cell dc08b329：`from laviz import style, mat_times_mat_rank1`
- 问题：laviz 不是标准包，未列入依赖，运行时 ModuleNotFoundError，halt 执行。
- 修复：同 L09，添加 pyproject.toml 依赖或用 matplotlib 替换。

---

### L17 · `notebooks/2_linear_algebra/L17_eigen_diagonalization.ipynb`

**#9 — 变量覆盖导致验证断言错误**
- 位置：Cell cell-7 和 cell-9（均重新赋值 `A = np.array([[4.,1.],[2.,3.]])`），Cell bd87cdd6（验证）
- 问题：cells cell-7/9 将 `A` 覆盖为 2×2 矩阵，验证 cell 使用 3×3 矩阵的特征值 (-3,-2,6) 检验 `char_poly(A, lam)`，结果断言全部失败。
- 修复：在 TODO cell 8f1febad 顶部或验证 cell bd87cdd6 顶部重新添加 `A = np.array([[3,3,3],[3,-1,1],[3,1,-1]], float)`。

**#10 — 第二处变量覆盖崩溃**
- 位置：Cell dee6428b（对称对角化检查）
- 问题：同一根因，`P.T @ A @ P` 中 `A` 是 2×2，`P` 是 3×3，形状不匹配，运行时报错。
- 修复：在 cell dee6428b 开头添加 `A = np.array([[3,3,3],[3,-1,1],[3,1,-1]], float)`。

---

### L26 · `notebooks/3_calculus/L26_visual_calculus.ipynb`

**#11 — 概念错误：将凸函数描述为有鞍点**
- 位置：Cell cell-17、cell-18、cell-19（鞍点实验）
- 问题：markdown 反复说从「鞍点旁边出发」，但 `cviz.py` 第 69 行中 contour_descent 使用 f(x,y) = x² + 2y²，这是严格凸函数，**不存在鞍点**。
- 为何错：∇²f = diag(2,4) 正定，所有轨迹直接收敛到 (0,0)，无任何被鞍点吸引再偏转的行为。学生形成错误的鞍点直觉。
- 修复：（a）将函数改为 f(x,y) = x² − y²（有真正鞍点）；或（b）删除所有「鞍点」引用，改为描述「从最小值旁出发观察收敛速度与学习率的关系」。

---

### L32 · `notebooks/5_audio_dsp/L32_numpy_signals.ipynb`

**#12 — aurora 和 aviz 均不可导入，notebook 已保存错误输出**
- 位置：Cell f180f27f
- 问题：`from aurora.audio import sine` 和 `import aviz` 均失败（保存输出已显示 ModuleNotFoundError）。
- 修复：用内联 `np.sin` 实现替代，删除 aurora.audio 和 aviz import。

---

### L33 · `notebooks/5_audio_dsp/L33_sine_wave.ipynb`

**#13 — aviz 导入崩溃**
- 位置：Cell 5a3970dd
- 问题：`import aviz; aviz.style(); aviz.waveform(...)` — aviz 不存在于项目环境。
- 修复：替换为纯 matplotlib 实现：`plt.stem(sine(440.0, duration=50/16000, sample_rate=16000)); plt.title('440 Hz 正弦 — 前 50 个采样点'); plt.show()`，删除 aviz import。

---

### L35 · `notebooks/5_audio_dsp/L35_euler_fft.ipynb`

**#14 — aviz 导入崩溃**
- 位置：Cell b9994aee
- 问题：`import aviz` 和 `aviz.twiddles(8)` — aviz 不存在，运行时 ImportError。
- 修复：删除该 cell 或替换为纯 numpy+matplotlib 实现（绘制 8 个旋转因子的复平面图）。

---

### L36 · `notebooks/5_audio_dsp/L36_windows.ipynb`

**#15 — 连续 5 个 cell 依赖不存在的 aviz**
- 位置：Cells 523a7128, bebf53a7, 7e86d1bc, 79fc9356, ebcad4a3（「图示」section）
- 问题：`import aviz` 及所有 `aviz.*` 调用（style, windows_overlay, framing, spectrogram, mel_filterbank_plot, mel_spectrogram_plot）均 ModuleNotFoundError。
- 修复：删除所有 aviz cell，或改为基于 matplotlib+aurora 现有 API 的等价实现，或加 `try/except ImportError: pass` 保护并注释说明。

---

### L44 · `notebooks/5_audio_dsp/L44_stft_implement.ipynb`

**#16 — TODO 桩迭代 None 崩溃**
- 位置：Cell-10（TODO 桩），循环体 `for f in windowed:`
- 问题：桩将 `windowed = None`，然后立即执行 `for f in windowed:`，抛出 `TypeError: 'NoneType' object is not iterable`，Cell-11 的验证断言永远无法触达。
- 修复：将裸 `for f in windowed:` 改为 `if windowed is not None:` 条件包裹，或将初始化改为空数组。

**#17 — 解答提前暴露（详细完整实现）**
- 位置：Cell-9，`<details>` 块
- 问题：折叠块中含有完整的参考实现，位于 TODO 练习 cell 正上方，一次点击即可看到答案。
- 修复：删除 `<details>` 块，或移到独立的 instructor-only notebook。

---

### L46 · `notebooks/5_audio_dsp/L46_mel.ipynb`

**#18 — 验证断言使用错误参考值**
- 位置：Cell-11，断言语句；Cell-9 expected output；Cell-3 文本
- 问题：`assert abs(hz_to_mel(700) - 782.7) < 0.5`，但正确值为 2595 × log10(2) = **781.17**，相差 1.53，超出容差 0.5。正确实现反而过不了断言。
- 修复：改为 `abs(hz_to_mel(700) - 781.2) < 0.5`；更新 Cell-9 expected output 和 Cell-3 文本（「约 783 Mel」→「约 781 Mel」）。

---

### L49 · `notebooks/5_audio_dsp/L49_dct.ipynb`

**#19 — IDCT 实现数学错误**
- 位置：Cell-13，函数 `_idct_ii_ref`
- 问题：该函数应用了未归一化 IDCT 的公式，但输入 `X_dct` 是正交归一化 DCT-II 的输出，两者不匹配，Experiment A 会显示大误差而非 ≈ 0。
- 为何错：`dct_ii([1,2,3,4])` ≈ [5,-2.23,0,-0.16]，正确逆变换应还原 [1,2,3,4]，但当前实现返回约 [0.095, 0.47, 0.72, 0.85]。
- 修复：替换为正确逆变换：使用前向矩阵的转置乘以缩放向量（scale[0]=√(1/N)，scale[k>0]=√(2/N)）。

---

### L55 · `notebooks/6_deep_learning/L55_forward_pass.ipynb`

**#20 — notebook 内容与官方课题完全不符**
- 位置：Cell 0，H1 标题
- 问题：官方 L55 要求「矩阵乘 + 偏置 + 激活函数，逐层打印输出形状」，实际 notebook 实现标量 Value 类算子（__pow__, relu, tanh, exp），是 L54 内容的延续，与 L55 课题完全不同。
- 修复：（a）重写 notebook 实现矩阵级前向传播（W @ x + b），每层打印形状；或（b）更新 README.md L55 条目描述实际内容。

---

### L64 · `notebooks/6_deep_learning/L64_kws_train_eval.ipynb`

**#21 — 下一课预告描述错误内容**
- 位置：Cell-17（本课收束段落）
- 问题：预告说下一节讲「推理/实时输出关键词概率、延迟指标」，但 L65 实际是「训练可视化 — Loss/Acc 曲线、梯度范数、权重分布直方图」。
- 修复：替换为「下一节将深入训练过程可视化：实时绘制 Loss/Acc 曲线、监控梯度范数，以及权重分布直方图，帮助诊断训练是否健康。」

---

### L72 · `notebooks/7_asr/L72_whisper_finetune.ipynb`

**#22 — HuggingFace 数据集分片名称错误**
- 位置：Cell-6，`load_dataset` 调用，split 参数
- 问题：使用 `'train.100'` 和 `'test'`，实际 librispeech_asr 'clean' 配置的正确名称为 `'train.clean.100'` 和 `'test.clean'`。
- 为何错：错误 split 名会在运行时抛出 DatasetNotFoundError/ValueError，notebook 无法运行。
- 修复：改为 `{"train": "train.clean.100", "test": "test.clean"}`。

---

### L80 · `notebooks/8_music/L80_similarity.ipynb`

**#23 — 实验循环在 TODO 未完成时崩溃**
- 位置：Cell-13（Section 5 实验循环）
- 问题：`idx, scores = find_similar(query, library, top_k=top_k)` 直接解包，未实现时 `find_similar` 返回 None，抛出 `TypeError: cannot unpack non-iterable NoneType`。Cell-11 有正确的 None 保护，Cell-13 没有。
- 修复：在循环体加 `result = find_similar(...); if result is None: print('⬜ find_similar 未实现'); break; idx, scores = result`。

---

### L82 · `notebooks/8_music/L82_visual_music.ipynb`

**#24 — 标题承诺三种可视化，notebook 只实现一种**
- 位置：整个 notebook
- 问题：标题和官方课名承诺「色度图、节拍图、相似度热力图」三种可视化，notebook 只实现了色度图和 t-SNE 散点图（t-SNE 不在标题中），节拍图和热力图完全缺失。
- 修复：（a）添加节拍追踪可视化 Section 2 和相似度热力图 Section 3；或（b）将标题改为「音乐特征可视化 — Chroma 热力图与 Embedding t-SNE 聚类」并更新 README。

---

### L89 · `notebooks/9_llm/L89_rag_pipeline.ipynb`

**#25 — 验证 cell 在定义前执行，导致 NameError**
- 位置：Cell 9f212137 和 cell cbc38021
- 问题：两个验证 cell 均出现在其所依赖的定义之前——`format_rag_prompt` 直到 cell-10 才定义，`matrix`/`vocab` 直到 cell-11 才构建，顶部到底部运行时均抛 NameError。
- 修复：将 cell-10（`format_rag_prompt` 定义）移到「任务 2」header cell 之后；将 cell-11（`build_tfidf` 调用）移到 end-to-end 验证 cell 之前。

---

### L90 · `notebooks/9_llm/L90_agent.ipynb`

**#26 — notebook 内容与课程主题完全不符**
- 位置：Cell 0，H1 标题
- 问题：标题为「对话式 RAG — 会话记忆、来源归因与 Podcast Q&A 流水线」，但官方 L90 应为「Tool-calling Agent — 工具定义、函数调用解析、多步推理循环」。整个 notebook 讲错了主题。
- 修复：（a）重写为工具调用 Agent 课程内容；或（b）更新 README L90 条目为对话式 RAG，并重新排列课程编号。

---

### L91 · `notebooks/9_llm/L91_visual_llm.ipynb`

**#27 — LoRA 矩阵形状标注错误**
- 位置：Cell-1 和 Cell-5
- 问题：定义 A(d×r) 和 B(r×d)，然后声称 ΔW = B @ A 形状为 (d, d)，但 B(r,d) @ A(d,r) = (r,r)，不是 (d, d)。
- 为何错：标准 LoRA 应为 A(r×d)、B(d×r)，使 B @ A 产生 (d, d)。
- 修复：Cell-1 改「A（d×r）和 B（r×d）」为「A（r×d）和 B（d×r）」；Cell-5 对应修正。

---

### L95 · `notebooks/10_integration/L95_research_papers.ipynb`

**#28 — notebook 内容与官方课题完全不符**
- 位置：Cell d797b4eb，H1 标题
- 问题：官方标题承诺「论文精读 — Whisper、MusicGen、VALL-E 三遍法：略读 → 精读 → 复现关键实验」，实际 notebook 是通用学术出版入门（投稿期刊、rebuttal 写作、学术合作路径），完全没有三篇论文的深度阅读。
- 修复：（a）重写为 Whisper/MusicGen/VALL-E 三遍法精读，包含公式提取和复现 cell；或（b）更新 README L95 条目为当前通用内容，并相应修改 H1。

---

### L97 · `notebooks/10_integration/L97_interview.ipynb`

**#29 — 验证断言期望错误形状**
- 位置：Cell id=4304d489
- 问题：`assert frames.shape == (3, 8)`，但对 x=np.arange(20)、win_len=8、hop=4 的正确实现产生 `(4, 8)`（n_frames = 1 + (20-8)//4 = 4）。
- 为何错：正确代码会被断言拒绝，产生假阴性。
- 修复：改为 `assert frames.shape == (4, 8), f"期望 (4,8)，得到 {frames.shape}"`。

---

## 三、重大问题（Major）

> 共 143 处，按课号排序。重复规律的问题（如 `<details>` 答案泄漏、下一课预告错误）已在第六节「交叉规律」中做系统分析。

### L01
- **checklist 7**（下一课预告）：Cell c23 预告 L02 是「make_sine 三函数数字音频课」，但 README 登记 L02 为 NumPy 速成。修复：将预告改为「NumPy 速成——数组、dtype、广播与切片」。

### L04
- **checklist 4**（解答泄漏）：Cell 17f744ee `<details>` 块暴露完整 `make_wave` 实现，位于 TODO cell f97dfde9 正上方。修复：删除或移至验证 cell 之后。

### L05
- **checklist 1**（标题/内容不符）：Cell 1592bd0f H1 标题缺少「复数乘法 = 旋转 + 缩放」，且该概念在 notebook 中完全未涉及。修复：添加演示复数乘法即旋转缩放的 section，更新 H1。
- **checklist 4**（解答泄漏）：Cell 1242eb23 `<details>` 块暴露完整 `magnitude_phase` 实现，位于 TODO 正上方。修复：移至验证 cell 之后。

### L06
- **checklist 7**（下一课预告）：Cell cell-19 说 L07 讲「DFT 为何能分解信号到各频率」，实际 L07 是「万物皆正弦 — 用三角波叠加合成方波」。修复：将预告改为「用正弦波叠加合成方波，一图建立傅里叶直觉」。
- **checklist 4**（解答泄漏）：Cell fba5501d `<details>` 暴露完整 `twiddle(k,n,N)` 实现。修复：移至验证 cell 之后。

### L07
- **checklist 4**（解答泄漏）：Cell 8daaadd9 `<details>` 暴露完整 `square_approx` 实现。
- **checklist 7**（下一课预告）：Cell cell-18 说 L08 用 `xviz`，但 L08 官方标题用 `matplotlib`。修复：「下一课（L08）将用 matplotlib 动态演示复数平面上的单位圆旋转、共轭对称与相位概念。」

### L08
- **checklist 3**（描述与代码不符）：三处引用 `week01/day4_euler.ipynb`（已删除），应改为 `notebooks/1_complex_trig/L06_euler.ipynb`。
- **checklist 3**：引用 `aurora/audio/fft.py`，但该文件不存在，实际为 `aurora/audio/transforms.py`。

### L09
- **checklist 4**（解答泄漏）：Cell b1b4933e `<details>` 暴露 `scale()` 完整实现。

### L10
- **checklist 4**（解答泄漏）：Cell 791bf4b7 `<details>` 暴露 `cosine_similarity` 完整实现。

### L11
- **checklist 4**（解答泄漏）：Cell c7bce6f0 `<details>` 暴露 `normalize()` 完整实现 `return v / np.linalg.norm(v)`。

### L12
- **checklist 4**（解答泄漏）：Cell ee061bac `<details>` 暴露完整 `matvec` 循环实现。

### L13
- **checklist 4**（解答泄漏）：Cell 47eaf451 `<details>` 暴露完整 `is_orthogonal()` 实现。

### L14
- **checklist 3**（解答提示即完整答案）：Cell id=25e6f24a 和 cell-18 的「提示」直接给出完整代码 `U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]`，学生无需推导。
- **checklist 2**（目录重复编号）：PCA 和 SVD 均标为「## 2.」，应将 SVD 改为「## 3.」。
- **checklist 2**（教学顺序错误）：SVD 代码（cells cell-9, cell-11）出现在 SVD 概念介绍之前的特征值 section 中。

### L15
- **checklist 2**（术语错误）：Cell-7 使用「正定」（positive definite）表示「方阵/恰定」（exactly determined）系统，概念混淆。修复：改为「超定（m>n）、恰定（m=n）还是欠定（m<n）」。
- **checklist 4**（解答泄漏）：Cell ab06e2fb `<details>` 暴露完整 `classify_system` 实现。

### L16
- **checklist 4**（解答泄漏）：Cell 586d2ce0 `<details>` 暴露 `det_2x2` 和 `inv_2x2` 完整实现。

### L17
- **checklist 4**（解答泄漏）：Cell 505c5565 `<details>` 暴露完整 `char_poly` 实现。
- **checklist 3**（section 标题与代码不符）：标题说「动手观察 A @ v ≈ λ * v」，代码实际验证的是重建误差 `A ≈ P @ D @ P⁻¹`。

### L18
- **checklist 4**（解答泄漏）：Cell 2cb7662e `<details>` 暴露完整 `is_sdd` 实现。
- **checklist 5**（实验描述但无代码）：Cell cell-18 描述 Jacobi 迭代收敛/发散实验，但没有对应代码 cell。
- **checklist 5**（laviz 依赖缺失）：Cell 06aaebea `from laviz import style, heatmap`，未声明依赖。

### L22
- **checklist 4**（解答泄漏）：Cell 202a8bdf `<details>` 暴露完整 `numeric_derivative` 实现。
- **checklist 3**（代码与描述不符）：Cell cell-6/7 描述 sin/cos 实验，代码实际用 x²；Cell cell-8/9 同样不符。

### L23
- **checklist 4**（解答泄漏）：Cell 120c1e12 `<details>` 暴露完整 `gradient()` 实现。
- **checklist 3**（点不一致）：Cell cell-16 描述在 [1,2] 处验证，Cell cell-15 实际在 [3,4] 处。

### L24
- **checklist 3**（描述与代码不符）：Cell cell-6 说观察 `cos(x²)·2x`，Cell cell-7 实现的是纯 `x²` 导数。
- **checklist 4**（解答泄漏）：Cell 6c2ab08a `<details>` 暴露完整复合函数导数实现。

### L25
- **checklist 7**（下一课预告错误）：Cell cell-20 说下一节讲「链式法则」，但链式法则是 L24（上一课），实际 L26 是微积分可视化。
- **checklist 4**（解答泄漏）：Cell d64eec88 `<details>` 暴露 `gd_step` 完整实现。

### L26
- **checklist 3**（代码与解释顺序颠倒）：Cell-17（代码）出现在 Cell-18（说明 markdown）之前，破坏「先解释再演示」的教学流程。

### L27
- **checklist 4**（解答泄漏）：Cell 8ab84f7c `<details>` 暴露完整 `estimate_prob_six` 实现。
- **checklist 3**（seed 不一致）：Cell cell-16 说 seed=42，Cell cell-17 代码使用 seed=7。

### L28
- **checklist 4**（解答泄漏）：Cell 50b00530 `<details>` 暴露 `zscore()` 完整实现。
- **checklist 7**（下一课预告）：Cell cell-20 说「下一节 softmax 和交叉熵」，实际 L29 是常见概率分布。

### L29
- **checklist 4**（解答泄漏）：Cell 5feb5fbc `<details>` 暴露完整 `gaussian_pdf` 实现。

### L30
- **checklist 4**（解答泄漏）：Cell b25194b7（softmax）和 cell 7edf4d8b（cross_entropy）均含 `<details>` 完整实现。

### L36
- **checklist 3**（描述与代码不符）：Cell cell-27 说「旁瓣高度 dB 对比」使用非整数频率 sine，实际 Cell cell-28 代码对 `np.ones(N)` DC 信号测边缘能量，完全不同。

### L38
- **checklist 4**（解答泄漏）：Cell-11 `<details>` 暴露完整 `butterfly()` 实现。
- **checklist 7**（下一课预告）：Cell-17 说 L39 是「迭代位反转 FFT」，但 L39 实际是「Cooley-Tukey 递归实现」。

### L39
- **checklist 4**（解答泄漏）：Cell-11 `<details>` 暴露完整 `my_fft()` 实现。

### L40
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `frequency_bins` 实现。

### L41
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `windowed_fft` 实现。

### L42
- **checklist 3**（markdown 参数与代码不符）：Cell 9 描述 duration=0.05，N=400，bins≈2.75/5.5；Cell 10 实际用 duration=0.032，N=256，实际 bins≈14/28。
- **checklist 1**（标题承诺内容缺失）：标题承诺「和弦/噪声频谱对比」，notebook 只有两频率叠加，无和弦无噪声。

### L43
- **checklist 4**（解答泄漏）：Cell 9 `<details>` 暴露完整 `frame_signal` 实现。
- **checklist 3**（预测帧数错误）：markdown 说 win_len=128 约 125 帧（实际 122），win_len=2048 约 7 帧（实际 4）。帧数之比声称 16 倍（实际约 30 倍）。

### L44
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `my_stft()` 实现。
- **checklist 7**（下一课预告）：说下一课是 L46（Mel 滤波器组），实际 L45（声谱图生成）。

### L45
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `plot_spectrogram()` 实现。

### L46
- **checklist 4**（解答泄漏）：Cell-9 和 Cell-12 均含 `<details>` 完整实现（hz_to_mel 和 mel_filterbank）。

### L47
- **checklist 3**（矩阵乘法顺序错误）：Cell-3 一行公式 `log_mel = log(mel_filterbank @ power_spectrum.T + eps)` 产生形状 (n_mels, n_frames)，但 notebook 其余部分和代码均使用 (n_frames, n_mels)。正确顺序应为 `power_spectrum @ mel_filterbank.T`。
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `log_mel_spectrogram` 实现。

### L49
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `dct_ii` 实现。

### L50
- **checklist 3**（可视化与代码矛盾）：Cell-4 和 Cell-6 的图标注 k=0 为「跳过」，但 Cell-3 文本和代码均说「保留 k=0」。学生看图会写出错误实现。
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `my_mfcc()` 实现。

### L51
- **checklist 7**（下一课预告）：说 L52 会做「DTW 或 kNN 音素识别分类器」，实际 L52 是「Audio Core 完结，38 个单元测试全绿，面试证据整理」。

### L52
- **checklist 7**（下一课预告）：说 L54 训练序列模型，实际下一课是 L53（MFCC 图形化）。

### L53
- **checklist 3**（承诺的可视化层次缺失）：标题承诺「波形 → 声谱图 → Mel 谱 → 倒谱系数逐层图示」，但 notebook 从未绘制波形和 STFT 声谱图，直接跳到 log-Mel 和 DCT。

### L54
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 Value 类实现（14 个方法含 backward）。

### L55
- **checklist 4**（解答泄漏）：Cell 9 `<details>` 暴露 `__pow__`、relu、tanh、exp 四个算子的完整实现。

### L56
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `backward()` 实现。

### L58
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `train()` 实现。
- **checklist 7**（下一课预告）：用过期标签「a6」，描述 DataLoader/mini-batch 内容，实际 L59 是 PyTorch Tensor 基础。

### L59
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `mel_to_batch()` 实现。
- **checklist 7**（下一课预告）：说 L60 是 nn.Module + Conv2d，实际 L60 是 autograd 机制（grad_fn、backward()、retain_graph）。

### L60
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `verify_gradients()` 实现。
- **checklist 1**（标题承诺内容缺失）：标题包含「retain_graph 原理」，但 notebook 中完全未演示或解释该概念。

### L61
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `AudioMLP` 类实现。
- **checklist 7**（下一课预告）：说 L62 是「training loop（p4_training_loop）」，实际 L62 是 Dataset 和 DataLoader。

### L62
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `extract_features` 实现。
- **checklist 7**（下一课预告）：说 L63 涉及 Dataset/DataLoader 包装，实际 L63 是 CNN 模型定义。
- **checklist 1**（标题承诺内容缺失）：标题承诺「自定义 __getitem__，音频数据批量加载」，notebook 从未实现 Dataset 子类或 DataLoader。

### L63
- **checklist 4**（解答泄漏）：Cell 9 `<details>` 暴露完整 `KeywordCNN.__init__` 和 `forward` 实现。

### L64
- **checklist 4**（解答泄漏）：Cell-9 和 Cell-12 均含 `<details>` 完整实现（train_epoch 和 eval_accuracy）。

### L65
- **checklist 7**（下一课预告）：Cell-9 和 Cell-11 均错误描述 L66 为「KeywordCNN 完整训练循环」，实际 L66 是「ASR 系统全览」。
- **checklist 7**：Cell-11 还包含过期路径「month02/a5_train.ipynb」，且是重复收束 section。

### L66
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `compute_wer` 实现（含完整 DP 回溯）。

### L67
- **checklist 7**（下一课预告）：结尾说 CTC 对齐「直接服务于 Whisper 的训练目标」，但 Whisper 使用交叉熵而非 CTC。修复：改为「服务于 CTC 系列模型（如 wav2vec 2.0、DeepSpeech）的训练目标」。

### L68
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `ctc_greedy_decode` 实现。
- **checklist 7**（下一课预告）：Cell-14 描述 Whisper 架构，实际 L69 是「CTC 前向算法」。

### L70
- **checklist 2**（数值不一致）：Cell-1 说 decoder 关注 750 encoder steps，Cells 5/6/8 正确使用 1500。修复：Cell-1 改为「1500 步」。
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `whisper_preprocess` 实现。
- **checklist 7**（下一课预告）：Cell-14 描述「cross-attention 权重可视化」，实际 L71 是「贪婪解码与 beam search」。

### L71
- **checklist 3**（复杂度声明矛盾）：Cell-1 说贪婪解码 O(T)，Cell-8 表格正确说 O(T×V)。修复：Cell-1 改为 O(T×V)。
- **checklist 4**（解答泄漏为伪 TODO）：Tasks 1/2 标注 ✏️ 但各 task 的代码 cell 已包含完整实现，无空白供学生填写。

### L72
- **checklist 7**（下一课预告）：Cell-11 描述「流式转录与时间戳对齐」，实际 L73 是「WER 评估」。

### L73
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `analyze_errors()` 实现（含 DP 回溯和最差案例逻辑）。

### L75
- **checklist 5**（未使用但危险的 import）：Cell-2 `import torch`，torch 未使用但会导致无 torch 的学生 ImportError，阻塞整个 notebook。

### L76
- **checklist 4**（解答泄漏为伪 TODO）：Cell 4 和 Cell 6 中三个 TODO 函数均已有完整实现，学生无任何空白可填。

### L77
- **checklist 2**（标题内容缺失）：标题承诺 ZCR（零交叉率），但 notebook 从未定义、解释或实现 ZCR，以节拍追踪替代。
- **checklist 4**（解答泄漏）：Cell 9（chroma_vector）和 Cell 12（rms_envelope）均含 `<details>` 完整实现。
- **checklist 7**（下一课预告）：Cell 17 说 L78「实时流式场景、增量式 chroma 累积」，实际 L78 是「onset 包络、自相关与 BPM 估计」。

### L78
- **checklist 4**（解答泄漏为伪 TODO）：Cell-5 `onset_envelope` 和 Cell-7 `autocorrelation` 均在 TODO 注释后立即给出完整实现。

### L79
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `triplet_loss` 实现。
- **checklist 7**（下一课预告）：Cell-eadb2c04 指向 L82，实际下一课是 L80。

### L80
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `find_similar()` 实现。

### L81
- **checklist 4**（解答泄漏）：Cell 9 `<details>` 暴露完整 `recommend()` 实现。
- **checklist 7**（下一课预告）：Cell 14 描述「Recall@K 与 NDCG 评估」，实际 L82 是「音乐特征可视化」。

### L83
- **checklist 7**（下一课预告）：Cell-20 说 L84 是「封装 MultiHeadAttention」，实际 L84 是「LoRA 低秩适配」。
- **checklist 3**（引用不存在的课）：Cell-7 引用「L2」将实现 MultiHeadAttention，该编号不存在。

### L84
- **checklist 4**（解答泄漏）：Cell-9 `<details>` 暴露完整 `LoRALinear` 类实现。
- **checklist 7**（下一课预告）：Cell-14 描述「LoRA 注入 Transformer」，实际 L85 是「KV-Cache 从零实现」。

### L85
- **checklist 4**（解答泄漏为伪 TODO）：Cell-3 和 Cell-5 的 TODO 注释后立即给出完整实现。

### L86
- **checklist 4**（解答泄漏为伪 TODO）：Cell-5（top_k_sample）和 Cell-7（top_p_sample）均在 TODO 注释后立即给出完整实现。

### L88
- **checklist 4**（解答泄漏为伪 TODO）：Cells 5/7/9 三个 TODO 均立即跟随完整实现。

### L89
- **checklist 4**（解答泄漏为伪 TODO）：Cell-5（chunk_text）和 Cell-10（format_rag_prompt）均标 ✏️ 但已有完整实现。

### L90
- **checklist 4**（解答泄漏）：Cell 9 `<details>` 暴露完整 `podcast_qa()` 实现。

### L91
- **checklist 3**（标题/实现不符）：标题和 README 承诺「多头注意力」，notebook 只实现单头注意力（无头分割、无拼接、无 W_O 投影）。

### L92
- **checklist 7**（下一课预告）：Cell-17 称 L93 为「持续集成与部署监控」，实际 L93 是「MLOps 基础 — W&B 实验追踪、模型版本管理、Docker 打包与部署脚本」。

### L93
- **checklist 7**（下一课预告）：Cell-17 说「课程回顾与能力自测」，实际 L94 是「Aurora v1 全景 Demo — 综合展示所有能力，面试材料与证据链整理」。

### L94
- **checklist 3**（demo 路径过期）：Cell-11 demo 流程表格中 `week01/day4_euler.ipynb`、`month03/`、`month05/` 均已不存在，应改为 L-编号路径。

### L95
- **checklist 7**（下一课预告）：Cell 33136589 预告「L96：课程复盘」，实际 L96 是「白板演练 — DFT/FFT/注意力机制口述推导，面试现场模拟」。

### L96
- **checklist 1**（标题不符）：Cell c72481d0 H1 是「FFT/CTC/注意力机制」，官方标题是「DFT/FFT/注意力机制口述推导，面试现场模拟」（缺 DFT，多 CTC，缺「口述推导，面试现场模拟」）。
- **checklist 7**（下一课预告）：Cell fe1cedc6 说 L97「30 分钟讲清 Aurora 模块」，实际 L97 是「30 秒 elevator pitch、GitHub 证据链、简历技术点对照」（30 分钟 vs 30 秒错误）。

### L97
- **checklist 1**（标题不符）：H1「面试准备与技术沟通——如何讲清你做的每一件事」≠ 官方「面试材料整理 — 30 秒 elevator pitch、GitHub 证据链、简历技术点对照」。

### L98
- **checklist 1**（标题不符）：H1「L98 · 课程总结——做到了什么，还差什么」≠ 官方「复盘 — 6 个月里程碑回顾，方法论总结，成长曲线量化」。

### L99
- **checklist 1**（标题不符）：H1「Aurora v2 与持续成长——6 个月之后怎么走」≠ 官方「下一步 — 进阶路线规划：研究方向、开源贡献、下一个里程碑」。

---

## 四、次要问题（Minor）

> 共 136 处，以下按课号列出，简要描述。

| 课号 | 位置 | 问题 |
|------|------|------|
| L01 | Cell c19 | 使用 `Path` 类但该 cell 未导入，kernel 重启后运行会 NameError |
| L03 | 练习 markdown cell | 提示学生在「下面 Markdown cell」写预测，但该 cell 不存在 |
| L04 | Cell cell-21 | 预告 L05 时未提及极坐标和复数乘法=旋转+缩放两个核心主题 |
| L04 | H1 cell f618dc89 | H1 缺少「，亲手实现」后缀，与官方标题不完全一致 |
| L05 | Cell cell-5 | 说「角度每增加 π/4 移一步」但代码中 angles 为 π/2 间距 |
| L05 | Cells cell-14/cell-16 | 完全相同的代码，cell-16 是重复副本 |
| L06 | Cell cell-17 | 使用 `np` 但 cell 自身未 `import numpy as np` |
| L07 | Cell id=cell-21 | e^{iθ} 演示 cell 与 L06 欧拉公式相关，与 L07 傅里叶级数无关，是复制残留 |
| L07 | Cell-15 vs cell-35e71676 | 频谱幅值表用 4/(πk)，`square_approx` 实际输出 ≈ π/4，两者归一化不同，未说明 |
| L08 | Cell cell-22 | 下一课说「向量空间和矩阵乘法」，L09 实际不包含矩阵乘法 |
| L08 | Cells cell-19/cell-21 | 完全相同的 twiddle factor 循环代码，cell-21 是重复副本 |
| L08 | Cell cell-20 vs cell-19/21 | markdown 用负指数 DFT 约定，代码用正指数，差异未注释 |
| L09 | H1 cell 56c37ff7 | 添加「（vector）」和「（linear combination）」英文注释，与 README 标题不完全一致 |
| L10 | Cell cell-7/cell-18 | 两个矩阵-向量乘法 cell 游离于点积主题之外，无过渡说明 |
| L10 | Cell 9d64d7b5 | `round(None, 3)` 产生 TypeError 而非有意义的 AssertionError |
| L11 | Cell 5ec7bbf2 | H1 含「（vector）」注释，与 README 标题不符 |
| L11 | Cell aa9aeb95 | `from laviz import style, arrows2d`，未声明依赖 |
| L11 | Cell 16166fa5 | `np.linalg.norm(None)` 产生 TypeError，应先运行 assert |
| L12 | Cell cell-21 | 下一课预告称「对角矩阵」，实际 L13 重点是对称矩阵和正定性判定 |
| L13 | Cell a770d882 | 未 `import numpy as np`，kernel 重启后 NameError |
| L13 | Cell cell-21 | 下一课预告未提 SVD（L14 官方标题的核心之一） |
| L14 | Cell id=15f78c03/b728553e | 未 `import numpy as np` |
| L15 | Cell 0352c35f | 注释「# ER3 + ER2」标注不准确（实际是缩放后加法），应改为更清晰描述 |
| L16 | Cell 8ca2c154 | `from laviz import style, matrix_4ways`，未声明依赖 |
| L16 | Cell cell-22 | 下一课预告说「特征分解会用 det=0 识别奇异矩阵」，L17 实际重点是 A=PDP⁻¹ 坐标变换 |
| L17 | Cell 08f8be3c | 引用 `aurora/dsp/`，实际模块在 `aurora/audio/` |
| L17 | Cell 237c9bc0 | `from laviz import style, show_factorization`，未声明依赖 |
| L18 | Cell 9a32c935 | 断言前无 None 保护，顶部到底部运行 AssertionError 阻断后续 cell |
| L19 | Cell-24 | 下一课预告用「v2」而非「L20」，且只提 SVD/特征分解，遗漏 LU/QR |
| L19 | Cell-27 | 小检查 cell 只打印不断言，无法自动验证正确性 |
| L20 | Cell cell-20/70ec5c49 | 下一课预告用「v3」，描述错误（说 SVD 奇异值分布，实际 L21 是 DFT/Mel 矩阵即滤波） |
| L20 | 多处 cell | 五处交叉引用使用废弃 p-编号（p6→L14, p7→L15, p9→L17, v3） |
| L21 | Cell-18 | 未使用变量 `k = np.arange(N // 2 + 1)` |
| L21 | Cell-18 | MFCC 流水线跳过 Mel 步骤，注释「简化版，跳过Mel」不够显眼 |
| L22 | Cells cell-16/cell-18 | 完全相同的 h-sweep 代码，cell-16 是副本 |
| L22 | Cell 19151071 | 引用旧文件名 `c2_gradients.ipynb`，应为 `L23_gradients.ipynb` |
| L23 | Cell cell-11 | 公式写 `(f(p + e*h) - f(p - e*h)) / (2h)`，实现中 e 已包含 h，公式应为 `(f(p+e) - f(p-e)) / (2h)` |
| L24 | Cell cell-4 | markdown 说「在 x = π/4 处计算」，代码用 x = 1.3 |
| L25 | Cell cell-7 | 使用 f(x) = x²，但课程主例是 f(x) = (x-3)²，无说明原因 |
| L26 | H1 cell 60d1ac13 | 添加大量双语括号注释，与官方标题不完全一致 |
| L26 | Cell-17 | contour_descent 调用缺少分号，Figure 对象 repr 会打印 |
| L27 | Cells cell-15/cell-17 | 完全相同的 seed=7 循环代码，cell-15 是副本 |
| L29 | Cell-0/cc9f7f03 | 两个 H1 cell，第一个用「正态（Gaussian）」，官方用「高斯」 |
| L30 | Cells cell-3/b25194b7 | 两处均标「## 1.」，重复编号 |
| L30 | Cells cell-22/cell-24 | 完全相同的 scale-loop 代码，cell-24 是副本（且 markdown 描述的两个不同实验从未实现） |
| L31 | Cells cell-25/cell-27 | softmax 函数在两个不同 cell 中重复定义 |
| L32 | Cell 1e7763ce | 代码 print 文本与已保存输出不符（stale output） |
| L33 | Cell ef820af3/8617b5a4 | 说精度「1e-15 量级」，断言只要求 `< 1e-6`，两者不一致 |
| L34 | H1 cell de71088c | 添加「（aliasing）」注释，与官方标题不完全一致 |
| L34 | Cells cell-20/cell-22 | 完全相同代码，cell-22 是副本 |
| L34 | Cell a7dfc2d7 | `import aviz; aviz.aliasing(...)` 未声明依赖 |
| L35 | Cells cell-25/cell-27 | 完全相同的 5-angle 验证循环，cell-27 是副本 |
| L36 | Cells cell-26/cell-28 | 完全相同代码，cell-26 是副本 |
| L37 | Cell-14 | 交叉引用写「L39 实现 FFT」，正确应为 L38 |
| L38 | Cell fcdf275c | 导航链接跳至 L42，跳过 L39/L40/L41 |
| L39 | H1 / Cell-13 | 标题承诺「误差 < 1e-10」，断言用 `atol=1e-9`（宽松 10 倍） |
| L39 | Cell-15 | 基准测试 cell 调用 `my_fft(x_bench)` 无 try/except 保护，TODO 未实现时崩溃 |
| L40 | Cell-13 | 实验 cell 无 `frequency_bins` 未实现时的保护 |
| L41 | H1 cell-0 | 添加「（windowing）」「（magnitude spectrum）」注释，与官方标题不完全一致 |
| L42 | Cell 11 | 引用旧文件名「day1_stft.ipynb」，应为「L43_stft.ipynb」 |
| L43 | Cell-14 | 下一课预告略去 L44「与 aurora.audio.stft 对齐验证」的核心特点 |
| L45 | Cell-3/4 vs cell-9/10 | eps 在概念说明用 1e-10，所有演示/解答 cell 用 1e-8，不一致 |
| L45 | Cell-3/4 vs cell-9 | dB 公式在 cell-3/4 为 `10*log10(P+eps)`（功率域），在后续均为 `20*log10(A+eps)`（幅度域），未说明一致性 |
| L45 | H1 cell-0 | 标题含「pcolormesh 热力图」，但 notebook 全部使用 `plt.imshow`，从未用 pcolormesh |
| L45 | Cell-13 | 引用 `dB_ref` 但该变量在 cell-11 中定义，跳过 cell-11 会 NameError |
| L46 | Cell-9/12 | 两个 TODO 均含 `<details>` 完整实现（轻量级 Minor 层面，实际已在 Critical/Major 章节处理） |
| L48 | Cell-8 | 注释 `# (n_frames, n_mels) → (n_frames, n_mels)` 错误（实际 `.T` 后是 (n_mels, n_frames)） |
| L48 | Cell-2 | `stft` 导入未使用 |
| L48 | Cell-9 | 下一课预告说「MFCC 应用」，实际 L49 重点是「DCT-II 算法实现」 |
| L49 | H1 cell-0 | 添加「（decorrelation）」注释，与官方标题不完全一致 |
| L50 | Cell-9 | 参考输出注释「# out.shape == (61, 13)」但注释内「≈ 63」自相矛盾 |
| L51 | Cell-10 | 行 `cfg["hop_length"] = cfg.get("hop_length")` 是无操作死代码，注释也误导 |
| L52 | Cell-2 | `from aurora.audio.io import sine, chirp`，`sine` 未使用 |
| L53 | Cell-7 | markdown 说「能量保留率应 > 95%」，cell-8 只打印不断言 |
| L53 | Cell-9 | 总结说「pipeline 包含 `power_to_db`」，代码实际用 `10 * np.log10(...)` 内联，从未调用 `power_to_db` |
| L56 | H1 | 含双语括号注释，与官方标题不完全一致 |
| L56 | Cell-10 | 死代码绑定行：`Value.backward = types.MethodType.__func__.__get__ if False else lambda...`，且 True 分支会 AttributeError |
| L57 | Cell-15 | 引用旧文件名 `a5_train.ipynb`，应为 `L58_training_loop.ipynb` |
| L59 | Cell-2 | `from aurora.audio.mfcc import mfcc` 未使用 |
| L60 | Cell-14 | 「吴合」是「吻合」的错别字 |
| L62 | Cells cell-11/13 | 重复 `import tempfile, soundfile as sf`；且 `delete=False` 临时文件未清理 |
| L63 | Cell-14 | 下一课预告遗漏混淆矩阵和过拟合诊断（L64 两个核心主题），使用「M2-K3」内部标签 |
| L64 | Cell-11/14 | 验证 cell 无 try/except 保护，学生未实现 TODO 时直接 NotImplementedError 崩溃 |
| L65 | H1 cell-0 | 含大量双语括号注释，与官方标题不完全一致 |
| L65 | Cell-9/11 | 两个「本课收束」section，结构重复 |
| L66 | Cell-9 | 编辑距离例子描述「交换」（swap），Levenshtein 基本操作中不含 swap |
| L67 | H1 cell-0 | 含「（dynamic programming，DP）」注释，与官方标题不完全一致 |
| L67 | Cells cell-3/4 和 cell-6/7 | 标 ✏️ 任务但紧接着的代码 cell 已有完整实现，无空白可填 |
| L68 | Cell-11 | 无条件打印「✅」即使 result 为 None，误导学生 |
| L68 | Cell-1 | 「单调路径」出现在标题但 notebook 正文从未定义或演示 |
| L69 | H1 cell-0 | 含双重括号注释，与官方标题不完全一致 |
| L70 | Cell-6 | `tuple(torch.zeros(1,80,3000).shape)` 总打印 (1,80,3000)，隐藏 conv1 中间形状 |
| L71 | Cell-7 | beam search 无验证/断言 cell |
| L72 | H1 | 含「（fine-tuning）」注释，与官方标题不完全一致 |
| L73 | Cell-14 | 下一课预告描述「数据增强策略」，实际 L74 是「S/D/I 错误模式分析」 |
| L74 | Cell-8 | 下一课说「可视化仪表板」，L75 实际是「波形→声谱图→token→文字路径可视化」 |
| L74 | Cell-2 | `alignment()` 不小写输入，`wer()` 小写输入，潜在大小写敏感不一致 |
| L75 | Cell-9 | 下一课描述 L76 为「音阶、和弦、调性」，实际 L76 是「音高、音程、色度轮、十二平均律」 |
| L76 | H1 | 含「（chroma）」「（chroma wheel）」注释，与官方标题不完全一致 |
| L76 | Cell 7 | `plt.savefig('Path.cwd() / chroma_wheel.png')` 使用 cwd() 相对路径 |
| L77 | Cell 2 | `from aurora.audio.stft import stft` 未使用 |
| L78 | Cell-9 | 下一课描述 L79 为「基于聚类的嵌入检索」，实际 L79 是「对比学习」 |
| L79 | H1 | 含「（embedding）」「（contrastive learning）」注释 |
| L79 | Cell-14 | 使用废弃标签「M4-MU3」而非「L80」 |
| L80 | H1 cell-0 | 含「（cosine similarity）」注释，与官方标题不完全一致 |
| L80 | Cell-14 | 使用废弃标签「MU4」而非「L81」 |
| L81 | H1 | 含「（embedding）」注释，与官方标题不完全一致 |
| L82 | Cell 9 | 下一课预告只有「**L83**。」，无任何描述内容 |
| L83 | Cells cell-12/cell-14 | 两个 section 均标「## 5.」，编号重复 |
| L83 | Cell-9 | `<details>` 暴露完整 `scaled_dot_product_attention` 实现（Minor 层面的解答泄漏） |
| L85 | Cell-6 | `KVCache(n_heads=4, head_dim=64)` 与测试数据 `n_heads=2, d=8` 不匹配 |
| L85 | Cell-6 | 验证 cell 无任何数值断言，仅打印「✅」 |
| L87 | Cell-4 | bits-vs-error 循环使用简化 offset 公式（无 zero_point），与 `quantize_int8` 的 zero_point 公式不一致，未说明等价性 |
| L87 | Cell-7 | 汇总表称 L88 为「RAG 检索」，实际 L88 是「TF-IDF 检索从零实现」，混淆子组件与完整系统 |
| L88 | Cell-10 | 打印「✅ TF-IDF 检索验证通过」但无数值 assert，错误实现也会通过 |
| L89 | H1 cell-0 | 含「（Document Chunking）」「（Prompt）」注释，与官方标题不完全一致 |
| L90 | Cell-14 | 下一课预告「下一课：L91」无任何描述 |
| L92 | Cell a58a8e3a | ASCII 时序图声称并行路径 2500ms，代码实际含第二个 RAG refine 步骤，总计约 2530ms |
| L92 | Cell-4 | `plt.savefig('pipeline_latency.png')` 相对路径不稳定 |
| L93 | Cell id=99df8103 | `int(0.95 * 20) = 19`，取的是最大值（p100），不是 p95 |
| L93 | Cell id=99df8103 | CI YAML 中 `make test -- --json-report` 语法无效，额外参数会被 Make 忽略 |
| L94 | H1 cell-0 | 含「（evidence chain）」注释，与官方标题不完全一致 |
| L94 | Cell 869c557c | 能力矩阵中多个模块路径不存在（如 aurora.asr、aurora.music.embed 等），打印「待实现」但暗示是完成交付物 |
| L95 | Cell 561b2e49 | Section「5. 与学术机构合作」编号重复（已有另一个 section 5） |
| L96 | Cell fe96cd55 | CTC 问题用 1-indexed（α₁(1)），答案代码用 0-indexed（alpha[0][0]），无过渡注释 |
| L97 | Cell 285c2b52 | 两个「## 4.」section（「系统设计题」和「模拟面试练习」）编号重复 |
| L97 | Cell e3f1d2d0 | 下一课预告描述「Aurora v2 的方向」，L98 官方标题无此内容 |
| L98 | Section headers | 编号跳跃（1, 2, 2b, 3, 4b, 5, 6b），4 和 6 缺失 |
| L98 | Cell ee6da094 | 下一课预告称 L99「Aurora v2 与持续成长路线图」，与官方标题不符 |

---

## 五、特殊问题

### 5A — 无法继续的课（can_proceed = false）

以下 67 门课存在阻塞性问题，**不得在修复前发布给学生**：

```
L01  L02  L03  L05  L07  L09  L12  L14  L15  L17  L18  L22  L23  L24
L25  L26  L27  L28  L32  L33  L34  L35  L36  L37  L39  L40  L41  L42
L43  L44  L45  L46  L47  L49  L50  L53  L55  L56  L58  L59  L60  L61
L62  L64  L65  L68  L70  L71  L72  L73  L75  L76  L77  L78  L79  L80
L81  L82  L83  L84  L85  L86  L89  L90  L91  L95  L97
```

---

### 5B — 标题与 README 不符（28 处）

| 课号 | 实际 H1（节选） | README 官方标题（节选） |
|------|-----------------|------------------------|
| L01 | Aurora 是什么——从正弦波到 Whisper | 环境配置 — conda/venv、Jupyter 内核选择 |
| L02 | 声音的数字表示——采样、数组 | NumPy 速成 — 数组、dtype、广播与切片 |
| L03 | 谱图（spectrogram）直觉 | 全课程地图 — 从正弦波到 Transformer |
| L04 | 正弦波三要素（缺「亲手实现」） | 正弦波三要素 — … 亲手实现 |
| L05 | 复数几何本质——频谱分析语境版 | 复数几何本质 — 实部虚部 → 极坐标，复数乘法 = 旋转 + 缩放 |
| L09 | 向量（vector）代数 … | 向量代数 — … |
| L11 | 向量（vector）范数 | 向量范数 — … |
| L26 | 微积分可视化（含大量双语注释） | 微积分可视化 — 切线、等高线与梯度下降轨迹动态演示 |
| L29 | 常见概率分布（含「正态（Gaussian）」） | 常见概率分布 — 均匀、高斯、伯努利 |
| L34 | Nyquist 定理与混叠（aliasing） | Nyquist 定理与混叠 |
| L41 | 加窗（windowing）FFT … 幅度谱（magnitude spectrum） | 加窗 FFT … 幅度谱 |
| L55 | 前向传播算子扩展（__pow__、relu、tanh） | 前向传播拆解 — 矩阵乘 + 偏置 + 激活函数，逐层打印输出形状 |
| L56 | 反向传播（backpropagation）手推 … | 反向传播手推 — … |
| L67 | Edit Distance … 动态规划（dynamic programming，DP） | Edit Distance … 动态规划 |
| L69 | CTC（Connectionist Temporal Classification，CTC）前向算法（forward algorithm） | CTC 前向算法 — … |
| L72 | Whisper 微调（fine-tuning） | Whisper 微调 — … |
| L76 | 音乐理论速成 — … 色度（chroma）轮（chroma wheel） | 音乐理论速成 — … 色度轮 |
| L79 | 音乐嵌入向量（embedding） — 对比学习（contrastive learning） | 音乐嵌入向量 — 对比学习 |
| L80 | 向量相似度检索 — 余弦相似度（cosine similarity） | 向量相似度检索 — 余弦相似度 |
| L81 | 音乐推荐系统 — … 嵌入向量（embedding） | 音乐推荐系统 — … 嵌入向量 |
| L82 | L82 🎨 音乐特征可视化 — 色度（chroma）图 | 音乐特征可视化 — 色度图 |
| L89 | RAG … 文档切片（Document Chunking）+ … 提示词（Prompt） | RAG … 文档切片 + … 提示词 |
| **L90** | **对话式 RAG — 会话记忆、Podcast Q&A** | **Tool-calling Agent — 工具定义、函数调用解析、多步推理循环** |
| **L95** | **研究论文入门——阅读、写作、投稿与学术合作** | **论文精读 — Whisper、MusicGen、VALL-E 三遍法** |
| L96 | 白板推导演练——FFT/CTC/注意力机制 | 白板演练 — DFT/FFT/注意力机制口述推导，面试现场模拟 |
| L97 | 面试准备与技术沟通——如何讲清你做的每一件事 | 面试材料整理 — 30 秒 elevator pitch、GitHub 证据链、简历技术点对照 |
| L98 | 课程总结——做到了什么，还差什么 | 复盘 — 6 个月里程碑回顾，方法论总结，成长曲线量化 |
| L99 | Aurora v2 与持续成长——6 个月之后怎么走 | 下一步 — 进阶路线规划：研究方向、开源贡献、下一个里程碑 |

---

### 5C — 答案提前暴露（Solution Leaks，68 课次）

**模式 A：`<details><summary>点击查看参考实现</summary>` 折叠块**（最普遍，约 50 处）
出现于：L04, L05, L06, L07, L09, L10, L11, L12, L13, L14, L15, L16, L17, L18, L22, L23, L24, L25, L27, L28, L29, L30, L32, L33, L34, L35, L36, L37, L38, L39, L40, L41, L43, L44, L45, L46, L47, L49, L50, L54, L55, L56, L58, L59, L60, L61, L62, L63, L64, L66, L68, L70, L73, L79, L80, L81, L83, L84, L90

折叠块统一位于 TODO cell **正上方**，折叠块在 JupyterLab 渲染后一键可见。

**模式 B：TODO 注释后直接给出完整实现（同 cell 内）**（约 18 处）
出现于：L69（alpha 初始条件+递推）、L71（greedy_decode + beam_search）、L76（三个函数体）、L78（onset_envelope + autocorrelation）、L85（scaled_dot_product + KVCache.update）、L86（top_k_sample + top_p_sample）、L88（tokenize + build_tfidf + cosine_retrieve）、L89（chunk_text + format_rag_prompt）

**统一修复原则：**
- 模式 A：将 `<details>` 块移到验证 cell 之后，或移到独立的 solutions notebook。
- 模式 B：将实现代码替换为 `raise NotImplementedError("TODO")` 或 `pass`。

---

### 5D — 下一课预告不准确（59 处）

以下是错误预告中最严重的 15 个（涉及完全错误的课号或主题）：

| 课号 | 预告说 | 实际下一课 |
|------|--------|------------|
| L02 | L03 谱图直觉 | L03 全课程地图 |
| L25 | L26 链式法则 | L26 微积分可视化 |
| L28 | L29 softmax 和交叉熵 | L29 常见概率分布 |
| L34 | L35 汉宁窗 | L35 欧拉公式与 FFT 旋转因子 |
| L39 | L42/L43 STFT | L40 频谱分析实战 |
| L40 | L46 Mel 滤波器组 | L41 加窗 FFT 完整流程 |
| L41 | L43 STFT | L42 FFT 图形化 |
| L44 | L46 Mel | L45 声谱图生成 |
| L58 | L60 DataLoader/mini-batch（标签用「a6」） | L59 PyTorch Tensor 基础 |
| L59 | L60 nn.Module + Conv2d | L60 autograd 机制 |
| L64 | L65 推理/延迟指标 | L65 训练可视化 |
| L65 | L66 KeywordCNN 训练循环 | L66 ASR 系统全览 |
| L68 | L69 Whisper 架构 | L69 CTC 前向算法 |
| L70 | L71 cross-attention 可视化 | L71 贪婪解码与 beam search |
| L79 | L82 音乐特征可视化 | L80 向量相似度检索 |

---

## 六、交叉规律（Cross-cutting Patterns）

### 规律 1：`<details>` 解答泄漏（≥50 门课）

整个课程从 L04 到 L90 存在系统性的解答泄漏模式：每个 TODO 练习 cell 之前都有一个 `<details><summary>点击查看参考实现</summary>` 折叠块，内含完整可运行代码。这显然是批量复制 cell 模板时引入的，未在发布前清理。

**根因**：notebook 模板中包含参考实现，面向学生发布时未执行「清理解答」步骤。

**系统修复**：编写脚本扫描所有 notebook，找出所有 `<details>` 块，将其自动提取到同目录的 `solutions/` 子文件夹，原位置替换为提示性 hint。

---

### 规律 2：`aviz` 不存在依赖（L32, L33, L34, L35, L36）

5 门连续的 Audio DSP 课（L32–L36）均导入 `aviz` 模块，该模块不在任何标准包仓库也不在项目依赖中。这批课无法运行到对应 cell，是同一时期编写时引入的虚构依赖。

**系统修复**：在 Module 5 所有 notebook 中全局搜索 `import aviz`，用纯 `matplotlib` + `aurora` API 替代，或将 aviz 代码实现并发布。

---

### 规律 3：废弃的 p-编号和 week/month 路径（L08, L20, L38, L57, L58, L65, L94）

多门课仍引用已删除的旧目录结构（`week01/`、`month02/`、`month03/`、`month05/`）或旧的 `p6`/`p7`/`p9`/`a6`/`M2-K3` 内部编号，这些在 commit cc43b29（重命名为 L01–L94）后全部失效。

**系统修复**：全局 grep `week0[0-9]/`、`month0[0-9]/`、`p[0-9]_`、`a[0-9]_`、`M[0-9]-`，批量替换为对应 L 编号。

---

### 规律 4：下一课预告系统性错误（59 门课）

约 60% 的课程在「本课收束」section 中预告了错误的下一课内容，最常见的错误类型：
1. **跳号**（如 L40 指向 L46，L79 指向 L82）
2. **主题描述属于更远的课**（如 L58 描述 L60 的内容）
3. **旧内部标签未更新**（如「M2-A4」、「p4_training_loop」）

**根因**：课程内容在重命名/重排序后，各 notebook 的收束 section 未同步更新。

**系统修复**：建立课程序列映射表（L01→L02→…→L99），对每门课验证「下一课 Lnn」标注是否与映射表一致。

---

### 规律 5：`laviz` 不存在依赖（L09, L14, L17, L18, L19）

线性代数模块（Module 2）多门课导入 `laviz` 包（style, arrows2d, mat_times_mat_rank1, show_factorization, heatmap），该包未在 `pyproject.toml` 中声明，在项目环境中不存在。

**系统修复**：确认 laviz 是否为内部工具；如是，补充安装文档；如否，用 matplotlib 替代所有 laviz 可视化调用。

---

### 规律 6：TODO 桩返回 None 导致后续断言崩溃（L12, L44, L80）

三处 TODO 桩（matvec、windowed 帧化、find_similar）在返回 None 后被立即以不安全方式使用（`np.allclose(None, ...)` 或 `for f in None:` 或直接解包），导致 TypeError 而非有意义的 AssertionError。

**系统修复**：所有 TODO 桩改为 `raise NotImplementedError` 或在验证 cell 首行加 `if result is None: print("TODO 未完成"); raise SystemExit()`。

---

### 规律 7：伪 TODO（TODO 注释后立即给出完整实现，约 18 门课）

L69、L71、L76、L78、L85、L86、L88、L89 等 Module 7-9 课程中，`# ✏️ TODO:` 注释后的同一 cell 内立即跟随完整的实现代码，学生完全没有空白可填写。这比 `<details>` 折叠块更直接，是更严重的教学设计缺陷。

**根因**：可能是先写完整实现，再补加 TODO 注释时忘记删除实现体。

**系统修复**：扫描所有含 `# ✏️ TODO` 的 code cell，检查 TODO 注释之后是否存在非桩实现，自动替换为 `pass`。

---

## 七、无问题课程

> 本次审计中，**无任何课程达到零问题标准**（clean_lesson_count = 0）。

所有 99 门课均发现至少 1 处问题。问题最少的课程为 L52（1 处 major）、L57（1 处 minor）、L99（1 处 major）。

---

## 八、每课简况

| 课号 | 问题数 | 可继续 | 一句话摘要 |
|------|--------|--------|------------|
| L01 | 3 | ✗ | 标题与 README 不符（动机 vs 环境配置），下一课预告错误，Path 未导入 |
| L02 | 3 | ✗ | 三处 Critical：标题不符、下一课预告错误、max_abs 断言容差过严 |
| L03 | 2 | ✗ | 内容（谱图直觉）占据了本应是「课程地图」的 L03 槽位 |
| L04 | 3 | ✓ | 解答泄漏 + 标题略有差异 + 下一课预告不完整 |
| L05 | 4 | ✗ | 核心主题「复数乘法=旋转+缩放」完全缺失 + 解答泄漏 |
| L06 | 3 | ✓ | 解答泄漏 + 下一课预告错误（DFT 分解 vs 正弦叠加） |
| L07 | 4 | ✗ | 解答泄漏 + 下一课预告工具名（xviz vs matplotlib）和主题双错 |
| L08 | 5 | ✓ | 两处过期路径（week01/euler 和 aurora/audio/fft.py）需更新 |
| L09 | 3 | ✗ | laviz ModuleNotFoundError（Critical）+ 解答泄漏 |
| L10 | 3 | ✓ | 解答泄漏 + 两个游离矩阵 cell + None 保护缺失 |
| L11 | 4 | ✓ | 解答泄漏 + laviz 未声明 + 验证 cell TypeError |
| L12 | 3 | ✗ | 桩返回 None 导致 TypeError 崩溃 + 解答泄漏 |
| L13 | 3 | ✓ | 解答泄漏 + 缺 numpy import + 下一课预告遗漏 SVD |
| L14 | 5 | ✗ | laviz ModuleNotFoundError + 两处解答泄漏 + 双重「## 2.」 |
| L15 | 3 | ✗ | 「正定」术语错误（应为「恰定」）+ 解答泄漏 |
| L16 | 3 | ✓ | 解答泄漏 + laviz 未声明 + 下一课预告描述错误焦点 |
| L17 | 6 | ✗ | 两处变量覆盖崩溃 + 解答泄漏 + section 标题与代码不符 |
| L18 | 4 | ✗ | 解答泄漏 + Jacobi 实验有描述无代码 + laviz 未声明 |
| L19 | 2 | ✓ | 下一课预告不完整 + 小检查 cell 只打印不断言 |
| L20 | 2 | ✓ | 5 处废弃 p-编号 + 下一课预告描述错误主题 |
| L21 | 2 | ✓ | 未使用变量 k + MFCC 流水线跳过 Mel 步骤未明显标注 |
| L22 | 5 | ✗ | 解答泄漏 + 两组 markdown/代码不符 + 重复 cell |
| L23 | 3 | ✗ | 解答泄漏 + 验证点描述（[1,2]）与实际代码（[3,4]）不符 |
| L24 | 3 | ✗ | 解答泄漏 + sin(x²) 描述但代码用 x² |
| L25 | 3 | ✗ | 解答泄漏 + 下一课预告指向已学过的「链式法则」 |
| L26 | 4 | ✗ | Critical：凸函数被描述为有鞍点 + 代码/说明顺序颠倒 |
| L27 | 3 | ✗ | 解答泄漏 + seed 42/7 不一致 + 重复 cell |
| L28 | 2 | ✗ | 解答泄漏 + 下一课预告（softmax vs 概率分布）错误 |
| L29 | 2 | ✓ | 双 H1 cell + 解答泄漏 |
| L30 | 4 | ✓ | 两处解答泄漏 + 重复 section 编号 + 重复 cell |
| L31 | 2 | ✓ | 下一课预告（FFT vs NumPy 信号基础）+ 重复 softmax 定义 |
| L32 | 3 | ✗ | Critical：aurora+aviz 双重 ImportError（保存输出已报错）+ 解答泄漏 |
| L33 | 3 | ✗ | aviz ModuleNotFoundError + 解答泄漏 + 精度说明/断言不一致 |
| L34 | 5 | ✗ | 解答泄漏 + 下一课预告（窗函数 vs 欧拉公式）错误 + aviz + 重复 cell |
| L35 | 3 | ✗ | aviz ModuleNotFoundError + 两处解答泄漏 + 重复 cell |
| L36 | 4 | ✗ | 5 个 aviz cell 崩溃 + 实验描述与代码完全不符 + 解答泄漏 |
| L37 | 2 | ✗ | 解答泄漏 + 交叉引用「L39」应为「L38」 |
| L38 | 3 | ✓ | 解答泄漏 + 下一课预告（迭代 vs 递归 FFT）错误 |
| L39 | 5 | ✗ | 解答泄漏 + 两处下一课预告错误（L42/L43 vs L40）|
| L40 | 3 | ✗ | 解答泄漏 + 下一课预告（L46 vs L41）错误 |
| L41 | 3 | ✗ | 解答泄漏 + 下一课预告（L43 STFT vs L42 FFT 图形化）错误 |
| L42 | 3 | ✗ | markdown 参数与代码不符 + 标题承诺和弦/噪声但缺失 |
| L43 | 4 | ✗ | 解答泄漏 + 帧数预测严重偏差（7 vs 实际 4）|
| L44 | 3 | ✗ | None 迭代崩溃 + 解答泄漏 + 下一课预告（L46 vs L45）|
| L45 | 5 | ✗ | 解答泄漏 + eps 不一致 + dB 公式不一致 + 标题含 pcolormesh 但从未使用 |
| L46 | 3 | ✗ | Critical：hz_to_mel 断言值错误（782.7 vs 781.17）+ 解答泄漏 |
| L47 | 2 | ✗ | 矩阵乘顺序错误（形状错误）+ 解答泄漏 |
| L48 | 3 | ✓ | 形状注释错误 + 未使用 stft import + 下一课预告描述不精确 |
| L49 | 4 | ✗ | Critical：IDCT 数学错误 + 解答泄漏 + M@M.T/N 说「2 倍单位阵」实为 1/2 |
| L50 | 4 | ✗ | k=0 图/代码矛盾（说保留但图标「跳过」）+ 解答泄漏 |
| L51 | 2 | ✓ | 下一课预告（DTW 分类器 vs Audio Core 收口）+ 无操作死代码 |
| L52 | 1 | ✓ | 下一课预告（L54 训练 vs L53 MFCC 可视化）|
| L53 | 4 | ✗ | 承诺四层可视化但只实现后两层（波形和声谱图缺失）|
| L54 | 2 | ✓ | 解答泄漏 + 下一课预告（MLP vs 前向传播形状打印）|
| L55 | 2 | ✗ | Critical：内容错误（算子扩展 vs 矩阵级前向传播）+ 解答泄漏 |
| L56 | 4 | ✗ | 解答泄漏 + retain_graph 完全未涉及（违反标题承诺）|
| L57 | 1 | ✓ | 旧文件名引用（a5_train.ipynb → L58） |
| L58 | 2 | ✗ | 解答泄漏 + 下一课预告（DataLoader/a6 vs PyTorch Tensor 基础）|
| L59 | 3 | ✗ | 解答泄漏 + 下一课预告（Conv2d vs autograd）+ 未使用 mfcc import |
| L60 | 3 | ✗ | 解答泄漏 + retain_graph 完全缺失（标题承诺）+ 错别字「吴合」|
| L61 | 2 | ✗ | 解答泄漏 + 下一课预告（training loop vs Dataset/DataLoader）|
| L62 | 4 | ✗ | 解答泄漏 + 下一课预告错误 + 标题承诺 __getitem__/DataLoader 但从未实现 |
| L63 | 2 | ✓ | 解答泄漏 + 下一课预告不完整 |
| L64 | 4 | ✗ | Critical 下一课预告（推理 vs 训练可视化）+ 两处解答泄漏 |
| L65 | 4 | ✗ | 两处下一课预告均错（KeywordCNN vs ASR 系统全览）+ 重复收束 section |
| L66 | 2 | ✓ | 解答泄漏 + 例子用词「交换」不精确 |
| L67 | 3 | ✓ | Whisper 错误归因 CTC + 伪 TODO（任务含完整实现）|
| L68 | 4 | ✗ | 解答泄漏 + 下一课预告（Whisper 架构 vs CTC 前向）|
| L69 | 3 | ✓ | 伪 TODO + 公式域（log vs probability space）标注矛盾 |
| L70 | 4 | ✗ | 750 vs 1500 encoder steps 错误 + 解答泄漏 + 下一课预告错误 |
| L71 | 3 | ✗ | 伪 TODO + O(T) vs O(T×V) 矛盾 + beam search 无验证 |
| L72 | 3 | ✗ | Critical：split 名错误（train.100 vs train.clean.100）+ 下一课预告错误 |
| L73 | 2 | ✗ | 解答泄漏 + 下一课预告（数据增强 vs 错误模式分析）|
| L74 | 2 | ✓ | 下一课预告不精确 + alignment() 无大小写归一化 |
| L75 | 2 | ✗ | `import torch` 未使用但阻塞执行 + 下一课预告（音阶和弦 vs 色度轮十二律）|
| L76 | 3 | ✗ | 三个 TODO 均已预填完整实现（伪 TODO）|
| L77 | 5 | ✗ | ZCR 承诺但完全缺失 + 两处解答泄漏 + 下一课预告错误 |
| L78 | 3 | ✗ | 两处伪 TODO + 下一课预告（聚类 vs 对比学习）|
| L79 | 4 | ✗ | 解答泄漏 + 下一课预告（L82 vs L80）错误 |
| L80 | 4 | ✗ | Critical：None 解包崩溃 + 解答泄漏 |
| L81 | 3 | ✗ | 解答泄漏 + 下一课预告（评估指标 vs 可视化）|
| L82 | 3 | ✗ | Critical：节拍图和热力图完全缺失 + 下一课预告空白 |
| L83 | 4 | ✗ | 下一课预告（MHA vs LoRA）错误 + 引用不存在的「L2」|
| L84 | 2 | ✗ | 解答泄漏 + 下一课预告（LoRA 注入 vs KV-Cache）|
| L85 | 4 | ✗ | 两处伪 TODO + KVCache 构造参数与测试数据不匹配 + 验证 cell 无断言 |
| L86 | 2 | ✗ | 两处伪 TODO |
| L87 | 2 | ✓ | dequantization 公式不一致 + 汇总表标签混淆 |
| L88 | 3 | ✓ | 三处伪 TODO + 验证 cell 无数值断言 |
| L89 | 3 | ✗ | Critical：验证 cell 在定义前执行 NameError + 两处伪 TODO |
| L90 | 3 | ✗ | Critical：内容完全错误（对话 RAG vs Tool-calling Agent）+ 解答泄漏 |
| L91 | 3 | ✗ | Critical：LoRA 矩阵形状标注错误 + 单头 vs 多头不符 + 无下一课预告 |
| L92 | 3 | ✓ | 下一课预告（「持续集成」vs MLOps 基础）+ 时序图数值误差 |
| L93 | 3 | ✓ | 下一课预告（「课程回顾」vs Aurora Demo）+ p95 计算错误 |
| L94 | 3 | ✓ | Demo 表格中旧路径（week01/month03/month05）+ 标题双语注释 |
| L95 | 3 | ✗ | Critical：内容完全错误（通用学术入门 vs 三篇论文精读）+ 下一课预告错误 |
| L96 | 3 | ✓ | 标题缺 DFT 多 CTC + 下一课预告（30分钟 vs 30秒，主题不符）|
| L97 | 4 | ✗ | Critical：frame_signal 断言期望 (3,8) 实应为 (4,8) + 标题与 README 不符 |
| L98 | 3 | ✓ | 标题不符 + 下一课预告主题不符 + section 编号跳跃 |
| L99 | 1 | ✓ | 标题与 README 不符（Aurora v2 vs 进阶路线规划）|

---

## 九、修复优先级排序

以下 15 项修复按影响学生数量和严重程度排列，应**优先处理**：

1. **全局清理 `<details>` 解答泄漏**（影响 ≥50 门课）
   编写脚本扫描所有 notebook，将 `<details>` 内实现代码移到同目录 `solutions/` 文件夹，原位替换为简短概念提示。这一步骤影响课程中超过一半的练习，是最高优先级。

2. **全局修复「伪 TODO」**（影响 L69, L71, L76, L78, L85, L86, L88, L89 等 ≥18 处）
   扫描所有含 `# ✏️ TODO` 的 code cell，检测其下是否有非桩实现代码，自动替换为 `raise NotImplementedError("TODO")`。

3. **aviz 依赖问题**（影响 L32, L33, L34, L35, L36 五门课）
   决策：实现并发布 aviz，或用 matplotlib 替代。这五门课是 Audio DSP 核心序列，无法运行。

4. **laviz 依赖问题**（影响 L09, L14, L17, L18，含 Critical 级问题）
   同上，在 pyproject.toml 添加依赖或用 matplotlib 替代。

5. **L46 hz_to_mel 断言参考值错误**（Critical）
   `782.7 → 781.2`，三处同步修改（assert、expected output、prose 文本）。影响所有实现正确但会被误判失败的学生。

6. **L97 frame_signal 断言期望值错误**（Critical）
   `(3,8) → (4,8)`，一行修改，但在 interview 准备课中出错影响极大。

7. **L26 鞍点概念错误**（Critical）
   f(x,y)=x²+2y² 是严格凸函数，无鞍点。修改函数或删除所有「鞍点」引用，防止核心概念误导。

8. **L49 IDCT 数学错误**（Critical）
   `_idct_ii_ref` 使用非归一化逆变换但输入是正归一化 DCT 输出，重建误差应 ≈ 0 但实际极大。需重写该函数。

9. **L91 LoRA 矩阵形状标注**（Critical）
   A(d×r) B(r×d) → A(r×d) B(d×r)，两处修改，防止学生学到错误的 LoRA 实现规范。

10. **L17 变量覆盖崩溃**（两处 Critical）
    在两个 cell 顶部重新赋值 `A = np.array([[3,3,3],[3,-1,1],[3,1,-1]], float)`，防止所有验证断言失败。

11. **L72 HuggingFace split 名错误**（Critical）
    `'train.100'/'test' → 'train.clean.100'/'test.clean'`，防止 notebook 无法加载数据集。

12. **L44 None 迭代崩溃**（Critical）
    `for f in windowed:` → `if windowed is not None: for f in windowed:`，让错误提示清晰而非崩溃。

13. **L80 None 解包崩溃**（Critical）
    Cell-13 加 None 保护，与 Cell-11 保持一致。

14. **全局更新下一课预告**（影响 59 门课）
    建立 L01→L99 序列表，批量检查和更新所有「本课收束」section 中的「下一课 Lnn」标注。

15. **L55/L90/L95 内容与课题完全不符**（三处 Critical）
    - L55：重写为矩阵级前向传播或更新 README
    - L90：重写为工具调用 Agent 或重新排列课程
    - L95：重写为三篇论文精读或更新 README

---

*本报告由 Claude Code 自动生成，覆盖 99 个 notebook 的 8 项检查维度。审计日期：2026-06-28。*

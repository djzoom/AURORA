# Aurora 课程全库审计报告（历史快照，合并版）
> 这是 2026-06-28 的合并审计快照，保留用于追溯。当前口径请看 `/Users/z/AURORA/docs/README.md` 或最新评审集。

**日期：2026-06-28 · 覆盖范围：L01–L99（99 个 notebook）+ 全部文档 + src/**

---

## 一、全库数字总览

| 指标 | 数值 |
|---|---|
| Notebook 总数 | 99（L01–L99，无缺号，L95–L99 均为实际内容，非空占位） |
| Cell 总数 | 1787 |
| 代码 Cell | 738 |
| Markdown Cell | 1049 |
| ✏️ TODO 标记 | 101 |
| Stub 函数（return None / pass） | 33 处（均为设计意图的学生练习桩） |
| 验证 Cell（含 assert/✅/⬜） | 163 |
| 英文括注（bilingual annotations） | 795（本次审计前 ~571，已补全到 795） |

---

## 二、模块结构概览

```
0_foundation      L01–L03    3 nb   avg 20 cells/nb   TODOs/nb 2.7
1_complex_trig    L04–L08    5 nb   avg 23 cells/nb   TODOs/nb 0.8
2_linear_algebra  L09–L21   13 nb   avg 26 cells/nb   TODOs/nb 0.8
3_calculus        L22–L26    5 nb   avg 23 cells/nb   TODOs/nb 0.8
4_probability     L27–L31    5 nb   avg 24 cells/nb   TODOs/nb 1.0
5_audio_dsp       L32–L53   22 nb   avg 18 cells/nb   TODOs/nb 1.2
6_deep_learning   L54–L65   12 nb   avg 15 cells/nb   TODOs/nb 1.0
7_asr             L66–L75   10 nb   avg 12 cells/nb   TODOs/nb 0.6
8_music           L76–L82    7 nb   avg 14 cells/nb   TODOs/nb 1.6
9_llm             L83–L91    9 nb   avg 12 cells/nb   TODOs/nb 1.6
10_integration    L92–L99    8 nb   avg 18 cells/nb   TODOs/nb 0.1
```

---

## 三、问题汇总（合并自双轨审计）

### 3A — 代码级 Bug（P0，影响可运行性）

| # | 文件 | 位置 | 问题 | 状态 |
|---|------|------|------|------|
| P0-1 | `L40_spectrum.ipynb` | cell[8], cell[13] | `sine(440, sr, duration)` 参数顺序错误，应为 `sine(440, duration, sr)`；所有频谱图产生垃圾输出 | ✅ 已修复 |
| P0-2 | `L50_mfcc.ipynb` | cell[3][7][9][10][14] | 教学内容用 `coeffs[:, 1:n_mfcc+1]`（跳过 k=0），但 `aurora.mfcc()` 返回 `[:, :n_mfcc]`；断言永远失败 | ✅ 已修复 |
| P0-3 | `L92_pipeline.ipynb` | cell[10] line 20 | f-string 内嵌双引号 SyntaxError；`async_llm()` 无法编译 | ✅ 已修复 |
| P0-4 | `L92_pipeline.ipynb` | cell[10] lines 40–41 | `asyncio.run()` 在 Jupyter event loop 中抛 RuntimeError | ✅ 已修复 |
| P0-5 | `L68_ctc_alignment.ipynb` | cell[11] | `assert ..., msg1, msg2` 多余第二个 f-string → SyntaxError | ✅ 已修复 |
| P0-6 | `L07_fourier_intuition.ipynb` | cell[15] | 方波幅度公式 `4/(π·k)` 适用于归一化方波，但实现用的是未归一化版本（峰值 ≈ π/4 而非 1）；预测值与实际 FFT 峰不符 | ✅ 已修复 |
| P0-7 | `L08_visual_complex.ipynb` | cell[20], cell[22] | 单位根公式写成 `W_N^k = e^{+i2πk/N}`（正号），与实现 `xviz.roots_of_unity()` 的负号约定矛盾 | ✅ 已修复 |
| P0-8 | `L25_gradient_descent.ipynb` | cell[3], cell[18] | 错误声称 lr=0.9 不收敛（"数列不收敛"）；实际上 lr<1 均收敛（仅振荡），lr≥1 才发散 | ✅ 已修复 |
| P0-9 | `src/aurora/music/features.py` | line 30 | `np.fft.rfftfreq()` 违反 Audio Core 策略；已有 `fft_frequencies()` 可替代 | ✅ 已修复 |

### 3B — 内容错误（P1）

| # | 文件 | 问题 | 状态 |
|---|------|------|------|
| P1-1 | `L03_spectrogram.ipynb` | 线性扫频公式错误，`sweep = sin(2π(f0+(f1-f0)t/T)t)` 使瞬时频率翻倍；应用积分形式 | ✅ 已修复 |
| P1-2 | `L17_eigen_diagonalization.ipynb` | `char_poly(A,5) ≈ -384`，正确值为 +56 | ✅ 已修复 |
| P1-3 | `L22_derivatives.ipynb` | 参数实验 cell 包含梯度下降模板代码（x²），与导数/数值微分主题不符 | ✅ 已修复 |
| P1-4 | `L23_gradients.ipynb` | 参数实验 cell 包含错误的 GD loop 代码 | ✅ 已修复 |
| P1-5 | `L24_chain_rule.ipynb` | 参数实验 cell 包含 GD loop 而非链式法则实验 | ✅ 已修复 |
| P1-6 | `L25_gradient_descent.ipynb` | cell[17/19] 用 `f(x)=(x-2)²+1`，整节课基于 `(x-3)²` | ✅ 已修复 |
| P1-7 | `L26_visual_calculus.ipynb` | 参数实验 cell 包含 GD loop 而非 `contour_descent` 调用 | ✅ 已修复 |
| P1-8 | `L27-L31`（全模块） | Bayes 定理 + Shannon 熵缺失 | ✅ L27 Bayes 已补充；✅ L30 Shannon 熵 + H(p,q)=H(p)+KL 推导 + 数值验证 |
| P1-9 | `L27_probability_basics.ipynb` | 标题承诺条件概率+独立性，但主体仅有 LLN 掷骰子 | ✅ 已修复 |
| P1-10 | `L29_distributions.ipynb` | 标题承诺伯努利分布，但 Bernoulli 完全缺失；CDF 无独立章节 | ✅ 已修复 |
| P1-11 | `L30_softmax_crossentropy.ipynb` | 标题承诺"手推梯度"，但 `dL/dz_i = p_i − y_i` 的推导从未出现 | ✅ 已修复（含数值验证） |
| P1-12 | `L41_fft_full.ipynb` | Hann 窗公式用对称型（N-1 分母），aurora 实现用周期型（N 分母）；"两端值为 0"不对 | ✅ 已修复 |
| P1-13 | `L48_visual_stft.ipynb` | 输出形状描述颠倒：应为 `(n_frames, n_fft//2+1)` 和 `(n_frames, n_mels)` | ✅ 已修复 |
| P1-14 | `L53_visual_mfcc.ipynb` | 倒谱定义错误："余弦变换"应改为"逆傅里叶变换（IDFT）" | ✅ 已修复 |
| P1-15 | `L61_pytorch_nn.ipynb` | 参数量计算：`40×128+128 = 5258` 应为 `5248` | ✅ 已修复 |
| P1-16 | `L66_asr_overview.ipynb` | `n_vocab = 50257` 应为 `51865`（Whisper 多语言词表） | ✅ 已修复 |
| P1-17 | `L70_whisper_arch.ipynb` | Encoder 输出写 `(750, d_model)` 应为 `(1500, d_model)`；cell-6 标签错误 | ✅ 已修复 |
| P1-18 | `L72_whisper_finetune.ipynb` | 引用 `aurora.audio.features.mel_spectrogram`（不存在），应为 `aurora.audio.mel.mel_spectrogram` | ✅ 已修复 |
| P1-19 | `L83_transformer.ipynb` | 标题承诺位置编码+FFN 完整实现，但两者均缺失 | ✅ 已修复（PE + FFN + 集成前向） |
| P1-20 | `L97/L98/L99` | `量化（quantization，INT8）` 用于"量化成果"语境，英文括注语义混淆 | ✅ 已修复 |

### 3C — 文档与 API 不一致（P2）

| # | 文件 | 问题 | 状态 |
|---|------|------|------|
| P2-1 | `notebooks/README.md` line 1,24,187 | 仍写 94 节，Phase 10 只到 L94；缺 L95–L99 | ✅ 已修复 |
| P2-2 | `ROADMAP.md` line 66 | Phase 6 规划到 L92–L94；应为 L92–L99 | ✅ 已修复 |
| P2-3 | `docs/LEARNING_PLAN.md` lines 100,107 | 残留 `notebooks/month02/`–`month06/` 旧目录说法；课程范围只到 L94 | ✅ 已修复 |
| P2-4 | `docs/obsidian/INDEX.md` | 自称 "complete glossary"，但标注仍有 350 个缺失（已部分补全）；措辞需更新 | ✅ 已修复 |
| P2-5 | `src/aurora/llm/README.md` | Status: planned（模块已实现） | ✅ 已修复 |
| P2-6 | `src/aurora/music/README.md` | Status: planned（模块已实现） | ✅ 已修复 |
| P2-7 | `docs/week-02-checklist.md` | 引用不存在的 `src/aurora/audio/fft.py`（实际为 `transforms.py`）；写"递归" FFT 而实现是迭代 | ✅ 已修复 |
| P2-8 | `aurora.music.__init__` | 导出 `knn_search`，L80 教 `find_similar()`——API 不匹配 | ✅ 已修复（添加别名） |
| P2-9 | `L85_kv_cache.ipynb` | `KVCache()` 无参实例化，但构造函数需要 `n_heads, head_dim` | ✅ 已修复 |
| P2-10 | `L80_similarity.ipynb` | `find_similar()` API 不存在于 `aurora.music.similarity` | ✅ 已修复（添加别名） |
| P2-11 | `L20_visual_factorizations.ipynb` | `import scipy.linalg` 与依赖轻量化原则矛盾 | ✅ 已修复（手写 LU） |
| P2-12 | `docs/playtest-report.md` | 历史文档，保留 L01–L94 说法无问题，但不应被当作当前索引 | 无需修复（已标注历史） |
| P2-13 | `tests/llm/` `tests/music/` | 完全不存在；违反 CLAUDE.md "每个从零实现需有测试" | ✅ 已修复（5 个测试文件，41 个测试用例，全绿）|

### 3D — 结构质量问题（P2–P3，来自结构审计）

| # | 问题 | 影响范围 | 状态 |
|---|------|---------|------|
| Q1 | L57_mlp cell-10：14 个 TODO 拆成 Neuron / Layer / MLP 三个独立 cell | 1 nb | ✅ 已修复 |
| Q2 | L46_mel cell-13：10 个 TODO 拆成频率映射（步骤1-3）+ 三角矩阵（步骤4）两个 cell | 1 nb | ✅ 已修复 |
| Q3 | L03_spectrogram：无任何数值验证 cell | 1 nb | ✅ 已修复 |
| Q4 | L74_asr_error_analysis：无验证 cell，内容仅 488 字符 | 1 nb | ✅ 已修复 |
| Q5 | 64 个 notebook 缺"本课收束 + 下一课预告" | 全课程 | 长期优化 |
| Q6 | 78 个 notebook 缺结构化学习目标列表 | 全课程 | 长期优化 |
| Q7 | L66–L91 各节 markdown 字符数 < 1000（内容稀薄） | 后期模块 | 长期优化 |
| Q8 | 整体 check/code 比率约 12%，目标 25% | 全课程 | 长期优化 |

---

## 四、当前修复进度

### 已完成
- ✅ 全部 9 个 P0 代码 Bug 修复
- ✅ P2-1 notebooks/README.md 更新到 99 节
- ✅ P2-2 ROADMAP.md Phase 6 范围更新
- ✅ P2-3 LEARNING_PLAN.md 旧目录名修复
- ✅ P2-4 obsidian/INDEX.md 措辞更新
- ✅ P2-5/6 llm/music README 状态更新
- ✅ P2-7 week-02-checklist.md 路径修复
- ✅ P1-20 量化括注语义修复（L97/L98/L99）
- ✅ 英文括注全库补全（571 → 795 处）
- ✅ docs/obsidian/ 新建双语术语索引 vault

### 待完成（按优先级）
1. P1-1, P1-8 ~ P1-11, P1-19：内容错误（缺失章节、内容补写）
2. P2-13：测试文件缺失
3. Q5 ~ Q8：长期内容优化

---

## 五、优点记录（不变）

| 优点 | 具体体现 |
|---|---|
| Aurora 政策执行严格 | 99 个 notebook 中零处直接 `import librosa`（仅 2 处可选对比），`scipy.signal` 零导入 |
| 数学手推贯彻 | FFT、STFT、Mel、DCT、MFCC 全部从零实现，与 `aurora.audio` 模块一一对应 |
| Stub 设计合理 | 33 个 TODO 桩各自有明确签名、docstring 和验证 cell |
| 验证 cell 存在 | 163 个 assert/check cell，大多数核心实现都有数值验证 |
| 双语标注覆盖良好 | 795 个英文括注分布于全库，术语一致性已显著提升 |
| 核心算法正确 | 38 个 audio 测试全通过；autograd、CTC 前向算法、Levenshtein DP 均数学正确 |

---

## 六、风险摘要

```
P0（已全部修复）：9 个代码 Bug，含 SyntaxError、参数错误、策略违规
P1（待修）：20 个内容错误，影响数学正确性和教学完整性
P2（部分修复）：13 个文档/API 不一致，7 个已修复
P3 / 长期：内容密度、验证覆盖、收束指引——不影响可运行性
```

---

*报告由 Claude Code 自动生成，合并自双轨审计（结构扫描 + 14-agent 代码审查）。*


---

## 2026-06-28 最终状态（全面检查）

### 三项结构性指标全部清零

| 指标 | 初始 | 修复后 |
|------|------|--------|
| 缺 本课收束 | 64 个 | **0 / 99** ✅ |
| 缺学习目标（**目标**/**为什么**） | 78 个 | **0 / 99** ✅ |
| 缺下一课预告 | 71 个 | **0 / 99** ✅ |

### 代码质量指标

| 指标 | 值 | 状态 |
|------|----|------|
| pytest 测试函数 | 79 个，全绿 | ✅ |
| Audio Core 禁用 API 违规（src/） | 0 | ✅ |
| np.trapz（已废弃）残留 | 0 | ✅（已替换为 np.trapezoid）|
| Shannon 熵章节（L30 Section 2 + L31 Section 7/8）| 已补全 | ✅ |

### 仍属长期项目（不阻塞课程使用）

| 项目 | 现状 |
|------|------|
| Obsidian 双语词汇注释 | 462 词条，76% 缺英文注释；由 annotation-audit.md 持续追踪 |
| 后期模块内容密度（L87、L71、L74 等） | 可运行；细化留后续迭代 |
| speech / tts / rag 模块实现 | ROADMAP Phase 3–6 范围；stub 状态符合预期 |

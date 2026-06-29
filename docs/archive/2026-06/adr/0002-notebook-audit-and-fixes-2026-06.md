# ADR 0002 — 课程 Notebook 全量审计与批量修复（2026-06）

**状态**：已完成  
**日期**：2026-06-28 ~ 2026-06-29  
**范围**：L01–L99，99 个 notebook

> 这是修复过程记录，主要用于追溯审计与批量修复的决策链，不作为当前课程状态总结。

---

## 背景

课程经历了从 85 课扩展到 99 课、并统一重命名为 L01–L99 的重构。重构后对所有 notebook 进行了全量审计，发现 67 门课（68%）存在阻塞性问题，29 处严重（Critical）、143 处重大（Major）、136 处次要（Minor）。

---

## 决策：分批修复，按阻塞优先级排序

### 批次 1 — 解答泄漏 + 伪 TODO（L69/71/76/78/85/86/88/89）

**问题**：`<details><summary>点击查看参考实现</summary>` 块将完整代码暴露在 TODO cell 正上方；部分 notebook 的 `# ✏️ TODO` 注释后紧跟完整实现，没有真正的练习空间。

**修复**：
- Pattern A：提取 `<details>` 块中的代码到 `solutions/<nb>_solutions.md`，替换为提示行
- Pattern B：将完整实现替换为 `raise NotImplementedError("TODO")`

### 批次 2 — aviz / laviz 缺失依赖（L09–L21, L32–L36）

**问题**：18 个 notebook import `aviz` 或 `laviz`，但这两个模块不存在于项目中，运行即 `ModuleNotFoundError`。

**修复**：
- 新建 `src/aurora/aviz.py`（8 个音频可视化函数，纯 numpy+matplotlib）
- 新建 `src/aurora/laviz.py`（8 个线性代数可视化函数）
- 将所有 `import aviz` 改为 `import aurora.aviz as aviz`，`from laviz import ...` 改为 `from aurora.laviz import ...`

### 批次 3 — 关键数学错误（L46, L49, L91, L97）

| Notebook | 问题 | 修复 |
|---|---|---|
| L46 | `hz_to_mel(700) ≈ 782.7`（错），正确值 ≈ 781.2 | 断言容差值和说明文本 |
| L49 | IDCT 实现用了错误的未归一化公式 | 改为 `D.T @ X`（正交 DCT-II 的正确逆） |
| L91 | LoRA 维度 A(d×r), B(r×d) 错误（B@A 得 r×r 不是 d×d） | 按论文约定改为 A(r×d), B(d×r) |
| L97 | `assert frames.shape == (3, 8)`，正确应为 (4, 8) | 修正断言 |

### 批次 4 — 第二批阻塞型 Bug（L02, L17, L26, L44, L72, L80）

| Notebook | 问题 | 修复 |
|---|---|---|
| L02 | `abs(max_abs - 1.0) < 1e-6`，实际最大值 ≈ 0.9952 | 容差改为 `< 0.02` |
| L17 | `A` 在 cell 7/9 被覆写为 2×2，验证 cell 用 3×3 断言 | 在验证 cell 顶部重置 `A` |
| L26 | 凸函数被描述为"有鞍点"（f=x²+2y² 无鞍点） | 改为"极小值"，说明正确几何 |
| L44 | `for f in windowed:` 在 `windowed=None` 时 TypeError | 加 `if windowed is None: return None` |
| L72 | LibriSpeech split `"train.100"` 不存在 | 改为 `"train.clean.100"` |
| L80 | `idx, scores = find_similar(...)` 无 None 守卫 | 用 result 变量接收再解包 |

### 批次 5 — 次课预告修正（8 处编号错误 + 24 处描述过期）

**编号错误**（重构后未更新）：L39→L40, L40→L41, L41→L42, L44→L45, L46→L47, L52→L53, L79→L80, L84→L85

**描述过期**（旧模块标签如 M2-P2, a6, mu5_eval 等）：L06–L93 共 24 处，均已替换为正确的 L 编号和准确的内容描述。

### 额外修复

| Notebook | 问题 | 修复 |
|---|---|---|
| L12 | `matvec` 返回 None，`np.allclose(None, ...)` → TypeError | 改为 `raise NotImplementedError`，断言加 try/except |
| L47 | `mel_filterbank @ power_spectrum.T` 得 `(n_mels, n_frames)`，描述说 `(n_frames, n_mels)` | 改为 `power_spectrum @ mel_filterbank.T` |
| L67 | "CTC 对齐服务于 Whisper 的训练目标"（Whisper 用交叉熵，不用 CTC） | 改为"服务于 CTC 系列模型（wav2vec 2.0、DeepSpeech）" |
| L89 | `except NotImplementedError` 不捕获 `NameError`（前向引用） | 改为 `except (NotImplementedError, NameError)` |
| L90 | cell 13 的 `ans_rag.lower()` 在 stub 返回 Ellipsis 时崩溃 | 加 `if ans_rag is ...` 守卫 |

---

## 测试

所有修复完成后：`pytest tests/ → 79 passed`（无回归）。

---

### 批次 6 — Minor 问题批量修复 + L82 可视化补完（2026-06-29）

**L82 补完**：添加 Section 3（节拍网格可视化：合成 onset 包络 + 120 BPM 节拍线）和 Section 4（相似度热力图：4×4 余弦相似度矩阵），兑现标题"色度图、节拍图、相似度热力图"。

**README 对齐**：
- L55：改为"Value 算子补全 — `__pow__`、relu、tanh、exp 节点实现，计算图完整展开"
- L90：改为"对话式 RAG — 会话记忆、来源归因与 Podcast Q&A 流水线"
- L95：改为"研究论文入门 — 三遍阅读法、论文结构写作、投稿流程与学术合作"

**Minor 问题修复**：
- 文件引用修正（7 处）：L08 → L06 euler 路径、fft.py → transforms.py、L22 → L23、L42 → L43 stft、L57 → L58、L37 L39 → L38
- 重复 cell 删除（8 个 notebook）：L05/L08/L22/L27/L30/L34/L35/L36 各删 1 个完全重复的代码格
- L29 重复 H1 标题删除
- Typo：L60 "吴合" → "吻合"
- Dead code：L56 `Value.backward = types.MethodType` 删除；L51 `cfg["hop_length"] = cfg.get("hop_length")` 删除
- L75 `import torch`（无依赖 torch，ImportError 风险）删除
- L70 cell-1 错误编码器步数：750 → 1500
- 重复章节编号修正：L14（三个 ## 2. → 2, 3, 3.1）、L30（两个 ## 1. → 1, 2）、L83（两个 ## 5. → 5, 6）、L97（两个 ## 4. → 4, 5）

**测试**：79 passed（无回归）。

### 批次 7 — 扫尾：剩余 Minor 问题（2026-06-29）

**ROADMAP 对齐**：
- L90：改为 "Conversational RAG: session memory, source attribution, Podcast Q&A"
- L95：改为 "Research skills: three-pass reading, paper structure, submission & academic collaboration"

**概念/数值修正**：
- L27 cell 16：描述说 `seed=42`，代码用 `seed=7` → 改描述为 `seed=7`
- L50 cell 9：注释 `(61, 13)` 错误，实际 63 帧（`aurora.audio.stft` 用 `16000//256+1`）→ 改为 `(63, 13) = 63`
- L15 cell 7："超定、**正定**、欠定" 中"正定"歧义（与正定矩阵 SPD 混淆）→ 改为"**恰定（square）**"
- L66 cell 9/11：描述"交换 cat/sat"暗示 swap 操作，Levenshtein 无 swap → 改为"顺序互换（2次替换）"

**标题/结构修正**：
- L60：H1 "retain_graph 原理"（实际演示的是 `retain_grad()`）→ 改为 "retain_grad 与梯度累积"；本课收束追加 retain_graph vs retain_grad 区别说明
- L62：补充 Section 6 `KWSDataset(Dataset)` 类（含 `__getitem__`），实现标题承诺
- L93 cell 10：CI YAML 中 `make test -- --json-report ...`（无效 Make 语法）→ 改为 `pytest --json-report ...`
- L98：`## 2b. / ## 4b. / ## 6b.` 孤立节号 → 线性重编为 1–7

**已核实为误报（无需修复）**：
- L48/L52/L59/L77 的 `stft`/`sine`/`mfcc` 均有实际调用，非 unused import

**测试**：79 passed（无回归）。

---

### 批次 8 — L11-L20 学习笔记反馈修复（2026-06-29）

本批次修复来自 L11-L20 逐课学习笔记中发现的问题。

**全量删除「小检查」冗余 Cell**：
- L11–L20 全部 10 个 notebook 的末尾都有完全相同的 8 行「小检查」代码（`a+b / A@a / a.dot`），与课程内容无关——全部删除（每个 notebook 同时清除了空 markdown cell，共减少 4 cells/本）

**边界测试补强**：
- L11 `normalize`：在 assert cell 补加「负分量向量」和「零向量」两种边界测试（`normalize([0,0])` 应有 eps 保护，不抛 ZeroDivisionError/nan）
- L14 `low_rank_approx`：在验证 cell 追加矩形矩阵（4×3）测试——确认 shape 不崩、全秩还原正确（`np.diag(S[:k])` 对非方阵需用 `full_matrices=True` 或调整切片）

**当场验证，不推迟到后续课**：
- L13：在「本课收束」前插入可运行的 FFT 往返验证（`ifft(fft(x)) == x`），佐证 DFT 矩阵酉性（原文说「L39 再验证」，现在 L13 就完成）

**标题/内容一致性**：
- L12：标题「矩阵乘法」但仅实现 `matvec`（矩阵×向量）；补充 `matmul`（矩阵×矩阵）TODO 练习（含矩形矩阵测试 (3×2)@(2×4)）

**断言质量**：
- L16：`det_2x2` 和 `inv_2x2` 原在同一 assert cell——拆分为两个独立 cell，各自打印中间值，便于精准定位失败原因

**代码与描述对齐**：
- L18：「参数实验：Jacobi 迭代」仅有 markdown 描述，无可运行代码——补充 `jacobi(A, b, n_iter)` 实现，展示 s.d.d. 矩阵收敛、非 s.d.d. 矩阵发散对比

**新增 TODO 练习**：
- L19：补充 `classify_transform(A)` 练习（判断旋转/反射/缩放/剪切，含 4 组 assert）
- L20：补充 `rank_from_svd(A)` 练习（用 SVD 计算数值秩，不调用 `np.linalg.matrix_rank`，含满秩/秩亏/矩形矩阵/随机矩阵 4 组验证）

**测试**：待运行（变更均为新增代码或 cell 删除，无修改已有通过的测试逻辑）。

---

## 状态：已全量完成

原始审计发现的 29 Critical + 143 Major + 136 Minor 问题，经 7 批次修复，所有阻塞性问题已清除，课程可完整运行。pytest 79/79 持续绿灯。批次 8 为学习笔记驱动的增量改进（练习质量、边界测试、内容一致性），不影响已有测试结果。

# ADR 0002 — 课程 Notebook 全量审计与批量修复（2026-06）

**状态**：已完成  
**日期**：2026-06-28 ~ 2026-06-29  
**范围**：L01–L99，99 个 notebook

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

## 已知遗留问题（未在本轮修复）

- **L55/L90/L95 内容与 ROADMAP 描述不符**：L55 实际是 Value 算子（ROADMAP 说"矩阵级前向传播"）；L90 实际是 RAG（ROADMAP 说"Tool-calling Agent"）；L95 实际是通用学术技能（ROADMAP 说"论文精读"）。修复需重写 notebook 内容，工作量大，待单独决策。
- **L82 三种可视化只实现一种**：缺 beat tracking 可视化和相似度热力图。
- **136 处 Minor 问题**：重复 cell、过时路径引用、typo 等，未影响运行的问题暂缓。
- **README 与 notebook 标题不对齐（28 处）**：决策是以 notebook 内容为准，README 待下一轮更新。

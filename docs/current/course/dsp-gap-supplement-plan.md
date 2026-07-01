# DSP 跃升点补充计划

> **约束**：不插入新课、不改 L01–L99 标号与顺序。所有补充以**现有 notebook 内增删改**、
> **checklist 附录**、**solutions 参考**、**Obsidian 概念卡**形式完成。
>
> **背景**：见课程纵向分析（`docs/current/audit/02_纵向分析.md`）与 DSP 跃升点评析。
> **目标**：削平 Audio DSP 段六处认知断崖，不增加课节数量。
>
> **总索引**：全课三处顶级断崖见 [`gap-supplement-plan.md`](gap-supplement-plan.md)；
> L53→L54 见 [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md)；
> L68→L69 见 [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md)。
>
> **状态**：🟡 执行中（2026-07-01）— P0 Week1（L36–L39）✅ 已落地待复审；P0 Week2（L42–L45）✅ 已落地待复审；P1/P2 📋 待做

---

## 0. 防断崖目标：提升到何种程度？

### 0.1 两个层级，不要混为一谈

| 层级 | 问什么 | 当前状态（2026-07-01） | 防断崖目标 |
|------|--------|------------------------|------------|
| **单课质量** | 这节课本身写得好不好？ | 79 课 A-、13 课 B+、7 课 B；无 B- | **维持**：内容课 ≥ A-，可视化课 ≥ B+ |
| **纵向连续** | 相邻课之间学生会不会摔下去？ | DSP 六处 + 全课 L53→L54、L68→L69（另两份分计划） | **新增**：各段跃升点有桥接；Δ认知 ≤ 1（或 Δ=2 有桥） |

**结论**：单课升到 A- **不能自动消除断崖**。第四轮科普升级解决的是「每课是否达标」，不是「课与课之间是否连贯」。防断崖是在 A- 基线上的**第二层工程**。

### 0.2 防断崖验收标准（可检查）

满足以下 **全部** 条件，即认定 DSP 段（L32–L53）「断崖已削平」：

#### A. 认知坡度（相邻课）

| 编号 | 标准 | 度量方式 | 达标线 |
|------|------|----------|--------|
| **A1** | 相邻课认知等级差 | 对每对 `L(n)→L(n+1)` 标 0–3 级（见下表） | **Δ ≤ 1**；仅 L37→L38、L43→L44 允许 Δ=2 且必须有桥接 |
| **A2** | 跃升点桥接覆盖率 | 6 处 DSP 跃升点每处 ≥1 个「桥接格」或 checklist 附录 | **6/6** |
| **A3** | 时间断崖回调 | L03/L07/L21 在首次被依赖的课（L32/L35/L37/L47）有「≤2 分钟复习」格 | **4/4** |

**认知等级定义**（审计用，非学生可见）：

| 等级 | 学生在做什么 |
|------|-------------|
| 0 | 读/看演示，无 TODO |
| 1 | 按公式翻译为代码（单函数、单循环） |
| 2 | 组合 2–3 个已有零件，或推导递推关系 |
| 3 | 设计完整算法或五段流水线，误差 < 1e-10 |

当前超标对（需桥接，不要求改课号）：

- L36→L37：1→2（可接受，需 periodic 窗补充）
- L37→L38：1→2
- L38→L39：2→3
- L41→L43：1→2
- L43→L44：2→3
- L48→L50：1→3（L49 为缓冲，需加强）

#### B. 练习与可运行性（跃升点课节）

| 编号 | 标准 | 达标线 |
|------|------|--------|
| **B1** | 推理路线不泄漏可粘贴通过的完整实现 | 跃升点课（L37–L39、L44、L47、L50）**0 处**全文伪代码 |
| **B2** | 桩代码未实现时 notebook 可顶到底跑 | 补充 cell 不得使下游 `NameError` / 未捕获 `NotImplementedError` |
| **B3** | 半步练习存在 | L38、L44 各有 ≥1 个**不替代**主 TODO 的半步格 |
| **B4** | solutions 归档 | L39、L44、L47、L49 均有 `solutions/Lxx_*.md` |

#### C. 学生体验（定性抽测）

| 编号 | 标准 | 达标线 |
|------|------|--------|
| **C1** | 跃升课完成时间倍率 | 自测：`T(L39)/T(L37) ≤ 3` 且 `T(L44)/T(L43) ≤ 2.5`（同一学生，已做完前驱） |
| **C2** | 卡住回退路径 | 每个主 TODO 旁有「卡住 → 回 Lxx §附录」一行 |
| **C3** | checklist 与 notebook 一致 | `week-01/02`、`prep-checklist` 中预习项与 notebook 附录标题**逐字可搜** |

#### D. 与现有 A- rubric 的关系

防断崖 **不降低** 现有单课要求：

- 科普引入 + 任务表 + 白板 + 自评（A- 五要素）**保留**
- 桥接格、复习格、半步练习 **叠加**，不替换主练习
- 数值断言仍 `atol=1e-10`（Audio Core 课）

**防断崖完成后的 DSP 段目标画像**：

> 单课仍 ≥ A-；纵向 Δ认知 ≤ 1（除 2 处允许 Δ=2 且有桥接）；6 处跃升点 100% 有回调/附录；学生从 L32 学到 L53 **无需跳号补课**。

---

### 0.3 本计划涵盖哪些「期」？

与 `ROADMAP.md` Phase 对齐如下：

| ROADMAP Phase | 课节 | 本计划是否涵盖 | 说明 |
|---------------|------|----------------|------|
| **Phase 0** 数学基础 | L01–L31 | **部分** | 只动 L03、L07、L21、L31（回调源 + L31→L32 桥）；不改 L04–L30 主干 |
| **Phase 1** Audio DSP | L32–L53 | **全部** | 六处跃升点 + week-01/02 checklist；核心工作区 |
| Phase 2 深度学习 | L53–L58 | **见分计划** | [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) — **L53→L54 全课最陡** |
| Phase 3 ASR | L67–L71 | **见分计划** | [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md) — **L68→L69** |
| Phase 4–6 | L76–L99 | **未涵盖** | L89→L90 等待三计划落地后评估 |

**本文件内 P0/P1/P2** 是**执行优先级**，不是 ROADMAP Phase 号：

| 执行优先级 | 含义 | 对应 ROADMAP |
|------------|------|--------------|
| P0 | 最陡两处，先做 | Phase 1 核心（L36–L44） |
| P1 | 模块入口 + MFCC 综合 | Phase 0 末 + Phase 1 末（L31–L32、L48–L51） |
| P2 | 回调与微调 | Phase 0 回调点 + Phase 1 次级 |

---

### 0.4 分期修改意见总表

下表为**每期（ROADMAP Phase）在本计划范围内的全部修改项**；✅=已有审计修复，📋=本计划待做。

#### Phase 0（部分）— L01–L31，仅 5 课

| 课节 | 修改项 | 类型 | 优先级 |
|------|--------|------|--------|
| L03 | 收束加一句「L32 将从时间轴重建此图」；Obsidian 链到 L32 附录 | 时间回调锚点 | P2 |
| L07 | 收束加「L35/L37 将用复指数形式实现同一直觉」 | 时间回调锚点 | P2 |
| L21 | 在 DFT 矩阵验证 cell 后加「L37 将用循环写同一变换」前向引用 | 时间回调锚点 | P2 |
| L31 | 收束加「进入 L32 心理切换」段；补 1 个可选 TODO（`shannon_entropy` 或复盘 L30） | 模块桥接 | P1 |
| L31 | 与 `prep-checklist.md` L31→L32 段交叉链接 | checklist | P1 |

#### Phase 1（全部）— L32–L53，18 课有具体修改

| 课节 | 修改项 | 类型 | 优先级 | 状态 |
|------|--------|------|--------|------|
| L32 | 开篇「回顾 L03」格 + 可选示意图 code cell | 模块桥接 | P1 | 📋 |
| L35 | 开篇回调 L07 方波叠加（2 分钟） | 时间回调 | P2 | 📋 |
| L36 | 附录 A「分治预习」；periodic vs symmetric 窗对照表 | 断崖桥接 | P0 | ✅ 已落地 |
| L37 | 开篇 L21 复习桥；收束 L 编号复查；删跳 L42 引用 | 断崖桥接 | P0 | ✅ 已落地 |
| L38 | 附录 B 递归/迭代对照；N=4 手写蝶形草稿格；回调 L06/L35 | 断崖桥接 | P0 | ✅ 已落地 |
| L39 | 非 2 幂说明格；五步表降泄漏 → solutions；确认 `L39_*_solutions.md` | 断崖桥接 + B4 | P0 | ✅ 已落地；solutions 已有 |
| L42 | 附录「整段 FFT → STFT 多一维」 | 断崖桥接 | P0 | ✅ 已落地 |
| L43 | 「零件清点」格；参数量化表 + 实测 `n_frames` | 断崖桥接 | P0 | ✅ 已落地 |
| L44 | 常见失败模式；半步「单帧 STFT」；`solutions/L44_*.md` | 断崖桥接 + B3/B4 | P0 | ✅ 已落地；solutions 已有 |
| L45 | shape 备忘口诀（与 L50 一致） | 断崖桥接 | P0 | ✅ 已落地 |
| L46 | 末尾三角滤波器手绘练习（markdown） | 次级跃升 | P2 | 📋 |
| L47 | 开篇 L21 矩阵滤波回调；推理路线删全文 for 循环 | 次级 + B1 | P2 | 📋 |
| L48 | 末尾 DCT/倒谱动机预告（与 L49 二选一） | 断崖桥接 | P1 | 📋 |
| L49 | FFT vs DCT 差异表；`_dct_ii_ref` 移出验证 cell；`solutions/L49_*.md` | 断崖桥接 + B4 | P1 | 📋 |
| L50 | 流水线 checklist cell；每键「卡住回 Lxx」 | 断崖桥接 | P1 | 📋 |
| L51 | 真实 WAV 坑 + librosa 定位 + ROADMAP 项说明 | 工程桥接 | P1 | 📋 |
| — | `week-01-checklist.md`：L32 准备、L36 末预习 L37 | checklist | P1 | ✅ 已落地 |
| — | `week-02-checklist.md`：L37 前准备 + L42–L44 桥接项 | checklist | P0 | ✅ 已落地 |
| — | `prep-checklist.md`：L31→L32 切换 20 分钟 | checklist | P1 | 📋 |
| — | `obsidian/domains/audio-dsp.md`：跃升点导航节 | 汇总 | P2 | 📋 |

**Phase 1 本文件内无需改内容（维持 A-）**：L33、L34、L40、L41、L52（仅引用复查）。

**L52、L53 出口桥接**：在 [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) §2（L52 结业清单、L53 附录 A 模式切换），不在此重复。

#### Phase 2–3 — 已立分计划

| 跃升点 | 文档 | 核心修改 |
|--------|------|----------|
| **L53→L54** | [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) | L53 附录 A、L54 L24 复习桥、半步 forward、`solutions/L54`、week-03 |
| **L68→L69** | [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md) | L68 附录 C、L69 复习桥、暴力枚举半步、log 域双写、week-04 |

#### Phase 5–6 — 待评估

| 跃升点 | 课节 | 状态 |
|--------|------|------|
| L89→L90 TF-IDF→dense | L89 收束 | 三计划完成后再写 |

---

## 1. 补充原则

| 原则 | 说明 |
|------|------|
| **课号不动** | 只在 `Lxx_*.ipynb` 现有 cell 之间插入 markdown / code，或用「附录」「预习回顾」折叠块 |
| **可选不强制** | 陡峭处加「⏸ 若卡住，先读本节再做题」；熟练者可跳过 |
| **回调不超前** | 补充块只引用**已学过的 L 编号**，或明确标「复习 L21，非新内容」 |
| **可验证** | 新增 code cell 须有 `assert`；不写无法运行的空承诺 |
| **不改主干** | 原有 TODO → assert 流程保持不变；补充在侧翼，不替换核心练习 |

**补充物五种形态**：

1. **预习回顾格**（markdown）：上课前 5 分钟能读完
2. **概念桥接格**（markdown + 可选示意图）：解释「上一课输出 → 本课输入」
3. **半步练习格**（code，可选）：降低一级难度，不替代原 TODO
4. **checklist 附录**（`week-0N-checklist.md` 末尾）：「进入 L37 前 15 分钟」
5. **Obsidian 概念卡**（`docs/current/obsidian/domains/audio-dsp.md`）：跨课双链汇总

---

## 2. 优先级总览

| 阶段 | 目标跃升点 | 涉及课节 | 预估工作量 |
|------|-----------|----------|-----------|
| **P0** | L37→L38→L39 分治断崖 | L36, L37, L38, L39 | 中 |
| **P0** | L41→L43→L44 STFT 系统集成 | L42, L43, L44 | 中 |
| **P1** | L31→L32 模块入口 | L31, L32, prep-checklist | 小 |
| **P1** | L48→L49→L50 DCT + 流水线 | L48, L49, L50 | 中 |
| **P2** | 时间断崖（L03/L07/L21 回调） | L03, L07, L21, L35, L37 | 小 |
| **P2** | L36→L37、L45→L47、L50→L51 | L36, L37, L46, L47, L51 | 小 |

---

## 3. P0 — L37→L38→L39（最陡断崖）

### 2.1 L36 末尾 · 分治预习附录

**位置**：`L36_windows.ipynb`，「本课收束」之前插入 markdown cell。

**标题**：`## 附录 A · 进入 L37 前：分治思维 5 分钟预习（非新课）`

**内容要点**：

- 用「高塔二分找楼层」类比 FFT 分治（与 L39 剧情呼应，此处首次轻量出现）
- 明示：**L37 仍用暴力循环**；分治是 L38–L39 的事，现在只需知道「存在更快做法」
- 回调 **L07**：任何周期信号 = 正弦叠加 → DFT 问「各频率分量多大」
- 回调 **L06 欧拉公式**：`e^{-2πikn/N}` 是 L35 旋转因子的课号锚点
- 一行预告：`L38` 画蝶形图，`L39` 写递归

**可选 code cell**：对 `N=8` 用 `np.fft.fft` 打印幅度谱，标注「L40 才系统讲谱分析，此处只看有输出」。

### 2.2 L37 开篇 · L21 矩阵视角复习格

**位置**：`L37_dft.ipynb`，cell 0 学习目标之后。

**标题**：`## 复习桥 · L21 的 DFT 矩阵（2 分钟）`

**内容**：

```text
L21 已证：X = W @ x 与 np.fft.fft(x) 数值相同（atol=1e-10）。
L37 不用矩阵——用双重循环直接写 Σ x[n]·e^{-2πikn/N}。
两种写法等价；循环版帮你记住每个指数项，矩阵版帮你记住「FFT = 线性变换」。
```

**可选 code cell**：`N=4` 时打印 `W @ x` 与 `naive_dft(x)` 各 4 个系数，误差 < 1e-12。

### 2.3 L37 收束 · 修正前向引用

**核对项**（审计已部分修复，补充时复查）：

- 「本课收束」中蝶形运算指向 **L38**，完整实现指向 **L39**
- 删除/改正任何「完成后直接跳 L42」的引用 → 应指向 L38

### 2.4 L38 中段 · 递归 vs 迭代心智桥

**位置**：`L38_fft_butterfly.ipynb`，蝶形公式推导之后、「TODO butterfly」之前。

**标题**：`## 附录 B · 递归版 vs 生产版迭代版（读即可）`

**内容要点**：

- `aurora.audio.transforms.fft()` 是**迭代** Cooley-Tukey（位逆序 + 层序蝶形），不是递归
- L39 写**递归**是为了画清分治树；L41 会走**迭代/管线**路径
- 对照表：

  | | L39 `my_fft` | `aurora_fft` |
  |---|---|---|
  | 结构 | 递归 | 迭代 |
  | 目的 | 理解分治 | 生产 STFT 内调用 |
  | 验证 | 互相对齐 atol=1e-10 | tests/audio |

- 贴 `src/aurora/audio/transforms.py` 中 `fft()` 函数签名链接（不贴全文）

### 2.5 L38 练习前 · 手写 N=4 蝶形草稿格

**位置**：TODO 实现之前，markdown + 空白作答 code cell。

**内容**：给出 `x=[1,0,1,0]`，要求学生在纸上填 `E=fft([1,1])`、`O=fft([0,0])` 的四条合并式；
下一格公布答案并 `assert_allclose` 与 `np.fft.fft(x)`。

### 2.6 L39 练习后 · 非 2 幂与补零说明格

**位置**：`my_fft` 验证通过之后。

**内容**：

- 生产 `fft()` 对非 2 幂会 `next_power_of_two` 补零；`my_fft` 本课只要求 2 幂
- 与 L39 已有「补零演示」cell 交叉引用，避免重复——此处只加**与 `stft.py` 调用约定**的一句
- 指向 L44：`my_stft` 每帧长度 `win_len` 通常取 2 幂

### 2.7 week-02-checklist 附录

**位置**：`week-02-checklist.md` 的「准备（L37 开始前 15 分钟）」段扩充：

```markdown
- [ ] 重读 L21 cell-12：`W @ x` 与 `fft(x)` 对齐（5 分钟）
- [ ] 重读 L35 旋转因子公式（3 分钟）
- [ ] 浏览 L36 附录 A「分治预习」（5 分钟）
- [ ] 确认 `make test` 中 audio transforms 全绿（环境就绪）
```

---

## 4. P0 — L41→L43→L44（STFT 系统集成）

### 3.1 L42 末尾 · STFT 过渡附录

**位置**：`L42_visual_fft.ipynb`，「下一课」导航 cell 之前。

**标题**：`## 附录 · 从「整段 FFT」到「STFT」：多出来的一个维度`

**内容要点**：

- L41 输出：一组频率 bin（一个时间点）
- STFT 输出：矩阵 `(n_frames, n_bins)`——**时间 × 频率**
- 三个新参数：`win_len`、`hop_length`、`window`（L36 已学）
- 帧数公式预告：`n_frames = 1 + (len(x) - win_len) // hop`（L43 手推）
- ASCII 示意图：信号轴上滑动窗口

**不引入新 TODO**；纯 markdown。

### 3.2 L43 开篇 · 子组件清点格

**位置**：`L43_stft.ipynb`，剧情引入之后。

**标题**：`## 你已拥有的零件（无需新写）`

| 零件 | 来源课 | 仓库函数 |
|------|--------|----------|
| FFT | L39 | `aurora.audio.transforms.fft` |
| 窗函数 | L36 | `aurora.audio.windows.hann` |
| 分帧 | 本课 TODO | `aurora.audio.stft.frame_signal` |

**目的**：降低「又要从零写一切」的焦虑；明确 L44 是**组装**而非**新算法**。

### 3.3 L43 练习后 · 参数量化直觉格

**位置**：`frame_signal` 验证通过之后（审计曾修正帧数预测，补充时与代码输出对齐）。

**内容**：固定 `sr=16000, len=1s`，表格对比：

| win_len | hop | 约 n_frames | 时间分辨率 (ms) | 频率分辨率 (Hz) |
|---------|-----|-------------|-----------------|-----------------|
| 512 | 128 | 122 | 8 | 31.25 |
| 2048 | 512 | 30 | 32 | 7.8 |

**code cell**：用 `aurora.audio.stft.frame_signal` 打印实测 `n_frames`，与表内公式互证。

### 3.4 L44 练习前 · 五步组装路线图（加强版）

**位置**：`L44_stft_implement.ipynb`，现有推理路线 cell 之后。

**补充**：增加「常见失败模式」bullet：

- 忘记 `rfft` 只取 `win_len//2+1` 个 bin
- `center=True` 时 padding 长度与 L43 手推公式差 1 帧——以 `aurora.stft` 为准
- 窗函数未乘在帧上就直接 FFT（泄漏爆炸）

**半步练习格**（可选，不替代 `my_stft`）：

```python
# 只实现「单帧」：第 0 帧 window → rfft → 幅度
# 与 aurora.stft 第 0 行对齐后再写循环
```

### 3.5 L44 与 L45 之间 · shape 备忘格

**位置**：`L44` 收束或 `L45` 开篇。

**固定口诀**（与 L50 一致）：

```text
1 秒 @ 16 kHz, win=512, hop=256, center=True
→ STFT 幅度谱约 (63, 257)  时间 × 频率
→ Mel 约 (63, 40)
→ MFCC 约 (63, 13)
```

避免 L50 综合课时 shape 再次成为断崖。

---

## 5. P1 — L31→L32（模块入口）

### 4.1 L31 收束 · 显式桥接到 L32

**位置**：`L31_visual_probability.ipynb`，「下一课」cell。

**补充段落**：

```markdown
### 进入音频 DSP（L32）前的心理切换

L27–L31 是「分布与损失」的数学语言；L32 起是「数组与采样」的工程语言。
你在 L03 已经看过谱图——L32–L53 要把那张图从里到外做出来。
建议：打开 L03 回顾 3 分钟，再开 L32。
```

### 4.2 L32 开篇 · L03 回调格

**位置**：`L32_numpy_signals.ipynb`，cell 0 之后。

**标题**：`## 回顾 L03 · 谱图直觉 → 今天要造时间轴`

**内容**：谱图横轴=时间、纵轴=频率、颜色=能量；今天第一步是 `t = np.arange(N)/sr`。

**code cell**：加载 L03 中同款示意图路径（若 notebook 内有图）或 `matplotlib` 重画静态示意。

### 4.3 prep-checklist 扩充

**位置**：`prep-checklist.md`，「进入 L32」条目前。

```markdown
### L31 → L32 切换（约 20 分钟）

- [ ] 重读 L03（谱图直觉，不推公式）
- [ ] 重读 L01 cell-2（正弦波一行代码）
- [ ] 运行 `python -c "import aurora; import numpy; print('ok')"`
- [ ] 阅读 L31 收束「心理切换」段
```

---

## 6. P1 — L48→L49→L50（DCT + MFCC 流水线）

### 5.1 L48 末尾 · 倒谱预告

**位置**：`L48_visual_stft.ipynb` 或 `L49` 开篇（二选一，避免重复）。

**内容**：

- Mel 谱相邻滤波器高度相关（相关系数 ~0.9）
- DCT 的作用 = 去相关 + 能量压缩（与 JPEG 同源不同域）
- **不实现**，只建立动机；实现留在 L49

### 5.2 L49 练习前 · 与 FFT 的差异表

**位置**：`L49_dct.ipynb`，DCT 公式之前。

| | FFT 基 | DCT-II 基 |
|---|--------|-----------|
| 复数/实数 | 复指数 | 余弦 |
| 对称性 | 圆周 | 偶对称延拓 |
| 用途 | 频谱分析 | 倒谱/压缩 |
| Aurora | `transforms.fft` | `mfcc.dct_ii` |

### 5.3 L49 练习设计修正

**审计项**：参考实现 `_dct_ii_ref` 不得与 TODO 验证同 cell。

**补充计划**：

- 验证基准只用 `scipy.fft.dct(norm='ortho')` 或 `aurora.audio.mfcc.dct_ii`
- 参考实现仅放 `solutions/L49_dct_solutions.md`（若文件不存在则创建）

### 5.4 L50 开篇 · 流水线 checklist cell

**位置**：`L50_mfcc.ipynb`，TODO 之前。

**可勾选 code cell**（学生填 `True/False`）：

```python
pipeline_checklist = {
    "stft_shape_ok":      None,  # 能写出 (T, n_bins)？
    "mel_matmul_ok":      None,  # power @ fb.T 方向对吗？
    "log_floor_ok":       None,  # log(max(power, eps)) 为何需要 eps？
    "dct_ortho_ok":       None,  # k=0 权重为何特殊？
}
```

每格附一行「卡住回哪课」：`L44` / `L47` / `L49`。

### 5.5 L50→L51 工程衔接

**位置**：`L51_real_audio.ipynb` 开篇。

**补充**：

- 真实 WAV 常见坑：采样率不一致、单声道/立体声、幅度归一化
- librosa 对比的定位：**交叉验证**，不是生产依赖
- ROADMAP 未完成项「MFCC on LibriSpeech」与本课关系写清

---

## 7. P2 — 时间断崖回调（分散注入）

不新开复习课；在**首次需要该记忆**的课节开头加「2 分钟复习」格。

| 回调知识点 | 首次注入位置 | 引用课节 |
|-----------|-------------|----------|
| 谱图三轴含义 | L32 开篇 | L03 |
| 方波 = 谐波叠加 | L35 开篇 | L07 |
| `W @ x = fft(x)` | L37 开篇 | L21 |
| 矩阵乘法 = 滤波 | L47 开篇 | L21 |
| 欧拉公式 ↔ 旋转因子 | L38 开篇 | L06, L35 |

**Obsidian 汇总**：在 `docs/current/obsidian/domains/audio-dsp.md` 增加「跃升点导航」节，
每条链到上述 appendix 标题，便于 Graph View 一眼看到孤岛。

---

## 8. P2 — 次级跃升微调

### 7.1 L36 → L37

- L36 补充 **periodic vs symmetric** 窗对照表（审计缺口），与 `aurora.hann(periodic=True)` 对齐
- 明确指出：`np.hanning` ≠ `aurora.hann` 的峰值位置差异

### 7.2 L46 → L47

- L46 末尾加「三角滤波器三锚点」手绘练习（markdown，纸上完成）
- L47 推理路线**删减**完整 for 循环伪代码，改为描述性三步（降答案泄漏）

### 7.3 练习答案泄漏全课扫描（DSP 段）

| 课节 | 动作 |
|------|------|
| L68 式 | L47、L39 五步表改为「步骤名 + 一句话提示」，代码放 solutions |
| L39 | 保留 N=2 手算，但 N=8 分步表改为「自填 E[k]、O[k]」 |

---

## 9. 交付物与验收

### 8.1 完成定义（每项补充）

- [ ] 插入位置明确到 notebook 文件名 + 「某节之前/之后」
- [ ] 新增 code cell 在**桩代码未实现**时仍可运行（或不崩溃）
- [ ] `python scripts/validate_pipeline.py --syntax` 通过
- [ ] 不新增任何 `L100` 或 `L36b` 类文件
- [ ] `week-01/02-checklist.md` 与 notebook 附录交叉引用一致

### 8.2 建议执行顺序

```
周 1：P0 §3（L36–L39）+ week-02 附录 — ✅ 已写回 AURORA（2026-07-01）
周 2：P0 §4（L42–L45）— ✅ 已写回 AURORA（2026-07-01）；脚本 `apply_dsp_week2_l42_l45_supplement.py`
周 3：P1 §5–§6（L31–L32、L48–L51）— 📋 待做
周 4：P2 §7–§8 + Obsidian 导航 + 泄漏扫描 — 📋 待做
```

### 8.3 不在本计划内

- 新建课节或重排 L 编号
- 修改 `src/aurora/audio/` 算法（除非为对齐教学表述的注释/docstring）
- L53→L54、L68→L69 — 见 [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md)、[`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md)

---

## 10. 相关文件索引

| 文件 | 用途 |
|------|------|
| [`gap-supplement-plan.md`](gap-supplement-plan.md) | **全课总索引**、8 周执行顺序 |
| [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) | L53→L54、week-03 |
| [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md) | L68→L69、week-04 |
| `docs/current/audit/02_纵向分析.md` | 断崖原始诊断 |
| `docs/current/course/week-01-checklist.md` | L32–L36 打卡 |
| `docs/current/course/week-02-checklist.md` | L37–L42 打卡 |
| `docs/current/course/prep-checklist.md` | 开课前准备 |
| `docs/current/obsidian/domains/audio-dsp.md` | 概念网汇总 |
| `notebooks/5_audio_dsp/solutions/` | 参考实现归档 |

---

*下一步：人工复审 L36–L45 diff → 提交课程文件 → P1（L31–L32、L48–L51）。补丁脚本：`slideroom/outputs/patches/apply_l36_supplement.py`、`apply_dsp_week1_l37_l39_supplement.py`、`apply_dsp_week2_l42_l45_supplement.py`。*
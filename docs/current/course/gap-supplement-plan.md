# 全课跃升点补充计划（总索引）

> **约束**：不插入新课、不改 L01–L99 标号与顺序。
>
> **背景**：`docs/current/audit/02_纵向分析.md` 识别三处**全课级断崖**（Δ认知 ≥ 2）；
> Audio DSP 段另有六处**模块内跃升**。单课 A- 评级 ≠ 纵向连贯。
>
> **状态**：🟡 执行中（2026-07-01）— DSP / ML / ASR 三份分计划已落地待复审

---

## 1. 三份分计划

| 文档 | ROADMAP Phase | 课节 | 最陡跃升 | 状态 |
|------|---------------|------|----------|------|
| [`dsp-gap-supplement-plan.md`](dsp-gap-supplement-plan.md) | Phase 0 片段 + **Phase 1** | L03–L07、L21、L31–L53 | L37→L39、L43→L44 等 6 处 | 🟡 P0/P1/P2 已落地待复审 |
| [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) | **Phase 2** | L22–L25、L53–L58 | **L53→L54**（全课最陡，Δ=3） | 🟡 已落地待复审 |
| [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md) | **Phase 3** | L24、L27、L67–L71 | **L68→L69**（数学密度最高） | 🟡 已落地待复审 |

**未单列计划**（优先级低于上述三处）：L89→L90 检索范式切换、L92 幻影模块集成——待 DSP/ML/ASR 三计划完成后评估。

---

## 2. 全课防断崖统一标准

与 [`dsp-gap-supplement-plan.md`](dsp-gap-supplement-plan.md) §0.2 相同，适用于 **L32–L71** 所有跃升点：

### 2.1 认知等级（0–3）

| 等级 | 学生活动 |
|------|----------|
| 0 | 看演示 / 可视化，无核心 TODO |
| 1 | 单函数、单循环按公式实现 |
| 2 | 组合 2–3 零件，或推导递推 |
| 3 | 完整算法 / 多段流水线 / 训练系统 |

### 2.2 达标线（全课）

| 编号 | 标准 | 全课达标线 |
|------|------|------------|
| **A1** | 相邻课 Δ认知 | **≤ 1**；允许 Δ=2 的课对见下表，且**必须有桥接格 + checklist** |
| **A2** | 全课级断崖桥接 | **3/3**（L53→L54、L68→L69、L37→L39 作为代表验收） |
| **A3** | 时间断崖回调 | 首次依赖点有 ≤2 分钟复习格（各分计划 § 内清单） |
| **B1** | 无答案泄漏 | 跃升点课推理路线无可粘贴完整实现 |
| **B2** | 可顶到底运行 | 桩未实现时无级联崩溃 |
| **B3** | 半步练习 | 每处 Δ≥2 跃升有 ≥1 个半步格 |
| **B4** | solutions | 主 TODO 课有 `solutions/Lxx_*.md` |

### 2.3 允许 Δ=2 的课对（必须有桥接）

| 课对 | 分计划 | 桥接落点 |
|------|--------|----------|
| L37→L38 | DSP | L36 附录 A、L37 复习桥 |
| L43→L44 | DSP | L42 STFT 过渡、L43 零件清点 |
| **L53→L54** | **ML** | **L53 模式切换附录、L54 链式法则复习** |
| **L68→L69** | **ASR** | **L68 DP 预告、L69 log 域对照** |

**不允许无桥接的 Δ=3**：当前仅 **L53→L54**（0→3）超标，必须通过 L53 附录 + L54 分步半步降至有效 Δ≤2。

---

## 3. 全课级断崖一览

```
难度
  ███████████  L53→L54   信号处理 → 计算图 autograd     [ML 计划]
  ██████████   L68→L69   CTC 直觉 → 前向 DP log 域      [ASR 计划]
  █████████    L37→L39   DFT → Cooley-Tukey FFT         [DSP 计划]
  ████████     L43→L44   STFT 原理 → 手写 my_stft      [DSP 计划]
  ██████       L31→L32   数学 → 音频工程                [DSP 计划]
  ██████       L48→L50   Mel 可视化 → MFCC 流水线        [DSP 计划]
```

---

## 4. 建议执行顺序（8 周）

| 周 | 文档 | 内容 |
|----|------|------|
| 1–2 | DSP §P0 | L36–L44 两处断崖 |
| 3 | DSP §P1 | L31–L32、L48–L51 |
| 4 | DSP §P2 | 时间回调、Obsidian |
| **5** | **ML** | **L53→L54 桥接 + L54 solutions + week-03-checklist** |
| **6** | **ML** | L54 边界测试、L55 衔接复查 |
| **7** | **ASR** | **L68→L69 桥接 + L69 暴力对照 + logaddexp 半步** |
| **8** | **ASR** | L67 回调、L69 边界测试、Obsidian `asr.md` |

每完成一课，在 `ROADMAP.md` 对应 Phase 备注 `supplement ✓`。

---

## 5. 文件索引

```
docs/current/course/
├── gap-supplement-plan.md      ← 本文件（总索引）
├── dsp-gap-supplement-plan.md
├── ml-gap-supplement-plan.md
├── asr-gap-supplement-plan.md
├── week-01-checklist.md        L32–L36
├── week-02-checklist.md        L37–L42
├── week-03-checklist.md        L53–L58（ML 计划新建）
└── week-04-checklist.md        L67–L71（ASR 计划新建）
```

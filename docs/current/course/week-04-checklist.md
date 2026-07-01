# L67–L71 逐日打卡 — CTC 与 Whisper 入门

> 配套 [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md)。课号不变。

---

## 进入 L69 前（25 分钟，必做）

- [ ] 读 `L68_ctc_alignment.ipynb` **附录 C**「L69 预习」
- [ ] 重读 L67 编辑距离 DP 填表逻辑（5 分钟）
- [ ] 运行 L69 开篇 **复习桥**（编辑距离 vs CTC 前向对照）
- [ ] 运行 L69 `logaddexp` 演示 cell
- [ ] 理解：L68 贪婪 ≈ 一条路径；L69 前向 = 所有合法路径 log 概率和

---

## L67 — Edit Distance

- [ ] 手推或实现 Levenshtein DP
- [ ] 读收束：「L69 是同一种填表递推」

---

## L68 — CTC 对齐

- [ ] 实现 `collapse` + `ctc_greedy_decode`（**不**复制推理路线全文 Python）
- [ ] 读 Section 6 单调路径 + 附录 C
- [ ] 可选：阅读 T=3 路径枚举演示 cell

---

## L69 — CTC 前向算法

- [ ] **先**完成或读懂「半步练习 B」`ctc_forward_brute_force`
- [ ] **再**实现 `ctc_forward` 三段 TODO（初始化 / 递推 / 终态 logaddexp）
- [ ] DP 与暴力 `atol ≤ 1e-5`
- [ ] 边界：空 `labels`、T 过短
- [ ] 卡住 → 附录 C / 复习桥 / `solutions/L69_ctc_forward_solutions.md`

---

## L70 — Whisper 架构

- [ ] 开篇：Whisper 用交叉熵，非 CTC 训练目标；L68–L69 是序列对齐基线

---

## 本周末检查

- [ ] `l68_review`、`l69_review` 自评已填
- [ ] 能口头解释 blank 的两个作用 + collapse 两步
- [ ] 能写出 log 域递推一行（logaddexp 三前驱）
- [ ] ROADMAP Phase 3 备注 `supplement L68–L69 ✓`（维护者）
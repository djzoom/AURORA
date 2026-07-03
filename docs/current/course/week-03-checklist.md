# L53–L58 逐日打卡 — 计算图与 MLP

> 配套 [`ml-gap-supplement-plan.md`](../../archive/2026-07/ml-gap-supplement-plan.md)（已完成，归档）。课号不变；预习项与 notebook 附录标题一致。

---

## 进入 L54 前（30 分钟，必做）

- [ ] 读 `L53_visual_mfcc.ipynb` **附录 A**「前向特征 → 反向学习」
- [ ] 浏览 **附录 B** MFCC shape 口诀（回调 L50）
- [ ] 重跑 `L54` 开篇 **复习桥** code cell（链式法则手算，或重读 L24）
- [ ] 阅读 L54 **模式对照表**（MFCC ndarray vs Value 标量）
- [ ] 确认环境：纯 Python，本段不用 numpy（L54）

---

## L53 — MFCC 图形化（若未结业）

- [ ] 跑通 `mfcc()` 全链路热力图
- [ ] 完成 DCT 重构误差可选练习
- [ ] 读完附录 A/B 再点「下一课 L54」

---

## L54 — Value 计算图

- [ ] **先**完成「半步练习 A」（仅 `__init__` / `__add__` / `__mul__` 前向）
- [ ] **再**实现完整 `Value` + `backward()`（参考 cell 6 `topo()`）
- [ ] 通过 `a+a` 梯度累积断言（`grad == 2`）
- [ ] 卡住 → 复习桥 / 半步 A / `solutions/L54_value_autograd_solutions.md`

---

## L55 — Value 算子补全

- [ ] 开篇确认：补全 `tanh` / `relu` / `exp`（L54 动机例题的缺口）
- [ ] 实现 `__pow__` 等算子

---

## L56–L58 — 反向传播与训练循环

- [ ] L58 开篇：清点 `Value` + `Neuron` + 损失 + 优化器（零件表）
- [ ] 准备进入 L59 PyTorch（模块切换）

---

## 本周末检查

- [ ] `l54_review` 自评五键已填
- [ ] 能白板画出 `z=x*y+y²` 的计算图并写 `dz/dx`、`dz/dy`
- [ ] ROADMAP Phase 2 备注 `supplement L53–L54 ✓`（维护者）
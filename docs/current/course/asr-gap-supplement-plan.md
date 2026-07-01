# ASR 跃升点补充计划（L68→L69 及 Phase 3 CTC 段）

> **约束**：不插入新课、不改 L01–L99 标号与顺序。
>
> **背景**：`02_纵向分析.md` 将 **L68→L69** 标为**全课数学密度最高跃升**：
> L68 为 CTC 贪婪解码与 collapse 直觉（等级 1–2），L69 要求 log 域前向 DP、
> `logaddexp`、扩展标签与三路递推（等级 3）。审计曾评 L69 可运行性与验证薄弱。
>
> **关联**：总索引 [`gap-supplement-plan.md`](gap-supplement-plan.md)
>
> **状态**：📋 下一步计划（2026-07-01）

---

## 0. 防断崖目标（Phase 3 CTC 段）

### 0.1 本计划涵盖范围

| ROADMAP Phase | 课节 | 涵盖 |
|---------------|------|------|
| Phase 0（回调） | L27–L29 | **部分** — 概率期望、log 概率直觉 |
| Phase 2（回调） | L24 | **部分** — 递推与链式结构类比 |
| Phase 3 | **L66–L71** | **核心 L67–L69**；L66/L70+ 仅衔接项 |

**不涵盖**：L72 Whisper 微调、L71 beam search 深度（另有 per_lesson 审计项）。

### 0.2 验收标准（L67–L69 段）

| 编号 | 标准 | 达标线 |
|------|------|--------|
| **S1** | L68→L69 有效 Δ认知 | 经桥接后 **≤ 2**（L69 拆为 log 域预习 + 暴力枚举半步 + DP 主 TODO） |
| **S2** | L67 DP 显式回调 | L69 开篇有「L67 编辑距离 DP → CTC 前向 DP」对照 |
| **S3** | log 域公式与代码一致 | L69 cell 1 概率域公式下有 log 域等价 + `np.logaddexp` 示例 |
| **S4** | 暴力对照验证 | L69 `ctc_forward_brute_force` 与 DP 在玩具例上 `atol≤1e-5` |
| **S5** | 可顶到底运行 | L69 桩为分段 TODO + placeholder；演示 cell 有 try/except |
| **S6** | L68 无答案泄漏 | `ctc_greedy_decode` 推理路线删完整 Python 去重表达式 |
| **S7** | week-04-checklist | L68→L69 预习项可搜 |

**完成画像**：

> 学生在 L68 已见「单调路径 → DP 预告」；进 L69 先懂 log 域，再用 T≤4 暴力验证 DP；
> 主 `ctc_forward` 有三段 TODO（初始化 / 递推 / 终态聚合）。

---

## 1. 断崖诊断：L68→L69

| 维度 | L68 | L69 |
|------|-----|-----|
| 认知等级 | 1–2（贪婪解码、collapse） | 3（前向算法、log-sum） |
| 核心操作 | `argmax` + 过滤 | 动态规划 + `logaddexp` |
| 数学 | 路径概率乘积（直觉） | log 域加法、扩展标签 `l'` |
| 验证 | 离散 argmax 断言 | 需 DP vs 暴力对照 |
| 前驱 | L67 编辑距离 DP（**应显式回调**） | 隐含需 L27–L29 概率期望 |

**L66 教学顺序问题**（本计划顺带修）：L66 曾要求 DP 而 L67 才讲——在 L69 计划中不新增课，仅在 **L66 收束** 加「WER 实现请等 L67 后再做」。

---

## 2. P0 — L68 补强（为 L69 着陆）

### 2.1 L68 Section 6 扩充 · DP 预告（已有则加强）

**位置**：`L68_ctc_alignment.ipynb`，单调路径 cell 之后、本课收束之前。

**标题**：`## 附录 C · 从贪婪解码到前向算法：L69 预习（8 分钟）`

**要点**：

1. **L68 做了什么**：找**一条**最优路径（贪婪近似）。
2. **L69 要做什么**：对**所有**合法路径的概率**求和**（精确训练损失）。
3. **为何需要 DP**：路径数 O(V^T)；DP 降到 O(T·S)，S=2L+1。
4. **与 L67 的关系**：编辑距离 DP 也是「填表递推」；CTC 是「log 概率填表」。
5. **log 域一句**：概率相乘 → log 域用 `logaddexp` 做「log 下的加法」。

**ASCII 表结构预告**（markdown）：

```text
        s=0   s=1   s=2   …   (扩展标签轴)
t=0     α     ·     ·
t=1     ·     ·     ·
…
```

### 2.2 L68 · 手工 T=3 路径枚举格（半步，B3）

**位置**：附录 C 之后。

**code cell**（只读演示，无学生 TODO）：

- T=3，标签 `ab`，blank=0，固定 logits 使路径可手算
- 枚举 ≤27 条路径 → collapse → 过滤 → 与「正确答案集合」对照
- 末行：`精确求和需要 L69 的 ctc_forward`

### 2.3 L68 练习 · 降答案泄漏（S6）

**位置**：`ctc_greedy_decode` 任务说明 cell。

**删除**：

```python
deduped = [p for i,p in enumerate(preds) if i==0 or p!=preds[i-1]]
```

**改为描述性三步**：

1. 每帧取 `argmax` 得长度 T 序列
2. 第一次过滤：去掉何种相邻重复？
3. 第二次过滤：去掉 blank 后得到什么？

完整实现 → `solutions/L68_ctc_alignment_solutions.md`（若不存在则创建）。

### 2.4 L68 · 删除无用 `import torch`

改为 markdown 注：`训练时用 torch.nn.CTCLoss`；本课手写解码，**本 notebook 不需 torch**。

或增加只读 cell 展示 `CTCLoss` 签名（不执行 GPU）。

### 2.5 L68 导航 cell

```markdown
→ **下一课** [L69 · CTC 前向算法](...)
> **必读**：本课附录 C「L69 预习」；建议先复习 L67 的 DP 填表。
```

### 2.6 L67 收束 · 前向引用

**位置**：`L67_edit_distance.ipynb` 收束。

加一句：「L69 的 CTC 前向算法是同一种『填表递推』思想，在 log 概率域求路径总和。」

---

## 3. P0 — L69 开篇与实现（断崖着陆）

### 3.1 L69 开篇 · L67 DP 复习桥

**位置**：`L69_ctc_forward.ipynb`，学习目标之后。

**标题**：`## 复习桥 · L67 编辑距离 DP → CTC 前向 DP（5 分钟）`

| | L67 编辑距离 | L69 CTC 前向 |
|---|-------------|--------------|
| 表维度 | `(len_a+1, len_b+1)` | `(T, S)`，S=2L+1 |
| 递推 | min(删/插/替) | logsumexp(三前驱) + log p |
| 目标 | 最小编辑代价 | 所有路径 log 概率和 |
| 输出 | 整数距离 | 标量 log 概率 |

**code cell**：打印 L67 与 L69 的「填表」伪代码并排（markdown 或注释块）。

### 3.2 L69 cell 1 · 概率域 + log 域双写（S3）

在概率域递推公式后**紧接**：

```markdown
### Log 域等价（实现用此式）

log α[t,s] = log p[t,l'[s]] + logaddexp(
    log α[t-1,s],      # 停留
    log α[t-1,s-1],    # 跳一步
    log α[t-1,s-2]     # 跳两步（仅当 l'[s]≠l'[s-2]）
)

`np.logaddexp(a,b)` = log(exp(a)+exp(b))，数值稳定。
```

**code cell** 演示：

```python
import numpy as np
a, b = np.log([0.3, 0.7])
assert np.isclose(np.logaddexp(a, b), np.log(1.0))
```

### 3.3 L69 · 半步练习 B：暴力枚举（S4 前置）

**位置**：`ctc_forward` TODO **之前**。

**标题**：`## 半步练习 B · ctc_forward_brute_force（先写/先读此函数）`

**规格**：

```python
def ctc_forward_brute_force(log_probs, labels, blank):
    """T,V ≤ 小，枚举所有长度 T 路径，collapse 后匹配 labels 的求 logsumexp。"""
    raise NotImplementedError
```

- 参考实现放 **solutions** 或教师 cell（学生可先读再写 DP）
- 玩具例 T=4, L=2 断言有限且 < 0

**目的**：学生先理解「求和的对象是什么」，再写 DP。

### 3.4 L69 主练习 · 三段 TODO 骨架（S5）

**禁止**整函数体 `raise NotImplementedError` 一处挡死。

**结构**：

```python
def ctc_forward(log_probs, labels, blank=0):
    # --- 步骤 0：构造 lprime（已给出或 TODO 0）---
    # --- TODO 1：初始化 alpha[0, :] ---
    # --- TODO 2：for t in 1..T-1: 三路 logaddexp 递推 ---
    # --- TODO 3：return logaddexp(alpha[T-1,S-1], alpha[T-1,S-2]) ---
    ...
```

每段旁注「卡住 → 读附录 C / 半步 B / solutions」。

### 3.5 L69 验证格 · DP vs 暴力（S4）

```python
lp_dp = ctc_forward(log_probs_toy, LABELS, blank=BLANK)
lp_bf = ctc_forward_brute_force(log_probs_toy, LABELS, blank=BLANK)
assert np.isclose(lp_dp, lp_bf, atol=1e-5), f'DP={lp_dp}, brute={lp_bf}'
```

另加边界：

- `labels=[]`，T=3 → 有限 log 概率
- `T < len(labels)` → 文档约定返回 `NEG_INF` 或 `ValueError`

### 3.6 L69 · log-softmax 稳定写法

统一用手写稳定版（不引入 scipy）：

```python
def log_softmax(logits, axis=-1):
    m = logits.max(axis=axis, keepdims=True)
    return logits - m - np.log(np.exp(logits - m).sum(axis=axis, keepdims=True))
```

替换 cell 3/8 中不稳定写法。

### 3.7 L69 · Aurora 连接

```markdown
🔗 **Aurora 连接（计划）**：`ctc_forward` 将迁入 `src/aurora/speech/ctc.py`；
与 `aurora.speech.metrics`（WER）同属 ASR 训练/评估链。Whisper 训练用交叉熵（L70），
CTC 是理解「无对齐序列损失」的通用基线。
```

### 3.8 L69 复杂度表述统一

标题/正文统一为 **O(T·S)**，S = 2L+1；避免「2L」与「2L+1」混用。

---

## 4. P1 — Phase 0 概率回调

| 课节 | 修改 |
|------|------|
| **L28** | 收束：「期望 E[f(X)] 的求法将在 L68 压缩率分析出现」 |
| **L29** | 收束：「分类分布下概率连乘 → log 域求和，见 L69」 |

**L68 压缩率**（已修 ~93%）保留作期望练习实例。

---

## 5. P1 — L66/L70 衔接

| 课节 | 修改 |
|------|------|
| **L66** | 收束：「`compute_wer` 依赖 L67 DP，请 L67 后再实现 WER 练习」 |
| **L70** | 开篇：「Whisper 用交叉熵而非 CTC；L68–L69 是理解序列对齐的基线」 |

---

## 6. P2 — checklist 与 Obsidian

### 6.1 新建 `week-04-checklist.md`

```markdown
# L67–L71 逐日打卡 — CTC 与 Whisper 入门

## 进入 L69 前（25 分钟，必做）

- [ ] 读 L68 附录 C「L69 预习」
- [ ] 重读 L67 DP 填表逻辑（5 分钟）
- [ ] 运行 L69 复习桥「编辑距离 vs CTC」对照
- [ ] 理解 logaddexp 演示 cell

## L68 — CTC 对齐

- [ ] 实现 collapse + ctc_greedy_decode（无复制粘贴推理路线）
- [ ] 单调路径与压缩率实验

## L69 — CTC 前向

- [ ] 先完成/读懂半步 B 暴力枚举
- [ ] 再实现 ctc_forward 三段 TODO
- [ ] DP 与暴力 atol≤1e-5
- [ ] 边界：空 labels、T 过短
```

### 6.2 Obsidian

`docs/current/obsidian/domains/asr.md` 增加跃升点链：

`[[L67 编辑距离]]` → `[[L68 附录 C]]` → `[[L69 复习桥]]` → `[[L70 Whisper]]`

---

## 7. 分期修改总表

| 课节 | 修改项 | 优先级 |
|------|--------|--------|
| L66 | 收束：WER 练习等 L67 | P1 |
| L67 | 收束：CTC 前向 DP 预告 | P1 |
| **L68** | **附录 C L69 预习 + T=3 枚举演示** | **P0** |
| L68 | 贪婪解码推理降泄漏；删/改 torch | P0 |
| L68 | 导航 + solutions/L68 | P0 |
| **L69** | **L67 复习桥 + log 域双写 + logaddexp demo** | **P0** |
| L69 | 半步 B 暴力枚举 + 三段 TODO 骨架 | P0 |
| L69 | DP vs 暴力验证 + 边界测试 | P0 |
| L69 | 稳定 log_softmax；复杂度 O(T·S) | P1 |
| L69 | Aurora 连接文案 | P1 |
| L70 | Whisper vs CTC 开篇一句 | P1 |
| L28、L29 | 收束前向引用 | P2 |
| — | `week-04-checklist.md` 新建 | P0 |
| — | `solutions/L69_ctc_forward_solutions.md` | P0 |
| — | Obsidian asr 导航 | P2 |

---

## 8. 交付验收

- [ ] L68 附录 C 可搜；L69 复习桥可搜
- [ ] L68 推理路线无完整去重 Python
- [ ] L69 未完成 TODO 时，演示/暴力 cell 仍可运行（try/except 或读 solutions）
- [ ] 玩具例 DP 与暴力 `atol≤1e-5`
- [ ] `validate_pipeline.py --syntax` 通过
- [ ] 自测：`T(L69 主练习) / T(L69 半步B) ≤ 3`

---

## 9. 执行顺序

```
周 7：L68 附录 C + 降泄漏 + L69 复习桥 + log 域 + 半步 B
周 8：L69 三段 TODO 验证 + 边界 + week-04-checklist + L66/L67/L70 衔接
```

*完成后在 `ROADMAP.md` Phase 3 备注 `supplement L68–L69 ✓`。*
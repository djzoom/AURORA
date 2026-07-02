# ML 跃升点补充计划（L53→L54 及 Phase 2 入口）

> **约束**：不插入新课、不改 L01–L99 标号与顺序。
>
> **背景**：`02_纵向分析.md` 将 **L53→L54** 标为**全课程最陡认知跃升**（Δ=3）：
> L53 仍在 MFCC 可视化（等级 0），L54 立即要求手写 `Value` 计算图 + 拓扑排序 `backward()`（等级 3）。
> 学生从「音频工程师」切换到「autograd 编译器作者」，且无过渡课。
>
> **关联**：总索引 [`gap-supplement-plan.md`](gap-supplement-plan.md)
>
> **状态**：🟡 已落地待复审（2026-07-01）— L53→L54 / L55–L59 / week-03 / deep-learning 导航已回写

---

## 0. 防断崖目标（Phase 2 入口）

### 0.1 本计划涵盖范围

| ROADMAP Phase | 课节 | 涵盖 |
|---------------|------|------|
| Phase 0（回调） | L22–L25 | **部分** — 链式法则/梯度回调锚点 |
| Phase 1（出口） | **L52、L53** | **全部** — Audio DSP 收束 → ML 入口 |
| **Phase 2** | **L54–L58** | **入口段** — autograd + MLP 链；L59+ 仅列衔接项 |

**不涵盖**：L62 shape、KWS 训练（另有审计修复跟踪）；L59–L65 PyTorch 段坡度相对平缓。

### 0.2 验收标准（L53–L58 段）

在 DSP 计划 §0.2 通用标准上，增加：

| 编号 | 标准 | 达标线 |
|------|------|--------|
| **M1** | L53→L54 有效 Δ认知 | 经桥接后 **≤ 2**（L54 拆为「读链式法则复习 + 半步 forward + 主 TODO backward」） |
| **M2** | 微积分前驱显式回调 | L54 开篇有 L24 链式法则 **≤5 分钟**复习格 |
| **M3** | `Value` 可落地 | `solutions/L54_value_autograd_solutions.md` 存在；可选 `src/aurora/ml/value.py` 与 notebook 对齐 |
| **M4** | 梯度累积断言 | L54 含 `a+a` → `grad==2` 测试 |
| **M5** | 拓扑排序提示 | L54 `backward()` TODO 明确指向 cell 6 `topo()` |
| **M6** | week-03-checklist | L53→L54 预习项与 notebook 附录标题可搜 |

**完成画像**：

> 学生读完 L53 附录后知道「下模块学训练而非特征」；L54 先复习 L24 再半步再主练习；
> 卡住可回 solutions；**不要求**先学完 PyTorch 再碰 `Value`。

---

## 1. 断崖诊断：L53→L54

| 维度 | L53 | L54 |
|------|-----|-----|
| 认知等级 | 0（可视化 B+） | 3（手写 autograd） |
| 思维模式 | 信号 → 谱 → 系数（前向流水线） | 计算图、反向传播、拓扑序 |
| 语言 | NumPy 数组、aurora.audio | 纯 Python 标量、`__add__` 重载 |
| Aurora 连接 | `aurora.audio.mfcc` ✅ | `src/aurora/ml/` ❌ 不存在 |
| 前驱 | L50 流水线 | 应依赖 L24 链式法则，但**无显式回调** |

**本质**：不是「多学一个公式」，而是**问题域切换**——从「提取特征」到「用梯度更新参数」。

---

## 2. P0 — L53 收束（模块出口桥接）

### 2.1 L52 收束 · Phase 1 毕业证

**位置**：`L52_features_done.ipynb`，「本课收束」之前。

**标题**：`## 附录 · Audio Core 结业：你已具备的能力清单`

**内容**（checkbox 列表）：

- [ ] 能从空白重写 `fft` / `stft` / `mel_filterbank` / `mfcc`（口述 + 白板）
- [ ] `make test` audio 全绿
- [ ] 能解释 MFCC 五段 shape：`(T, n_mels)` → `(T, 13)`
- [ ] **下一步不是更多 DSP**，而是 **L54：学模型如何从新数据中学习**

### 2.2 L53 收束 · 模式切换附录（核心桥接）

**位置**：`L53_visual_mfcc.ipynb`，cell「本课收束」之前、「下一课 L54」导航之前。

**标题**：`## 附录 A · 进入深度学习：从「前向特征」到「反向学习」（必读，10 分钟）`

**markdown 要点**：

1. **L32–L53 你在做什么**：固定变换（FFT/Mel/MFCC）——输入音频，输出向量；**权重不变**。
2. **L54 起你在做什么**：带**可学习参数**的模型；用**损失函数**衡量错多少；用**梯度**告诉参数往哪改。
3. **同一门数学**：L53 的 DCT 是前向矩阵乘法；L54 的 `backward()` 是问「若损失变一点，哪个参数该动」——即 L24 链式法则的代码版。
4. **不必先学 PyTorch**：L54–L58 用自写 `Value` 理解 `loss.backward()`；L59 才切 PyTorch。
5. **心理句**：`我学完 MFCC，是为了给 L62 的 CNN 准备输入；我学完 L54，是为了让 CNN 能从错误中学习。`

**可选 code cell**（只读，无 TODO）：

```python
# 感受「学习」与「特征」的区别（无需实现）
# 特征：y = mfcc(x)           — 无参数
# 学习：loss = (w*x - y)**2   — 要算 d_loss/d_w
```

### 2.3 L53 · 与 L50 流水线对照格

**位置**：附录 A 之后。

**标题**：`## 附录 B · MFCC 流水线最后一眼（回调 L50）`

一行 shape 口诀（与 DSP 计划 L45/L50 一致），强调 **L54 不再处理音频数组**，而是 **标量计算图**。

### 2.4 L53 导航 cell 修改

将「下一课 L54」描述从单纯「Value 计算图」扩展为：

```markdown
→ **下一课** [L54 · Value 计算图](...)
> **模块切换**：先读 L54 开篇「链式法则复习」（2 分钟），再开始 `Value` 实现。
> 若感到突兀，回到本课附录 A。
```

---

## 3. P0 — L54 开篇与练习（断崖着陆）

### 3.1 L54 开篇 · L24 链式法则复习桥（核心）

**位置**：`L54_value_autograd.ipynb`，cell 0 学习目标之后、剧情引入之前。

**标题**：`## 复习桥 · L24 链式法则（5 分钟，不跳过）`

**内容**：

- 公式：`z = f(g(x))` → `dz/dx = (dz/dg)·(dg/dx)`
- 手算例题：`z = x*y + y²`，`x=3,y=2` → `dz/dx=2`，`dz/dy=7`（与 L54 断言一致）
- 明示：**本课用代码自动做上述乘法**；你实现的是「每个节点存局部偏导」

**code cell**（运行即复习）：

```python
x, y = 3.0, 2.0
z = x * y + y**2
dz_dx = y          # 2
dz_dy = x + 2*y    # 7
assert z == 10 and dz_dx == 2 and dz_dy == 7
print('链式法则手算与 L54 断言一致')
```

### 3.2 L54 · 模式对照表

**位置**：复习桥之后。

| | L53 MFCC | L54 Value |
|---|----------|-----------|
| 数据类型 | `ndarray (T, 13)` | 标量 `float` |
| 方向 | 仅前向 | 前向 + 反向 |
| 目标 | 压缩表示 | 自动求 `dL/d参数` |
| 库 | aurora.audio | 本课自写（L59 换 PyTorch） |

### 3.3 L54 cell 1 · tanh 动机脚注

在 `L = tanh(a*b + b**2)` 例题末尾加：

> 本课实现 `add` / `mul` / `pow`；`tanh` 在 **L55** 补全。下方手算例题用 `z = a*b + b²` 即可跑通。

### 3.4 L54 cell 4 · 梯度累积演示修正

加注释：`# 设 a=3.0, b=3.0`；或改为 `a_val, b_val = 3.0, 3.0` 显式计算。

### 3.5 L54 · 半步练习：仅 forward 的 Value（B3）

**位置**：cell 9 推理路线之前。

**标题**：`## 半步练习 A · 只做前向（15 分钟）`

**要求**：仅实现 `__init__`、`__add__`、`__mul__`（**不含** `_backward` / `backward`）。

**验证**：

```python
a, b = Value(2.0), Value(3.0)
assert (a + b).data == 5.0
assert (a * b).data == 6.0
```

**提示**：完成后再做完整 TODO；卡住不算失败。

### 3.6 L54 cell 9 · backward 与 cell 6 拓扑连接

在 `backward()` 推理路线末加：

```text
提示：拓扑排序参考本课 cell 6 的 topo()——DFS 收集后序，再 reverse。
```

### 3.7 L54 主练习 · 降泄漏

将五步推理路线改为：

| 步骤 | 提示（不给完整代码） |
|------|---------------------|
| 1 | `__init__`：存 data/grad/children/op |
| 2 | `__add__`：构造新 Value，`_backward` 里写 `self.grad += out.grad` |
| 3 | `__mul__`：局部偏导 `d(a*b)/da=b`，`d(a*b)/db=a` |
| 4 | `__pow__`：幂法则 |
| 5 | `backward`：拓扑序逆序调 `_backward` |

完整代码 → `solutions/L54_value_autograd_solutions.md`（**待创建**）。

### 3.8 L54 验证格 · 边界测试（M4）

在现有断言后追加：

```python
# 同节点多路径梯度累积
a4 = Value(3.0)
L4 = a4 + a4
L4.backward()
assert a4.grad == 2.0, '两条路径梯度应相加'
```

可选：`Value(0.0) * b` 梯度为 0。

### 3.9 L54 cell 17 · 修正 Aurora 连接

删除或改正 `from aurora.llm.autograd import Value`（模块不存在）。

改为：

```markdown
🔗 **Aurora 连接（计划）**：`Value` 将迁入 `src/aurora/ml/value.py`（Phase 2）；
当前权威实现见本 notebook TODO 与 `solutions/L54_value_autograd_solutions.md`。
L62 的 KWS 训练最终使用 PyTorch autograd，但 L54 是理解 `backward()` 的必经台阶。
```

**可选仓库工作**（不强制，但满足 M3）：

- 新建 `src/aurora/ml/__init__.py` + `value.py`（从 solutions 同步，仅 add/mul/pow）
- `tests/ml/test_value.py`：与 notebook 相同断言

### 3.10 L54 每个主 TODO 旁 · 卡住回退

```text
卡住 → 读本课「复习桥 L24」/「半步练习 A」/ solutions/L54
```

---

## 4. P1 — Phase 0 时间回调（支撑 L54）

| 课节 | 修改 | 位置 |
|------|------|------|
| **L24** | 收束加：「L54 将把链式法则变成 `Value.backward()`」 | 本课收束 |
| **L25** | 收束加：「梯度下降更新公式将在 L58 与 `Value` 汇合」 | 本课收束 |
| **L30** | 收束加：「交叉熵梯度将在 L58 损失函数课出现」 | 本课收束 |

不在 L22–L23 大改——仅收束一句前向引用。

---

## 5. P1 — L55–L58 衔接（防二次跌落）

| 课节 | 修改 | 说明 |
|------|------|------|
| **L55** | 开篇回调：「L54 的 `Value` 缺 tanh/relu/exp，本课补全」 | 避免 L54 未完成就跳 L55 |
| **L58** | 开篇「零件清点」：`Value` + `Neuron` + 损失 + 优化器步 | 类比 L43 STFT 零件表 |
| **L59** | 开篇「模块切换」：自写 autograd → PyTorch 张量；对应关系表 | 第二次模式切换，轻度桥接 |

**L54→L55 坡度**：Δ=1（补算子），一般可接受；L55 solutions 已存在，保持即可。

---

## 6. P2 — checklist 与 Obsidian

### 6.1 新建 `week-03-checklist.md`

```markdown
# L53–L58 逐日打卡 — 计算图与 MLP

## 进入 L54 前（30 分钟，必做）

- [ ] 读 L53 附录 A「前向特征 → 反向学习」
- [ ] 重跑 L24 链式法则例题（或 L54 复习桥 code cell）
- [ ] 浏览 L54「模式对照表」
- [ ] 确认纯 Python 环境（本课不用 numpy）

## L54 — Value 计算图

- [ ] 先完成「半步练习 A」前向
- [ ] 再实现完整 `Value` + `backward`
- [ ] 通过 `a+a` 梯度累积断言
- [ ] 卡住查 solutions/L54_value_autograd_solutions.md

## L55–L58 — …（按 notebook 推进）
```

### 6.2 Obsidian

在 `docs/current/obsidian/domains/deep-learning.md`（若无则建）增加：

- `[[L53 附录 A]]` → `[[L54 复习桥]]` → `[[L24 链式法则]]`
- 标签 `#跃升点` `#面试高频`

---

## 7. 分期修改总表

| 课节 | 修改项 | 优先级 |
|------|--------|--------|
| L52 | 附录「Audio Core 结业清单」 | P1 |
| **L53** | **附录 A 模式切换 + 附录 B shape 回调** | **P0** |
| L53 | 导航 cell 扩展 | P0 |
| **L54** | **L24 复习桥 + 模式对照表** | **P0** |
| L54 | 半步练习 A（仅 forward） | P0 |
| L54 | 推理路线降泄漏；backward↔topo 提示 | P0 |
| L54 | `a+a` 梯度测试；修正 aurora.llm.autograd 死链 | P0 |
| L54 | 创建 `solutions/L54_value_autograd_solutions.md` | P0 |
| L54 | 可选 `src/aurora/ml/value.py` | P2 |
| L24、L25、L30 | 收束前向引用一句 | P1 |
| L55、L58、L59 | 开篇衔接格 | P1 |
| — | `week-03-checklist.md` 新建 | P0 |
| — | Obsidian deep-learning 跃升点导航 | P2 |

---

## 8. 交付验收

- [ ] L53 附录 A 标题可在 notebook 内 `Ctrl+F` 搜到
- [ ] L54 复习桥 code cell 手算断言通过
- [ ] 半步练习 A 与主 TODO 分离；主 TODO 未完成时半步仍可运行
- [ ] `solutions/L54_value_autograd_solutions.md` 存在
- [ ] `validate_pipeline.py --syntax` 通过
- [ ] 自测：读完 L53 附录 + L54 复习桥后，`T(L54 主练习) / T(L54 半步) ≤ 4`

---

## 9. 执行顺序

```
周 5：L53 附录 A/B + L54 复习桥 + 半步 A + solutions/L54 — ✅ 已落地待复审（2026-07-01）
周 6：L54 边界测试 + Aurora 连接文案 + week-03-checklist + L55/L58 衔接 — ✅ 已落地待复审（2026-07-01）
```

*完成后在 `ROADMAP.md` Phase 2 备注 `supplement L53–L54 ✓`。*
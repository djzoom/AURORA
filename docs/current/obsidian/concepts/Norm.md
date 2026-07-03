---
tags: [aurora, concept, linear-algebra, interview]
aliases: [Norm, 范数, L1, L2, L∞, 向量长度, normalize, 归一化]
domain: linear-algebra
whiteboard: ★★★★
first_seen: L11
mastered: L11
---

# Norm · 范数（Norm）

[[_lifecycle|← 生命周期总表]] · [[../domains/linear-algebra|← Linear Algebra 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：给向量量一个"长度"——但量法不止一种，直线距离是 L2、街区距离是 L1、最长的那一步是 L∞，选哪把尺子取决于任务。

---

## 📖 定义
范数是把向量映射到一个非负实数、满足"长度"公理的函数。三把常用尺子：
- **L1**：`‖v‖₁ = Σ|vᵢ|`（街区/曼哈顿距离，鼓励稀疏）
- **L2**：`‖v‖₂ = √(Σvᵢ²) = √(v·v)`（欧氏/直线距离，最常用）
- **L∞**：`‖v‖∞ = max|vᵢ|`（最坏分量）

归一化 `normalize(v) = v / ‖v‖₂` 把向量压到单位球上（长度变 1，方向不变）。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** "两个 embedding 差多远""这个梯度更新多大""权重是不是太大了"——没有长度的度量就无法回答。
- **它解决了什么真实问题？** 用地图量距离有多种走法：鸟飞（L2）、出租车沿街（L1）、国王走棋（L∞）。不同任务要不同尺子：L2 做几何距离与权重衰减，L1 求稀疏与抗异常值，L∞ 给最坏误差界。
- **它是相似度与正则化的地基。** [[Cosine-Similarity|余弦相似度]] 要除以两个 L2 范数；L2 正则（weight decay）就是惩罚权重的 L2 范数。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L09  向量"长度"首次出现
正式动机     L11  量距离有多种尺子
拆解原理     L11  L1 / L2 / L∞ 三种定义
真正掌握     L11  ★ 手写 normalize，白板挑战（8 分钟）
再次使用     L10  余弦相似度 = 点积 ÷ 两个范数
再次使用     L47  MFCC 特征归一化
再次使用     L58  L2 正则 / weight decay
最终应用     L80  embedding L2 归一化后做检索
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学范数之前你得先会
```
Norm
 ├─ 需要 → 向量与分量           (L09)
 ├─ 需要 → [[Dot-Product|点积]]（L2=√(v·v)） (L10)
 └─ 需要 → 平方根 / 绝对值        (基础)
被谁依赖 → [[Cosine-Similarity|余弦相似度]] · 正则化 · 特征归一化 · LayerNorm
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **L1 vs L2 vs L∞** | 三种长度 | L1 抓稀疏、L2 抓几何、L∞ 抓最坏分量 |
| **范数 vs 距离** | 长度 vs 两点差 | 距离 = **差向量的范数** `‖a−b‖` |
| **归一化 vs 标准化** | ÷范数 vs 减均值除标准差 | 归一化只改长度；标准化改分布 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — L11 手写 normalize + 白板挑战，必须做到：
- ✅ 写出 L1/L2/L∞ 定义并手算一个例子（如 (3,4)→L2=5）
- ✅ 实现 `normalize`，说明 `‖v‖=0` 的边界处理
- ✅ 讲清 L1 稀疏 vs L2 平滑的梯度差异

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#LinearAlgebra`
> 常见追问："L1 为什么产生稀疏？""weight decay 惩罚的是哪个范数？"

## 🌍 现实系统里它在哪发挥作用
embedding 检索前的 L2 归一化 · 权重衰减 / Lasso · 梯度裁剪 · LayerNorm / BatchNorm · 特征标准化

## 📚 出现于（反查）
[[../lessons/L09]] · [[../lessons/L10]] · **[[../lessons/L11]]** · [[../lessons/L25]] · [[../lessons/L47]] · [[../lessons/L58]] · [[../lessons/L80]] · [[../lessons/L83]]

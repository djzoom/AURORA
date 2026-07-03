---
tags: [aurora, concept, linear-algebra, interview]
aliases: [Dot Product, 点积, 内积, dot product, inner product, a·b]
domain: linear-algebra
whiteboard: ★★★★
first_seen: L09
mastered: L10
---

# Dot-Product · 点积（Dot Product）

[[_lifecycle|← 生命周期总表]] · [[../domains/linear-algebra|← Linear Algebra 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把两个向量对应位置相乘再全加起来，得到**一个数**——这个数告诉你它们"方向有多一致"，是整个深度学习里出现最频繁的运算。

---

## 📖 定义
点积（内积）把两个等长向量压成一个标量：`a·b = Σᵢ aᵢbᵢ = ‖a‖·‖b‖·cosθ`。代数上是逐项相乘求和，几何上是"一个向量投影到另一个上的长度 × 另一个的长度"。符号：正 → 大体同向，零 → 垂直（正交），负 → 反向。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 要判断"两首歌像不像""这个词和那个词相关不相关"，没有一个统一的数值标尺就无从下手。
- **它解决了什么真实问题？** Spotify 把每首歌描述成向量（genre, tempo, energy…），用点积测"方向有多接近"，正数就推、负数就避。它把**相似度**这件事变成一次乘加。
- **它是一切的地基。** 矩阵乘法是逐行点积、[[DFT]] 是信号与复指数的点积、注意力是 Query 与 Key 的点积——学会它，后面全是它的复用。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L09  向量运算里首次出现
正式动机     L10  音乐推荐："有多像"要能量化
拆解原理     L10  a·b=Σaᵢbᵢ = ‖a‖‖b‖cosθ 的双重含义
真正掌握     L10  ★ 手写点积/余弦，白板挑战（8 分钟）
再次使用     L12  矩阵×向量 = 逐行点积
再次使用     L37  DFT：信号与复指数基的点积
再次使用     L80  余弦相似度 k-NN 检索
最终应用     L83  Self-Attention 的 QKᵀV 全是点积
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学点积之前你得先会
```
Dot-Product
 ├─ 需要 → 向量与分量           (L09)
 ├─ 需要 → 逐元素乘 + 求和       (L09)
 └─ 需要 → cosθ 的几何直觉       (L04)
被谁依赖 → [[Matrix-Multiplication|矩阵乘法]] · [[Cosine-Similarity|余弦相似度]] · [[Norm|范数]] · [[DFT]] · [[Self-Attention]]
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **逐元素乘（Hadamard）** | 输出还是向量 | 点积**多了一步求和**，输出是标量 |
| **叉积（cross product）** | 输出是向量，仅 3D | 点积输出**标量**、任意维；叉积测"垂直程度" |
| **余弦相似度** | 归一化后的点积 | 余弦 = 点积 **÷ 两个范数**，去掉了长度影响 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 核心原语，L10 有白板挑战，必须做到：
- ✅ 手写 `sum(a[i]*b[i])`，讲清 O(n)
- ✅ 说清 `a·b = ‖a‖‖b‖cosθ`，由此推余弦相似度
- ✅ 解释正/零/负号的几何意义与正交投影

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#Spotify` `#LinearAlgebra`
> 看似简单，却是"手写注意力""解释 embedding 检索"的必经第一步。

## 🌍 现实系统里它在哪发挥作用
Transformer 注意力 · 推荐/检索的相似度 · TF-IDF 打分 · 卷积（滑动点积）· 几乎所有神经网络的一层前向

## 📚 出现于（反查）
[[../lessons/L09]] · **[[../lessons/L10]]** · [[../lessons/L12]] · [[../lessons/L37]] · [[../lessons/L49]] · [[../lessons/L80]] · [[../lessons/L83]] · [[../lessons/L88]]

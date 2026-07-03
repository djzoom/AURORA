---
tags: [aurora, concept, linear-algebra, interview]
aliases: [Eigendecomposition, 特征分解, 特征值, 特征向量, eigenvalue, eigenvector, A=PDP⁻¹]
domain: linear-algebra
whiteboard: ★★★★
first_seen: L14
mastered: L17
---

# Eigendecomposition · 特征分解（Eigendecomposition）

[[_lifecycle|← 生命周期总表]] · [[../domains/linear-algebra|← Linear Algebra 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：给矩阵找到一组"天然坐标系"（特征向量），在这个坐标系里，复杂的矩阵乘法退化成"每个方向各自乘一个数"（特征值）。

---

## 📖 定义
若 `A·v = λ·v`（v ≠ 0），则 v 是特征向量、λ 是特征值——A 作用在 v 上只是把它拉伸 λ 倍，方向不变。特征值由特征方程 `det(A − λI) = 0` 求出。凑齐一组特征向量做成 P，就得到特征分解 `A = P D P⁻¹`，D 是对角矩阵（对角线是特征值）。对称矩阵可正交对角化 `A = QΛQᵀ`。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 算 `Aⁿ`（比如系统迭代 n 步、马尔可夫链走 n 步）要做 n 次矩阵乘，昂贵又看不出趋势。
- **它解决了什么真实问题？** 换到特征向量坐标系后，`Aⁿ = P Dⁿ P⁻¹`，`Dⁿ` 只是对角线各自 n 次方——一眼看出系统**收敛还是发散**（看 |λ| 是否 < 1）。
- **它是 PCA / 稳定性分析的引擎。** 协方差矩阵的特征向量 = 数据变化最大的方向；控制系统的特征值决定稳定性。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L14  eigen 与 SVD 一起初遇
正式动机     L17  换坐标系让乘法变成数乘
拆解原理     L17  det(A−λI)=0 → A=PDP⁻¹
真正掌握     L17  ★ 手写 char_poly，白板挑战（10 分钟）
再次使用     L14  σᵢ² 是 AᵀA 的特征值（连接 SVD）
再次使用     L17  Aⁿ=PDⁿP⁻¹ 稳定性/幂次
最终应用     PCA · 协方差主方向 · 系统稳定性判据
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学特征分解之前你得先会
```
Eigendecomposition
 ├─ 需要 → [[Matrix-Multiplication|矩阵乘法]]  (L12)
 ├─ 需要 → 行列式 det(A−λI)                    (L16)
 ├─ 需要 → 逆矩阵 P⁻¹                          (L16/L18)
 └─ 需要 → 对角/正交矩阵                        (L13)
被谁依赖 → [[SVD]] · PCA · 稳定性分析 · 矩阵幂次
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **SVD** | `A=UΣVᵀ`，任意矩阵 | 特征分解**只对方阵**、且要可对角化；奇异值 ≥ 0 |
| **奇异值 vs 特征值** | σ ≥ 0 vs λ 可负/复 | 对称正定阵二者才一致 |
| **对角化 vs 分解** | 找 P、D 的过程 | 对角化就是特征分解的别名（`PᵀAP=D`） |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — L17 手写 char_poly + 白板挑战，必须做到：
- ✅ 由 `det(A−λI)=0` 求特征值，回代求特征向量
- ✅ 写出 `A=PDP⁻¹`，解释三步：换基 → 各向缩放 → 换回
- ✅ 用 `Aⁿ=PDⁿP⁻¹` 讲稳定性（|λ|<1 收敛）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#NVIDIA` `#LinearAlgebra`
> 常与 PCA、SVD、稳定性一起考："特征值代表什么？为什么 PCA 用协方差的特征向量？"

## 🌍 现实系统里它在哪发挥作用
PCA 降维 · 谱聚类 · PageRank（主特征向量）· 控制系统稳定性 · 协方差分析

## 📚 出现于（反查）
[[../lessons/L14]] · [[../lessons/L16]] · **[[../lessons/L17]]** · [[../lessons/L18]] · [[../lessons/L20]] · [[../lessons/L21]]

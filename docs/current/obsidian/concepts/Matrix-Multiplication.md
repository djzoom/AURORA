---
tags: [aurora, concept, linear-algebra, interview]
aliases: [Matrix Multiplication, 矩阵乘法, 矩阵相乘, matmul, AB, 矩阵×向量, matvec]
domain: linear-algebra
whiteboard: ★★★★
first_seen: L12
mastered: L12
---

# Matrix-Multiplication · 矩阵乘法（Matrix Multiplication）

[[_lifecycle|← 生命周期总表]] · [[../domains/linear-algebra|← Linear Algebra 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：矩阵不是"数字表格"，是一台**坐标变换机器**；矩阵乘法就是把一次次变换串起来，而每个输出元素其实只是一次[[Dot-Product|点积]]。

---

## 📖 定义
`C = A @ B`，其中 `C[i][j] = Σₖ A[i][k]·B[k][j]`——输出第 i 行第 j 列，等于 A 的第 i 行与 B 的第 j 列做点积。形状规则：`(m×n) @ (n×p) → (m×p)`，内维必须相等。矩阵×向量是它的特例：`(Ax)ᵢ = A 的第 i 行 · x`，也可看作"A 的列的线性组合"。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 旋转、缩放、投影、神经网络的每一层……全是"对一堆向量做同一种线性变换"，没有矩阵乘法就得逐点手算，无法批量、无法组合。
- **它解决了什么真实问题？** 相机变焦是对角矩阵、镜头转动是旋转矩阵——矩阵乘法把这些变换**统一成一个运算**，还满足 `A(Bx)=(AB)x`（先做的变换可以预先合并成一个矩阵）。
- **它是算力的中心。** GPU/TPU 的存在几乎就是为了把矩阵乘法做快；[[DFT]]、[[Mel]] 滤波、注意力全部化归为矩阵乘。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L12  矩阵是坐标变换机器
正式动机     L12  相机变焦/旋转 = 一次线性变换
拆解原理     L12  逐行点积 / 列的线性组合两种视角
真正掌握     L12  ★ 手写 matvec + matmul，白板挑战（10 分钟）
再次使用     L37  DFT 写成矩阵 × 信号
再次使用     L47  Mel 滤波器组 = 滤波矩阵 × 功率谱
再次使用     L49  DCT 也是矩阵乘
最终应用     L83  Transformer 每一层都是矩阵乘（含 KV cache）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学矩阵乘法之前你得先会
```
Matrix-Multiplication
 ├─ 需要 → [[Dot-Product|点积]]      (L10)
 ├─ 需要 → 向量与形状               (L09)
 └─ 需要 → 线性变换的叠加/缩放       (L12)
被谁依赖 → [[DFT]] · [[Mel]] · [[Eigendecomposition|特征分解]] · [[SVD]] · [[Self-Attention]] · 几乎所有神经网络
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **逐元素乘（Hadamard `*`）** | 形状不变、对应位相乘 | 矩阵乘是**行×列求和**，形状会变 |
| **点积** | 两向量 → 标量 | 矩阵乘是**一堆点积的批量打包** |
| **AB vs BA** | 一般不相等 | 矩阵乘**不可交换**，顺序即变换先后 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — L12 手写实现 + 白板挑战，必须做到：
- ✅ 手写三重循环 `matmul`，讲清 O(mnp) 与形状规则
- ✅ 两种视角：逐行点积 / 列的线性组合
- ✅ 说明 `A(Bx)=(AB)x` 即"变换复合"，不可交换

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#NVIDIA` `#OpenAI` `#LinearAlgebra`
> 白板高频：手写 matmul、分析复杂度、解释一层全连接为何是矩阵乘。

## 🌍 现实系统里它在哪发挥作用
神经网络每一层 · Transformer 注意力 · 图形学变换管线 · [[DFT]]/DCT/Mel 等 DSP 变换 · 推荐系统批量打分

## 📚 出现于（反查）
[[../lessons/L09]] · **[[../lessons/L12]]** · [[../lessons/L19]] · [[../lessons/L21]] · [[../lessons/L37]] · [[../lessons/L47]] · [[../lessons/L49]] · [[../lessons/L83]] · [[../lessons/L85]]

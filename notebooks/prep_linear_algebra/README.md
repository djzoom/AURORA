# 前导课程 · 代码优先的线性代数

在写 Audio Core 之前先补这块数学。**全程用 numpy 代码学**，每课都连到 Aurora 的真实用途。

## 先做这个，再做 Week 1

```bash
jupyter lab     # 打开 notebooks/prep_linear_algebra/，从 p1 开始
```

按 `Shift+Enter` 一格格运行，看到 **✏️ TODO** 就动手填，下面的检查格会打 ✅。

## 课程表

| 笔记 | 学什么 | 连到 Aurora 哪里 |
|---|---|---|
| `p1_vectors` | 向量、加法、缩放、几何 | 音频 = 向量；调音量 = 缩放 |
| `p2_dot_product` | 点积、余弦相似度 | 音乐推荐；DFT 频点 = 点积 |
| `p3_norms` | 长度、距离、归一化 | 特征归一化；kNN 推荐 |
| `p4_matrices` | 矩阵 = 线性变换、矩阵乘 | 神经网络层 `Wx`；DFT 矩阵 |
| `p5_special_matrices` | 转置、逆、正交矩阵 | FFT/DCT 正交 → 可逆、能量守恒 |
| `p6_eigen_svd` | 特征值、PCA、SVD、低秩 | embedding 降维；推荐；LoRA |

## 这门课覆盖了 Aurora 全部核心数学吗？

**没有——线代是最大的一根支柱，不是全部。** 还需要：

- **微积分**（梯度/链式法则）→ 深度学习反向传播（Month 2 前补）
- **概率统计**（损失/分布/采样）→ ML 与生成模型（Month 2 前补）
- **复数 & 三角** → 傅里叶（已在 Week 1 Day 4 接触）

策略：现在专心线代；微积分/概率等快进 Month 2 时再补对应前导课。

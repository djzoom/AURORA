---
type: concept
tags: [待复习, 面试高频]
created: 2026-06-15
---

# 向量 (Vector)

## 一句话
向量就是一串有序的数；既能当"一组数据"，也能当"空间里带方向的箭头"。

## 它解决什么问题 / 为什么存在
让我们能把"一段音频""一首歌的特征""神经网络的一层输入"统一成同一种数学对象，
从而用同一套运算（加法、缩放、点积）去处理它们。

## 关键公式 / 直觉
- 加法逐元素：$a + b = [a_1+b_1, \dots]$（信号叠加=向量加法）
- 缩放：$c \cdot v$（调音量=标量缩放）
- 长度(L2 范数)：$|v| = \sqrt{\sum v_i^2}$

## 最小代码例子
```python
import numpy as np
audio = np.array([0.2, -0.4, 0.6])   # 3 维向量
louder = 1.5 * audio                  # 缩放 = 调大音量
```

## 在 Aurora 哪里用到
- 一段音频 = N 维向量（每个采样点一维），见 `aurora.audio.io.sine`
- 特征向量做相似度 → Music Core 推荐
- 练习：`notebooks/prep_linear_algebra/p1_vectors.ipynb`

## 相关概念
[[点积]] · [[范数]] · [[矩阵]]

## 我还没搞懂的点
- 高维向量（几百维 embedding）没法画图，怎么建立直觉？ #卡住了

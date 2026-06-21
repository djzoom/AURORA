# 数学前导课程 · 打卡表

四门代码优先的数学课，**足以支撑 Aurora 普通工程的全部核心数学**。
每课：图形直觉 → numpy 演示 → ✏️ 填空 → 自动判卷。打勾把 `[ ]` 改成 `[x]`。

> 启动：`make install` 后 `jupyter lab`，进入对应 `notebooks/prep_*/`。

## 推荐顺序

```
① prep_complex_trig   ┐ 撑起 Audio Core（先学）
② prep_linear_algebra ┘
        ↓  做 week01（信号/FFT 实践）
③ prep_calculus       ┐ 进 Month 2 深度学习前补
④ prep_probability    ┘
```

## ① 复数与三角 `prep_complex_trig/`
- [ ] 🎨 `v1_visual_complex` 看图建立直觉
- [ ] `x1_trig` 正弦三要素
- [ ] `x2_complex_numbers` 复数模与相位
- [ ] `x3_euler` 欧拉公式 / 旋转因子
- [ ] `x4_fourier_intuition` 正弦叠加成方波

## ② 线性代数 `prep_linear_algebra/`
- [ ] 🎨 `v1_visual_multiply` / `v2_visual_factorizations` / `v3_aurora_as_matrices`
- [ ] `p1`–`p3` 向量 / 点积 / 范数
- [ ] `p4`–`p6` 矩阵 / 正交 / 特征值·SVD
- [ ] `p7`–`p10` 解方程组 / 行列式逆 / 对角化 / 可逆性（对齐 CQF）

## ③ 微积分 `prep_calculus/`
- [ ] 🎨 `v1_visual_calculus` 切线与下山
- [ ] `c1` 导数
- [ ] `c2` 梯度
- [ ] `c3` 链式法则
- [ ] `c4` 梯度下降（拟合直线）

## ④ 概率统计 `prep_probability/`
- [ ] 🎨 `v1_visual_probability` 分布与损失
- [ ] `s1` 随机 / 大数定律
- [ ] `s2` 均值方差 / 标准化
- [ ] `s3` 分布 / 高斯
- [ ] `s4` softmax / 交叉熵

## 收尾
- [ ] 每门课写一篇短笔记（用 `docs/notes/` 模板，可放 Obsidian）
- [ ] 进入 `docs/week-01-checklist.md` 开始 Audio Core

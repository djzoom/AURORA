# 数学前导课程 · 打卡表

四门代码优先的数学课，**足以支撑 Aurora 普通工程的全部核心数学**。
每课：图形直觉 → numpy 演示 → ✏️ 填空 → 自动判卷。打勾把 `[ ]` 改成 `[x]`。

> 启动：`make install` 后 `jupyter lab`，进入对应目录。

## 推荐顺序

```
L01–L03  0_foundation   环境先跑通
L04–L08  1_complex_trig ┐ 撑起 Audio Core（先学）
L09–L21  2_linear_algebra ┘
        ↓  做 L32–L36 Audio DSP 入门
L22–L26  3_calculus     ┐ 进深度学习前补
L27–L31  4_probability  ┘
```

## ⓪ 基础前导 `0_foundation/`
- [ ] `L01_environment` 环境配置、内核选择、依赖验证
- [ ] `L02_python_numpy` Notebook 操作、变量/函数/数组最小动作
- [ ] `L03_course_map` 全课程地图与面试能力对照

## ① 复数与三角 `1_complex_trig/`
- [ ] 🎨 `L08_visual_complex` 看图建立直觉
- [ ] `L04_trig` 正弦三要素
- [ ] `L05_complex_numbers` 复数模与相位
- [ ] `L06_euler` 欧拉公式 / 旋转因子
- [ ] `L07_fourier_intuition` 正弦叠加成方波

## ② 线性代数 `2_linear_algebra/`
- [ ] 🎨 `L19_visual_multiply` / `L20_visual_factorizations` / `L21_aurora_matrices`
- [ ] `L09`–`L11` 向量 / 点积 / 范数
- [ ] `L12`–`L14` 矩阵 / 正交 / 特征值·SVD
- [ ] `L15`–`L18` 解方程组 / 行列式逆 / 对角化 / 可逆性

## ③ 微积分 `3_calculus/`
- [ ] 🎨 `L26_visual_calculus` 切线与下山
- [ ] `L22_derivatives` 导数
- [ ] `L23_gradients` 梯度
- [ ] `L24_chain_rule` 链式法则
- [ ] `L25_gradient_descent` 梯度下降（拟合直线）

## ④ 概率统计 `4_probability/`
- [ ] 🎨 `L31_visual_probability` 分布与损失
- [ ] `L27_probability_basics` 随机 / 大数定律
- [ ] `L28_descriptive_stats` 均值方差 / 标准化
- [ ] `L29_distributions` 分布 / 高斯
- [ ] `L30_softmax_crossentropy` softmax / 交叉熵

## 收尾
- [ ] 每门课写一篇短笔记（用 `docs/notes/` 模板，可放 Obsidian）
- [ ] 进入 `L32_numpy_signals`（`5_audio_dsp/`）开始 Audio Core

# 数学前导课程 · 打卡表

四门代码优先的数学课，**足以支撑 Aurora 普通工程的全部核心数学**。
每课：图形直觉 → numpy 演示 → ✏️ 填空 → 自动判卷。打勾把 `[ ]` 改成 `[x]`。

> 启动：`make install` 后 `jupyter lab`，进入对应目录。

## 推荐顺序

```
L01–L05  0_foundation + 1_complex_trig 开头   动机、声音、谱图、三角、复数
L06–L08  1_complex_trig 其余  ┐ 撑起 Audio Core（先学）
L09–L21  2_linear_algebra     ┘
        ↓  做 L32–L36 Audio DSP 入门
L22–L26  3_calculus     ┐ 进深度学习前补
L27–L31  4_probability  ┘
```

## ⓪ 开场五课 `0_foundation/` + `1_complex_trig/` 前两课
- [ ] `L01_motivation`    动机与路线图：Aurora 原则、11 模块路径、月通关标志、`check_imports`
- [ ] `L02_sound_digital` 声音的数字表示：`samples_count`、`make_time_axis`、`make_sine`、`signal_summary`
- [ ] `L03_spectrogram`   谱图直觉：先看图，不推公式，为 L37-L41 种下视觉印象
- [ ] `L04_trig`          正弦三要素：A·sin(2πft+φ)，实现 `sinusoid`，和弦叠加 demo
- [ ] `L05_complex_numbers` 复数模与相位：实现 `magnitude_phase`，FFT 输出复数预览

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

## L31 → L32 切换（约 20 分钟）

进入 Audio DSP 前，不需要重学完整数学，只要把「样本 / 数组 / 坐标」三件事对齐：

- [ ] 重读 L03 的谱图图像直觉：横轴时间、纵轴频率、亮度能量。
- [ ] 重读 L01 或 L02 中「1 秒 @ 16 kHz = 16000 个采样点」的说明。
- [ ] 运行一次：`python -c "import aurora; import numpy; print('ok')"`，确认环境仍可用。
- [ ] 读完 L31 末尾「进入 L32 前的心理切换」。
- [ ] 带着问题打开 L32：`第 n 个采样点发生在第几秒？`

完成后再进入 `L32_numpy_signals`。如果卡住，先不要急着查 FFT，L32-L34 只是在给声音数组搭地基。

## 收尾
- [ ] 每门课写一篇短笔记（用 `docs/notes/` 模板，可放 Obsidian）
- [ ] 进入 `L32_numpy_signals`（`5_audio_dsp/`）开始 Audio Core

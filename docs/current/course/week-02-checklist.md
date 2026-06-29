# L37–L42 逐日打卡 — 傅里叶变换（FFT）

> 目标：从数学定义出发彻底理解 DFT，手写蝶形迭代 FFT（Cooley-Tukey 位反转）并通过 numpy.fft 验证，
> 能完整读懂 `src/aurora/audio/transforms.py` 的每一行，并用 FFT 做真实信号的频谱分析。
> 每天结束前 `git commit`。打勾方式：把 `[ ]` 改成 `[x]`。

## 准备（L37 开始前 15 分钟）

- [ ] `make test` 全绿（确认上一阶段代码没有破坏）
- [ ] 打开 `notebooks/5_audio_dsp/`
- [ ] 快速回顾 `1_complex_trig/L06_euler.ipynb`——旋转因子是本阶段的命根子

## L37 — DFT 定义

- [ ] 学：离散傅里叶变换公式 `X[k] = Σ x[n]·e^{-2πi·k·n/N}`，每个符号什么意思
- [ ] 学：DFT 的矩阵形式——`X = W · x`，`W` 是范德蒙矩阵
- [ ] 写：`L37_dft.ipynb` — 用双重 for 循环手写朴素 DFT（O(N²)）
- [ ] 验：对比 `np.fft.fft` 输出，数值误差 < 1e-10
- [ ] 自测：能口述 `X[k]` 代表的物理含义（频率 k 分量的幅度与相位）
- [ ] commit

## L38 — 蝶形运算与分治

- [ ] 学：Cooley-Tukey 分治思路——偶数下标 / 奇数下标分成两半
- [ ] 学：蝶形运算 `X[k] = E[k] + W^k · O[k]`，`W = e^{-2πi/N}`
- [ ] 画：在 `L38_fft_butterfly.ipynb` 里手绘（或用 matplotlib 画）N=8 的蝶形图
- [ ] 推导：时间复杂度从 O(N²) 降至 O(N log N) 的过程
- [ ] 日志：博客草稿《蝴蝶凭什么比暴力快》（3-5 句即可）
- [ ] commit

## L39 — 从零手写递归 FFT

- [ ] 写：`L39_fft_implement.ipynb` — 递归版 FFT（Cooley-Tukey radix-2）
- [ ] 验：与 `np.fft.fft` 对齐，误差 < 1e-10
- [ ] 压测：画出 N=16 / 64 / 256 / 1024 时朴素 DFT vs. 递归 FFT 的耗时对比图
- [ ] 扩展（选做）：试写迭代版（in-place butterfly）
- [ ] 日志：博客草稿《FFT 从零到一》代码段
- [ ] commit

## L40 — 频谱分析实战

- [ ] 学：频率分辨率 = `sr / N`，频率轴 = `np.fft.fftfreq(N, 1/sr)`
- [ ] 学：幅度谱 `|X[k]|`、功率谱 `|X[k]|²`、相位谱 `∠X[k]`
- [ ] 写：`L40_spectrum.ipynb` — 对 440Hz + 880Hz 混合正弦波做频谱，峰值清晰可见
- [ ] 实验：改变窗长 N，观察频率分辨率与时间分辨率的权衡
- [ ] 自测：能解释负频率分量为什么出现，以及如何取单边谱
- [ ] commit

## L41 — 加窗 + 完整流程整合

- [ ] 学：矩形窗的旁瓣泄漏问题——频谱"染色"现象
- [ ] 对比：Hann / Hamming / Blackman 窗对泄漏的抑制效果
- [ ] 写：`L41_fft_full.ipynb` — 加窗 FFT 流程（sine → window → FFT → 幅度谱）
- [ ] 集成：调用 `aurora.audio.windows` + 自写 FFT，两者结果一致
- [ ] 日志：博客《什么是数字信号 · 中》（FFT + 频谱分析）定稿，放 `docs/blog/`
- [ ] 更新 `ROADMAP.md` 的 checkpoint
- [ ] commit + `git push`

## L42 — 视觉化 FFT

- [ ] 跑完 `L42_visual_fft.ipynb`，看懂蝴蝶图 + 频谱对比
- [ ] 观察：不同信号（纯音、和弦、噪声）的频谱形态差异

## 本阶段通关标准

- [ ] 能手写（或口述） DFT 定义公式并解释每个符号
- [ ] 能口述蝶形分治的核心思路，说清 O(N²) → O(N log N)
- [ ] 手写的递归 FFT 与 numpy.fft 误差 < 1e-10
- [ ] 能做频谱分析并解释幅度谱、频率分辨率、旁瓣泄漏
- [ ] 至少 5 个 commit、1 篇博客
- [ ] 准备好进入 L43（STFT）

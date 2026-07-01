# L32–L36 逐日打卡 — 信号、复数、numpy 流畅度

> 目标：建立"数字信号"的直觉，掌握复数与欧拉公式，把 numpy 用顺，
> 能完整读懂 `src/aurora/audio/io.py` 和 `windows.py` 的每一行。
> 每天结束前 `git commit`。打勾方式：把 `[ ]` 改成 `[x]`。

## 准备（L32 开始前 30 分钟）

- [ ] `make install` 跑通（已含 Jupyter + matplotlib，见 `[notebooks]` 可选依赖）
- [ ] `make test` 全绿（确认环境 OK）
- [ ] `jupyter lab` 启动，打开 `notebooks/5_audio_dsp/`
- [ ] 练习全部在 notebook 里做：每节一个 `L3N_*.ipynb`，✏️ 标记处填空

## L32 — numpy 流畅度

- [ ] 看：numpy 官方 quickstart（数组创建、dtype、shape）
- [ ] 看：3Blue1Brown「线性代数本质」第 1-3 集（向量是什么）
- [ ] 练：在 notebook 里玩广播（broadcasting）、切片、`np.arange`/`np.linspace`
- [ ] 写：`L32_numpy_signals.ipynb` — 用 numpy 生成 0~1 秒、16kHz 的时间轴 `t`
- [ ] 日志：博客草稿《我理解的 numpy 数组》（3-5 句即可）
- [ ] commit

## L33 — 正弦波与采样

- [ ] 学：采样率、采样点、`x[n] = A·sin(2π·f·n/sr)` 的每个符号
- [ ] 写：`L33_sine_wave.ipynb` — 自己实现一个 `my_sine(freq, dur, sr)`
- [ ] 对答案：和仓库的 `aurora.audio.sine` 对比，数值应几乎一致
- [ ] 画：用 matplotlib 画出 440Hz 正弦波的前 50 个采样点
- [ ] commit

## L34 — Nyquist 与混叠（aliasing）

- [ ] 学：为什么采样率必须 > 2×最高频率（Nyquist 定理）
- [ ] 实验：用 8kHz 采样率去采一个 6kHz 的正弦波，画出来——观察它"伪装"成低频
- [ ] 写：`L34_aliasing.ipynb` — 混叠对比图（notebook 内联显示）
- [ ] 日志：博客《什么是数字信号 · 上》——用你画的混叠图讲清采样
- [ ] commit

## L35 — 复数与欧拉公式（FFT 的命根子）

- [ ] 看：3Blue1Brown「复数」+「欧拉公式」视频
- [ ] 学：`e^{iθ} = cosθ + i·sinθ`；复数 = 平面上的旋转
- [ ] 练：在 notebook 里用 `np.exp(1j*theta)` 画单位圆上转动的点
- [ ] 自测：能否手写解释"为什么 `e^{-2πi·k·n/N}` 是一个旋转因子（twiddle）"？
- [ ] 写：`L35_euler_fft.ipynb` — 画欧拉公式的可视化
- [ ] commit

## L36 — 读懂 io.py / windows.py，整周收口

- [ ] 读：逐行读 `src/aurora/audio/io.py`（`sine`/`chirp`/`read_wav`/`write_wav`）
- [ ] 读：逐行读 `src/aurora/audio/windows.py`（Hann/Hamming/Blackman 公式）
- [ ] 画：把三种窗函数画在同一张图上，观察形状差异
- [ ] 自测（通关标志）：合上代码，能口述 `sine` 和 Hann 窗各在做什么
- [ ] 预习：读 L36 附录 A，能口述 `signal → window → xw → DFT/FFT`
- [ ] 日志：博客《什么是数字信号 · 下》定稿，放 `docs/blog/`
- [ ] 更新 `ROADMAP.md` 的 Month-1 checkpoint
- [ ] commit + `git push`

## 本阶段通关标准

- [ ] 能解释采样、Nyquist、混叠，并有自己画的图
- [ ] 能写出 `e^{iθ}=cosθ+i·sinθ` 并解释它是"旋转"
- [ ] 能完整读懂 `io.py` 和 `windows.py`
- [ ] 至少 5 个 commit、1-2 篇短博客
- [ ] 准备好进入 L37（DFT）

# notebooks/ — 交互式教学

用 Jupyter 一格一格地学：左边读讲解、右边改代码、立刻看输出。比 `.py` 脚本更适合入门。

## 启动

```bash
make install                 # 含 Jupyter（notebooks 这个可选依赖）
# 或单独装: pip install -e ".[notebooks]"

jupyter lab                  # 浏览器里打开，进入 notebooks/week01/
```

## 用法

- 按 `Shift+Enter` 一格格运行；看到 **✏️ TODO** 的代码格 = 你要改的地方，
  改完运行，下面的检查格会打 ✅ 或报错。
- 配套宏观地图：`docs/LEARNING_PLAN.md`；逐日清单：`docs/week-01-checklist.md`。

## 学习顺序

```
① 数学前导（先打地基）        ② Audio Core 实践
   prep_complex_trig  ─┐         week01/  day1 → day5
   prep_linear_algebra ├─→ ──→   （信号 / FFT / mel / MFCC）
   prep_calculus  ────┤              ↓
   prep_probability ──┘          Month 1 吃透 Audio Core ...
```

**建议路径**：先过 `prep_complex_trig` + `prep_linear_algebra`（撑起 Audio Core），
再做 `week01`；`prep_calculus` + `prep_probability` 可在快进 Month 2（深度学习）前补。

## 数学前导课程（代码优先）

四块地基，**足以支撑 Aurora 普通工程的核心数学**：

| 课程 | 内容 | 主要服务于 |
|---|---|---|
| `prep_complex_trig/` | 正弦、复数、欧拉、傅里叶直觉 | DSP / FFT（Month 1） |
| `prep_linear_algebra/` | 向量、点积、矩阵、SVD（+CQF 对齐 +图形化） | 几乎所有模块 |
| `prep_calculus/` | 导数、梯度、链式、梯度下降 | 深度学习训练（Month 2+） |
| `prep_probability/` | 随机、分布、softmax、交叉熵 | ML 损失与生成（Month 2+） |

每门课的细目见各自文件夹的 `README.md`。

> 🎨 **图形化分册**：`prep_linear_algebra/` 里的 `v1–v3` + `laviz.py` 工具包，
> 受《The Art of Linear Algebra》启发，把线代画成图（含 DFT/mel 的矩阵视角）。

## Audio Core 实践

```
week01/
├── day1_numpy.ipynb      时间轴 / numpy 流畅度
├── day2_sine.ipynb       自己实现正弦波，和仓库对答案
├── day3_aliasing.ipynb   Nyquist 与混叠
├── day4_euler.ipynb      复数 / 欧拉公式 / FFT 旋转因子
└── day5_windows.ipynb    读 io.py·windows.py，对比窗函数
```

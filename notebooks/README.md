# notebooks/ — 交互式教学

用 Jupyter 一格一格地学：左边读讲解、右边改代码、立刻看输出。比 `.py` 脚本更适合入门。

## 启动

```bash
make install                 # 含 Jupyter（notebooks 这个可选依赖）
# 或单独装: pip install -e ".[notebooks]"

jupyter lab                  # 浏览器里打开，进入 notebooks/week01/
```

## 用法

- 进入 `week01/`，从 `day1_numpy.ipynb` 开始，按 `Shift+Enter` 一格格运行。
- 看到 **✏️ TODO** 的代码格 = 你要改的地方；改完运行，下面的检查格会打 ✅ 或报错。
- 配套宏观地图：`docs/LEARNING_PLAN.md`；逐日清单：`docs/week-01-checklist.md`。

## 目录

```
week01/
├── day1_numpy.ipynb      时间轴 / numpy 流畅度
├── day2_sine.ipynb       自己实现正弦波，和仓库对答案
├── day3_aliasing.ipynb   Nyquist 与混叠
├── day4_euler.ipynb      复数 / 欧拉公式 / FFT 旋转因子
└── day5_windows.ipynb    读 io.py·windows.py，对比窗函数
```

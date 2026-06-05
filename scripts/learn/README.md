# Week 1 — 引导练习骨架

这里每个 `dN_*.py` 对应 `docs/week-01-checklist.md` 里的某一天。
文件里用 `TODO` + `raise NotImplementedError` 标出**你要填的部分**，其余脚手架
（画图、对答案、打印结果）已经写好。

## 怎么用

```bash
make install            # 先确保环境 OK（仓库根目录）
pip install matplotlib  # 画图需要

python scripts/learn/d2_sine.py     # 跑某一天的练习
```

- 每个文件顶部有「今日目标」和提示。
- 看到 `raise NotImplementedError("TODO: ...")` 就是你动手的地方。
- 填完跑一下：脚本会**自动和仓库的标准实现对答案**（Day 2/4）或画图存到 `figs/`。
- 图片存进 `scripts/learn/figs/`（已被 git 忽略，不会污染仓库）。

## 节奏建议

填空 → 跑通 → 自己解释一遍（费曼）→ `git commit`。卡住超过 20 分钟就回去看
3Blue1Brown / 《Think DSP》对应章节，别硬磕。

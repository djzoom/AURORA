# notes/ — 你的学习笔记（Obsidian 友好）

这里放**你自己的话**写的笔记。Jupyter 管"跑代码"，Obsidian 管"织知识网"——互补。
全部用标准 Markdown，所以在 Obsidian 里能用双链 `[[...]]`，在 GitHub 上也能正常看。

## 怎么把 Obsidian 接上来（二选一）

**方案 A（推荐·私人）**：在 Obsidian 里「打开文件夹作为库」时，选你自己的私人目录，
把半成品想法、零散笔记放那；只把打磨好的成品复制进本仓库 `docs/blog/`。
好处：私人笔记自由随意，不污染专业的 Git 历史。

**方案 B（笔记进仓库）**：在 Obsidian 里直接「打开文件夹作为库」→ 选这个 `docs/` 目录。
笔记即仓库文件，`git push` 一起带走、也算 commit。
代价：`.obsidian/` 配置和 `[[双链]]` 语法会进仓库，GitHub 上双链不渲染。

> 不确定就用 **A**。模板可以复制到任何库里用。

## 用法

1. 学一个概念（如傅里叶），就新建一张笔记，套用 `templates/concept-template.md`。
2. 每天结束写一条 `templates/daily-template.md`（当日所学/卡点/明日计划）。
3. 概念之间用 `[[双链]]` 连起来，例：在「傅里叶变换」里写 `[[复数]]`、`[[欧拉公式]]`。
4. 打开 Obsidian 的 **Graph View** 看你的知识网——孤岛=还没学透的点。

## 目录

```
notes/
├── templates/
│   ├── concept-template.md   概念卡模板（费曼式：用自己的话讲清）
│   └── daily-template.md     每日学习日志模板
└── example-向量.md            一张写好的示例概念卡（照着仿）
```

## 标签建议

`#待复习`、`#面试高频`（FFT、注意力机制等）、`#卡住了`。
面试前用 Obsidian 搜索一键筛出 `#面试高频`。

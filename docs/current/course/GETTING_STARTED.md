# 新手上路 · 从零开始跑起来第一课

> 这份指南写给**完全零基础**的你——没装过 Python、没用过终端、没碰过 Jupyter 都没关系。
> 跟着走一遍，大约 **30 分钟**，你就能在自己的电脑上打开第 1 课、按下运行、看到第一条正弦波。
> 遇到任何一步卡住，翻到最后的 [「常见问题」](#常见问题) 表格。

---

## 你会用到三样东西

1. **终端（Terminal）**——一个用打字下命令的黑框框。别怕，你只需要复制粘贴。
   - **Mac**：按 `⌘ + 空格`，输入 `Terminal`，回车。
   - **Windows**：按开始键，输入 `PowerShell`，回车。
2. **Python**——这门课的编程语言（需要 **3.10 或更新**）。
3. **课程代码**——也就是这个 `AURORA` 文件夹。

下面一步步来。**每个灰底框里的命令，都是复制 → 粘贴到终端 → 回车。**

---

## 第 1 步：装 Python

先在终端里检查你是否已经有合适的 Python：

```bash
python3 --version
```

- 如果显示 `Python 3.10`（或更高，如 3.11 / 3.12）——✅ 跳到第 2 步。
- 如果提示"找不到命令"或版本低于 3.10——按下面装：

**Mac / Windows 通用**：打开 <https://www.python.org/downloads/>，下载最新版安装。
> ⚠️ **Windows 用户**：安装第一屏，一定要勾选 **"Add Python to PATH"** 再点安装，否则终端会找不到它。

装完**关掉终端重新打开**，再跑一次 `python3 --version` 确认。

---

## 第 2 步：拿到课程代码

**如果你已经有 `AURORA` 文件夹**（比如别人发给你、或已下载），用 `cd` 进去即可：

```bash
cd 你的路径/AURORA
```
> 小技巧：输入 `cd ` 后（注意有空格），把文件夹从访达/资源管理器**拖进终端**，路径会自动补上。

**如果还没有**，且你有访问权限，用 git 克隆（没装 git 会提示你安装，照着装就行）：

```bash
git clone https://github.com/djzoom/AURORA.git
cd AURORA
```
> 没有 git 也没关系：在仓库网页点 **Code → Download ZIP**，解压后 `cd` 进去。

确认你在正确的位置——下面这条应该能看到 `README.md`、`notebooks`、`pyproject.toml`：

```bash
ls
```

---

## 第 3 步：建一个"独立小屋"（虚拟环境）

我们把这门课要装的东西，关进一个叫 `.venv` 的独立环境里，**不污染你系统的 Python**。

```bash
python3 -m venv .venv
```

然后**激活**它（激活后，命令行前面会出现 `(.venv)` 字样）：

```bash
# Mac / Linux：
source .venv/bin/activate

# Windows PowerShell（用上面那条不行就用这条）：
.venv\Scripts\Activate.ps1
```

> 以后每次学这门课，**先 `cd` 进 AURORA、再激活 `.venv`**，看到 `(.venv)` 才开始。

---

## 第 4 步：安装课程需要的软件包

一条命令搞定（装的是跑 notebook 和做题需要的基础工具，**很轻量，只有 numpy / matplotlib / jupyter 等**）：

```bash
pip install -e ".[dev,notebooks]"
```

再把这个环境注册成 Jupyter 的一个"内核"（kernel），等下在 notebook 里要选它：

```bash
python -m ipykernel install --user --name aurora --display-name "Python (AURORA)"
```

> 🔸 **关于 PyTorch**：前 53 课（数学地基 + 音频 DSP）**只用 numpy，不需要 torch**。
> 等你学到**深度学习模块（第 59 课起）**，再回来补一句 `pip install -e ".[speech,llm]"` 装 torch 即可。
> 现在不用装，省时间省空间。

---

## 第 5 步：打开 Jupyter，进入第一课

```bash
jupyter lab
```

浏览器会自动弹出一个页面。在左边的文件树里，一路点开：

```
notebooks → 0_foundation → L01_motivation.ipynb
```

打开后，**右上角把内核切换成 `Python (AURORA)`**（如果没看到，先关掉重开一次 Jupyter）。

🎉 到这里，环境就装好了。下面学"怎么用 notebook"。

---

## 怎么用一个 Notebook

Notebook 是"一格一格"（cell）组成的：有的格是**讲解文字**，有的格是**可运行的代码**。

- **运行一格**：点中它，按 `Shift + Enter`。文字格会排版好，代码格会在下面显示输出。
- **从上往下依次运行**——后面的格常常依赖前面的结果，别跳着跑。

### 三种你会反复见到的记号

| 记号 | 含义 | 你要做的 |
|---|---|---|
| **✏️ TODO** | 这里留了空，等你填代码 | 把 `None` / `raise NotImplementedError` 换成你的实现，再运行 |
| **✅ 检查格** | 紧跟 TODO 的自动判分格 | 你填对了它打 ✅；填错了会报错并提示哪里不对 |
| **🧠 白板挑战 / 自评** | 闭卷小测或自我评估 | 按提示把 `None` 改成 `True/False` 或你的答案 |

> **重要心态**：在你还没填 TODO 时，运行到那一格**报错是正常的、是设计好的**——
> 它在等你动手。报错信息通常会告诉你"该实现什么"。这不是环境坏了。

### 卡住了？看参考答案

每个有 TODO 的模块，旁边都有一个 `solutions/` 文件夹，里面是**参考实现 + 讲解**。
例如 `notebooks/0_foundation/solutions/L01_motivation_solutions.md`。
> 建议：**先自己认真想 10 分钟再看答案**——卡住再突破，才记得牢。

---

## 检查你的进度（可选）

想确认所有 notebook 都健康、没被改坏，回到终端（激活 `.venv` 的状态）跑：

```bash
python scripts/validate_pipeline.py     # 课程验收门：JSON + 语法 + 流水线
make test                               # 运行 82 项测试（FFT 等对齐 numpy 验证）
```

全绿就说明一切正常。

---

## 学习节奏建议

- **按顺序走 L01 → L99**，别跳课——每一课都为下一课打地基。
- 每天 1–2 课，遇到"啊，原来如此"的瞬间就停下来回味一下。
- 完整课程地图见 [`notebooks/README.md`](../../../notebooks/README.md)；
  周计划见 [`LEARNING_PLAN.md`](LEARNING_PLAN.md)。

---

## 常见问题

| 症状 | 原因 & 解决 |
|---|---|
| `python3: command not found` | 没装好 / 没加 PATH。重装 Python，Windows 记得勾 "Add to PATH"，然后**重开终端**。 |
| 命令行前面没有 `(.venv)` | 环境没激活。先 `cd` 进 AURORA，再跑第 3 步的 `source .venv/bin/activate`。 |
| Jupyter 内核列表里没有 `Python (AURORA)` | 第 4 步的 `ipykernel install` 没跑，或 Jupyter 没重启。补跑那条命令，关掉浏览器标签重新 `jupyter lab`。 |
| 运行代码格报 `ModuleNotFoundError: numpy` | 内核选错了。右上角切成 `Python (AURORA)`。 |
| 运行到某格 `NotImplementedError` / 报错 | 多半是**你还没填的 ✏️ TODO**——这是设计好的，去把那格补上。 |
| 学到深度学习课 `No module named 'torch'` | 到第 59 课了才需要 torch：`pip install -e ".[speech,llm]"`。 |
| 图画不出来 / matplotlib 卡住 | 确认装了 `notebooks` 附加包（第 4 步）；notebook 里的图会内嵌显示，无需额外操作。 |
| `pip install` 很慢或失败 | 网络问题；可换国内镜像：`pip install -e ".[dev,notebooks]" -i https://pypi.tuna.tsinghua.edu.cn/simple`。 |

---

**准备好了吗？** 回到 Jupyter，打开 `L01_motivation.ipynb`，按下第一个 `Shift + Enter`。

**「拒绝黑盒——从一条正弦波亲手造出 Whisper 的 6 个月远征」** 现在开始。我们白板见。 🎧

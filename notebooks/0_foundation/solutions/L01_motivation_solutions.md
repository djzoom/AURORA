# 参考实现 — L01_motivation

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 0 · `course_purpose` 示范写法（第 6 节练习）

这道题没有唯一标准答案——它考的是"你能不能把模块接到 Aurora 上"，
不是背诵路线图。下面给出两类样品，让你知道"及格线长什么样"。

**样品 A：具体版**（适合前中段、你已经有点感觉的模块）——
句式里 X 和 Y 都落到实处，Y 一定指向 Aurora 里一件具体的事：

```python
'2_linear_algebra': '我学线性代数，是为了看懂 DFT 其实就是一次矩阵乘法——'
                    '一段声音乘上一张固定的表格，就得到了频谱',
'5_audio_dsp':      '我学音频 DSP，是为了亲手写出 FFT/STFT/Mel，'
                    '把 Whisper 输入端那张"声音配方表"从零造出来',
```

**样品 B：合格的笼统版**（适合 `8_music`、`9_llm` 这类你现在几乎一无所知的模块）——
诚实记下"我还不知道"，加一个"回来重写"的约定，这就是合格答案：

```python
'8_music': '我还不知道 music embedding 具体是什么，只知道它能把一首歌'
           '变成一串数字；学到 L76 我会回来把这条重写具体',
```

**自查两条**：
1. 句子里能找到 X（学什么）和 Y（在 Aurora 里做什么）吗？Y 不能只是"做音乐相关的功能"这种空话——
   要么落到具体的事（样品 A），要么诚实标注"待学后重写"（样品 B）。
2. 这本清单是活文档：每进入一个新模块，回来把对应那条从样品 B 升级成样品 A。

## 参考实现 1

`check_imports`：用 `importlib.util.find_spec` 检测每个包是否可导入。

```python
import importlib.util

def check_imports(names):
    """检测一组包是否可导入。返回 {包名: bool} 字典。"""
    result = {}
    for name in names:
        result[name] = importlib.util.find_spec(name) is not None
    return result
```

## 参考实现 2

`environment_report`：从当前目录逐级向上找到含 `pyproject.toml` 的项目根，
汇总解释器路径、版本、`aurora` 可用性与项目根。

```python
import sys
from pathlib import Path

def environment_report():
    """返回当前运行环境的快照字典。"""
    root = None
    for folder in [Path.cwd(), *Path.cwd().parents]:
        if (folder / 'pyproject.toml').exists():
            root = folder
            break
    return {
        'python_executable': sys.executable,
        'python_version':    sys.version,
        'aurora_available':  check_imports(['aurora'])['aurora'],
        'project_root':      str(root),
    }
```

#!/usr/bin/env python3
"""Apply the remaining DSP supplement updates.

This script patches the following notebooks and docs:
- notebooks/0_foundation/L03_spectrogram.ipynb
- notebooks/1_complex_trig/L07_fourier_intuition.ipynb
- notebooks/2_linear_algebra/L21_aurora_matrices.ipynb
- notebooks/5_audio_dsp/L35_euler_fft.ipynb
- notebooks/5_audio_dsp/L39_fft_implement.ipynb
- notebooks/5_audio_dsp/L46_mel.ipynb
- notebooks/5_audio_dsp/L47_mel_implement.ipynb
- notebooks/5_audio_dsp/L48_visual_stft.ipynb
- notebooks/5_audio_dsp/L49_dct.ipynb
- notebooks/5_audio_dsp/L50_mfcc.ipynb
- notebooks/5_audio_dsp/L51_real_audio.ipynb
- notebooks/5_audio_dsp/solutions/L47_mel_implement_solutions.md
- docs/current/course/dsp-gap-supplement-plan.md
- docs/current/course/gap-supplement-plan.md
- docs/current/obsidian/domains/audio-dsp.md
"""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell


REPO = Path(__file__).resolve().parent.parent
NB_DIR = REPO / "notebooks" / "5_audio_dsp"
DSP_PLAN = REPO / "docs" / "current" / "course" / "dsp-gap-supplement-plan.md"
INDEX_PLAN = REPO / "docs" / "current" / "course" / "gap-supplement-plan.md"
OBSIDIAN_AUDIO_DSP = REPO / "docs" / "current" / "obsidian" / "domains" / "audio-dsp.md"


def _read_nb(path: Path) -> nbformat.NotebookNode:
    with path.open("r", encoding="utf-8") as fh:
        return nbformat.read(fh, as_version=4)


def _write_nb(path: Path, nb: nbformat.NotebookNode) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp_path.replace(path)


def _cell_source(cell: nbformat.NotebookNode) -> str:
    return cell.get("source", "")


def _contains_cell(nb: nbformat.NotebookNode, marker: str) -> bool:
    return any(marker in _cell_source(cell) for cell in nb.cells)


def _insert_before_first(
    nb: nbformat.NotebookNode,
    predicate,
    new_cells: list[nbformat.NotebookNode],
) -> bool:
    for idx, cell in enumerate(nb.cells):
        if predicate(cell):
            nb.cells[idx:idx] = new_cells
            return True
    raise RuntimeError("anchor cell not found")


def _replace_cell_source(nb: nbformat.NotebookNode, needle: str, replacement: str) -> bool:
    for cell in nb.cells:
        if needle in _cell_source(cell):
            cell["source"] = replacement
            return True
    return False


def _write_text_if_changed(path: Path, content: str) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def _replace_text(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def _update_l03() -> bool:
    path = REPO / "notebooks/0_foundation/L03_spectrogram.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：谱图三根轴"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：谱图三根轴

            - 时间轴：横轴是采样点对应的秒数
            - 频率轴：纵轴是 Hz，越高越靠上
            - 能量轴：颜色越亮，能量越大

            L32 会把这三根轴重新画一遍，只不过这次从原始采样点出发，而不是现成谱图。
            如果记不住，就依次问自己：

            1. 这一列是哪个时间片？
            2. 这一行对应哪个频率？
            3. 这块亮表示能量大还是小？
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "code" and "def show_spec" in _cell_source(cell),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l07() -> bool:
    path = REPO / "notebooks/1_complex_trig/L07_fourier_intuition.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：方波 = 谐波叠加"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：方波 = 谐波叠加

            - 方波的跳变越尖锐，频域里需要越多高频分量才能逼近
            - 只保留奇次谐波，可以先抓住方波的上下平台
            - 项数越多，边缘越陡，但跳变处也更容易看到 Gibbs 振铃

            这节课先把这条直觉记住：复杂波形 = 多个正弦叠加。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown"
        and "## 1. 叠加几个正弦 → 复杂波形" in _cell_source(cell),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l21() -> bool:
    path = REPO / "notebooks/2_linear_algebra/L21_aurora_matrices.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：W @ x 其实就是 DFT"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：W @ x 其实就是 DFT

            - `x` 是长度 N 的信号向量
            - `W` 是 N×N 的 DFT 矩阵
            - `W @ x` 的每一行都是一次加权求和，正好对应一个频点

            L37 会把这件事换成手写循环；现在先把矩阵视角记牢。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "code"
        and _cell_source(cell).lstrip().startswith("import numpy as np"),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l35() -> bool:
    path = NB_DIR / "L35_euler_fft.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：方波 = 谐波叠加"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：方波 = 谐波叠加

            - 你已经见过奇次谐波叠加方波的轮廓
            - 现在要把这些正弦分量写成 `e^{-2πikn/N}` 的旋转因子
            - 负号只是告诉你：这是分析方向，旋转会顺时针走

            L07 的直觉会在这里重新出现，只不过这次用欧拉公式来描述。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown"
        and "## 1. 先把复数当成平面坐标" in _cell_source(cell),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l39() -> bool:
    path = NB_DIR / "L39_fft_implement.ipynb"
    nb = _read_nb(path)
    old = """## 4. ✏️ 实现 `my_fft(x)`（递归 Cooley-Tukey）

**四步实现路线**：

| 步骤 | 代码 | 说明 |
|---|---|---|
| 1 | `if len(x)==1: return x.astype(complex)` | 基础情形：单点 DFT = 输入本身 |
| 2 | `E = my_fft(x[::2])` | 递归：偶数下标子序列 |
| 3 | `O = my_fft(x[1::2])` | 递归：奇数下标子序列 |
| 4 | `return butterfly(E, O)` | 蝶形合并 → N 点频谱 |

**精度要求**：`np.allclose(my_fft(x), np.fft.fft(x), atol=1e-9)` 通过

**常见错误**：
- 忘了 `astype(complex)`：numpy 对实数组做整数操作会截断
- N 不是 2 的幂：补零 `x = np.pad(x, ...)` 后再递归
- 直接调用 `np.fft.fft` 而不是 `butterfly`：失去了学习价值

> **注意**：本课实现 `butterfly` 可直接复用 L38 里的实现，或者内联三行蝶形公式。"""
    new = """## 4. ✏️ 实现 `my_fft(x)`（递归 Cooley-Tukey）

**五步提示**：

1. 递归基：长度为 1 时直接返回复数输入
2. 偶奇拆分：把偶数位和奇数位分成两个子问题
3. 旋转因子：`twiddle` 只负责一圈里的相位步进
4. 蝶形合并：把 `E` 和 `O` 组合成上半 / 下半频谱
5. 拼接返回：先上半，再下半

**精度要求**：`np.allclose(my_fft(x), np.fft.fft(x), atol=1e-9)` 通过

**卡住回**：L38 的蝶形图、L38/L39 的分治树，或 `solutions/L39_fft_implement_solutions.md`
"""
    changed = _replace_cell_source(nb, old, new)
    if changed:
        _write_nb(path, nb)
    return changed


def _update_l46() -> bool:
    path = NB_DIR / "L46_mel.ipynb"
    nb = _read_nb(path)
    marker = "## 3a. 手绘练习：三角滤波器三锚点"
    if _contains_cell(nb, marker):
        return False

    exercise = new_markdown_cell(
        dedent(
            """
            ## 3a. 手绘练习：三角滤波器三锚点

            在纸上画一个三角滤波器，标出 left / center / right 三个锚点，再写出上升段和下降段的斜率。
            如果卡住，回想 `hz_to_mel` 只是坐标变换，真正的形状来自三个相邻中心点。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
        [exercise],
    )
    _write_nb(path, nb)
    return True


def _update_l47_solution() -> bool:
    path = NB_DIR / "solutions" / "L47_mel_implement_solutions.md"
    content = dedent(
        """
        # 参考实现 — L47_mel_implement

        > ⚠️ 请先独立完成练习，再查看参考实现。

        ## 参考实现 1

        ```python
        import numpy as np
        from aurora.audio.stft import stft
        from aurora.audio.mel import mel_filterbank


        def log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256):
            S = stft(x, n_fft=win_len, hop_length=hop)
            power = np.abs(S).T ** 2
            fb = mel_filterbank(n_mels, win_len, sr)
            mel_energy = power @ fb.T
            return np.log(mel_energy + 1e-8)
        ```
        """
    ).strip() + "\n"
    return _write_text_if_changed(path, content)


def _update_l47() -> bool:
    path = NB_DIR / "L47_mel_implement.ipynb"
    nb = _read_nb(path)
    changed = False

    marker = "## 开课前 2 分钟复习：矩阵乘法就是滤波"
    if not _contains_cell(nb, marker):
        review = new_markdown_cell(
            dedent(
                """
                ## 开课前 2 分钟复习：矩阵乘法就是滤波

                - `power @ fb.T` 是把每帧功率谱投影到 Mel 三角滤波器上
                - 这里的 `fb` 来自 L46 的三角滤波器组
                - 记住 shape：`power (T,F)` × `fb.T (F,M)` → `mel_energy (T,M)`

                L21 里你已经见过同一件事的矩阵版本；现在只是在 Audio DSP 里重新出现。
                """
            ).strip()
        )
        _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "code"
            and _cell_source(cell).lstrip().startswith("import numpy as np"),
            [review],
        )
        changed = True

    changed |= _replace_cell_source(
        nb,
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**五步串联（每步一行代码）**：

| 步骤 | 代码 | 输出 shape |
|---|---|---|
| 1 | `S = stft(x, n_fft=win_len, hop_length=hop)` | `(n_fft//2+1, n_frames)` |
| 2 | `power = np.abs(S).T ** 2` | `(n_frames, n_fft//2+1)` |
| 3 | `fb = mel_filterbank(n_mels, win_len, sr)` | `(n_mels, n_fft//2+1)` |
| 4 | `mel_energy = power @ fb.T` | `(n_frames, n_mels)` |
| 5 | `return np.log(mel_energy + 1e-8)` | `(n_frames, n_mels)` |

**验收标准**：
- `np.allclose(log_mel_spectrogram(x, sr), aurora_ref, atol=1e-9)` 通过
- 输出无 `nan` 或 `-inf`（ε 保护有效）
- shape = `(n_frames, n_mels)`

> **注意**：`stft` 可能返回 `(n_fft//2+1, n_frames)`（列=帧），注意 `.T` 转置方向。""",
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**三步提示**：

1. 先拿到 STFT，再把复数幅度变成功率谱
2. 用 `mel_filterbank(...)` 把频率轴压到 `n_mels`
3. `np.log(... + 1e-8)` 只是数值保护，不是算法核心

**卡住回**：L44 / L46 / L47

**参考实现**：`solutions/L47_mel_implement_solutions.md`
""",
    )

    if changed:
        _write_nb(path, nb)
    return changed


def _update_l48() -> bool:
    path = NB_DIR / "L48_visual_stft.ipynb"
    nb = _read_nb(path)
    marker = "## 附录 · 为什么下一课要做 DCT？（回调 L49）"
    if _contains_cell(nb, marker):
        return False

    appendix = new_markdown_cell(
        dedent(
            """
            ## 附录 · 为什么下一课要做 DCT？（回调 L49）

            L48 已经把声音切成一帧一帧的谱图，也把线性频率轴压成了 Mel 轴。
            但 Mel 通道彼此高度相关，邻近通道常常在重复同一件事，相关系数往往接近 0.9。

            DCT 的作用有两层：

            - 去相关：把重复的 Mel 能量旋转到更独立的坐标上
            - 能量压缩：把大部分信息集中到前几个低阶系数里

            这和 JPEG 里对像素块做 DCT 的思路同源，只是这里处理的是音频谱包络，不是图像亮度。
            如果一时不清楚，先回看 L49 开头的 FFT vs DCT-II 差异表，再回来读这一段。

            L49 会把这个动机变成真正的 `dct_ii` 实现；本节先记住：

            **Mel 负责感知压缩，DCT 负责去相关。**
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
        [appendix],
    )
    _write_nb(path, nb)
    return True


def _update_l49() -> bool:
    path = NB_DIR / "L49_dct.ipynb"
    nb = _read_nb(path)
    changed = False

    marker = "## 0. 先看 FFT vs DCT-II：它们不是同一个东西"
    if not _contains_cell(nb, marker):
        intro = new_markdown_cell(
            dedent(
                """
                ## 0. 先看 FFT vs DCT-II：它们不是同一个东西

                | | FFT / DFT | DCT-II |
                |---|---|---|
                | 基函数 | 复指数 | 余弦 |
                | 边界假设 | 圆周 / 周期延拓 | 偶对称延拓 |
                | 输出 | 复数频谱 | 实数倒谱系数 |
                | 典型用途 | 频谱分析 | 去相关 / 压缩 |
                | Aurora | `aurora.audio.transforms.fft` | `aurora.audio.mfcc.dct_ii` |

                DCT-II 放在 log-Mel 后面，是因为相邻 Mel 通道高度相关；
                DCT 把重复信息旋转到更少的坐标里。
                如果忘了为什么要做这一步，回看 L48 末尾的动机附录。
                """
            ).strip()
        )
        _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown" and "## 1. DCT-II 公式" in _cell_source(cell),
            [intro],
        )
        changed = True

    changed |= _replace_cell_source(
        nb,
        "# 注意：参考实现 _dct_ii_ref 已移至实验单元，避免完整答案出现在练习旁边",
        "# 注意：参考实现只保留在 notebooks/5_audio_dsp/solutions/L49_dct_solutions.md",
    )

    new_cell_source = dedent(
        """
        # 实验与练习解耦：若本地 dct_ii 还没写完，则临时用 aurora.audio.mfcc.dct_ii 跑后续实验。
        from aurora.audio.mfcc import dct_ii as aurora_dct_ii

        # numpy-based inverse DCT-II reference
        def _idct_ii_ref(X):
            # Inverse of ortho DCT-II: X = D @ x  ⟹  x = D.T @ X
            # where D[k,n] = scale[k] * cos(pi*k*(2n+1)/(2N)),
            # scale[0]=sqrt(1/N), scale[k>0]=sqrt(2/N)
            N = len(X)
            k = np.arange(N)
            n = np.arange(N)
            scale = np.full(N, np.sqrt(2.0 / N))
            scale[0] = np.sqrt(1.0 / N)
            D = scale[:, None] * np.cos(np.pi * np.outer(k, 2 * n + 1) / (2 * N))
            return D.T @ X

        # 用一段 26 维模拟 Mel 能量做实验
        rng = np.random.default_rng(7)
        x_mel = rng.standard_normal(26)

        try:
            probe = dct_ii(np.array([1.0, 2.0]))
        except NotImplementedError:
            probe = None

        _impl = dct_ii if probe is not None else aurora_dct_ii
        if _impl is aurora_dct_ii:
            print('⚠️  dct_ii 尚未实现，使用 aurora.audio.mfcc.dct_ii 演示实验（完成 TODO 后可切换）')
        X_dct = _impl(x_mel)

        # 实验 A：精确逆变换
        x_rec_full = _idct_ii_ref(X_dct)
        print('实验 A — 精确重建误差（应≈0）:', np.max(np.abs(x_rec_full - x_mel)))

        # 实验 B：截断重建
        print('\\n实验 B — 截断重建误差：')
        for k_keep in [3, 6, 13]:
            X_trunc = X_dct.copy()
            X_trunc[k_keep:] = 0.0
            x_trunc_rec = _idct_ii_ref(X_trunc)
            rmse = np.sqrt(np.mean((x_trunc_rec - x_mel) ** 2))
            print(f'  k_keep={k_keep:2d} → RMSE={rmse:.4f}')
        """
    ).strip()
    changed |= _replace_cell_source(nb, "_dct_ii_ref", new_cell_source)

    if changed:
        _write_nb(path, nb)
    return changed


def _update_l50() -> bool:
    path = NB_DIR / "L50_mfcc.ipynb"
    nb = _read_nb(path)
    marker = "## 4a. 进入 L50 前的 20 秒自检"
    if _contains_cell(nb, marker):
        return False

    intro = new_markdown_cell(
        dedent(
            """
            ## 4a. 进入 L50 前的 20 秒自检

            下面这组不是新知识，只是把前面几课的依赖显式列出来。
            先把每项写成 `True/False`，不确定就先回到对应课节。
            """
        ).strip()
    )
    checklist = new_code_cell(
        dedent(
            """
            pipeline_checklist = {
                "stft_shape_ok": None,  # 卡住回 L44：先确认 STFT 输出 (T, n_bins)
                "mel_matmul_ok": None,  # 卡住回 L47：先确认 power @ fb.T 的方向
                "log_floor_ok": None,   # 卡住回 L47：先想清为什么 log(max(power, eps)) 需要 eps
                "dct_ortho_ok": None,   # 卡住回 L49：回看 DCT-II 的正交归一化
            }

            pending = [name for name, value in pipeline_checklist.items() if value is None]
            print("把 None 改成 True/False；如果不确定，先回看对应课节。")
            print("待填写：", pending)
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "code" and _cell_source(cell).lstrip().startswith("def my_mfcc("),
        [intro, checklist],
    )
    _write_nb(path, nb)
    return True


def _update_l51() -> bool:
    path = NB_DIR / "L51_real_audio.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：真实 WAV 的三个坑"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：真实 WAV 的三个坑

            - 采样率可能不同：8k / 16k / 44.1k，必须和 samples 一起传递
            - 单声道 / 立体声先统一，再做特征
            - 幅度最好先归一化到 `[-1, 1]`

            `librosa` 在这里的角色只是对答案，不是生产依赖；`ROADMAP` 里的 “MFCC on LibriSpeech” 指的是把这条流水线接到真实数据集和训练任务上。
            如果前面的谐波 / Mel / DCT 记忆模糊，先回 L03、L07、L46、L47。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown"
        and "## 1. `read_wav()`" in _cell_source(cell),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l47_markdown(nb: nbformat.NotebookNode) -> bool:
    return _replace_cell_source(
        nb,
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**五步串联（每步一行代码）**：

| 步骤 | 代码 | 输出 shape |
|---|---|---|
| 1 | `S = stft(x, n_fft=win_len, hop_length=hop)` | `(n_fft//2+1, n_frames)` |
| 2 | `power = np.abs(S).T ** 2` | `(n_frames, n_fft//2+1)` |
| 3 | `fb = mel_filterbank(n_mels, win_len, sr)` | `(n_mels, n_fft//2+1)` |
| 4 | `mel_energy = power @ fb.T` | `(n_frames, n_mels)` |
| 5 | `return np.log(mel_energy + 1e-8)` | `(n_frames, n_mels)` |

**验收标准**：
- `np.allclose(log_mel_spectrogram(x, sr), aurora_ref, atol=1e-9)` 通过
- 输出无 `nan` 或 `-inf`（ε 保护有效）
- shape = `(n_frames, n_mels)`

> **注意**：`stft` 可能返回 `(n_fft//2+1, n_frames)`（列=帧），注意 `.T` 转置方向。""",
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**三步提示**：

1. 先拿到 STFT，再把复数幅度变成功率谱
2. 用 `mel_filterbank(...)` 把频率轴压到 `n_mels`
3. `np.log(... + 1e-8)` 只是数值保护，不是算法核心

**卡住回**：L44 / L46 / L47

**参考实现**：`solutions/L47_mel_implement_solutions.md`
""",
    )


def _update_l47_markdown_and_opening() -> bool:
    path = NB_DIR / "L47_mel_implement.ipynb"
    nb = _read_nb(path)
    changed = False

    if not _contains_cell(nb, "## 开课前 2 分钟复习：矩阵乘法就是滤波"):
        review = new_markdown_cell(
            dedent(
                """
                ## 开课前 2 分钟复习：矩阵乘法就是滤波

                - `power @ fb.T` 是把每帧功率谱投影到 Mel 三角滤波器上
                - 这里的 `fb` 来自 L46 的三角滤波器组
                - 记住 shape：`power (T,F)` × `fb.T (F,M)` → `mel_energy (T,M)`

                L21 里你已经见过同一件事的矩阵版本；现在只是在 Audio DSP 里重新出现。
                """
            ).strip()
        )
        _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "code"
            and _cell_source(cell).lstrip().startswith("import numpy as np"),
            [review],
        )
        changed = True

    if _update_l47_markdown(nb):
        changed = True

    if changed:
        _write_nb(path, nb)
    return changed


def _update_l47_opening() -> bool:
    # Kept for readability in main(); actual work is in _update_l47_markdown_and_opening.
    return False


def _update_l47_solution_file() -> bool:
    return _update_l47_solution()


def _update_l48() -> bool:
    path = NB_DIR / "L48_visual_stft.ipynb"
    nb = _read_nb(path)
    marker = "## 附录 · 为什么下一课要做 DCT？（回调 L49）"
    if _contains_cell(nb, marker):
        return False

    appendix = new_markdown_cell(
        dedent(
            """
            ## 附录 · 为什么下一课要做 DCT？（回调 L49）

            L48 已经把声音切成一帧一帧的谱图，也把线性频率轴压成了 Mel 轴。
            但 Mel 通道彼此高度相关，邻近通道常常在重复同一件事，相关系数往往接近 0.9。

            DCT 的作用有两层：

            - 去相关：把重复的 Mel 能量旋转到更独立的坐标上
            - 能量压缩：把大部分信息集中到前几个低阶系数里

            这和 JPEG 里对像素块做 DCT 的思路同源，只是这里处理的是音频谱包络，不是图像亮度。
            如果一时不清楚，先回看 L49 开头的 FFT vs DCT-II 差异表，再回来读这一段。

            L49 会把这个动机变成真正的 `dct_ii` 实现；本节先记住：

            **Mel 负责感知压缩，DCT 负责去相关。**
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
        [appendix],
    )
    _write_nb(path, nb)
    return True


def _update_l49() -> bool:
    path = NB_DIR / "L49_dct.ipynb"
    nb = _read_nb(path)
    changed = False

    marker = "## 0. 先看 FFT vs DCT-II：它们不是同一个东西"
    if not _contains_cell(nb, marker):
        intro = new_markdown_cell(
            dedent(
                """
                ## 0. 先看 FFT vs DCT-II：它们不是同一个东西

                | | FFT / DFT | DCT-II |
                |---|---|---|
                | 基函数 | 复指数 | 余弦 |
                | 边界假设 | 圆周 / 周期延拓 | 偶对称延拓 |
                | 输出 | 复数频谱 | 实数倒谱系数 |
                | 典型用途 | 频谱分析 | 去相关 / 压缩 |
                | Aurora | `aurora.audio.transforms.fft` | `aurora.audio.mfcc.dct_ii` |

                DCT-II 放在 log-Mel 后面，是因为相邻 Mel 通道高度相关；
                DCT 把重复信息旋转到更少的坐标里。
                如果忘了为什么要做这一步，回看 L48 末尾的动机附录。
                """
            ).strip()
        )
        _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown" and "## 1. DCT-II 公式" in _cell_source(cell),
            [intro],
        )
        changed = True

    if _replace_cell_source(
        nb,
        "# 注意：参考实现 _dct_ii_ref 已移至实验单元，避免完整答案出现在练习旁边",
        "# 注意：参考实现只保留在 notebooks/5_audio_dsp/solutions/L49_dct_solutions.md",
    ):
        changed = True

    new_cell = dedent(
        """
        # 实验与练习解耦：若本地 dct_ii 还没写完，则临时用 aurora.audio.mfcc.dct_ii 跑后续实验。
        from aurora.audio.mfcc import dct_ii as aurora_dct_ii

        # numpy-based inverse DCT-II reference
        def _idct_ii_ref(X):
            # Inverse of ortho DCT-II: X = D @ x  ⟹  x = D.T @ X
            # where D[k,n] = scale[k] * cos(pi*k*(2n+1)/(2N)),
            # scale[0]=sqrt(1/N), scale[k>0]=sqrt(2/N)
            N = len(X)
            k = np.arange(N)
            n = np.arange(N)
            scale = np.full(N, np.sqrt(2.0 / N))
            scale[0] = np.sqrt(1.0 / N)
            D = scale[:, None] * np.cos(np.pi * np.outer(k, 2 * n + 1) / (2 * N))
            return D.T @ X

        # 用一段 26 维模拟 Mel 能量做实验
        rng = np.random.default_rng(7)
        x_mel = rng.standard_normal(26)

        try:
            probe = dct_ii(np.array([1.0, 2.0]))
        except NotImplementedError:
            probe = None

        _impl = dct_ii if probe is not None else aurora_dct_ii
        if _impl is aurora_dct_ii:
            print('⚠️  dct_ii 尚未实现，使用 aurora.audio.mfcc.dct_ii 演示实验（完成 TODO 后可切换）')
        X_dct = _impl(x_mel)

        # 实验 A：精确逆变换
        x_rec_full = _idct_ii_ref(X_dct)
        print('实验 A — 精确重建误差（应≈0）:', np.max(np.abs(x_rec_full - x_mel)))

        # 实验 B：截断重建
        print('\\n实验 B — 截断重建误差：')
        for k_keep in [3, 6, 13]:
            X_trunc = X_dct.copy()
            X_trunc[k_keep:] = 0.0
            x_trunc_rec = _idct_ii_ref(X_trunc)
            rmse = np.sqrt(np.mean((x_trunc_rec - x_mel) ** 2))
            print(f'  k_keep={k_keep:2d} → RMSE={rmse:.4f}')
        """
    ).strip()
    if _replace_cell_source(nb, "_dct_ii_ref", new_cell):
        changed = True

    if changed:
        _write_nb(path, nb)
    return changed


def _update_l50() -> bool:
    path = NB_DIR / "L50_mfcc.ipynb"
    nb = _read_nb(path)
    marker = "## 4a. 进入 L50 前的 20 秒自检"
    if _contains_cell(nb, marker):
        return False

    intro = new_markdown_cell(
        dedent(
            """
            ## 4a. 进入 L50 前的 20 秒自检

            下面这组不是新知识，只是把前面几课的依赖显式列出来。
            先把每项写成 `True/False`，不确定就先回到对应课节。
            """
        ).strip()
    )
    checklist = new_code_cell(
        dedent(
            """
            pipeline_checklist = {
                "stft_shape_ok": None,  # 卡住回 L44：先确认 STFT 输出 (T, n_bins)
                "mel_matmul_ok": None,  # 卡住回 L47：先确认 power @ fb.T 的方向
                "log_floor_ok": None,   # 卡住回 L47：先想清为什么 log(max(power, eps)) 需要 eps
                "dct_ortho_ok": None,   # 卡住回 L49：回看 DCT-II 的正交归一化
            }

            pending = [name for name, value in pipeline_checklist.items() if value is None]
            print("把 None 改成 True/False；如果不确定，先回看对应课节。")
            print("待填写：", pending)
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "code" and _cell_source(cell).lstrip().startswith("def my_mfcc("),
        [intro, checklist],
    )
    _write_nb(path, nb)
    return True


def _update_l51() -> bool:
    path = NB_DIR / "L51_real_audio.ipynb"
    nb = _read_nb(path)
    marker = "## 开课前 2 分钟复习：真实 WAV 的三个坑"
    if _contains_cell(nb, marker):
        return False

    review = new_markdown_cell(
        dedent(
            """
            ## 开课前 2 分钟复习：真实 WAV 的三个坑

            - 采样率可能不同：8k / 16k / 44.1k，必须和 samples 一起传递
            - 单声道 / 立体声先统一，再做特征
            - 幅度最好先归一化到 `[-1, 1]`

            `librosa` 在这里的角色只是对答案，不是生产依赖；`ROADMAP` 里的 “MFCC on LibriSpeech” 指的是把这条流水线接到真实数据集和训练任务上。
            如果前面的谐波 / Mel / DCT 记忆模糊，先回 L03、L07、L46、L47。
            """
        ).strip()
    )
    _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 1. `read_wav()`" in _cell_source(cell),
        [review],
    )
    _write_nb(path, nb)
    return True


def _update_l47_markdown(nb: nbformat.NotebookNode) -> bool:
    return _replace_cell_source(
        nb,
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**五步串联（每步一行代码）**：

| 步骤 | 代码 | 输出 shape |
|---|---|---|
| 1 | `S = stft(x, n_fft=win_len, hop_length=hop)` | `(n_fft//2+1, n_frames)` |
| 2 | `power = np.abs(S).T ** 2` | `(n_frames, n_fft//2+1)` |
| 3 | `fb = mel_filterbank(n_mels, win_len, sr)` | `(n_mels, n_fft//2+1)` |
| 4 | `mel_energy = power @ fb.T` | `(n_frames, n_mels)` |
| 5 | `return np.log(mel_energy + 1e-8)` | `(n_frames, n_mels)` |

**验收标准**：
- `np.allclose(log_mel_spectrogram(x, sr), aurora_ref, atol=1e-9)` 通过
- 输出无 `nan` 或 `-inf`（ε 保护有效）
- shape = `(n_frames, n_mels)`

> **注意**：`stft` 可能返回 `(n_fft//2+1, n_frames)`（列=帧），注意 `.T` 转置方向。""",
        """## 4. ✏️ 实现 `log_mel_spectrogram(x, sr, n_mels=80, win_len=1024, hop=256)`

**三步提示**：

1. 先拿到 STFT，再把复数幅度变成功率谱
2. 用 `mel_filterbank(...)` 把频率轴压到 `n_mels`
3. `np.log(... + 1e-8)` 只是数值保护，不是算法核心

**卡住回**：L44 / L46 / L47

**参考实现**：`solutions/L47_mel_implement_solutions.md`
""",
    )


def _update_l47_and_solution() -> bool:
    path = NB_DIR / "L47_mel_implement.ipynb"
    nb = _read_nb(path)
    changed = False

    if not _contains_cell(nb, "## 开课前 2 分钟复习：矩阵乘法就是滤波"):
        review = new_markdown_cell(
            dedent(
                """
                ## 开课前 2 分钟复习：矩阵乘法就是滤波

                - `power @ fb.T` 是把每帧功率谱投影到 Mel 三角滤波器上
                - 这里的 `fb` 来自 L46 的三角滤波器组
                - 记住 shape：`power (T,F)` × `fb.T (F,M)` → `mel_energy (T,M)`

                L21 里你已经见过同一件事的矩阵版本；现在只是在 Audio DSP 里重新出现。
                """
            ).strip()
        )
        _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "code"
            and _cell_source(cell).lstrip().startswith("import numpy as np"),
            [review],
        )
        changed = True

    if _update_l47_markdown(nb):
        changed = True

    if changed:
        _write_nb(path, nb)

    changed |= _update_l47_solution()
    return changed


def _update_docs() -> bool:
    changed = False

    changed |= _replace_text(
        DSP_PLAN,
        [
            (
                "> **状态**：🟡 执行中（2026-07-01）— P0 Week1（L36–L39）✅ 已落地复审通过（L31–L40 polish）；P0 Week2（L42–L45）✅ 已落地待复审；P1 L31→L32 ✅ 已落地复审通过；P1 L48–L51 / P2（L03/L07/L21 回调源）📋 待做",
                "> **状态**：🟡 执行中（2026-07-01）— P0 Week1（L36–L39）✅ 已落地复审通过（L31–L40 polish）；P0 Week2（L42–L45）✅ 已落地待复审；P1 L31→L32 ✅ 已落地复审通过；P1 L48–L51 ✅ 已落地待复审；P2（L03/L07/L21/L35/L46/L47 回调源 + Obsidian）✅ 已落地待复审",
            ),
            (
                "| L46 | 末尾三角滤波器手绘练习（markdown） | 次级跃升 | P2 | 📋 |",
                "| L46 | 末尾三角滤波器手绘练习（markdown） | 次级跃升 | P2 | ✅ 已落地待复审 |",
            ),
            (
                "| L47 | 开篇 L21 矩阵滤波回调；推理路线删全文 for 循环 | 次级 + B1 | P2 | 📋 |",
                "| L47 | 开篇 L21 矩阵滤波回调；推理路线删全文 for 循环 | 次级 + B1 | P2 | ✅ 已落地待复审 |",
            ),
            (
                "| L48 | 末尾 DCT/倒谱动机预告（与 L49 二选一） | 断崖桥接 | P1 | 📋 |",
                "| L48 | 末尾 DCT/倒谱动机预告（与 L49 二选一） | 断崖桥接 | P1 | ✅ 已落地待复审 |",
            ),
            (
                "| L49 | FFT vs DCT 差异表；`_dct_ii_ref` 移出验证 cell；`solutions/L49_*.md` | 断崖桥接 + B4 | P1 | 📋 |",
                "| L49 | FFT vs DCT 差异表；`_dct_ii_ref` 移出验证 cell；`solutions/L49_*.md` | 断崖桥接 + B4 | P1 | ✅ 已落地待复审 |",
            ),
            (
                "| L50 | 流水线 checklist cell；每键「卡住回 Lxx」 | 断崖桥接 | P1 | 📋 |",
                "| L50 | 流水线 checklist cell；每键「卡住回 Lxx」 | 断崖桥接 | P1 | ✅ 已落地待复审 |",
            ),
            (
                "| L51 | 真实 WAV 坑 + librosa 定位 + ROADMAP 项说明 | 工程桥接 | P1 | 📋 |",
                "| L51 | 真实 WAV 坑 + librosa 定位 + ROADMAP 项说明 | 工程桥接 | P1 | ✅ 已落地待复审 |",
            ),
            (
                "| — | `obsidian/domains/audio-dsp.md`：跃升点导航节 | 汇总 | P2 | 📋 |",
                "| — | `obsidian/domains/audio-dsp.md`：跃升点导航节 | 汇总 | P2 | ✅ 已落地待复审 |",
            ),
            (
                "*下一步：P1 L48–L51（`apply_dsp_p1_l48_l51_supplement.py` 待写）→ P2 时间回调（L03/L07/L21 源课 + Obsidian）。已落地脚本：`apply_l36_supplement.py`、`apply_dsp_week1_l37_l39_supplement.py`、`apply_dsp_week2_l42_l45_supplement.py`、`apply_dsp_p1_l31_l32_supplement.py`、`apply_l31_l40_polish.py`（L31–L40 白板桥 + 答案泄漏修复 + L35 L07 回调）。*",
                "*下一步：人工复审 L48–L51 / P2 回调与泄漏扫描，确认导航与 solutions 同步。已落地脚本：`apply_l36_supplement.py`、`apply_dsp_week1_l37_l39_supplement.py`、`apply_dsp_week2_l42_l45_supplement.py`、`apply_dsp_p1_l31_l32_supplement.py`、`apply_l31_l40_polish.py`（L31–L40 白板桥 + 答案泄漏修复 + L35 L07 回调）、`apply_dsp_remaining_supplement.py`。*",
            ),
        ],
    )

    changed |= _replace_text(
        INDEX_PLAN,
        [
            (
                "| [`dsp-gap-supplement-plan.md`](dsp-gap-supplement-plan.md) | Phase 0 片段 + **Phase 1** | L03–L07、L21、L31–L53 | L37→L39、L43→L44 等 6 处 | 🟡 P0/P1 部分已落地；P2 待做 |",
                "| [`dsp-gap-supplement-plan.md`](dsp-gap-supplement-plan.md) | Phase 0 片段 + **Phase 1** | L03–L07、L21、L31–L53 | L37→L39、L43→L44 等 6 处 | 🟡 P0/P1/P2 已落地待复审 |",
            ),
        ],
    )

    return changed


def _update_obsidian_nav() -> bool:
    path = OBSIDIAN_AUDIO_DSP
    text = path.read_text(encoding="utf-8")
    if "## 跃升点导航" in text:
        return False

    section = dedent(
        """
        ## 跃升点导航

        - `L03` → `L32`：[[../../../notebooks/0_foundation/L03_spectrogram.ipynb|L03 谱图三轴]] → [[../../../notebooks/4_probability/L31_visual_probability.ipynb|L32 进入 L32 前的心理切换]]
        - `L07` → `L35`：[[../../../notebooks/1_complex_trig/L07_fourier_intuition.ipynb|L07 方波与谐波]] → [[../../../notebooks/5_audio_dsp/L35_euler_fft.ipynb|L35 开课前 2 分钟复习：方波 = 谐波叠加]]
        - `L21` → `L37`：[[../../../notebooks/2_linear_algebra/L21_aurora_matrices.ipynb|L21 矩阵即滤波]] → [[../../../notebooks/5_audio_dsp/L37_dft.ipynb|L37 复习桥 · L21 的 DFT 矩阵]]
        - `L21` → `L47`：[[../../../notebooks/2_linear_algebra/L21_aurora_matrices.ipynb|L21 矩阵即滤波]] → [[../../../notebooks/5_audio_dsp/L47_mel_implement.ipynb|L47 开课前 2 分钟复习：矩阵乘法就是滤波]]
        - `L35` → `L38`：[[../../../notebooks/5_audio_dsp/L35_euler_fft.ipynb|L35 欧拉公式与 FFT]] → [[../../../notebooks/5_audio_dsp/L38_fft_butterfly.ipynb|L38 开课前 2 分钟复习：方波 = 谐波叠加]]
        - `L46` → `L47`：[[../../../notebooks/5_audio_dsp/L46_mel.ipynb|L46 Mel 频率尺度]] → [[../../../notebooks/5_audio_dsp/L47_mel_implement.ipynb|L47 三角滤波器三锚点]]
        - `L48` → `L49` → `L50` → `L51`：[[../../../notebooks/5_audio_dsp/L48_visual_stft.ipynb|L48 时频图解]] → [[../../../notebooks/5_audio_dsp/L49_dct.ipynb|L49 DCT 差异表]] → [[../../../notebooks/5_audio_dsp/L50_mfcc.ipynb|L50 MFCC 流水线清单]] → [[../../../notebooks/5_audio_dsp/L51_real_audio.ipynb|L51 真实 WAV 工程桥接]]
        """
    ).strip() + "\n\n"
    new_text = text.replace("\n---\n\n## Signal Basics\n", f"\n---\n\n{section}## Signal Basics\n", 1)
    if new_text == text:
        raise RuntimeError("audio-dsp obsidian insertion point not found")
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed = False
    changed |= _update_l03()
    changed |= _update_l07()
    changed |= _update_l21()
    changed |= _update_l35()
    changed |= _update_l39()
    changed |= _update_l46()
    changed |= _update_l47_and_solution()
    changed |= _update_l48()
    changed |= _update_l49()
    changed |= _update_l50()
    changed |= _update_l51()
    changed |= _update_docs()
    changed |= _update_obsidian_nav()

    if changed:
        print("Applied remaining DSP supplement updates.")
    else:
        print("No changes needed; supplement already applied.")


if __name__ == "__main__":
    main()

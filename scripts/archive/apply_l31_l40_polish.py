#!/usr/bin/env python3
"""Additive polish for L31–L40 notebooks (incl. DSP P0 segment re-review)."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS = {
    31: ROOT / "notebooks/4_probability/L31_visual_probability.ipynb",
    32: ROOT / "notebooks/5_audio_dsp/L32_numpy_signals.ipynb",
    33: ROOT / "notebooks/5_audio_dsp/L33_sine_wave.ipynb",
    34: ROOT / "notebooks/5_audio_dsp/L34_aliasing.ipynb",
    35: ROOT / "notebooks/5_audio_dsp/L35_euler_fft.ipynb",
    36: ROOT / "notebooks/5_audio_dsp/L36_windows.ipynb",
    37: ROOT / "notebooks/5_audio_dsp/L37_dft.ipynb",
    38: ROOT / "notebooks/5_audio_dsp/L38_fft_butterfly.ipynb",
    39: ROOT / "notebooks/5_audio_dsp/L39_fft_implement.ipynb",
    40: ROOT / "notebooks/5_audio_dsp/L40_spectrum.ipynb",
}

L31_REVIEW = """# ✏️ 本课自评
l31_review = {
    "lln_curve_seen":          None,  # 看过频率收敛曲线？True/False
    "softmax_sum_one":         None,  # 能手推 softmax 输出和为 1？True/False
    "cross_entropy_understood": None,  # 理解交叉熵损失曲面含义？True/False
    "shannon_entropy_seen":    None,  # 看过 Shannon 熵曲线？True/False
    "l32_prep_read":           None,  # 读过 L31→L32 切换清单？True/False
}

unfilled = [k for k, v in l31_review.items() if v is None]
assert not unfilled, f'还未填写：{unfilled}'
weak = [k for k, v in l31_review.items() if v is False]
if weak:
    print(f'⚠️  需要加强：{weak}')
else:
    print('✅ L31 全部通关！进入 L32：NumPy 信号基础')
"""

L35_L07_BRIDGE = """## 复习桥 · L07 方波 = 谐波叠加（2 分钟）

L07 已证：周期波形可写成正弦波的加权和——方波 ≈ 奇次谐波 `sin(2πkt)/k` 的叠加。

DFT/FFT 做的是**逆问题**：给定一段信号，问「每个频率分量有多大？」
今天写的 `twiddle(k, n, N)` 就是离散时间第 `n` 步、频率 `k` 上的旋转位置。

带着这个对照进入欧拉公式：复指数不是新东西，是把 sin/cos 合并成单位圆上的坐标。
"""

ANSWER_REPLACEMENTS = [
    (
        'except NotImplementedError:\n    print(f"      my_sine 待实现（纯手算已验证 ✅）")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 my_sine()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  alias(6000, 8000) = |6000-8000×1| = 2000 Hz（predict_alias_freq 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 predict_alias_freq()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q2 ✅  alias(3000, 8000) = 3000 Hz（不折叠，predict_alias_freq 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q2：请先实现 predict_alias_freq()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q3 ✅  alias(9000, 8000) = |9000-8000×1| = 1000 Hz（predict_alias_freq 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q3：请先实现 predict_alias_freq()，再运行对答案格")',
    ),
    (
        "except NotImplementedError:\n    # 直接用公式验证\n    for theta, expected in [(0, 1+0j), (np.pi/2, 1j), (np.pi, -1+0j)]:\n        computed = np.cos(theta) + 1j*np.sin(theta)\n        assert np.isclose(computed, expected, atol=1e-12)\n    print(f\"Q1 ✅  euler(0)=1+0j  euler(π/2)≈0+1j  euler(π)=-1+0j  (euler 待实现)\")",
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 euler()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q3 ✅  twiddle(1,2,8) = e^{{-πi/2}} = 0-1j  (twiddle 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q3：请先实现 twiddle()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q4 ✅  twiddle(0,n,N)=e^(-2πi·0·n/N)=e^0=1（twiddle 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q4：请先实现 twiddle()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q5 ✅  Blackman 旁瓣-58dB >> Hann -31dB，代价：主瓣宽度增加约 50%（分辨率下降）")',
        'except NotImplementedError:\n    print("⬜ Q5：请先实现 describe_window()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  X[0]={X_np[0]:.4f}（DC=0），X[2]={X_np[2]:.4f}（naive_dft 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 naive_dft()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  N=1 时 DFT(x)=x，直接返回 x.astype(complex)（my_fft 待实现）")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 my_fft()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"      (my_fft 待实现，手算结果正确)")',
        'except NotImplementedError:\n    print("      ⬜ 请先实现 my_fft()，再运行对答案格")',
    ),
    (
        "except NotImplementedError:\n    # 验证手算\n    freqs_hand = np.arange(8) * 8000 / 8\n    result_hand = freqs_hand[:8//2+1]\n    assert np.allclose(result_hand, expected_bins, atol=1e-10)\n    print(f\"Q2 ✅  frequency_bins(8,8000)={result_hand}（frequency_bins 待实现）\")",
        'except NotImplementedError:\n    print("⬜ Q2：请先实现 frequency_bins()，再运行对答案格")',
    ),
]


def load_nb(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def text_of(cell: dict) -> str:
    return "".join(cell.get("source", []))


def set_text(cell: dict, text: str) -> None:
    cell["source"] = text.splitlines(keepends=True)


def add_whiteboard_bridge(nb: dict) -> None:
    if any(cell.get("id") == "whiteboard-bridge" for cell in nb["cells"]):
        return
    bridge = {
        "cell_type": "markdown",
        "id": "whiteboard-bridge",
        "metadata": {},
        "source": [
            "---\n",
            "⬇️ **通关检验**：收束小结已读；请完成下方白板挑战后再勾选自评。\n",
        ],
    }
    for idx, cell in enumerate(nb["cells"]):
        if "## ✏️ 白板挑战" in text_of(cell):
            nb["cells"].insert(idx, bridge)
            return


def add_halfstep_bridge(nb: dict) -> None:
    if any(cell.get("id") == "halfstep-bridge" for cell in nb["cells"]):
        return
    bridge = {
        "cell_type": "markdown",
        "id": "halfstep-bridge",
        "metadata": {},
        "source": [
            "---\n",
            "⬇️ **通关检验**：附录 B 已读；请完成下方 N=4 半步蝶形草稿后再进入主 TODO。\n",
        ],
    }
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("id") == "l38-n4-half-step" or "## 半步练习 · N=4 蝶形草稿" in text_of(
            cell
        ):
            nb["cells"].insert(idx, bridge)
            return


def patch_answer_leaks(nb: dict) -> None:
    for cell in nb["cells"]:
        if "# ✏️ 对答案格" not in text_of(cell):
            continue
        src = text_of(cell)
        for old, new in ANSWER_REPLACEMENTS:
            src = src.replace(old, new)
        set_text(cell, src)


def patch_l31(nb: dict) -> None:
    if any("l31_review" in text_of(c) for c in nb["cells"]):
        return
    review = {
        "cell_type": "code",
        "id": "l31_review",
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": L31_REVIEW.splitlines(keepends=True),
    }
    bridge = {
        "cell_type": "markdown",
        "id": "l31-closing-bridge",
        "metadata": {},
        "source": [
            "---\n",
            "⬇️ **通关检验**：六张图与收束小结已读；请勾选自评后再进入 L32。\n",
        ],
    }
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("id") == "nav-l31-clos":
            if not any(c.get("id") == "l31-closing-bridge" for c in nb["cells"]):
                nb["cells"].insert(idx, bridge)
            nb["cells"].insert(idx, review)
            return


def patch_l35_l07_recall(nb: dict) -> None:
    if any(cell.get("id") == "l35-l07-recall" for cell in nb["cells"]):
        return
    bridge = {
        "cell_type": "markdown",
        "id": "l35-l07-recall",
        "metadata": {},
        "source": L35_L07_BRIDGE.splitlines(keepends=True),
    }
    for idx, cell in enumerate(nb["cells"]):
        if "## 本课剧情" in text_of(cell):
            nb["cells"].insert(idx, bridge)
            return


def patch_notebook(lesson: int, nb: dict) -> None:
    if lesson == 31:
        patch_l31(nb)
    if lesson == 35:
        patch_l35_l07_recall(nb)
    if lesson == 38:
        add_halfstep_bridge(nb)
    if lesson in range(32, 41) and lesson != 38:
        add_whiteboard_bridge(nb)
    patch_answer_leaks(nb)


def validate_nb(name: str, text: str) -> None:
    nb = json.loads(text)
    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        try:
            ast.parse(text_of(cell))
        except SyntaxError as exc:
            raise SyntaxError(f"{name} cell {idx}: {exc}") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    summary = {}
    for lesson, path in NOTEBOOKS.items():
        nb = load_nb(path)
        before = len(nb["cells"])
        patch_notebook(lesson, nb)
        text = json.dumps(nb, ensure_ascii=False, indent=1) + "\n"
        validate_nb(path.name, text)
        summary[str(path)] = {"cells_before": before, "cells_after": len(nb["cells"])}
        if args.apply:
            path.write_text(text, encoding="utf-8")

    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "files": summary}, indent=2))


if __name__ == "__main__":
    main()
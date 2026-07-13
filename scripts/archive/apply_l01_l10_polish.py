#!/usr/bin/env python3
"""Additive polish for L01–L10 notebooks (navigation, leaks, guards, bridges)."""

from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

L01 = ROOT / "notebooks/0_foundation/L01_motivation.ipynb"
L02 = ROOT / "notebooks/0_foundation/L02_sound_digital.ipynb"
L03 = ROOT / "notebooks/0_foundation/L03_spectrogram.ipynb"
L04 = ROOT / "notebooks/1_complex_trig/L04_trig.ipynb"
L05 = ROOT / "notebooks/1_complex_trig/L05_complex_numbers.ipynb"
L07 = ROOT / "notebooks/1_complex_trig/L07_fourier_intuition.ipynb"
L06 = ROOT / "notebooks/1_complex_trig/L06_euler.ipynb"
L08 = ROOT / "notebooks/1_complex_trig/L08_visual_complex.ipynb"
L09 = ROOT / "notebooks/2_linear_algebra/L09_vectors.ipynb"
L10 = ROOT / "notebooks/2_linear_algebra/L10_dot_product.ipynb"


def load_nb(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_nb(nb: dict) -> str:
    return json.dumps(nb, ensure_ascii=False, indent=1) + "\n"


def text_of(cell: dict) -> str:
    return "".join(cell.get("source", []))


def set_text(cell: dict, text: str) -> None:
    cell["source"] = text.splitlines(keepends=True)


def insert_after(cells: list, needle: str, new_cells: list[dict]) -> None:
    for idx, cell in enumerate(cells):
        if needle in text_of(cell):
            cells[idx + 1 : idx + 1] = new_cells
            return
    raise RuntimeError(f"needle not found: {needle!r}")


def move_cell_after(cells: list, src_id: str, after_needle: str) -> None:
    src_idx = next((i for i, c in enumerate(cells) if c.get("id") == src_id), None)
    if src_idx is None:
        raise RuntimeError(f"cell id not found: {src_id}")
    cell = cells.pop(src_idx)
    for idx, c in enumerate(cells):
        if after_needle in text_of(c):
            cells.insert(idx + 1, cell)
            return
    raise RuntimeError(f"anchor not found after move: {after_needle!r}")


def validate_nb(name: str, text: str) -> None:
    nb = json.loads(text)
    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        try:
            ast.parse(text_of(cell))
        except SyntaxError as exc:
            raise SyntaxError(f"{name} cell {idx}: {exc}") from exc


def patch_l01(nb: dict) -> None:
    if "nav-l01-open" not in dump_nb(nb):
        nav = {
            "cell_type": "markdown",
            "id": "nav-l01-open",
            "metadata": {"tags": ["nav"]},
            "source": [
                "← **起点课**　无上一课\n",
                "\n",
                "> 本课建立 Aurora 动机、路线图与环境自检工具。\n",
                "> 下一课进入 **声音的数字表示**（L02）。\n",
            ],
        }
        insert_after(nb["cells"], "# 第1课 · Aurora 是什么", [nav])

    env_guard = """import sys
from pathlib import Path

try:
    report = environment_report()

    assert report['python_executable'] == sys.executable,  'python_executable 不正确'
    assert report['python_version'] == sys.version,        'python_version 不正确'
    assert isinstance(report['aurora_available'], bool),   'aurora_available 应为布尔值'
    assert report['project_root'] is not None,             'project_root 未找到'
    assert (Path(report['project_root']) / 'pyproject.toml').exists(), \\
        f"project_root={report['project_root']} 下没有 pyproject.toml"

    print('environment_report 通过')
    print()
    for k, v in report.items():
        val = str(v)[:80] + '...' if len(str(v)) > 80 else str(v)
        print(f'  {k}: {val}')
except NotImplementedError:
    print('⬜ environment_report 未实现，请填写函数体后再运行验证')
except (TypeError, AssertionError) as exc:
    print(f'⚠️ environment_report 验证未通过：{exc}')
    print('   提示：先实现四个键的返回值，再重新运行本格。')
"""
    for cell in nb["cells"]:
        if cell.get("id") != "c19":
            continue
        if "except NotImplementedError" in text_of(cell):
            return
        set_text(cell, env_guard)
        return


def patch_l02(nb: dict) -> None:
    for cell in nb["cells"]:
        if "## Aurora 连接" not in text_of(cell):
            continue
        set_text(
            cell,
            "## Aurora 连接\n\n"
            "本课四个函数是**课程学生版**（你在 notebook 内实现并验证）。\n"
            "它们与 Aurora Audio Core 的频域管线在概念上对齐，但**不是** `transforms.py` 的现成 API：\n\n"
            "| 本课函数 | 概念对应 | 说明 |\n"
            "|---|---|---|\n"
            "| `samples_count` | 帧长 / 采样点数 | 所有信号函数的第一步 |\n"
            "| `make_time_axis` | `t[n]=n/sr` | L32 会再次建立时间轴 |\n"
            "| `make_sine` | 正弦波生成 | L33–L37 反复使用 |\n"
            "| `signal_summary` | 信号统计摘要 | L40、L51 会读 RMS 等量 |\n\n"
            "> `src/aurora/audio/transforms.py` 现含 `dft` / `fft` / `stft` 等频域核；\n"
            "> 本课版本在 L32 管线中与你今日实现对接，不要直接 `from aurora.audio.transforms import make_sine`。\n\n"
            "L32（`notebooks/5_audio_dsp/L32_numpy_signals.ipynb`）会复用本课直觉，"
            "把「采样点 + 时间坐标」搭成完整信号地基。\n",
        )
        break

    if any(c.get("id") == "a1f71ebf" for c in nb["cells"]):
        move_cell_after(nb["cells"], "a1f71ebf", "## 本课收束")


def patch_l03(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if '"sig_c_sweep"' in src:
            set_text(
                cell,
                src.replace(
                    '"sig_c_sweep":       None,      # 描述 sig_c (200→3000 Hz 扫频) 的谱图形状',
                    '"sig_c_chord":       None,      # 描述 sig_c (500 Hz + 1500 Hz 双频叠加) 的谱图形状',
                ),
            )
        if "参考答案包含" in src:
            set_text(
                cell,
                src.replace(
                    "        print(f'  {fig} ⚠️  参考答案包含：{keywords}')",
                    "        print(f'  {fig} ⚠️  与 §2 四种指纹对照后再填；勿在本格查答案关键词')",
                ),
            )
        if src.startswith("## 本课收束") and "通关检验" not in src:
            set_text(
                cell,
                src
                + "\n---\n"
                + "⬇️ **通关检验**：收束小结已读；请完成下方「读谱图挑战」后再勾选自评。\n",
            )


def add_whiteboard_bridge(nb: dict) -> None:
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
        if cell.get("id") == "whiteboard-bridge":
            return
        if "## ✏️ 白板挑战" in text_of(cell):
            nb["cells"].insert(idx, bridge)
            return


def patch_l04(nb: dict) -> None:
    add_whiteboard_bridge(nb)


def patch_l05(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if "白板挑战：复数手算" in src and "arctan(4/3)" in src:
            set_text(
                cell,
                src.replace(
                    "**问 2**：z 的相位（phase）是多少弧度？公式 θ = arctan2(b, a)，arctan(4/3) ≈ 53.13° ≈ 0.9273 rad。",
                    "**问 2**：z 的相位（phase）是多少弧度？公式 θ = arctan2(b, a)（先手算，再运行对答案格）。",
                ),
            )


def patch_l07(nb: dict) -> None:
    add_whiteboard_bridge(nb)


def patch_l06(nb: dict) -> None:
    guard_twiddle = (
        "import numpy as np\n"
        "try:\n"
        "    assert abs(twiddle(0, 0, 8) - 1) < 1e-12, 'k·n=0 应为 1'\n"
        "    assert abs(abs(twiddle(3, 5, 8)) - 1) < 1e-12, '模长应为 1'\n"
        "    _ref = np.exp(-2j * np.pi * 1 * 1 / 8)\n"
        "    assert abs(twiddle(1, 1, 8) - _ref) < 1e-12, '相位方向错误：公式是 e^{-2πikn/N}，负号不能省'\n"
        "    print('✅ 通过：你握住了 FFT 的旋转因子。')\n"
        "except NotImplementedError:\n"
        "    print('⬜ 请先实现 twiddle(k, n, N)，再运行验证格')\n"
    )
    guard_phase = (
        "import numpy as np\n"
        "\n"
        "try:\n"
        "    # 学习目标 #4：确认旋转因子相位均匀递减，步长为 -2π/N\n"
        "    N = 8\n"
        "    for n in range(N):\n"
        "        w = twiddle(k=1, n=n, N=N)\n"
        "        print(f'n={n} | angle={np.angle(w):.4f} rad ({np.degrees(np.angle(w)):.1f}°)')\n"
        "\n"
        "    phases = [np.angle(twiddle(1, n, 8)) for n in range(8)]\n"
        "    diffs = np.diff(np.unwrap(phases))\n"
        "    assert np.allclose(diffs, -2 * np.pi / 8), '相位步长不均匀，检查 twiddle 实现'\n"
        "    print(f'\\n✅ 相位步长均匀，每步 {-2*np.pi/8:.4f} rad（= -2π/8）')\n"
        "    print('再把 N 改成 4 或 1024，感受 N 对频率分辨率的控制。')\n"
        "except NotImplementedError:\n"
        "    print('⬜ 请先实现 twiddle(k, n, N)，再运行相位实验')\n"
    )

    for cell in nb["cells"]:
        src = text_of(cell)
        if cell.get("id") == "25a0ea10" or (
            "assert abs(twiddle(0, 0, 8)" in src and "phase_experiment" not in (cell.get("id") or "")
        ):
            if "except NotImplementedError" not in src:
                set_text(cell, guard_twiddle)
        if cell.get("id") == "phase_experiment_L06":
            set_text(cell, guard_phase)
        if "白板挑战：旋转因子手算" in src:
            set_text(
                cell,
                "## ✏️ 白板挑战：旋转因子手算（目标 8 分钟）\n\n"
                "盖上屏幕，纸上作答：\n\n"
                "**参数**：N = 8（8 点 DFT），k = 1，n = 0, 1, 2, 3\n\n"
                "**问 1**：写出旋转因子公式 `W(k,n,N) = e^{-2πi·k·n/N}`，代入 k=1, N=8，化简指数部分。\n\n"
                "**问 2**：计算 W(1, 0, 8)、W(1, 1, 8)、W(1, 2, 8)、W(1, 3, 8) 的值（极坐标或直角坐标均可）。\n"
                "提示：先手算，再运行下方对答案格；需要公式提示时展开下方折叠块。\n\n"
                "<details><summary>卡住时可展开（先尽量不用）</summary>\n\n"
                "W(1,n,8) = e^{-iπn/4}；n=0→1，n=1→e^{-iπ/4}=cos(-45°)+i·sin(-45°)…\n\n"
                "</details>\n\n"
                "**问 3**：这 8 个旋转因子（n=0…7）均匀分布在单位圆的哪个方向？顺时针还是逆时针？\n\n"
                "**问 4**：若 k=0，所有旋转因子 W(0,n,N) 等于多少？为什么？\n\n"
                "推导完成后运行下面格对答案。",
            )
        if "三角波叠加合成方波" in src:
            set_text(cell, src.replace("三角波叠加合成方波", "正弦波谐波叠加合成方波"))


def patch_l08(nb: dict) -> None:
    has_review = any("l08_review" in text_of(c) for c in nb["cells"])
    for cell in nb["cells"]:
        src = text_of(cell)
        if "Aurora 的手写 FFT（`notebooks/1_complex_trig/L06_euler.ipynb`）" in src:
            set_text(
                cell,
                src.replace(
                    "Aurora 的手写 FFT（`notebooks/1_complex_trig/L06_euler.ipynb`）直接用这组单位根构造 DFT 矩阵。",
                    "L06 的旋转因子几何（`twiddle`）与本课单位根一致；L37–L39 会手写 FFT / DFT 矩阵。",
                ),
            )
        if src.startswith("# 验证 plot_conjugate 的数学属性"):
            set_text(
                cell,
                "# 共轭的数学性质（验证公式，不是白板答案格）\n" + src,
            )

    if not has_review:
        review = {
            "cell_type": "code",
            "id": "l08_review",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "# ✏️ 本课自评\n",
                "l08_review = {\n",
                '    "plot_conjugate_done":    None,  # plot_conjugate 实现并通过断言？True/False\n',
                '    "unit_circle_intuition":  None,  # 能把 e^{iθ} 与单位圆旋转对应？True/False\n',
                '    "twiddle_geometry":       None,  # 能解释单位根与 L06 twiddle 的关系？True/False\n',
                '    "whiteboard_passed":      None,  # 白板挑战完成？True/False\n',
                "}\n",
                "\n",
                "unfilled = [k for k, v in l08_review.items() if v is None]\n",
                "assert not unfilled, f'还未填写：{unfilled}'\n",
                "weak = [k for k, v in l08_review.items() if v is False]\n",
                "if weak:\n",
                "    print(f'⚠️  需要加强：{weak}')\n",
                "else:\n",
                "    print('✅ L08 全部通关！进入 L09：向量基础')\n",
            ],
        }
        for idx, cell in enumerate(nb["cells"]):
            if cell.get("id") == "nav-l08-clos":
                nb["cells"].insert(idx, review)
                break


def patch_l09(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if "# ✏️ 对答案格" not in src or "except NotImplementedError" not in src:
            continue
        set_text(
            cell,
            re.sub(
                r"except NotImplementedError:\n    q\d = [^\n]+\n    print\(f\"Q\d ✅[^\"]+\"\)",
                lambda m: m.group(0).split("\n")[0]
                + '\n    print("⬜ 请先实现上方函数，再运行对答案格")',
                src,
            ),
        )
        # cleaner explicit replace for the three blocks
        set_text(
            cell,
            "# ✏️ 对答案格\n"
            "import numpy as np\n\n"
            "passed = []\n\n"
            "# 问1：scale\n"
            "v, c = np.array([3.0, 4.0]), 2.5\n"
            "q1_expected = np.array([7.5, 10.0])\n"
            "try:\n"
            "    q1 = scale(v, c)\n"
            "    assert np.allclose(q1, q1_expected, atol=1e-10), f\"scale 结果 {q1} 与期望 {q1_expected} 不符\"\n"
            '    print(f"Q1 ✅  scale([3,4], 2.5) = {q1}")\n'
            "    passed.append(1)\n"
            "except NotImplementedError:\n"
            '    print("⬜ Q1：请先实现 scale()，再运行对答案格")\n\n'
            "# 问2：add_signals\n"
            "a, b = np.array([1.0, -0.5, 0.8]), np.array([0.2, 0.7, -0.3])\n"
            "q2_expected = np.array([1.2, 0.2, 0.5])\n"
            "try:\n"
            "    q2 = add_signals(a, b)\n"
            "    assert np.allclose(q2, q2_expected, atol=1e-10)\n"
            '    print(f"Q2 ✅  add_signals = {q2}")\n'
            "    passed.append(2)\n"
            "except NotImplementedError:\n"
            '    print("⬜ Q2：请先实现 add_signals()，再运行对答案格")\n\n'
            "# 问3：linear_combination\n"
            "coeffs = [2.0, -1.0, 0.5]\n"
            "vecs   = [np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([2.0, 2.0])]\n"
            "q3_expected = np.array([3.0, 0.0])\n"
            "try:\n"
            "    q3 = linear_combination(coeffs, vecs)\n"
            "    assert np.allclose(q3, q3_expected, atol=1e-10)\n"
            '    print(f"Q3 ✅  linear_combination = {q3}")\n'
            "    passed.append(3)\n"
            "except NotImplementedError:\n"
            '    print("⬜ Q3：请先实现 linear_combination()，再运行对答案格")\n\n'
            "if len(passed) == 3:\n"
            '    print("\\n🎉 白板挑战通过！向量三运算已内化。")\n',
        )
        break

    # remove empty markdown cells
    nb["cells"] = [
        c
        for c in nb["cells"]
        if not (c.get("cell_type") == "markdown" and text_of(c).strip() == "")
    ]


def patch_l10(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if src.startswith("## 本课收束") and "投影" not in src:
            set_text(
                cell,
                "## 本课收束\n\n"
                "`cosine_similarity(a, b)` 现在能把 `Σaᵢbᵢ` 归一化到 [-1, 1]。"
                "标量/向量投影是点积的几何输出——DFT 每个频点也是信号在对应基上的投影。"
                "Aurora 的 `dft()` 里，每个 `X[k]` 的计算就是信号数组与复指数序列的点积，"
                "和本节的代数结构完全相同。"
                "下一课：**L11** 讲范数，它是余弦相似度分母的来源，也是衡量向量「大小」的工具。",
            )
        if "l10_review" in src and "projection_understood" not in src:
            set_text(
                cell,
                src.replace(
                    '    "whiteboard_passed":             None,  # 白板挑战纸上推导完成？True/False\n',
                    '    "projection_understood":         None,  # 能解释标量/向量投影公式？True/False\n'
                    '    "whiteboard_passed":             None,  # 白板挑战纸上推导完成？True/False\n',
                ),
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    patches = [
        (L01, patch_l01),
        (L02, patch_l02),
        (L03, patch_l03),
        (L04, patch_l04),
        (L05, patch_l05),
        (L07, patch_l07),
        (L06, patch_l06),
        (L08, patch_l08),
        (L09, patch_l09),
        (L10, patch_l10),
    ]

    results = {}
    for path, fn in patches:
        nb = load_nb(path)
        before = len(nb["cells"])
        fn(nb)
        text = dump_nb(nb)
        validate_nb(path.name, text)
        results[str(path)] = {"cells_before": before, "cells_after": len(nb["cells"])}
        if args.apply:
            path.write_text(text, encoding="utf-8")

    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "files": results}, indent=2))


if __name__ == "__main__":
    main()
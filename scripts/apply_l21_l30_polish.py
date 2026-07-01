#!/usr/bin/env python3
"""Additive polish for L21–L30 notebooks."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS = {
    21: ROOT / "notebooks/2_linear_algebra/L21_aurora_matrices.ipynb",
    22: ROOT / "notebooks/3_calculus/L22_derivatives.ipynb",
    23: ROOT / "notebooks/3_calculus/L23_gradients.ipynb",
    24: ROOT / "notebooks/3_calculus/L24_chain_rule.ipynb",
    25: ROOT / "notebooks/3_calculus/L25_gradient_descent.ipynb",
    26: ROOT / "notebooks/3_calculus/L26_visual_calculus.ipynb",
    27: ROOT / "notebooks/4_probability/L27_probability_basics.ipynb",
    28: ROOT / "notebooks/4_probability/L28_descriptive_stats.ipynb",
    29: ROOT / "notebooks/4_probability/L29_distributions.ipynb",
    30: ROOT / "notebooks/4_probability/L30_softmax_crossentropy.ipynb",
}

L21_L37_BRIDGE = """## 前向锚点 · L37 将用循环写同一变换（2 分钟）

本课用矩阵形式：`X = W @ x`，与 `np.fft.fft(x)` 数值相同（`atol=1e-10`）。

**L37** 会换一种写法：不用整矩阵，用双重循环直接写
`X[k] = Σₙ x[n]·e^{-2πikn/N}`——两种写法等价；
矩阵版帮你记住「FFT = 线性变换」，循环版帮你记住每个指数项。
"""

L26_REVIEW = """# ✏️ 本课自评
l26_review = {
    "tangent_visualized":        None,  # 能解释切线 = 局部线性近似？True/False
    "descent_trajectory_seen":   None,  # 看过 descent/contour 轨迹图？True/False
    "lr_compare_understood":     None,  # 能对比不同 lr 的收敛/发散？True/False
    "l25_connection":            None,  # 理解与 L25 gd_step 同一更新规则？True/False
}

unfilled = [k for k, v in l26_review.items() if v is None]
assert not unfilled, f'还未填写：{unfilled}'
weak = [k for k, v in l26_review.items() if v is False]
if weak:
    print(f'⚠️  需要加强：{weak}')
else:
    print('✅ L26 全部通关！进入 L27：概率基础')
"""

ANSWER_REPLACEMENTS = [
    (
        "except NotImplementedError:\n    # 展示正确实现\n    k_i = np.arange(N)[:, None]\n    n_i = np.arange(N)[None, :]\n    W_ref = np.exp(-2j * np.pi * k_i * n_i / N)\n    x_ref = np.random.default_rng(42).standard_normal(N)\n    assert np.allclose(W_ref @ x_ref, np.fft.fft(x_ref), atol=1e-10)\n    print(f\"Q4 ✅  正确写法：np.exp(-2j*np.pi*np.outer(k,n)/N)  (build_dft_matrix 待实现)\")",
        'except NotImplementedError:\n    print("⬜ Q4：请先实现 build_dft_matrix()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  f\'(x)=3x²，f\'(2)={df1_analytical(2)}  (numeric_derivative 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 numeric_derivative()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q2 ✅  ∇f(3,4)={grad_analytical}  (gradient 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q2：请先实现 gradient()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q3 ✅  ∇f(1,1,1)={grad_3d_analytical}  (gradient 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q3：请先实现 gradient()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  dy/dx|_{x=1} = cos(1)·2 = {dy_dx1:.6f}  (composite_derivative 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 composite_derivative()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q2 ✅  gd_step(0.0,-6.0,0.1) = 0 - 0.1×(-6) = 0.6  (gd_step 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q2：请先实现 gd_step()，再运行对答案格")',
    ),
    (
        "except NotImplementedError:\n    # 验证公式正确性\n    z_manual = (x - x.mean()) / x.std()\n    assert abs(z_manual.mean()) < 1e-10 and abs(z_manual.std() - 1.0) < 1e-10\n    print(f\"Q3 ✅  (x-μ)/σ → mean={z_manual.mean():.2e}≈0，std={z_manual.std():.6f}≈1  (zscore 待实现)\")",
        'except NotImplementedError:\n    print("⬜ Q3：请先实现 zscore()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  f(0;0,1)=1/√(2π)={peak_expected:.6f}  (gaussian_pdf 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 gaussian_pdf()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q1 ✅  softmax([2,1,0.1])={np.round(sm_expected,4)}  (softmax 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q1：请先实现 softmax()，再运行对答案格")',
    ),
    (
        'except NotImplementedError:\n    print(f"Q2 ✅  CE=-log({sm_expected[0]:.4f})={ce_expected:.5f}  (cross_entropy 待实现)")',
        'except NotImplementedError:\n    print("⬜ Q2：请先实现 cross_entropy()，再运行对答案格")',
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


def patch_answer_leaks(nb: dict) -> None:
    for cell in nb["cells"]:
        if "# ✏️ 对答案格" not in text_of(cell):
            continue
        src = text_of(cell)
        for old, new in ANSWER_REPLACEMENTS:
            src = src.replace(old, new)
        set_text(cell, src)


def patch_l21(nb: dict) -> None:
    if "l21-l37-bridge" in json.dumps(nb, ensure_ascii=False):
        return
    bridge = {
        "cell_type": "markdown",
        "id": "l21-l37-bridge",
        "metadata": {},
        "source": L21_L37_BRIDGE.splitlines(keepends=True),
    }
    for idx, cell in enumerate(nb["cells"]):
        if "W@x ≈ np.fft.fft(x)" in text_of(cell) or "W @ x ≈ np.fft.fft" in text_of(cell):
            nb["cells"].insert(idx + 1, bridge)
            return
    for idx, cell in enumerate(nb["cells"]):
        if "## 1. DFT 是一个矩阵 W" in text_of(cell):
            nb["cells"].insert(idx, bridge)
            return


def patch_l22(nb: dict) -> None:
    for cell in nb["cells"]:
        if "現在可以用" in text_of(cell):
            set_text(cell, text_of(cell).replace("現在可以用", "现在可以用"))


def patch_l26(nb: dict) -> None:
    nb["cells"] = [
        c
        for c in nb["cells"]
        if not (c.get("cell_type") == "markdown" and text_of(c).strip() == "")
    ]
    if any("l26_review" in text_of(c) for c in nb["cells"]):
        return
    review = {
        "cell_type": "code",
        "id": "l26_review",
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": L26_REVIEW.splitlines(keepends=True),
    }
    bridge = {
        "cell_type": "markdown",
        "id": "l26-closing-bridge",
        "metadata": {},
        "source": [
            "---\n",
            "⬇️ **通关检验**：收束小结已读；请运行下方数学性质验证格，再勾选自评。\n",
        ],
    }
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("id") == "nav-l26-clos":
            if not any(c.get("id") == "l26-closing-bridge" for c in nb["cells"]):
                nb["cells"].insert(idx, bridge)
            nb["cells"].insert(idx, review)
            return


def patch_l27(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if "# ✏️ 对答案格" not in src:
            continue
        set_text(
            cell,
            src.replace(
                'except NotImplementedError:\n    print(f"     (estimate_prob_six 待实现)")',
                'except NotImplementedError:\n    print("     ⬜ 请先实现 estimate_prob_six()，再运行对答案格")',
            ),
        )


def patch_l30_closing(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if not src.startswith("## 本课收束"):
            continue
        if "L31" in src and "心理切换" in src:
            return
        set_text(
            cell,
            src.rstrip()
            + "\n\n"
            + "**下一课 L31** 会把 softmax、交叉熵与 Shannon 熵画成图；"
            + "读完后进入 Audio DSP（L32）前，建议先完成 L31 末尾的模块切换清单。\n",
        )


def patch_notebook(lesson: int, nb: dict) -> None:
    if lesson == 21:
        patch_l21(nb)
    if lesson == 22:
        patch_l22(nb)
    if lesson == 26:
        patch_l26(nb)
    if lesson == 27:
        patch_l27(nb)
    if lesson == 30:
        patch_l30_closing(nb)
    if lesson in range(21, 31) and lesson != 26:
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
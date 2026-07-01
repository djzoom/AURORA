#!/usr/bin/env python3
"""Additive polish for L11–L20 linear algebra notebooks."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS = {
    f"L{n}": ROOT / "notebooks/2_linear_algebra" / path
    for n, path in [
        (11, "L11_norms.ipynb"),
        (12, "L12_matrices.ipynb"),
        (13, "L13_special_matrices.ipynb"),
        (14, "L14_eigen_svd.ipynb"),
        (15, "L15_linear_systems.ipynb"),
        (16, "L16_determinant_inverse.ipynb"),
        (17, "L17_eigen_diagonalization.ipynb"),
        (18, "L18_invertibility.ipynb"),
        (19, "L19_visual_multiply.ipynb"),
        (20, "L20_visual_factorizations.ipynb"),
    ]
}

L13_CLOSING = """## 本课收束

现在可以用 `is_orthogonal(Q)` 检验任意方阵，并用 `Q.T` 直接代替 `np.linalg.inv(Q)` 求逆。
Aurora 的 `aurora.audio.transforms.dft()` 在内部使用酉矩阵乘法（旋转因子与信号做内积）；
L39 验证 `ifft(fft(x)) == x` 时直接依赖这条性质。
注：`dft_matrix(n)` 作为独立函数尚未导出——矩阵形式在 **L21** 内联完成。
下一节进入特征值分解，正交矩阵将作为特征向量矩阵再次出现。
"""

L19_REVIEW = """# ✏️ 本课自评
l19_review = {
    "matvec_picture_understood": None,  # 能解释 A@x 的列线性组合图？True/False
    "matmul_rank1_intuition":    None,  # 理解 A@B 的秩1叠加视角？True/False
    "classify_transform_done":   None,  # classify_transform 实现并通过断言？True/False
    "transform_det_sign":        None,  # 知道旋转 det=+1、反射 det=-1？True/False
}

unfilled = [k for k, v in l19_review.items() if v is None]
assert not unfilled, f'还未填写：{unfilled}'
weak = [k for k, v in l19_review.items() if v is False]
if weak:
    print(f'⚠️  需要加强：{weak}')
else:
    print('✅ L19 全部通关！进入 L20：矩阵分解图解')
"""

L20_REVIEW = """# ✏️ 本课自评
l20_review = {
    "svd_parts_understood":   None,  # 能说出 U、Σ、Vᵀ 各自含义？True/False
    "rank_from_svd_done":     None,  # rank_from_svd 实现并通过断言？True/False
    "low_rank_intuition":     None,  # 理解截断奇异值 = 低秩近似？True/False
    "l21_bridge_read":        None,  # 读过收束中 L21 矩阵滤波预告？True/False
}

unfilled = [k for k, v in l20_review.items() if v is None]
assert not unfilled, f'还未填写：{unfilled}'
weak = [k for k, v in l20_review.items() if v is False]
if weak:
    print(f'⚠️  需要加强：{weak}')
else:
    print('✅ L20 全部通关！进入 L21：矩阵即滤波')
"""


def load_nb(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_nb(nb: dict) -> str:
    return json.dumps(nb, ensure_ascii=False, indent=1) + "\n"


def text_of(cell: dict) -> str:
    return "".join(cell.get("source", []))


def set_text(cell: dict, text: str) -> None:
    cell["source"] = text.splitlines(keepends=True)


def is_corrupted_closing(cell: dict) -> bool:
    src = cell.get("source", [])
    if not isinstance(src, list) or len(src) < 8:
        return False
    joined = "".join(src)
    return joined.replace("\n", "").startswith("##本课收束") or (
        src[0] == "#" and src[1] == "#" and "本" in joined and "课" in joined
    )


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


def insert_review_before_nav(nb: dict, review_id: str, review_code: str, nav_id: str) -> None:
    if any(review_id in text_of(c) for c in nb["cells"]):
        return
    review = {
        "cell_type": "code",
        "id": review_id,
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": review_code.splitlines(keepends=True),
    }
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("id") == nav_id:
            nb["cells"].insert(idx, review)
            return


def patch_l13(nb: dict) -> None:
    for cell in nb["cells"]:
        if is_corrupted_closing(cell):
            set_text(cell, L13_CLOSING)


def patch_answer_leaks(nb: dict) -> None:
    replacements = [
        (
            "except NotImplementedError:\n    nv = v / np.linalg.norm(v)\n    print(f\"Q2 ✅  [3,4]/5 = {np.round(nv,4)}  (normalize 待实现)\")",
            'except NotImplementedError:\n    print("⬜ Q2：请先实现 normalize()，再运行对答案格")',
        ),
        (
            'except NotImplementedError:\n    print(f"Q1 ✅  手算: 1×5+2×6=17, 3×5+4×6=39 → {y1_ref} (matvec 待实现)")',
            'except NotImplementedError:\n    print("⬜ Q1：请先实现 matvec()，再运行对答案格")',
        ),
        (
            "except NotImplementedError:\n    col_norms = [np.linalg.norm(D[:, j]) for j in range(D.shape[1])]\n    print(f\"Q3 ✅  diag(3,5) 列模={col_norms}，均≠1，不是正交矩阵（is_orthogonal 待实现）\")",
            'except NotImplementedError:\n    print("⬜ Q3：请先实现 is_orthogonal()，再运行对答案格")',
        ),
        (
            'except NotImplementedError:\n    print(f"\\nQ2 ✅  输出 shape = 输入 shape (3,5)，不是 (3,2)（low_rank_approx 待实现）")',
            'except NotImplementedError:\n    print("\\n⬜ Q2：请先实现 low_rank_approx()，再运行对答案格")',
        ),
        (
            "except NotImplementedError:\n    d1 = 3*4 - 1*2\n    print(f\"Q1 ✅  det = 3×4-1×2 = {d1}  (det_2x2 待实现)\")",
            'except NotImplementedError:\n    print("⬜ Q1：请先实现 det_2x2()，再运行对答案格")',
        ),
        (
            "except NotImplementedError:\n    inv_theory = (1/det_B) * np.array([[3., -3.], [-6., 4.]])\n    print(f\"Q2 ✅  det(B)={det_B}, B⁻¹ = (1/{det_B})·[[3,-3],[-6,4]]=\\n{inv_theory}\")\n    print(f\"       numpy 验证: {np.round(B_inv_ref, 4)}\")",
            'except NotImplementedError:\n    print("⬜ Q2：请先实现 inv_2x2()，再运行对答案格")',
        ),
        (
            "except NotImplementedError:\n    cp_manual = np.linalg.det(A - lam1 * np.eye(2))\n    print(f\"Q2 ✅  det(A-5I) = {cp_manual:.2e} ≈ 0  (char_poly 待实现)\")",
            'except NotImplementedError:\n    print("⬜ Q2：请先实现 char_poly()，再运行对答案格")',
        ),
        (
            "except NotImplementedError:\n    # 手动验证\n    rows_ok = [abs(B[i,i]) > sum(abs(B[i,j]) for j in range(2) if j!=i) for i in range(2)]\n    assert all(rows_ok)\n    print(f\"Q2 ✅  [[3,1],[1,2]] 是 SDD：行检查={rows_ok}  (is_sdd 待实现)\")",
            'except NotImplementedError:\n    print("⬜ Q2：请先实现 is_sdd()，再运行对答案格")',
        ),
    ]
    for cell in nb["cells"]:
        if "# ✏️ 对答案格" not in text_of(cell):
            continue
        src = text_of(cell)
        for old, new in replacements:
            src = src.replace(old, new)
        set_text(cell, src)


def patch_l18_whiteboard(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if "## ✏️ 白板挑战：可逆性手算" not in src:
            continue
        set_text(
            cell,
            src.replace(
                "**问 1**：A = [[2, 1], [1, 3]]，手算 det(A) = 2×3 - 1×1 = ?，A 可逆吗？",
                "**问 1**：A = [[2, 1], [1, 3]]，手算 det(A)（公式 ad−bc），A 可逆吗？",
            ),
        )


def patch_l20_closing(nb: dict) -> None:
    for cell in nb["cells"]:
        src = text_of(cell)
        if not src.startswith("## 本课收束"):
            continue
        if "rank_from_svd" in src:
            return
        set_text(
            cell,
            "## 本课收束\n\n"
            "现在可以用 `np.linalg.svd(A)` 拿到 U、Σ、Vᵀ，用奇异值序列判断矩阵的有效秩和各方向的信息量。"
            "本课 `rank_from_svd` 把「数大于门限的奇异值个数」这条判据手写了一遍——"
            "与 L18 的秩判据、L15 的 `classify_system` 同属「矩阵能表达多少独立信息」。\n\n"
            "这套分解直接对应 Aurora mel 频谱矩阵的低秩近似：保留前 k 个奇异值即可重建主要频谱结构。"
            "下一节 **L21** 把矩阵视角对准音频核心：DFT 矩阵 / Mel 矩阵 = 滤波器组乘法。\n",
        )


def patch_notebook(name: str, nb: dict) -> None:
    lesson = int(name[1:])
    if lesson == 13:
        patch_l13(nb)
    if lesson == 18:
        patch_l18_whiteboard(nb)
    if lesson == 20:
        patch_l20_closing(nb)
    if 11 <= lesson <= 18:
        add_whiteboard_bridge(nb)
    patch_answer_leaks(nb)
    if lesson == 19:
        insert_review_before_nav(nb, "l19_review", L19_REVIEW, "nav-l19-clos")
    if lesson == 20:
        insert_review_before_nav(nb, "l20_review", L20_REVIEW, "nav-l20-clos")


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
    for name, path in NOTEBOOKS.items():
        nb = load_nb(path)
        before = len(nb["cells"])
        patch_notebook(name, nb)
        text = dump_nb(nb)
        validate_nb(path.name, text)
        summary[str(path)] = {"cells_before": before, "cells_after": len(nb["cells"])}
        if args.apply:
            path.write_text(text, encoding="utf-8")

    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "files": summary}, indent=2))


if __name__ == "__main__":
    main()
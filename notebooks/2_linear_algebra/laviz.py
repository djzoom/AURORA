"""laviz — "Art of Linear Algebra" 风格的可视化工具包.

灵感来自 Kenji Hiranabe《The Art of Linear Algebra》(基于 Strang
《Linear Algebra for Everyone》)。用统一的配色与版式，把矩阵/向量运算
画成图形：矩阵的多种看法、点积 vs 外积、矩阵×向量 = 列的线性组合、
矩阵×矩阵 = 秩1之和、以及各种分解。

在 notebook 里：
    from laviz import *
    style()
    matrix_4ways(np.array([[1,2],[3,4],[5,6]]))
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ───────────────────────── 设计系统 ─────────────────────────
PALETTE = ["#2A9D8F", "#E76F51", "#E9C46A", "#577590", "#8AB17D", "#BC6C8E"]
INK = "#22333B"      # 文字/线条
PAPER = "#FBF8F3"    # 背景纸色
CELL_BG = "#E7E1D7"  # 中性单元格
GOLD = "#E9C46A"     # 结果高亮


def _pick_cjk_font():
    """从常见 CJK 字体里挑一个系统已装的，保证中文不出现豆腐块。"""
    from matplotlib import font_manager as fm
    available = {f.name for f in fm.fontManager.ttflist}
    for name in ("Noto Sans CJK SC", "Source Han Sans SC", "Microsoft YaHei",
                 "PingFang SC", "SimHei", "WenQuanYi Zen Hei", "Heiti SC",
                 "Droid Sans Fallback"):
        if name in available:
            return name
    return None


def style():
    """统一画布观感，notebook 开头调用一次。"""
    cjk = _pick_cjk_font()
    families = ([cjk] if cjk else []) + ["DejaVu Sans"]
    plt.rcParams.update({
        "figure.facecolor": PAPER,
        "axes.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "font.size": 11,
        "font.family": "sans-serif",
        "font.sans-serif": families,
        "axes.unicode_minus": False,
    })


def _fmt(v):
    v = float(v)
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)) + 0)  # 去掉 -0
    return f"{v:.2f}"


def _colors_for(M, mode):
    m, n = M.shape
    grid = [[CELL_BG] * n for _ in range(m)]
    if mode == "columns":
        for j in range(n):
            for i in range(m):
                grid[i][j] = PALETTE[j % len(PALETTE)]
    elif mode == "rows":
        for i in range(m):
            for j in range(n):
                grid[i][j] = PALETTE[i % len(PALETTE)]
    elif isinstance(mode, str) and mode.startswith("#"):
        grid = [[mode] * n for _ in range(m)]
    return grid


def draw_grid(ax, M, x_left=0.0, y_center=0.0, cell=1.0, mode="plain",
              colors=None, alpha=0.85, label=None, label_color=None, fontsize=12):
    """在 ax 上画一个矩阵(带方括号)，竖直居中于 y_center，返回占用宽度。"""
    M = np.atleast_2d(np.asarray(M, float))
    m, n = M.shape
    if colors is None:
        colors = _colors_for(M, mode)
    top = y_center + m * cell / 2.0
    for i in range(m):
        for j in range(n):
            x = x_left + j * cell
            y = top - (i + 1) * cell
            ax.add_patch(Rectangle((x, y), cell, cell, facecolor=colors[i][j],
                                   edgecolor="white", lw=2.2, alpha=alpha, zorder=2))
            ax.text(x + cell / 2, y + cell / 2, _fmt(M[i, j]), ha="center",
                    va="center", color=INK, fontsize=fontsize, fontweight="bold",
                    family="monospace", zorder=3)
    h = m * cell
    serif = 0.16 * cell
    for bx, d in [(x_left - 0.10 * cell, serif), (x_left + n * cell + 0.10 * cell, -serif)]:
        ax.plot([bx, bx], [top, top - h], color=INK, lw=2.5, zorder=4)
        ax.plot([bx, bx + d], [top, top], color=INK, lw=2.5, zorder=4)
        ax.plot([bx, bx + d], [top - h, top - h], color=INK, lw=2.5, zorder=4)
    if label:
        ax.text(x_left + n * cell / 2, top + 0.30 * cell, label, ha="center",
                va="bottom", color=label_color or INK, fontsize=13, fontweight="bold")
    return n * cell


def _row(ax, items, cell=0.7, gap=0.55, y=0.0):
    """左到右排版一行 token；token: {'type':'mat'|'sym', ...}。返回(总宽, 最大半高)。"""
    xs, x, maxhalf = [], 0.0, cell
    for it in items:
        if it["type"] == "mat":
            M = np.atleast_2d(np.asarray(it["M"], float))
            w = M.shape[1] * cell
            pad = 0.28 * cell
            xs.append(x + pad)
            x += w + 2 * pad + gap
            maxhalf = max(maxhalf, M.shape[0] * cell / 2 + 0.5 * cell)
        else:
            w = it.get("w", 0.7)
            xs.append(x)
            x += w + gap
    for it, xleft in zip(items, xs):
        if it["type"] == "mat":
            draw_grid(ax, it["M"], x_left=xleft, y_center=y, cell=cell,
                      mode=it.get("mode", "plain"), colors=it.get("colors"),
                      label=it.get("label"), label_color=it.get("label_color"),
                      alpha=it.get("alpha", 0.85))
        else:
            ax.text(xleft + it.get("w", 0.7) / 2, y, it["s"], ha="center",
                    va="center", fontsize=it.get("size", 22), fontweight="bold",
                    color=it.get("color", INK))
    return x - gap, maxhalf


def _finish(ax, width, half, title=None):
    ax.set_xlim(-0.6, width + 0.6)
    ax.set_ylim(-half - 0.4, half + 0.9)
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=13, color=INK, fontweight="bold", pad=8)


# ───────────────────────── 高层图示 ─────────────────────────
def matrix_4ways(A, title="一个矩阵的 4 种看法"):
    """整体 / 数字 / 列 / 行。"""
    A = np.atleast_2d(np.asarray(A, float))
    style()
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.4))
    views = [("1 个矩阵", "#9AA4A8"), ("mn 个数字", "plain"),
             ("n 个列", "columns"), ("m 个行", "rows")]
    for ax, (name, mode) in zip(axes, views):
        w = draw_grid(ax, A, mode=mode if mode != "plain" else "plain",
                      colors=_colors_for(A, mode) if mode in ("columns", "rows")
                      else ([[mode] * A.shape[1] for _ in range(A.shape[0])]
                            if mode.startswith("#") else None))
        _finish(ax, w, A.shape[0] * 0.5 + 0.6, title=name)
    fig.suptitle(title, fontsize=15, fontweight="bold", color=INK, y=1.02)
    fig.tight_layout()
    return fig


def vec_times_vec(u, v, title="向量 × 向量 — 2 种"):
    """(v1) 内积→标量    (v2) 外积→秩1矩阵。"""
    u = np.asarray(u, float).ravel()
    v = np.asarray(v, float).ravel()
    style()
    fig, axes = plt.subplots(2, 1, figsize=(8.5, 5.2))
    # v1 内积
    items = [
        {"type": "mat", "M": u[None, :], "mode": "rows", "label": "u (行)"},
        {"type": "sym", "s": "·"},
        {"type": "mat", "M": v[:, None], "mode": "columns", "label": "v (列)"},
        {"type": "sym", "s": "="},
        {"type": "mat", "M": [[float(u @ v)]], "mode": GOLD, "label": "标量"},
    ]
    w, h = _row(axes[0], items)
    _finish(axes[0], w, h, title="(v1) 内积 = 标量")
    # v2 外积
    items = [
        {"type": "mat", "M": u[:, None], "mode": "columns", "label": "u (列)"},
        {"type": "sym", "s": "·"},
        {"type": "mat", "M": v[None, :], "mode": "rows", "label": "v (行)"},
        {"type": "sym", "s": "="},
        {"type": "mat", "M": np.outer(u, v), "mode": "#E9C46A", "label": "秩1 矩阵"},
    ]
    w, h = _row(axes[1], items)
    _finish(axes[1], w, h, title="(v2) 外积 = 秩 1 矩阵 ← 后续分解的关键")
    fig.suptitle(title, fontsize=15, fontweight="bold", color=INK, y=1.0)
    fig.tight_layout()
    return fig


def mat_times_vec(A, x, title="矩阵 × 向量 — 2 种"):
    """(Mv1) 行·向量=点积    (Mv2) 列的线性组合。"""
    A = np.atleast_2d(np.asarray(A, float))
    x = np.asarray(x, float).ravel()
    res = A @ x
    style()
    fig, axes = plt.subplots(2, 1, figsize=(9, 5.6))
    # Mv1
    items = [
        {"type": "mat", "M": A, "mode": "rows", "label": "A (按行)"},
        {"type": "sym", "s": "·"},
        {"type": "mat", "M": x[:, None]},
        {"type": "sym", "s": "="},
        {"type": "mat", "M": res[:, None], "mode": GOLD},
    ]
    w, h = _row(axes[0], items)
    _finish(axes[0], w, h, title="(Mv1) 每行 · 向量 = 一组点积")
    # Mv2 线性组合
    items = []
    n = A.shape[1]
    for j in range(n):
        items.append({"type": "sym", "s": f"{_fmt(x[j])}·", "size": 16, "w": 0.9})
        items.append({"type": "mat", "M": A[:, [j]],
                      "colors": [[PALETTE[j % len(PALETTE)]] for _ in range(A.shape[0])]})
        items.append({"type": "sym", "s": "+" if j < n - 1 else "="})
    items.append({"type": "mat", "M": res[:, None], "mode": GOLD})
    w, h = _row(axes[1], items)
    _finish(axes[1], w, h, title="(Mv2) 列向量的线性组合  ← Ax 的灵魂")
    fig.suptitle(title, fontsize=15, fontweight="bold", color=INK, y=1.0)
    fig.tight_layout()
    return fig


def mat_times_mat_rank1(A, B, title="矩阵 × 矩阵 = 秩 1 矩阵之和"):
    """AB = Σ_k  col_k(A) × row_k(B)。"""
    A = np.atleast_2d(np.asarray(A, float))
    B = np.atleast_2d(np.asarray(B, float))
    style()
    fig, ax = plt.subplots(figsize=(10, 3.4))
    items = []
    k = A.shape[1]
    for c in range(k):
        term = np.outer(A[:, c], B[c, :])
        col = PALETTE[c % len(PALETTE)]
        items.append({"type": "mat", "M": term,
                      "colors": [[col] * term.shape[1] for _ in range(term.shape[0])]})
        items.append({"type": "sym", "s": "+" if c < k - 1 else "="})
    items.append({"type": "mat", "M": A @ B, "mode": GOLD})
    w, h = _row(ax, items, cell=0.62)
    _finish(ax, w, h, title=title)
    fig.tight_layout()
    return fig


def show_factorization(A, mats, names, modes=None, title="矩阵分解"):
    """画 A = M1 · M2 · ... ，每个因子带名字与配色。"""
    style()
    modes = modes or ["#9AA4A8"] * len(mats)
    fig, ax = plt.subplots(figsize=(2.0 * (len(mats) + 1) + 3, 3.4))
    items = [{"type": "mat", "M": A, "mode": "#9AA4A8", "label": "A"},
             {"type": "sym", "s": "="}]
    for i, (M, nm, md) in enumerate(zip(mats, names, modes)):
        items.append({"type": "mat", "M": M, "mode": md, "label": nm})
    w, h = _row(ax, items, cell=0.62)
    _finish(ax, w, h, title=title)
    fig.tight_layout()
    return fig


def arrows2d(vectors, labels=None, title=None, figsize=(5, 5)):
    """把若干 2D 向量画成从原点出发的箭头(配色统一)。"""
    style()
    vs = [np.asarray(v, float).ravel() for v in vectors]
    fig, ax = plt.subplots(figsize=figsize)
    for i, v in enumerate(vs):
        c = PALETTE[i % len(PALETTE)]
        ax.annotate("", xy=(v[0], v[1]), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=c, lw=2.8))
        if labels:
            ax.text(v[0] * 1.06, v[1] * 1.06, labels[i], color=c,
                    fontweight="bold", fontsize=11)
    m = max(2.0, np.abs(np.array(vs)).max() * 1.35)
    ax.set_xlim(-m, m); ax.set_ylim(-m, m); ax.set_aspect("equal")
    ax.axhline(0, color="#ccc", lw=.8); ax.axvline(0, color="#ccc", lw=.8)
    ax.grid(alpha=.3)
    if title:
        ax.set_title(title, fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def heatmap(M, title=None, cmap="viridis", figsize=(6, 4), colorbar=True):
    """大矩阵用热力图(如 DFT 矩阵、mel 滤波器组)。"""
    style()
    M = np.atleast_2d(np.asarray(M, float))
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(M, cmap=cmap, aspect="auto")
    if colorbar:
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold", color=INK)
    fig.tight_layout()
    return fig

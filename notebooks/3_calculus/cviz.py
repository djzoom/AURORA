"""cviz — 微积分的图形化工具(matplotlib)。

导数=切线斜率、一维梯度下降轨迹、二维等高线+梯度箭头+下山路径、学习率对比。
用法：from cviz import *; style()
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt

from aurora._plot_theme import DARK_THEME, apply_theme

PALETTE = ["#2A9D8F", "#E76F51", "#E9C46A", "#577590", "#8AB17D", "#BC6C8E"]
_THEME = DARK_THEME
INK, AXIS, GRID, SURFACE, SHADOW, PAPER = (
    _THEME.ink,
    _THEME.axis,
    _THEME.grid,
    _THEME.surface,
    _THEME.shadow,
    _THEME.paper,
)


def _cjk():
    from matplotlib import font_manager as fm
    have = {f.name for f in fm.fontManager.ttflist}
    for n in ("PingFang SC", "Arial Unicode MS", "Source Han Sans CN", "Source Han Sans CN Normal",
              "Noto Sans CJK SC", "Source Han Sans SC", "Microsoft YaHei",
              "PingFang SC", "SimHei", "WenQuanYi Zen Hei", "Droid Sans Fallback"):
        if n in have:
            return n
    return None


def _sync_theme(theme):
    global INK, AXIS, GRID, SURFACE, SHADOW, PAPER
    INK = theme.ink
    AXIS = theme.axis
    GRID = theme.grid
    SURFACE = theme.surface
    SHADOW = theme.shadow
    PAPER = theme.paper


def style(theme: str | None = None):
    theme_spec = apply_theme(theme, cjk_font=_cjk(), figure_size=(6, 4), font_size=11)
    _sync_theme(theme_spec)
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
    })


def tangent(f, df, x0=1.5, span=(-1, 3)):
    """曲线 + 在 x0 处的切线，切线斜率 = 导数。"""
    style()
    xs = np.linspace(*span, 300)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xs, f(xs), color=PALETTE[0], lw=2.5, label="f(x)")
    slope = df(x0)
    ax.plot(xs, f(x0) + slope * (xs - x0), color=PALETTE[1], lw=2, ls="--",
            label=f"切线 (斜率=f'({x0})={slope:.2f})")
    ax.plot([x0], [f(x0)], "o", color=PALETTE[1], ms=9)
    ax.legend(fontsize=9); ax.grid(alpha=.3); ax.axhline(0, color=AXIS, lw=.6)
    ax.set_title("导数 = 切线的斜率 = 变化率", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def descent_1d(f, grad, x0=-2.5, lr=0.1, steps=12):
    """一维梯度下降：小球一步步滚向最低点。"""
    style()
    xs = np.linspace(-3, 3, 300)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xs, f(xs), color=PALETTE[0], lw=2.5)
    x = x0; path = [x]
    for _ in range(steps):
        x = x - lr * grad(x); path.append(x)
    path = np.array(path)
    ax.plot(path, f(path), "o-", color=PALETTE[1], ms=6, lw=1.2, alpha=.8)
    ax.plot([path[0]], [f(path[0])], "o", color=PALETTE[3], ms=11, label="起点")
    ax.plot([path[-1]], [f(path[-1])], "*", color=PALETTE[2], ms=18, label="终点")
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    ax.set_title(f"梯度下降：沿斜坡下山 (lr={lr})", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def contour_descent(start=(-2.3, 2.0), lr=0.15, steps=18):
    """二维：等高线 + 梯度方向 + 下山路径，f(x,y)=x²+2y²。"""
    style()
    f = lambda x, y: x**2 + 2 * y**2
    gx, gy = (lambda x, y: 2 * x), (lambda x, y: 4 * y)
    X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.contour(X, Y, f(X, Y), levels=15, cmap="viridis", alpha=.7)
    x, y = start; path = [(x, y)]
    for _ in range(steps):
        x, y = x - lr * gx(x, y), y - lr * gy(x, y); path.append((x, y))
    p = np.array(path)
    ax.plot(p[:, 0], p[:, 1], "o-", color=PALETTE[1], ms=5, lw=1.4)
    ax.plot([p[0, 0]], [p[0, 1]], "o", color=PALETTE[3], ms=11, label="起点")
    ax.plot([0], [0], "*", color=PALETTE[2], ms=20, label="最低点")
    ax.legend(fontsize=9); ax.set_aspect("equal")
    ax.set_title("二维梯度下降：垂直等高线下山", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def lr_compare(x0=-2.6, lrs=(0.05, 0.3, 0.95), steps=12):
    """学习率太小(慢)/适中/太大(震荡发散)。"""
    style()
    f = lambda x: (x) ** 2
    grad = lambda x: 2 * x
    xs = np.linspace(-3, 3, 300)
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.4))
    titles = ["太小 → 慢", "适中 → 稳", "太大 → 震荡"]
    for a, lr, tt in zip(ax, lrs, titles):
        a.plot(xs, f(xs), color=PALETTE[0], lw=2)
        x = x0; path = [x]
        for _ in range(steps):
            x = x - lr * grad(x); path.append(x)
        path = np.array(path)
        a.plot(path, f(path), "o-", color=PALETTE[1], ms=5, lw=1, alpha=.8)
        a.set_title(f"lr={lr}  ({tt})", fontsize=11); a.grid(alpha=.3)
    fig.suptitle("学习率的影响", fontweight="bold", fontsize=14)
    fig.tight_layout(); return fig

"""xviz — 复数与三角的图形化工具(matplotlib)。

统一配色 + 中文字体，画：单位圆与欧拉公式、正弦三要素、复数极坐标、
单位根(DFT 旋转因子)、正弦叠加成方波(傅里叶)。
用法：from xviz import *; style()
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
    theme_spec = apply_theme(theme, cjk_font=_cjk(), figure_size=(6, 6), font_size=11)
    _sync_theme(theme_spec)
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.2,
    })


def unit_circle_euler(theta=np.pi / 3):
    """单位圆上的 e^{iθ}=cosθ+i·sinθ，展示 cos/sin 投影。"""
    style()
    fig, ax = plt.subplots(figsize=(5, 5))
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(t), np.sin(t), color=INK, lw=1.5)
    c, s = np.cos(theta), np.sin(theta)
    ax.plot([0, c], [0, s], color=PALETTE[0], lw=3, zorder=3)        # 半径
    ax.plot([c, c], [0, s], color=PALETTE[1], lw=2.5, ls="--")       # sin
    ax.plot([0, c], [0, 0], color=PALETTE[3], lw=2.5, ls="--")       # cos
    ax.plot([c], [s], "o", color=PALETTE[0], ms=10, zorder=4)
    ax.annotate(r"$e^{i\theta}$", (c, s), (c + .08, s + .08), fontsize=15, color=PALETTE[0])
    ax.text(c / 2, -.12, "cosθ", color=PALETTE[3], ha="center", fontweight="bold")
    ax.text(c + .04, s / 2, "sinθ", color=PALETTE[1], va="center", fontweight="bold")
    ax.set_aspect("equal"); ax.axhline(0, color=AXIS, lw=.8); ax.axvline(0, color=AXIS, lw=.8)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
    ax.set_title("欧拉公式：e^{iθ} 是单位圆上的旋转", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def sinusoid_anatomy():
    """振幅 A / 频率 f / 相位 φ 各控制什么。"""
    style()
    t = np.linspace(0, 1, 500)
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.2))
    for A in (1, 2):
        ax[0].plot(t, A * np.sin(2 * np.pi * 2 * t), label=f"A={A}")
    ax[0].set_title("振幅 A = 多响")
    for f in (2, 4):
        ax[1].plot(t, np.sin(2 * np.pi * f * t), label=f"f={f}Hz")
    ax[1].set_title("频率 f = 多高")
    for p in (0, np.pi / 2):
        ax[2].plot(t, np.sin(2 * np.pi * 2 * t + p), label=f"φ={p:.1f}")
    ax[2].set_title("相位 φ = 起点偏移")
    for a in ax:
        a.legend(fontsize=9); a.grid(alpha=.3); a.axhline(0, color=AXIS, lw=.6)
    fig.suptitle("一个正弦波 = A·sin(2π·f·t + φ)", fontweight="bold", fontsize=14)
    fig.tight_layout(); return fig


def complex_point(z=3 + 4j):
    """复数的极坐标：模 |z| 与相位 ∠z。"""
    style()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot([0, z.real], [0, z.imag], color=PALETTE[0], lw=3)
    ax.plot([z.real], [z.imag], "o", color=PALETTE[0], ms=10)
    ang = np.linspace(0, np.angle(z), 50); r = 0.8
    ax.plot(r * np.cos(ang), r * np.sin(ang), color=PALETTE[1], lw=2)
    ax.annotate(f"z = {z.real:.0f}+{z.imag:.0f}i", (z.real, z.imag),
                (z.real * .4, z.imag + .6), fontsize=12, color=PALETTE[0])
    ax.text(z.real / 2 - .3, z.imag / 2 + .3, f"|z|={abs(z):.0f}",
            color=PALETTE[0], fontweight="bold")
    ax.text(1.0, .35, f"∠z={np.angle(z):.2f}", color=PALETTE[1], fontweight="bold")
    ax.axhline(0, color=AXIS, lw=.8); ax.axvline(0, color=AXIS, lw=.8)
    ax.set_aspect("equal"); ax.set_xlim(-1, 5); ax.set_ylim(-1, 6)
    ax.set_xlabel("实部 Re"); ax.set_ylabel("虚部 Im")
    ax.set_title("复数 = 平面上的点（模 + 相位）", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def roots_of_unity(N=8):
    """N 个单位根 = DFT 的旋转因子 e^{-2πik/N}。"""
    style()
    fig, ax = plt.subplots(figsize=(5, 5))
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(t), np.sin(t), color=INK, lw=1.2)
    k = np.arange(N); w = np.exp(-2j * np.pi * k / N)
    ax.scatter(w.real, w.imag, color=PALETTE[0], s=90, zorder=3)
    for i in range(N):
        ax.plot([0, w[i].real], [0, w[i].imag], color=PALETTE[0], lw=.8, alpha=.5)
        ax.annotate(f"k={i}", (w[i].real, w[i].imag),
                    (w[i].real * 1.12, w[i].imag * 1.12), fontsize=8, ha="center")
    ax.set_aspect("equal"); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
    ax.axhline(0, color=AXIS, lw=.6); ax.axvline(0, color=AXIS, lw=.6)
    ax.set_title(f"{N} 个单位根 = DFT 的旋转因子", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def fourier_square(terms=(1, 3, 9, 50)):
    """用奇次谐波叠加逼近方波(傅里叶级数直觉)。"""
    style()
    t = np.linspace(0, 1, 1000)
    fig, ax = plt.subplots(figsize=(9, 3.6))
    for n in terms:
        y = sum(np.sin(2 * np.pi * k * t) / k for k in range(1, 2 * n, 2))
        ax.plot(t, y, label=f"{n} 个谐波", alpha=.85)
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    ax.set_title("正弦叠加 → 方波（谐波越多越方）", fontweight="bold", color=INK)
    fig.tight_layout(); return fig

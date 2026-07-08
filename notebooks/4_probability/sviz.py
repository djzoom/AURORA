"""sviz — 概率统计的图形化工具(matplotlib)。

大数定律、均匀vs正态、高斯钟形+标准差带、z-score前后、softmax 柱状、交叉熵曲线。
用法：from sviz import *; style()
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


def law_of_large_numbers(n=2000, seed=0):
    """抛硬币的累计频率，逐渐收敛到 0.5。"""
    style()
    rng = np.random.default_rng(seed)
    flips = rng.integers(0, 2, n)
    running = np.cumsum(flips) / np.arange(1, n + 1)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(running, color=PALETTE[0], lw=1.5)
    ax.axhline(0.5, color=PALETTE[1], ls="--", lw=2, label="真实概率 0.5")
    ax.legend(fontsize=9); ax.grid(alpha=.3); ax.set_xlabel("抛掷次数")
    ax.set_title("大数定律：样本越多，频率越接近概率", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def dist_compare(n=5000, seed=0):
    """均匀分布 vs 正态分布。"""
    style()
    rng = np.random.default_rng(seed)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.4))
    ax[0].hist(rng.uniform(-3, 3, n), bins=40, color=PALETTE[3])
    ax[0].set_title("均匀分布（处处等可能）")
    ax[1].hist(rng.normal(0, 1, n), bins=40, color=PALETTE[0])
    ax[1].set_title("正态分布（中间多，两边少）")
    fig.tight_layout(); return fig


def gaussian(mu=0.0, sigma=1.0):
    """高斯钟形曲线 + ±1σ/±2σ 区间。"""
    style()
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
    pdf = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(x, pdf, color=PALETTE[0], lw=2.5)
    for k, c in [(1, PALETTE[2]), (2, PALETTE[1])]:
        ax.fill_between(x, pdf, where=np.abs(x - mu) <= k * sigma, alpha=.18, color=c)
    ax.axvline(mu, color=PALETTE[3], ls="--", label=f"μ={mu}")
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    ax.set_title(f"正态分布 N(μ={mu}, σ={sigma})", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def zscore_demo(seed=0):
    """标准化前后：均值移到 0、标准差缩到 1。"""
    style()
    rng = np.random.default_rng(seed)
    raw = rng.normal(50, 15, 2000)
    z = (raw - raw.mean()) / raw.std()
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.4))
    ax[0].hist(raw, bins=40, color=PALETTE[1]); ax[0].set_title("原始 (μ≈50, σ≈15)")
    ax[1].hist(z, bins=40, color=PALETTE[0]); ax[1].set_title("标准化后 (μ=0, σ=1)")
    fig.tight_layout(); return fig


def softmax_bars(scores=(2.0, 1.0, 0.1)):
    """分数 → softmax 概率(和为1)。"""
    style()
    z = np.array(scores, float)
    e = np.exp(z - z.max()); p = e / e.sum()
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
    idx = [f"类{i}" for i in range(len(z))]
    ax[0].bar(idx, z, color=PALETTE[3]); ax[0].set_title("原始分数 (logits)")
    ax[1].bar(idx, p, color=PALETTE[0]); ax[1].set_title("softmax 概率 (和=1)")
    for i, v in enumerate(p):
        ax[1].text(i, v + .01, f"{v:.2f}", ha="center", fontweight="bold")
    fig.tight_layout(); return fig


def cross_entropy_curve():
    """交叉熵：预测正确类的概率越高，损失越小。"""
    style()
    p = np.linspace(0.01, 1.0, 200)
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(p, -np.log(p), color=PALETTE[1], lw=2.5)
    ax.set_xlabel("预测正确类别的概率"); ax.set_ylabel("交叉熵损失 −log(p)")
    ax.grid(alpha=.3)
    ax.set_title("越自信且正确 → 损失越小", fontweight="bold", color=INK)
    fig.tight_layout(); return fig

"""aviz — Audio Core 的图形化工具(matplotlib)，与 laviz 同一套设计语言。

把信号/分帧/窗/频谱/mel 画成统一观感。用 Aurora 自己的 DSP(不依赖 librosa)。
用法：from aviz import *; style()
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt

from aurora.audio import (blackman, hamming, hann, mel_filterbank,
                          mel_spectrogram, power_spectrogram)
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
    theme_spec = apply_theme(theme, cjk_font=_cjk(), figure_size=(9, 3.2), font_size=11)
    _sync_theme(theme_spec)
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
    })


def waveform(x, title="波形 = 一串采样点", stem=False, figsize=(9, 3.2)):
    """画一段信号；stem=True 时画采样点(适合短信号)。"""
    style()
    x = np.asarray(x, float)
    fig, ax = plt.subplots(figsize=figsize)
    if stem:
        ax.plot(x, color=PALETTE[0], lw=1, alpha=.5)
        ax.plot(x, "o", color=PALETTE[0], ms=4)
    else:
        ax.plot(x, color=PALETTE[0], lw=1.5)
    ax.axhline(0, color=AXIS, lw=.6); ax.grid(alpha=.3)
    ax.set_xlabel("采样点 n"); ax.set_ylabel("幅度")
    ax.set_title(title, fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def aliasing(true_freq, sr, dur=0.01, figsize=(9, 3.2)):
    """欠采样：高频被"伪装"成低频。"""
    from aurora.audio import sine
    style()
    k = round(true_freq / sr); alias = abs(true_freq - k * sr)
    hi = sine(true_freq, duration=dur, sample_rate=sr)
    lo = sine(alias, duration=dur, sample_rate=sr)
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(hi, "o-", color=PALETTE[0], ms=5, label=f"采样 {true_freq}Hz @ {sr}Hz")
    ax.plot(lo, "x--", color=PALETTE[1], ms=6, label=f"看起来像 {alias:.0f}Hz")
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    ax.set_title("混叠：高频伪装成低频", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def twiddles(N=8, figsize=(5, 5)):
    """DFT 旋转因子 e^{-2πik/N} 落在单位圆上。"""
    style()
    fig, ax = plt.subplots(figsize=figsize)
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(t), np.sin(t), color=INK, lw=1.2)
    w = np.exp(-2j * np.pi * np.arange(N) / N)
    ax.scatter(w.real, w.imag, color=PALETTE[0], s=90, zorder=3)
    for i in range(N):
        ax.plot([0, w[i].real], [0, w[i].imag], color=PALETTE[0], lw=.8, alpha=.5)
        ax.annotate(f"k={i}", (w[i].real, w[i].imag),
                    (w[i].real * 1.13, w[i].imag * 1.13), fontsize=8, ha="center")
    ax.set_aspect("equal"); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
    ax.axhline(0, color=AXIS, lw=.6); ax.axvline(0, color=AXIS, lw=.6)
    ax.set_title(f"{N} 个旋转因子 = FFT 的积木", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def windows_overlay(N=64, figsize=(8, 3.4)):
    """三种窗函数对比：Hann / Hamming / Blackman。"""
    style()
    fig, ax = plt.subplots(figsize=figsize)
    for name, w, c in [("Hann", hann(N), PALETTE[0]),
                       ("Hamming", hamming(N), PALETTE[1]),
                       ("Blackman", blackman(N), PALETTE[3])]:
        ax.plot(w, label=name, color=c, lw=2)
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    ax.set_xlabel("采样点"); ax.set_ylabel("权重")
    ax.set_title(f"窗函数 (N={N}) — 两端压低以减少频谱泄漏", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def framing(x, frame_len=256, hop=128, n_frames=5, figsize=(10, 3.6)):
    """STFT 分帧：把长信号切成重叠的加窗短帧。"""
    style()
    x = np.asarray(x, float)
    w = hann(frame_len)
    amp = np.abs(x).max() or 1.0
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, color=INK, lw=.8, alpha=.45)
    for i in range(n_frames):
        s = i * hop
        if s + frame_len > len(x):
            break
        c = PALETTE[i % len(PALETTE)]
        ax.axvspan(s, s + frame_len, color=c, alpha=.08)
        ax.plot(np.arange(s, s + frame_len), w * amp, color=c, lw=2)
    ax.grid(alpha=.3); ax.set_xlabel("采样点 n"); ax.set_ylabel("幅度")
    ax.set_title(f"STFT 分帧：帧长={frame_len}, 跳步={hop}（帧间重叠 + 加窗）",
                 fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def spectrogram(x, n_fft=256, hop_length=128, figsize=(8, 3.6)):
    """功率谱图(分帧→FFT→|·|²)，dB 显示。"""
    style()
    P = power_spectrogram(np.asarray(x, float), n_fft=n_fft, hop_length=hop_length)
    db = 10 * np.log10(P.T + 1e-10)          # → (freq, frames)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(db, origin="lower", aspect="auto", cmap="magma")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="dB")
    ax.set_xlabel("帧 (时间)"); ax.set_ylabel("频率 bin")
    ax.set_title("功率谱图 = 一列列 FFT 拼起来", fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def mel_filterbank_plot(n_mels=20, n_fft=256, sample_rate=16000, figsize=(8, 3.6)):
    """mel 滤波器组 = 一个矩阵(每行一个三角滤波器)。"""
    style()
    M = mel_filterbank(n_mels=n_mels, n_fft=n_fft, sample_rate=sample_rate)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(M, origin="lower", aspect="auto", cmap="viridis")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set_xlabel("频率 bin"); ax.set_ylabel("mel 滤波器编号")
    ax.set_title("mel 滤波器组 = 一个矩阵 (M·功率谱 = mel 特征)",
                 fontweight="bold", color=INK)
    fig.tight_layout(); return fig


def mel_spectrogram_plot(x, sample_rate=16000, n_mels=40, figsize=(8, 3.6)):
    """mel 频谱图(感知加权的频谱)。"""
    style()
    S = mel_spectrogram(np.asarray(x, float), sample_rate=sample_rate, n_mels=n_mels)
    db = 10 * np.log10(S.T + 1e-10)          # → (mel, frames)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(db, origin="lower", aspect="auto", cmap="magma")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="dB")
    ax.set_xlabel("帧 (时间)"); ax.set_ylabel("mel 频带")
    ax.set_title("mel 频谱图 = 贴近人耳的频率表示", fontweight="bold", color=INK)
    fig.tight_layout(); return fig

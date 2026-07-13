"""Shared plotting theme helpers for Aurora figures.

The notebook bootstrap and the visualization helpers in ``aurora`` use this
module so that course plots can switch between a dark, VS Code-friendly theme
and a light fallback without duplicating rcParams logic.
"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from functools import wraps
from typing import Any

import matplotlib.pyplot as plt
from matplotlib import patheffects as pe


@dataclass(frozen=True)
class PlotTheme:
    name: str
    ink: str
    axis: str
    grid: str
    surface: tuple[float, float, float, float]
    shadow: tuple[float, float, float, float]
    legend_face: tuple[float, float, float, float]
    legend_edge: str
    paper: str = "none"


LIGHT_THEME = PlotTheme(
    name="light",
    ink="#22333B",
    axis="#53616B",
    grid="#D6DEE6",
    surface=(1.0, 1.0, 1.0, 0.88),
    shadow=(1.0, 1.0, 1.0, 0.95),
    legend_face=(1.0, 1.0, 1.0, 0.88),
    legend_edge="#C4CDD6",
)

DARK_THEME = PlotTheme(
    name="dark",
    ink="#EAF2FA",
    axis="#8FA8BF",
    grid="#34465A",
    surface=(0.05, 0.08, 0.14, 0.82),
    shadow=(0.02, 0.04, 0.09, 0.95),
    legend_face=(0.05, 0.08, 0.14, 0.84),
    legend_edge="#58708B",
)

_CURRENT_THEME = DARK_THEME
_HOOKS_INSTALLED = False

# Effective first-match order shared by the viz modules (duplicates removed
# from the historical per-module lists; the match result is unchanged).
_CJK_FONT_CANDIDATES = (
    "PingFang SC",
    "Arial Unicode MS",
    "Source Han Sans CN",
    "Source Han Sans CN Normal",
    "Heiti SC",
    "Noto Sans CJK SC",
    "SimHei",
    "WenQuanYi Zen Hei",
    "Droid Sans Fallback",
)


def find_cjk_font() -> str | None:
    """Return the first installed CJK font from the shared candidate list."""
    from matplotlib import font_manager as fm

    have = {f.name for f in fm.fontManager.ttflist}
    for name in _CJK_FONT_CANDIDATES:
        if name in have:
            return name
    return None


def sync_palette(namespace: dict[str, Any], theme: PlotTheme) -> None:
    """Write the theme palette into a viz module's globals (INK, AXIS, ...)."""
    namespace["INK"] = theme.ink
    namespace["AXIS"] = theme.axis
    namespace["GRID"] = theme.grid
    namespace["SURFACE"] = theme.surface
    namespace["SHADOW"] = theme.shadow
    namespace["LEGEND_FACE"] = theme.legend_face
    namespace["LEGEND_EDGE"] = theme.legend_edge
    namespace["PAPER"] = theme.paper


def _normalize_theme_name(theme: str) -> str:
    value = theme.strip().lower()
    if value not in {"auto", "light", "dark"}:
        raise ValueError(f"Unknown plot theme: {theme!r}")
    return value


def _env_theme_hint() -> str | None:
    for key in ("AURORA_PLOT_THEME", "VSCODE_THEME_KIND", "AURORA_THEME"):
        value = os.environ.get(key)
        if not value:
            continue
        lowered = value.strip().lower()
        if "dark" in lowered:
            return "dark"
        if "light" in lowered:
            return "light"
    return None


def _detect_auto_theme() -> str:
    hint = _env_theme_hint()
    if hint:
        return hint

    if os.name == "posix":
        try:
            proc = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                check=False,
                capture_output=True,
                text=True,
            )
        except Exception:
            proc = None
        else:
            if proc.returncode == 0 and "dark" in (proc.stdout or "").strip().lower():
                return "dark"

    return "dark"


def resolve_theme(theme: str | None = None) -> str:
    candidate = (
        theme if theme is not None else os.environ.get("AURORA_PLOT_THEME", "auto")
    )
    normalized = _normalize_theme_name(candidate)
    if normalized == "auto":
        return _detect_auto_theme()
    return normalized


def get_theme(theme: str | None = None) -> PlotTheme:
    return DARK_THEME if resolve_theme(theme) == "dark" else LIGHT_THEME


def theme_rcparams(
    theme: str | None = None,
    *,
    cjk_font: str | None = None,
    figure_size: tuple[float, float] | None = None,
    font_size: int | None = None,
) -> dict[str, Any]:
    spec = get_theme(theme)
    sans = [cjk_font] if cjk_font else []
    sans.append("DejaVu Sans")

    rc: dict[str, Any] = {
        "font.family": "sans-serif",
        "font.sans-serif": sans,
        "axes.unicode_minus": False,
        "figure.facecolor": spec.paper,
        "axes.facecolor": spec.paper,
        "savefig.facecolor": spec.paper,
        "savefig.edgecolor": spec.paper,
        "savefig.transparent": True,
        "figure.edgecolor": spec.paper,
        "text.color": spec.ink,
        "axes.labelcolor": spec.ink,
        "axes.titlecolor": spec.ink,
        "axes.edgecolor": spec.axis,
        "xtick.color": spec.ink,
        "ytick.color": spec.ink,
        "grid.color": spec.grid,
        "legend.facecolor": spec.legend_face,
        "legend.edgecolor": spec.legend_edge,
        "legend.framealpha": 0.92,
        "patch.edgecolor": spec.paper,
        # unified line/grid weights so figures look like one system
        "axes.linewidth": 1.1,
        "lines.linewidth": 1.8,
        "lines.markersize": 6.0,
        "xtick.major.width": 1.0,
        "ytick.major.width": 1.0,
        "grid.linewidth": 0.5,
        "grid.alpha": 0.18,
        "legend.fontsize": 9,
    }
    if figure_size is not None:
        rc["figure.figsize"] = figure_size
    if font_size is not None:
        rc["font.size"] = font_size
    return rc


def _halo_effects() -> list[Any]:
    return [pe.withStroke(linewidth=3.0, foreground=_CURRENT_THEME.shadow)]


def _on_image_axes(text: Any) -> bool:
    """True when the text sits on an axes carrying an imshow image (a heatmap)."""
    ax = getattr(text, "axes", None)
    return bool(getattr(ax, "images", None)) if ax is not None else False


_MATH_SYMS = (("ᵀ", "$^{T}$"), ("ᴴ", "$^{H}$"), ("∇", r"$\nabla$"), ("⊗", r"$\otimes$"))


def _mathify_symbols(text: Any) -> None:
    """Render math glyphs the text font lacks (∇, ᵀ, ᴴ, ⊗) via mathtext, IN FIGURES
    ONLY. Source keeps the raw unicode (which shows fine in stdout/markdown); this
    hook rewrites just the figure Text objects. Idempotent (no raw glyph after)."""
    try:
        s = text.get_text()
    except Exception:
        return
    if not s or not any(ch in s for ch, _ in _MATH_SYMS):
        return
    for a, b in _MATH_SYMS:
        s = s.replace(a, b)
    try:
        text.set_text(s)
    except Exception:
        pass


def _apply_text_contrast(text: Any) -> Any:
    if text is None or not hasattr(text, "set_path_effects"):
        return text
    _mathify_symbols(text)
    # Heatmap cell labels: fixed-color text is unreadable on a diverging or dark
    # colormap (dark-on-dark / light-on-light). Force white fill + a black outline,
    # which stays legible on any cell — light, dark, or near-white.
    if _on_image_axes(text):
        try:
            text.set_color("white")
            text.set_path_effects([pe.withStroke(linewidth=2.5, foreground="#0A0D12")])
        except Exception:
            pass
        return text
    try:
        fontsize = float(text.get_fontsize())
    except Exception:
        fontsize = 0.0
    if fontsize and fontsize < 8.0:
        return text
    try:
        text.set_path_effects(_halo_effects())
    except Exception:
        return text
    return text


def _apply_legend_contrast(legend: Any) -> Any:
    if legend is None:
        return legend
    for text in getattr(legend, "get_texts", lambda: [])():
        _apply_text_contrast(text)
    title = getattr(legend, "get_title", lambda: None)()
    if title is not None:
        _apply_text_contrast(title)
    return legend


def _apply_origin_cross(ax: Any) -> None:
    """Turn a Cartesian-plane axes into a single cross through the origin.

    Instead of the default box frame (left+bottom spines with edge ticks) *plus*
    a separate axhline/axvline at 0 — two redundant axis sets — move the left and
    bottom spines onto x=0 / y=0, hide the outer frame, and drop the now-duplicate
    origin lines. Applied only when a plot draws BOTH an x=0 and a y=0 line, i.e.
    it really is a coordinate plane (signal-vs-time plots draw only one, untouched).
    """
    if getattr(ax, "_aurora_origin_done", False):
        return
    ax._aurora_origin_done = True
    for ln in list(ax.lines):
        if getattr(ln, "_aurora_origin", False):
            try:
                ln.remove()
            except Exception:
                pass
    try:
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_color(_CURRENT_THEME.axis)
        ax.spines["bottom"].set_color(_CURRENT_THEME.axis)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
        # blank the 0 tick on both axes so they don't collide at the origin
        from matplotlib.ticker import FuncFormatter

        def _no_zero(v, _pos):
            return "" if abs(v) < 1e-9 else f"{v:g}"

        ax.xaxis.set_major_formatter(FuncFormatter(_no_zero))
        ax.yaxis.set_major_formatter(FuncFormatter(_no_zero))
        # arrowheads at the positive ends (standard math axes)
        ax.plot(
            1,
            0,
            marker=">",
            ms=6,
            color=_CURRENT_THEME.axis,
            clip_on=False,
            transform=ax.get_yaxis_transform(),
            zorder=6,
        )
        ax.plot(
            0,
            1,
            marker="^",
            ms=6,
            color=_CURRENT_THEME.axis,
            clip_on=False,
            transform=ax.get_xaxis_transform(),
            zorder=6,
        )
    except Exception:
        pass


def install_contrast_hooks() -> None:
    """Install lightweight hooks so titles/labels get a soft halo."""
    global _HOOKS_INSTALLED
    if _HOOKS_INSTALLED:
        return

    from matplotlib.axes import Axes
    from matplotlib.figure import Figure

    def _wrap(method_name: str, applier):
        original = getattr(Axes, method_name)

        @wraps(original)
        def wrapper(self, *args, **kwargs):
            result = original(self, *args, **kwargs)
            return applier(result)

        setattr(Axes, method_name, wrapper)

    _wrap("set_title", _apply_text_contrast)
    _wrap("set_xlabel", _apply_text_contrast)
    _wrap("set_ylabel", _apply_text_contrast)
    _wrap("text", _apply_text_contrast)
    _wrap("annotate", _apply_text_contrast)
    _wrap("legend", _apply_legend_contrast)

    fig_suptitle = Figure.suptitle

    @wraps(fig_suptitle)
    def suptitle_wrapper(self, *args, **kwargs):
        result = fig_suptitle(self, *args, **kwargs)
        return _apply_text_contrast(result)

    Figure.suptitle = suptitle_wrapper

    fig_legend = Figure.legend

    @wraps(fig_legend)
    def figure_legend_wrapper(self, *args, **kwargs):
        result = fig_legend(self, *args, **kwargs)
        return _apply_legend_contrast(result)

    Figure.legend = figure_legend_wrapper

    # Origin-cross axes: tag x=0 / y=0 reference lines; when an axes has both,
    # collapse the frame to a single cross through (0, 0).
    _orig_axhline = Axes.axhline

    @wraps(_orig_axhline)
    def axhline_wrapper(self, y=0, *args, **kwargs):
        line = _orig_axhline(self, y, *args, **kwargs)
        if y == 0:
            try:
                line._aurora_origin = True
            except Exception:
                pass
            self._aurora_h0 = True
            if getattr(self, "_aurora_v0", False):
                _apply_origin_cross(self)
        return line

    Axes.axhline = axhline_wrapper

    _orig_axvline = Axes.axvline

    @wraps(_orig_axvline)
    def axvline_wrapper(self, x=0, *args, **kwargs):
        line = _orig_axvline(self, x, *args, **kwargs)
        if x == 0:
            try:
                line._aurora_origin = True
            except Exception:
                pass
            self._aurora_v0 = True
            if getattr(self, "_aurora_h0", False):
                _apply_origin_cross(self)
        return line

    Axes.axvline = axvline_wrapper

    _HOOKS_INSTALLED = True


def _quiet_font_warnings() -> None:
    """Silence matplotlib font noise (Arial Unicode MS lacks a bold weight, and a
    few rare glyphs fall back) so it doesn't clutter notebook outputs or consoles."""
    import logging
    import warnings

    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
    warnings.filterwarnings("ignore", message=r"Glyph \d+ .* missing from font.*")
    warnings.filterwarnings("ignore", message=".*findfont.*")


def apply_theme(
    theme: str | None = None,
    *,
    cjk_font: str | None = None,
    figure_size: tuple[float, float] | None = None,
    font_size: int | None = None,
    extra_rc: dict[str, Any] | None = None,
) -> PlotTheme:
    """Apply theme-aware matplotlib rcParams and install contrast hooks."""
    global _CURRENT_THEME
    _CURRENT_THEME = get_theme(theme)
    plt.rcParams.update(
        theme_rcparams(
            _CURRENT_THEME.name,
            cjk_font=cjk_font,
            figure_size=figure_size,
            font_size=font_size,
        )
    )
    if extra_rc:
        plt.rcParams.update(extra_rc)
    _quiet_font_warnings()
    install_contrast_hooks()
    return _CURRENT_THEME

"""Shared matplotlib bootstrap for Aurora notebooks.

This file is imported from sitecustomize.py in each notebook directory so that
matplotlib picks a writable config dir, a real CJK-capable sans-serif font,
and the Aurora plot theme before any figure code runs.
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

_APPLIED = False


def _in_notebook_kernel() -> bool:
    try:
        from IPython import get_ipython
    except Exception:
        return False

    shell = get_ipython()
    if shell is None:
        return False

    # ZMQInteractiveShell is the Jupyter kernel used by notebooks / nbclient.
    shell_name = shell.__class__.__name__
    return shell_name == "ZMQInteractiveShell" or hasattr(shell, "kernel")


def _pick_cjk_font():
    try:
        from matplotlib import font_manager as fm
    except Exception:
        return None

    have = {f.name for f in fm.fontManager.ttflist}
    # PingFang SC first: Apple's modern standard simplified-Chinese face, crisp and
    # with clean Latin. Math symbols it lacks (∇, ᵀ, ⊗ …) are rendered via mathtext
    # in the figures, so they don't depend on the text font.
    candidates = (
        "PingFang SC",
        "Arial Unicode MS",
        "Hiragino Sans GB",
        "Heiti SC",
        "Source Han Sans CN",
        "Source Han Sans CN Normal",
        "Source Han Sans SC",
        "Heiti SC",
        "Songti SC",
        "Noto Sans CJK SC",
        "Microsoft YaHei",
        "PingFang SC",
        "SimHei",
        "WenQuanYi Zen Hei",
        "Droid Sans Fallback",
    )
    for name in candidates:
        if name in have:
            return name
    return None


def apply(theme: str | None = None) -> None:
    """Apply the Aurora matplotlib bootstrap once per interpreter."""
    global _APPLIED
    if _APPLIED:
        return

    os.environ.setdefault(
        "MPLCONFIGDIR",
        str(Path(tempfile.gettempdir()) / f"aurora-matplotlib-{os.getpid()}"),
    )

    try:
        import matplotlib
    except Exception:
        return

    if _in_notebook_kernel():
        try:
            matplotlib.use("module://matplotlib_inline.backend_inline", force=True)
        except Exception:
            # If the inline backend is unavailable, keep going and fall back
            # to the regular rcParams-only styling below.
            pass

    try:
        from aurora._plot_theme import apply_theme as _apply_theme
    except Exception:
        _apply_theme = None

    try:
        from matplotlib import pyplot as plt
    except Exception:
        return

    cjk = _pick_cjk_font()

    if _apply_theme is not None:
        _apply_theme(theme, cjk_font=cjk)
    else:
        sans = [cjk] if cjk else []
        sans.append("DejaVu Sans")
        plt.rcParams.update(
            {
                "font.family": "sans-serif",
                "font.sans-serif": sans,
                "axes.unicode_minus": False,
                "figure.facecolor": "none",
                "axes.facecolor": "none",
                "savefig.facecolor": "none",
                "savefig.transparent": True,
                "text.color": "#EAF2FA",
                "axes.labelcolor": "#EAF2FA",
                "axes.titlecolor": "#EAF2FA",
                "axes.edgecolor": "#8FA8BF",
                "xtick.color": "#EAF2FA",
                "ytick.color": "#EAF2FA",
            }
        )
    _APPLIED = True

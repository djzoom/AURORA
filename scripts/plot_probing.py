"""Plot layer-wise probe accuracy from ``probe_whisper_layers.py`` results.

    python scripts/plot_probing.py results/probing/base.en results/probing/small.en

Writes ``results/probing/probe_layers.png``: one panel per model, accuracy of
the phone / speaker / gender probes at each encoder depth, with the
random-initialisation control dashed and majority-class chance dotted.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

TASKS = [
    ("phone", "Phone (39-way)", "#2a78d6"),
    ("speaker", "Speaker (40-way)", "#eb6834"),
    ("gender", "Gender (2-way)", "#1baf7a"),
]
INK, MUTED, GRID = "#1f1f1e", "#6b6a63", "#e4e3dc"


def main() -> None:
    dirs = [Path(p) for p in sys.argv[1:]]
    fig, axes = plt.subplots(
        1, len(dirs), figsize=(6.4 * len(dirs), 4.6), dpi=150, squeeze=False
    )
    for ax, d in zip(axes[0], dirs, strict=True):
        r = json.loads((d / "probe.json").read_text())
        layers = r["layers"]
        xs = range(len(layers))
        for key, label, c in TASKS:
            ax.plot(
                xs,
                [r["trained"][L][key] for L in layers],
                color=c,
                lw=2,
                marker="o",
                ms=5,
                label=label,
            )
            ri = [r["random_init"].get(L, {}).get(key) for L in layers]
            pts = [(x, v) for x, v in zip(xs, ri, strict=True) if v is not None]
            if pts:
                ax.plot(*zip(*pts, strict=True), color=c, lw=1.5, ls="--", alpha=0.7)
            ax.axhline(r["chance"][key], color=c, lw=1, ls=":", alpha=0.6)
        ax.set_xticks(list(xs), layers, color=INK, fontsize=9)
        ax.set_ylim(0, 1)
        ax.set_ylabel("held-out probe accuracy", color=MUTED)
        ax.set_title(f"Whisper {d.name} encoder", color=INK, loc="left", fontsize=12)
        ax.grid(axis="y", color=GRID)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0][0].legend(frameon=False, fontsize=9, loc="lower left")
    fig.text(
        0.01,
        0.01,
        "solid: trained model   dashed: same architecture, random "
        "weights   dotted: majority-class chance",
        color=MUTED,
        fontsize=8.5,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    out = dirs[0].parent / "probe_layers.png"
    fig.savefig(out, facecolor="white")
    print(out)


if __name__ == "__main__":
    main()

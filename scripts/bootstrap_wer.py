"""Paired bootstrap for the WER cost of an encoder edit.

    python scripts/bootstrap_wer.py results/probing/base.en results/probing/small.en

Reads ``hyps.json`` (written by ``probe_whisper_layers.py``), resamples
utterances with replacement and reports the corpus-WER difference between the
``speaker_leace`` and ``none`` conditions with a 95% percentile interval.
Writes ``bootstrap.json`` next to the model folders.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from aurora.speech import edit_distance


def main(n_boot: int = 10000) -> None:
    dirs = [Path(p) for p in sys.argv[1:]]
    out = {}
    for d in dirs:
        h = json.loads((d / "hyps.json").read_text())
        refs = [r.split() for r in h["refs"]]
        n = np.array([len(r) for r in refs], float)

        def errors(key, h=h, refs=refs):
            hyps = h[key]
            return np.array(
                [edit_distance(r, x.split()) for r, x in zip(refs, hyps, strict=True)],
                float,
            )

        a, b = errors("none"), errors("speaker_leace")
        rng = np.random.default_rng(0)
        idx = rng.integers(0, len(n), (n_boot, len(n)))
        diffs = (b[idx].sum(1) - a[idx].sum(1)) / n[idx].sum(1)
        lo, hi = np.percentile(diffs, [2.5, 97.5])
        out[d.name] = {
            "wer_none": float(a.sum() / n.sum()),
            "wer_spk": float(b.sum() / n.sum()),
            "delta": float((b.sum() - a.sum()) / n.sum()),
            "ci95": [float(lo), float(hi)],
            "p_le0": float(np.mean(diffs <= 0)),
            "words": int(n.sum()),
            "utts_changed": int((a != b).sum()),
        }
        r = out[d.name]
        print(
            f"{d.name}: {r['wer_none'] * 100:.2f}% -> {r['wer_spk'] * 100:.2f}%  "
            f"delta {r['delta'] * 100:+.2f} pp  CI [{lo * 100:+.2f}, {hi * 100:+.2f}]"
        )
    (dirs[0].parent / "bootstrap.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""scripts/validate_pipeline.py — Aurora notebook and pipeline acceptance gate.

Three checks, run in order:

  1. JSON validity       — every .ipynb is parseable JSON
  2. Syntax check        — every code cell parses as Python
                           (Jupyter magics %/!/? and top-level `await` are skipped)
  3. Audio pipeline      — synthetic 1-second sine wave flows through the full
                           aurora.audio stack; shapes are asserted at each step

Usage:
    python scripts/validate_pipeline.py            # all checks
    python scripts/validate_pipeline.py --json     # JSON only
    python scripts/validate_pipeline.py --syntax   # syntax only
    python scripts/validate_pipeline.py --pipeline # pipeline only

Exit code 0 = all checks passed.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NB_DIR = REPO / "notebooks"

# Jupyter cell prefixes that are not plain Python
_MAGIC_PREFIXES = ("%", "!", "?")


# ─── helpers ──────────────────────────────────────────────────────────────────


def _iter_notebooks() -> list[Path]:
    return sorted(NB_DIR.rglob("L*.ipynb"))


def _code_cells(nb: dict) -> list[str]:
    """Return source strings for all code cells."""
    out = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        out.append("".join(cell.get("source", [])))
    return out


def _filter_magic(src: str) -> str:
    """Remove lines that are Jupyter magics or top-level awaits."""
    lines = []
    for line in src.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(_MAGIC_PREFIXES):
            continue
        if stripped.startswith("await "):
            continue
        lines.append(line)
    return "\n".join(lines)


# ─── check 1: JSON validity ───────────────────────────────────────────────────


def check_json(notebooks: list[Path]) -> list[str]:
    failures: list[str] = []
    for nb_path in notebooks:
        try:
            json.loads(nb_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{nb_path.name}: {exc}")
    return failures


# ─── check 2: syntax ─────────────────────────────────────────────────────────


def check_syntax(notebooks: list[Path]) -> list[str]:
    failures: list[str] = []
    for nb_path in notebooks:
        try:
            nb = json.loads(nb_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue  # already caught by check_json
        for idx, src in enumerate(_code_cells(nb)):
            filtered = _filter_magic(src)
            if not filtered.strip():
                continue
            try:
                ast.parse(filtered)
            except SyntaxError as exc:
                failures.append(
                    f"{nb_path.name} cell {idx} line {exc.lineno}: {exc.msg}"
                )
    return failures


# ─── check 3: audio pipeline ─────────────────────────────────────────────────


def check_pipeline() -> list[str]:
    """Run synthetic audio through aurora.audio end-to-end; assert shapes."""
    failures: list[str] = []

    try:
        import numpy as np
    except ImportError:
        return ["numpy not installed"]

    # Insert src/ into path if not already importable
    src_dir = str(REPO / "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    # ── step 0: synthesise 1-second 440 Hz sine at 16 kHz ────────────────────
    SR = 16_000
    DURATION = 1.0
    t = np.linspace(0, DURATION, int(SR * DURATION), endpoint=False)
    signal = (0.5 * np.sin(2 * np.pi * 440 * t)).astype(np.float32)

    if signal.shape != (16_000,):
        failures.append(f"signal shape {signal.shape} != (16000,)")
        return failures

    # ── step 1: STFT ──────────────────────────────────────────────────────────
    try:
        from aurora.audio.stft import stft

        N_FFT, HOP = 1024, 256
        spec = stft(signal, n_fft=N_FFT, hop_length=HOP)
        # aurora.audio.stft returns (n_frames, n_bins)
        n_bins_expected = N_FFT // 2 + 1
        if spec.ndim != 2 or spec.shape[1] != n_bins_expected:
            failures.append(
                f"stft shape {spec.shape}, expected (n_frames, {n_bins_expected})"
            )
    except Exception as exc:
        failures.append(f"stft: {exc}")
        spec = None

    # ── step 2: mel spectrogram ───────────────────────────────────────────────
    try:
        from aurora.audio.mel import mel_spectrogram

        N_MELS = 40
        mel = mel_spectrogram(signal, sample_rate=SR, n_fft=N_FFT, hop_length=HOP, n_mels=N_MELS)
        # aurora.audio.mel returns (n_frames, n_mels)
        if mel.ndim != 2 or mel.shape[1] != N_MELS:
            failures.append(
                f"mel_spectrogram shape {mel.shape}, expected (n_frames, {N_MELS})"
            )
        else:
            n_frames = mel.shape[0]
    except Exception as exc:
        failures.append(f"mel_spectrogram: {exc}")
        mel = None

    # ── step 3: MFCC ─────────────────────────────────────────────────────────
    try:
        from aurora.audio.mfcc import mfcc

        N_MFCC = 13
        coeffs = mfcc(signal, sample_rate=SR, n_mfcc=N_MFCC, n_fft=N_FFT, hop_length=HOP, n_mels=N_MELS)
        if coeffs.ndim != 2 or coeffs.shape[1] != N_MFCC:
            failures.append(
                f"mfcc shape {coeffs.shape}, expected (n_frames, {N_MFCC})"
            )
    except Exception as exc:
        failures.append(f"mfcc: {exc}")

    # ── step 4: DataLoader shape (L62 fix validation) ────────────────────────
    try:
        from aurora.audio.mel import mel_spectrogram as _mel

        raw_mel = _mel(signal, sample_rate=SR, n_fft=2048, hop_length=512, n_mels=40)
        # L62 KWSDataset.__getitem__ must transpose to (n_mels, n_frames) for CNN
        cnn_input = raw_mel.T  # (40, n_frames)
        if cnn_input.shape[0] != 40:
            failures.append(
                f"CNN input shape[0]={cnn_input.shape[0]}, expected 40 (n_mels dim)"
            )
    except Exception as exc:
        failures.append(f"DataLoader shape check: {exc}")

    return failures


# ─── main ─────────────────────────────────────────────────────────────────────


def _section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json",     action="store_true", help="JSON check only")
    parser.add_argument("--syntax",   action="store_true", help="Syntax check only")
    parser.add_argument("--pipeline", action="store_true", help="Pipeline check only")
    args = parser.parse_args(argv)

    run_all = not (args.json or args.syntax or args.pipeline)
    notebooks = _iter_notebooks()
    all_failures: list[str] = []

    # ── JSON ──────────────────────────────────────────────────────────────────
    if run_all or args.json:
        _section(f"Check 1 / JSON validity  ({len(notebooks)} notebooks)")
        failures = check_json(notebooks)
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print(f"  ✅  All {len(notebooks)} notebooks are valid JSON")

    # ── Syntax ────────────────────────────────────────────────────────────────
    if run_all or args.syntax:
        _section(f"Check 2 / Python syntax  ({len(notebooks)} notebooks)")
        failures = check_syntax(notebooks)
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print(f"  ✅  All code cells pass syntax check")

    # ── Pipeline ──────────────────────────────────────────────────────────────
    if run_all or args.pipeline:
        _section("Check 3 / Audio pipeline  (signal → STFT → mel → MFCC → CNN shape)")
        failures = check_pipeline()
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print("  ✅  Full pipeline passes shape assertions")

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'═' * 60}")
    if all_failures:
        print(f"  FAILED  {len(all_failures)} issue(s)")
        print(f"{'═' * 60}\n")
        return 1
    else:
        print("  PASSED  all checks")
        print(f"{'═' * 60}\n")
        return 0


if __name__ == "__main__":
    sys.exit(main())

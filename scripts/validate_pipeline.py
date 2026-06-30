#!/usr/bin/env python3
"""scripts/validate_pipeline.py — Aurora notebook and pipeline acceptance gate.

Five checks, run in order:

  1. JSON validity       — every .ipynb is parseable JSON
  2. Syntax check        — every code cell parses as Python
                           (Jupyter magics %/!/? and top-level `await` are skipped)
  3. Audio pipeline      — signal → STFT → mel → MFCC → CNN orientation
  4. Multi-core pipelines— LLM (KVCache / sampling / retrieval),
                           Music (chromagram / beat_track),
                           ASR (word_error_rate correctness)
  5. Structural checks   — L-number in notebook title matches filename;
                           all L-references (L01–L99) point to real notebooks;
                           15 derivation-heavy lessons have a 闭卷推导 cell

Usage:
    python scripts/validate_pipeline.py            # all checks
    python scripts/validate_pipeline.py --json     # JSON only
    python scripts/validate_pipeline.py --syntax   # syntax only
    python scripts/validate_pipeline.py --pipeline # audio pipeline only
    python scripts/validate_pipeline.py --cores    # multi-core pipelines only
    python scripts/validate_pipeline.py --struct   # structural checks only

Exit code 0 = all checks passed.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NB_DIR = REPO / "notebooks"
AUDIT_DIR = REPO / "docs" / "current" / "audit" / "per_lesson"

# Jupyter cell prefixes that are not plain Python
_MAGIC_PREFIXES = ("%", "!", "?")

# 15 lessons that must contain a 闭卷推导 (derivation check) markdown cell
_DERIVATION_LESSONS = {
    "L38", "L44", "L47", "L49", "L50",
    "L54", "L56", "L67", "L69", "L70",
    "L83", "L84", "L85", "L86", "L89",
}


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


def _markdown_cells(nb: dict) -> list[str]:
    """Return source strings for all markdown cells."""
    return [
        "".join(cell.get("source", []))
        for cell in nb.get("cells", [])
        if cell.get("cell_type") == "markdown"
    ]


def _filter_magic(src: str) -> str:
    """Remove Jupyter magics/awaits; preserve block structure.

    Avoids false SyntaxErrors from ast.parse on magic-containing cells.

    Two cases handled:
    - Cell magic (%%foo): skip the entire remainder of the cell — the body is
      non-Python content (HTML, bash, etc.) that would fail ast.parse.
    - Line magic / shell / help / await: replace with `pass` at the same
      indentation level so that enclosing try/if/for blocks stay syntactically
      valid (bare deletion would produce "expected an indented block").
    """
    lines = []
    skip_cell_magic_body = False
    for line in src.splitlines():
        stripped = line.lstrip()
        # Cell magic (%%foo) — drop this line and all subsequent lines in cell
        if stripped.startswith("%%"):
            skip_cell_magic_body = True
            continue
        if skip_cell_magic_body:
            continue
        # Line magic / shell / help / top-level await — replace with `pass`
        if stripped.startswith(_MAGIC_PREFIXES) or stripped.startswith("await "):
            indent = len(line) - len(stripped)
            lines.append(" " * indent + "pass  # <filtered magic>")
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

    src_dir = str(REPO / "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    SR = 16_000
    DURATION = 1.0
    t = np.linspace(0, DURATION, int(SR * DURATION), endpoint=False)
    signal = (0.5 * np.sin(2 * np.pi * 440 * t)).astype(np.float32)

    if signal.shape != (16_000,):
        failures.append(f"signal shape {signal.shape} != (16000,)")
        return failures

    # step 1: STFT
    try:
        from aurora.audio.stft import stft

        N_FFT, HOP = 1024, 256
        spec = stft(signal, n_fft=N_FFT, hop_length=HOP)
        n_bins_expected = N_FFT // 2 + 1
        if spec.ndim != 2 or spec.shape[1] != n_bins_expected:
            failures.append(
                f"stft shape {spec.shape}, expected (n_frames, {n_bins_expected})"
            )
    except Exception as exc:
        failures.append(f"stft: {exc}")

    # step 2: mel spectrogram
    try:
        from aurora.audio.mel import mel_spectrogram

        N_MELS = 40
        mel = mel_spectrogram(
            signal, sample_rate=SR, n_fft=N_FFT, hop_length=HOP, n_mels=N_MELS
        )
        if mel.ndim != 2 or mel.shape[1] != N_MELS:
            failures.append(
                f"mel_spectrogram shape {mel.shape}, expected (n_frames, {N_MELS})"
            )
    except Exception as exc:
        failures.append(f"mel_spectrogram: {exc}")

    # step 3: MFCC
    try:
        from aurora.audio.mfcc import mfcc

        N_MFCC = 13
        coeffs = mfcc(
            signal,
            sample_rate=SR,
            n_mfcc=N_MFCC,
            n_fft=N_FFT,
            hop_length=HOP,
            n_mels=N_MELS,
        )
        if coeffs.ndim != 2 or coeffs.shape[1] != N_MFCC:
            failures.append(
                f"mfcc shape {coeffs.shape}, expected (n_frames, {N_MFCC})"
            )
    except Exception as exc:
        failures.append(f"mfcc: {exc}")

    # step 4: time-major orientation check (n_frames=32 ≠ n_mels=40 → distinguishable)
    try:
        from aurora.audio.mel import mel_spectrogram as _mel

        N_MELS_CNN, HOP_CNN = 40, 512
        raw_mel = _mel(
            signal, sample_rate=SR, n_fft=2048, hop_length=HOP_CNN, n_mels=N_MELS_CNN
        )
        expected_frames = 1 + len(signal) // HOP_CNN
        if raw_mel.shape != (expected_frames, N_MELS_CNN):
            failures.append(
                f"mel_spectrogram (hop=512) shape {raw_mel.shape}, "
                f"expected ({expected_frames}, {N_MELS_CNN}) — "
                f"check time-major vs feature-major"
            )
        else:
            cnn_input = raw_mel.T
            if cnn_input.shape[0] != N_MELS_CNN:
                failures.append(
                    f"CNN input (mel.T) shape[0]={cnn_input.shape[0]}, "
                    f"expected {N_MELS_CNN}"
                )
    except Exception as exc:
        failures.append(f"DataLoader orientation check: {exc}")

    return failures


# ─── check 4: multi-core pipelines ───────────────────────────────────────────


def check_multicore_pipelines() -> list[str]:
    """Smoke-test LLM, Music, and ASR pipelines for shape/type correctness."""
    failures: list[str] = []

    try:
        import numpy as np
    except ImportError:
        return ["numpy not installed"]

    src_dir = str(REPO / "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    rng = np.random.default_rng(0)

    # ── LLM: KVCache ─────────────────────────────────────────────────────────
    try:
        from aurora.llm.kvcache import KVCache

        cache = KVCache(n_heads=2, head_dim=8)
        k = rng.standard_normal((2, 1, 8)).astype(np.float32)
        v = rng.standard_normal((2, 1, 8)).astype(np.float32)
        k_out, v_out = cache.update(layer=0, new_k=k, new_v=v)
        if k_out.shape != (2, 1, 8):
            failures.append(f"KVCache step-1 k shape {k_out.shape} != (2,1,8)")
        # second token → seq grows
        k2 = rng.standard_normal((2, 1, 8)).astype(np.float32)
        v2 = rng.standard_normal((2, 1, 8)).astype(np.float32)
        k_out2, v_out2 = cache.update(layer=0, new_k=k2, new_v=v2)
        if k_out2.shape != (2, 2, 8):
            failures.append(f"KVCache step-2 k shape {k_out2.shape} != (2,2,8)")
    except Exception as exc:
        failures.append(f"LLM KVCache: {exc}")

    # ── LLM: sampling ────────────────────────────────────────────────────────
    try:
        from aurora.llm.sample import top_k_sample, top_p_sample

        logits = np.array([1.0, 3.0, 0.5, 2.0])
        tok_k = top_k_sample(logits, k=2)
        if not (0 <= tok_k < len(logits)):
            failures.append(f"top_k_sample returned {tok_k}, out of range")
        tok_p = top_p_sample(logits, p=0.9)
        if not (0 <= tok_p < len(logits)):
            failures.append(f"top_p_sample returned {tok_p}, out of range")
    except Exception as exc:
        failures.append(f"LLM sampling: {exc}")

    # ── LLM: retrieval ───────────────────────────────────────────────────────
    try:
        from aurora.llm.retrieve import build_tfidf, cosine_retrieve

        docs = ["audio signal processing", "fourier transform", "mel spectrogram"]
        tfidf_matrix, vocab = build_tfidf(docs)
        results = cosine_retrieve("audio", tfidf_matrix, vocab, docs, top_k=2)
        if len(results) != 2:
            failures.append(
                f"cosine_retrieve returned {len(results)} results, expected 2"
            )
    except Exception as exc:
        failures.append(f"LLM retrieval: {exc}")

    # ── Music: chromagram ────────────────────────────────────────────────────
    try:
        from aurora.music.features import chromagram, rms_envelope

        SR = 8_000
        t = np.linspace(0, 1.0, SR, endpoint=False)
        sig = (0.5 * np.sin(2 * np.pi * 440 * t)).astype(np.float64)

        cg = chromagram(sig, sample_rate=SR)
        if cg.ndim != 2 or cg.shape[-1] != 12:
            failures.append(
                f"chromagram shape {cg.shape}, expected (n_frames, 12)"
            )
        rms = rms_envelope(sig)
        if rms.ndim != 1 or len(rms) == 0:
            failures.append(f"rms_envelope shape {rms.shape}, expected (n_frames,)")
    except Exception as exc:
        failures.append(f"Music chromagram: {exc}")

    # ── Music: beat_track ────────────────────────────────────────────────────
    try:
        from aurora.music.features import beat_track

        result = beat_track(sig, sample_rate=SR)
        if not (isinstance(result, tuple) and len(result) == 2):
            failures.append("beat_track must return (bpm, beat_times) tuple")
        else:
            bpm, beat_times = result
            if not (bpm > 0):
                failures.append(f"beat_track bpm={bpm}, expected > 0")
            if not isinstance(beat_times, np.ndarray):
                failures.append("beat_track beat_times is not an ndarray")
    except Exception as exc:
        failures.append(f"Music beat_track: {exc}")

    # ── ASR: word error rate ─────────────────────────────────────────────────
    try:
        from aurora.speech.metrics import corpus_wer, wer

        wer_zero = wer("hello world", "hello world")
        if abs(wer_zero) > 1e-9:
            failures.append(f"wer(identical) = {wer_zero}, expected 0.0")

        wer_one = wer("hello world", "hello there")
        if not (0 < wer_one <= 1.0):
            failures.append(f"wer(one error) = {wer_one}, expected (0, 1]")

        cwer = corpus_wer(["hello world", "foo bar"], ["hello world", "foo baz"])
        if not (0 < cwer <= 1.0):
            failures.append(f"corpus_wer = {cwer}, expected (0, 1]")
    except Exception as exc:
        failures.append(f"ASR metrics: {exc}")

    return failures


# ─── check 5: structural consistency ─────────────────────────────────────────


def check_structure(notebooks: list[Path]) -> list[str]:
    """Verify notebook structure conventions across all lessons.

    Three sub-checks:
    a) L-number in first markdown H1 title matches filename.
    b) All L\\d{2} references in markdown cells point to real notebooks.
    c) 15 derivation-heavy lessons contain a 闭卷推导 markdown cell.
    """
    failures: list[str] = []

    # Build set of valid lesson numbers from actual files
    valid_lnums = set()
    for nb in notebooks:
        lnum = nb.stem.split("_")[0].upper()
        if re.fullmatch(r"L\d{2}", lnum):
            valid_lnums.add(lnum)

    for nb_path in notebooks:
        try:
            nb = json.loads(nb_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        stem = nb_path.stem
        lnum = stem.split("_")[0].upper()
        cells = nb.get("cells", [])

        md_cells = _markdown_cells(nb)
        all_md = "\n".join(md_cells)

        # 5a: L-number in first markdown H1 matches filename
        first_md = next(
            (c for c in cells if c.get("cell_type") == "markdown"), None
        )
        if first_md:
            first_src = "".join(first_md.get("source", [])).strip()
            first_line = first_src.split("\n")[0]
            if first_line.startswith("#"):
                upper_line = first_line.upper()
                # Accept 'L01', 'L01 ·', 'L01·', 'L01.' or '第1课', '第01课' etc.
                n = int(lnum[1:])  # numeric part of filename, e.g. 1 for L01
                old_ok = lnum in upper_line
                new_ok = f"第{n}课" in first_line or f"第{n:02d}课" in first_line
                if not old_ok and not new_ok:
                    failures.append(
                        f"{nb_path.name}: title L-number mismatch "
                        f"(filename={lnum}, title='{first_line[:60]}')"
                    )

        # 5b: all Lxx references in markdown point to real notebooks
        for ref_match in re.finditer(r"\bL(\d{2})\b", all_md):
            ref = "L" + ref_match.group(1)
            if ref not in valid_lnums:
                failures.append(
                    f"{nb_path.name}: references {ref} which has no notebook file"
                )

        # 5c: derivation lessons must have a 闭卷推导 cell
        if lnum in _DERIVATION_LESSONS:
            if "闭卷推导" not in all_md and "推导检查" not in all_md:
                failures.append(
                    f"{nb_path.name}: derivation lesson missing "
                    f"'闭卷推导' or '推导检查' markdown cell"
                )

    return failures


# ─── main ─────────────────────────────────────────────────────────────────────


def _section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--json",     action="store_true", help="JSON check only")
    parser.add_argument("--syntax",   action="store_true", help="Syntax check only")
    parser.add_argument("--pipeline", action="store_true", help="Audio pipeline only")
    parser.add_argument("--cores",  action="store_true", help="Multi-core pipelines")
    parser.add_argument("--struct", action="store_true", help="Structural checks only")
    args = parser.parse_args(argv)

    flags = (args.json, args.syntax, args.pipeline, args.cores, args.struct)
    run_all = not any(flags)
    notebooks = _iter_notebooks()
    all_failures: list[str] = []

    # ── Check 1: JSON ─────────────────────────────────────────────────────────
    if run_all or args.json:
        _section(f"Check 1 / JSON validity  ({len(notebooks)} notebooks)")
        failures = check_json(notebooks)
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print(f"  ✅  All {len(notebooks)} notebooks are valid JSON")

    # ── Check 2: Syntax ───────────────────────────────────────────────────────
    if run_all or args.syntax:
        _section(f"Check 2 / Python syntax  ({len(notebooks)} notebooks)")
        failures = check_syntax(notebooks)
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print("  ✅  All code cells pass syntax check")

    # ── Check 3: Audio pipeline ───────────────────────────────────────────────
    if run_all or args.pipeline:
        _section("Check 3 / Audio pipeline  (signal → STFT → mel → MFCC → CNN shape)")
        failures = check_pipeline()
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print("  ✅  Full audio pipeline passes shape assertions")

    # ── Check 4: Multi-core pipelines ─────────────────────────────────────────
    if run_all or args.cores:
        _section(
            "Check 4 / Multi-core pipelines  "
            "(LLM: KVCache/sampling/retrieval · Music: chroma/beat · ASR: WER)"
        )
        failures = check_multicore_pipelines()
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print("  ✅  LLM / Music / ASR pipelines pass")

    # ── Check 5: Structural consistency ───────────────────────────────────────
    if run_all or args.struct:
        _section(
            f"Check 5 / Structural consistency  ({len(notebooks)} notebooks · "
            f"title · L-refs · {len(_DERIVATION_LESSONS)} derivation cells)"
        )
        failures = check_structure(notebooks)
        if failures:
            for f in failures:
                print(f"  ❌  {f}")
            all_failures.extend(failures)
        else:
            print(
                f"  ✅  All notebooks pass structural checks "
                f"({len(_DERIVATION_LESSONS)} derivation cells confirmed)"
            )

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

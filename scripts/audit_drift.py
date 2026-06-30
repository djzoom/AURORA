#!/usr/bin/env python3
"""scripts/audit_drift.py — Course upgrade drift detector.

Compares the last-commit timestamp of each notebook against its corresponding
per-lesson audit document.  Flags notebooks that were modified AFTER their
audit was last updated — those lessons need re-auditing before the next
course revision cycle.

Exit codes:
    0  — all audits are current (or no notebooks changed since last audit)
    1  — at least one notebook has drifted ahead of its audit doc
    2  — usage / git error

Usage:
    python scripts/audit_drift.py              # full report
    python scripts/audit_drift.py --strict     # exit 1 if any drift found
    python scripts/audit_drift.py --missing    # report missing audit docs only
    python scripts/audit_drift.py --summary    # one-line summary only
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NB_DIR = REPO / "notebooks"
AUDIT_DIR = REPO / "docs" / "current" / "audit" / "per_lesson"


# ─── git helpers ──────────────────────────────────────────────────────────────


def _git_mtime(path: Path) -> int | None:
    """Return the Unix timestamp of the most recent commit touching *path*.

    Returns None if the file has never been committed (untracked / new).
    """
    try:
        result = subprocess.run(
            ["git", "log", "--format=%at", "-1", "--", str(path)],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        )
        ts = result.stdout.strip()
        return int(ts) if ts else None
    except (subprocess.CalledProcessError, ValueError):
        return None


def _git_available() -> bool:
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=REPO,
            capture_output=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


# ─── data model ───────────────────────────────────────────────────────────────


@dataclass
class LessonStatus:
    lnum: str           # 'L01'
    nb_path: Path
    audit_path: Path | None
    nb_ts: int | None       # last-commit timestamp of notebook
    audit_ts: int | None    # last-commit timestamp of audit doc

    @property
    def missing_audit(self) -> bool:
        return self.audit_path is None or not self.audit_path.exists()

    @property
    def drifted(self) -> bool:
        """Notebook committed after audit doc — needs re-audit."""
        if self.missing_audit:
            return False  # separate category
        if self.nb_ts is None or self.audit_ts is None:
            return False  # untracked; ignore
        return self.nb_ts > self.audit_ts

    @property
    def nb_newer_by(self) -> int:
        """Seconds by which notebook is ahead of audit doc."""
        if self.nb_ts and self.audit_ts:
            return self.nb_ts - self.audit_ts
        return 0


# ─── core logic ───────────────────────────────────────────────────────────────


def _iter_lessons() -> list[LessonStatus]:
    statuses = []
    for nb_path in sorted(NB_DIR.rglob("L*.ipynb")):
        stem = nb_path.stem
        lnum_raw = stem.split("_")[0]
        if not (lnum_raw.startswith("L") and lnum_raw[1:].isdigit()):
            continue
        lnum = lnum_raw.upper()

        audit_path = AUDIT_DIR / f"{lnum}.md"
        nb_ts = _git_mtime(nb_path)
        audit_ts = _git_mtime(audit_path) if audit_path.exists() else None

        statuses.append(
            LessonStatus(
                lnum=lnum,
                nb_path=nb_path,
                audit_path=audit_path if audit_path.exists() else None,
                nb_ts=nb_ts,
                audit_ts=audit_ts,
            )
        )
    return statuses


def _fmt_delta(seconds: int) -> str:
    if seconds < 3600:
        return f"{seconds // 60}m"
    if seconds < 86400:
        return f"{seconds // 3600}h"
    return f"{seconds // 86400}d"


# ─── reporting ────────────────────────────────────────────────────────────────


def report(statuses: list[LessonStatus], missing_only: bool = False) -> int:
    drifted = [s for s in statuses if s.drifted]
    missing = [s for s in statuses if s.missing_audit]
    current = [s for s in statuses if not s.drifted and not s.missing_audit]

    if missing_only:
        if missing:
            print(f"{'─'*60}")
            print(f"  Missing audit docs ({len(missing)} lessons)")
            print(f"{'─'*60}")
            for s in missing:
                print(f"  ⚠  {s.lnum}  — {s.nb_path.name}")
        else:
            print("  ✅  All lessons have audit docs")
        return 0

    # Full report
    print(f"{'─'*60}")
    print("  Aurora Audit Drift Report")
    print(f"  Notebooks: {len(statuses)}  |  "
          f"Current: {len(current)}  |  "
          f"Drifted: {len(drifted)}  |  "
          f"No audit: {len(missing)}")
    print(f"{'─'*60}")

    if drifted:
        print(f"\n  🔴  NEEDS RE-AUDIT ({len(drifted)} lessons)")
        print(f"  {'Lesson':<8} {'Drift':<8} Notebook")
        print(f"  {'─'*6:<8} {'─'*6:<8} {'─'*40}")
        for s in sorted(drifted, key=lambda x: -x.nb_newer_by):
            delta = _fmt_delta(s.nb_newer_by)
            print(f"  {s.lnum:<8} +{delta:<7} {s.nb_path.name}")
        print()

    if missing:
        print(f"  ⚠   MISSING AUDIT DOC ({len(missing)} lessons)")
        for s in missing:
            print(f"  {s.lnum:<8} {s.nb_path.name}")
        print()

    if current:
        print(f"  ✅  Current ({len(current)} lessons) — audit up to date")

    print(f"\n{'═'*60}")
    if drifted or missing:
        status_msg = []
        if drifted:
            status_msg.append(f"{len(drifted)} drifted")
        if missing:
            status_msg.append(f"{len(missing)} missing audit")
        print(f"  ACTION NEEDED  {', '.join(status_msg)}")
        print(f"{'═'*60}\n")
        return 1 if drifted else 0
    else:
        print("  ALL CLEAR  no drift detected")
        print(f"{'═'*60}\n")
        return 0


# ─── main ─────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 if any drift found (for CI gate)"
    )
    parser.add_argument(
        "--missing", action="store_true",
        help="Report missing audit docs only"
    )
    parser.add_argument(
        "--summary", action="store_true",
        help="One-line summary only"
    )
    args = parser.parse_args(argv)

    if not _git_available():
        print("ERROR: not a git repository", file=sys.stderr)
        return 2

    statuses = _iter_lessons()

    if args.summary:
        drifted = [s for s in statuses if s.drifted]
        missing = [s for s in statuses if s.missing_audit]
        current = len(statuses) - len(drifted) - len(missing)
        print(
            f"Aurora audit drift: "
            f"{current}/{len(statuses)} current, "
            f"{len(drifted)} drifted, "
            f"{len(missing)} missing"
        )
        return 1 if (drifted and args.strict) else 0

    rc = report(statuses, missing_only=args.missing)
    drifted_count = sum(1 for s in statuses if s.drifted)
    if args.strict and drifted_count > 0:
        return 1
    return rc


if __name__ == "__main__":
    sys.exit(main())

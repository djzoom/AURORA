#!/usr/bin/env python3
"""scripts/add_nav_cells.py — Add prev/next navigation cells to every notebook.

Inserts two tagged markdown cells per lesson (idempotent — safe to re-run):
  ① RECAP   (cell index 1, after the H1 title): recap of previous lesson + link
  ② PREVIEW (last cell): preview of next lesson + link

Links are OS-independent relative paths from each notebook's own directory,
calculated with os.path.relpath.  They work in JupyterLab without any
server configuration.  Cells are tagged {"tags": ["nav"]} so the script
can find and replace them on subsequent runs without duplicating content.

Usage:
    python scripts/add_nav_cells.py            # update all 99 notebooks
    python scripts/add_nav_cells.py --dry-run  # show changes, no writes
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NB_DIR = REPO / "notebooks"
README = NB_DIR / "README.md"

NAV_TAG = "nav"


# ─── title helpers ────────────────────────────────────────────────────────────


def _parse_titles() -> dict[str, str]:
    """Extract {L01: 'title', ...} from notebooks/README.md table."""
    titles: dict[str, str] = {}
    for line in README.read_text(encoding="utf-8").splitlines():
        # Use ((?:[^|\\]|\\.)*) to skip \| escape sequences in the title column
        m = re.match(
            r"\|\s*L(\d{2})\s*[^|]*\|\s*((?:[^|\\]|\\.)*)\s*\|", line
        )
        if m:
            lnum = f"L{m.group(1)}"
            title = re.sub(r"[🎨*_`]", "", m.group(2)).strip()
            title = title.replace(r"\|", "|")  # unescape markdown table pipe
            titles[lnum] = title
    return titles


def _get_nb_map() -> dict[str, Path]:
    """Return {L01: Path(...), ...} for all L*.ipynb notebooks."""
    nb_map: dict[str, Path] = {}
    for nb in NB_DIR.rglob("L*.ipynb"):
        raw = nb.stem.split("_")[0].upper()
        if re.fullmatch(r"L\d{2}", raw):
            nb_map[raw] = nb
    return nb_map


def _short(title: str) -> str:
    """Topic keyword — text before ' — '."""
    part = title.split(" — ")[0] if " — " in title else title
    return part.strip()[:38]


def _hint(title: str, max_len: int = 52) -> str:
    """Content description — text after ' — ', truncated."""
    if " — " in title:
        h = title.split(" — ", 1)[1].strip()
    else:
        h = title.strip()
    return h[:max_len] + "…" if len(h) > max_len else h


# ─── cell builders ────────────────────────────────────────────────────────────


def _source(text: str) -> list[str]:
    """Convert a string to Jupyter cell source (each line ends with \\n except last)."""
    lines = text.split("\n")
    result = [line + "\n" for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result


def _nav_cell(content: str, cell_id: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {"tags": [NAV_TAG]},
        "source": _source(content),
    }


def _opening(
    lnum: str,
    titles: dict[str, str],
    nb_map: dict[str, Path],
    nb_path: Path,
) -> dict | None:
    """Recap cell placed after the title cell."""
    n = int(lnum[1:])
    if n <= 1:
        return None  # L01 has no previous lesson
    prev = f"L{n - 1:02d}"
    if prev not in titles:
        return None

    pt = titles[prev]
    ct = titles.get(lnum, lnum)

    if prev in nb_map:
        rel = os.path.relpath(str(nb_map[prev]), str(nb_path.parent))
        link = f"[{prev} · {_short(pt)}]({rel})"
    else:
        link = f"{prev} · {_short(pt)}"

    content = (
        f"← **上一课**　{link}\n"
        f"\n"
        f"> 上节课学习了 **{_short(pt)}**：{_hint(pt)}。  \n"
        f"> 本课将探讨 **{_short(ct)}**。"
    )
    return _nav_cell(content, f"nav-{lnum.lower()}-open")


def _closing(
    lnum: str,
    titles: dict[str, str],
    nb_map: dict[str, Path],
    nb_path: Path,
) -> dict | None:
    """Preview cell appended at the end of the notebook."""
    n = int(lnum[1:])
    nxt = f"L{n + 1:02d}"
    if nxt not in titles:
        return None  # L99 has no next lesson

    nt = titles[nxt]

    if nxt in nb_map:
        rel = os.path.relpath(str(nb_map[nxt]), str(nb_path.parent))
        link = f"[{nxt} · {_short(nt)}]({rel})"
    else:
        link = f"{nxt} · {_short(nt)}"

    content = (
        f"---\n"
        f"\n"
        f"→ **下一课**　{link}\n"
        f"\n"
        f"> 下节课将学习 **{_short(nt)}**：{_hint(nt)}。"
    )
    return _nav_cell(content, f"nav-{lnum.lower()}-clos")


# ─── notebook processing ──────────────────────────────────────────────────────


def _is_nav(cell: dict) -> bool:
    return NAV_TAG in cell.get("metadata", {}).get("tags", [])


def process(
    nb_path: Path,
    lnum: str,
    titles: dict[str, str],
    nb_map: dict[str, Path],
    dry_run: bool,
) -> bool:
    """Insert/replace nav cells.  Returns True if the notebook was changed."""
    data = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = data.get("cells", [])

    # Strip existing nav cells so we can re-insert cleanly
    clean = [c for c in cells if not _is_nav(c)]

    open_cell = _opening(lnum, titles, nb_map, nb_path)
    close_cell = _closing(lnum, titles, nb_map, nb_path)

    new_cells = list(clean)
    if open_cell:
        new_cells.insert(min(1, len(new_cells)), open_cell)
    if close_cell:
        new_cells.append(close_cell)

    # Compare nav cell content (not just IDs) to detect content updates
    old_nav = [tuple(c.get("source", [])) for c in cells if _is_nav(c)]
    new_nav = [tuple(c.get("source", [])) for c in new_cells if _is_nav(c)]
    if old_nav == new_nav:
        return False  # already up-to-date

    if dry_run:
        n_added = sum(1 for c in new_cells if _is_nav(c))
        n_removed = sum(1 for c in cells if _is_nav(c))
        print(f"  {lnum}  +{n_added} nav cells  (removed {n_removed} old)")
        return True

    data["cells"] = new_cells
    nb_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    return True


# ─── main ─────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would change without writing files"
    )
    args = parser.parse_args(argv)

    titles = _parse_titles()
    nb_map = _get_nb_map()
    ordered = sorted(nb_map.keys())

    print(f"{'─' * 55}")
    print(f"  add_nav_cells  ({len(ordered)} notebooks)")
    print(f"{'─' * 55}")

    changed = 0
    for lnum in ordered:
        if process(nb_map[lnum], lnum, titles, nb_map, args.dry_run):
            changed += 1
            if not args.dry_run:
                print(f"  ✓ {lnum}  {nb_map[lnum].name}")

    action = "Would modify" if args.dry_run else "Modified"
    print(f"\n{action} {changed}/{len(ordered)} notebooks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

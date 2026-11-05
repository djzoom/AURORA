"""Extract translatable text from a lesson notebook and apply a translation.

Workflow for producing ``L##_<name>.en.ipynb`` next to the Chinese original::

    python scripts/i18n/nb_i18n.py extract notebooks/0_foundation/L01_motivation.ipynb \
        > /tmp/L01.segments.json
    # translate the "source" fields in that JSON (keep "i", "type", "tags")
    python scripts/i18n/nb_i18n.py apply notebooks/0_foundation/L01_motivation.ipynb \
        /tmp/L01.segments.en.json

``extract`` emits every cell that contains Chinese text. ``apply`` writes the
English notebook and refuses to do so if a translated *code* cell differs from
the original in anything other than comments and string literals: the token
stream with COMMENT and STRING tokens masked must be identical. That keeps the
exercises, the check cells and the answer keys working exactly as before.
Code cells whose source changed have their stale outputs cleared.
"""

from __future__ import annotations

import io
import json
import re
import sys
import tokenize
from pathlib import Path

CJK = re.compile(r"[　-〿一-鿿＀-￯]")


def _src(cell: dict) -> str:
    s = cell.get("source", "")
    return "".join(s) if isinstance(s, list) else s


def _to_lines(text: str) -> list[str]:
    lines = text.splitlines(keepends=True)
    return lines


def _masked_tokens(code: str) -> list[tuple[int, str]]:
    """Token stream with comments dropped and string contents masked."""
    out = []
    # Notebook cells may contain IPython magics; treat those lines verbatim.
    lines = []
    for line in code.splitlines(keepends=True):
        lines.append("pass  # magic\n" if line.lstrip().startswith(("%", "!")) else line)
    try:
        toks = tokenize.generate_tokens(io.StringIO("".join(lines)).readline)
        for tok in toks:
            if tok.type in (tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE):
                continue
            if tok.type == tokenize.STRING:
                out.append((tok.type, "<STR>"))
            elif tok.type in (
                getattr(tokenize, "FSTRING_MIDDLE", -1),
                getattr(tokenize, "TSTRING_MIDDLE", -1),
            ):
                out.append((tok.type, "<FSTR>"))
            elif tok.type in (tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER):
                out.append((tok.type, ""))
            else:
                out.append((tok.type, tok.string))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return [(-1, code)]  # untokenisable: require exact equality
    # Collapse runs of masked f-string pieces so splitting one literal into
    # several is not mistaken for a code change.
    collapsed: list[tuple[int, str]] = []
    for t in out:
        if t[1] == "<FSTR>" and collapsed and collapsed[-1][1] == "<FSTR>":
            continue
        collapsed.append(t)
    return collapsed


def extract(nb_path: Path) -> list[dict]:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    segs = []
    for i, cell in enumerate(nb["cells"]):
        text = _src(cell)
        if not CJK.search(text):
            continue
        segs.append(
            {
                "i": i,
                "type": cell["cell_type"],
                "tags": cell.get("metadata", {}).get("tags", []),
                "source": text,
            }
        )
    return segs


def apply(nb_path: Path, seg_path: Path, out_path: Path | None = None) -> Path:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    segs = json.loads(seg_path.read_text(encoding="utf-8"))
    expected = {s["i"] for s in extract(nb_path)}
    got = {s["i"] for s in segs}
    problems = []
    if expected != got:
        problems.append(
            f"segment indices differ: missing {sorted(expected - got)}, "
            f"extra {sorted(got - expected)}"
        )
    for s in segs:
        i = s["i"]
        if i >= len(nb["cells"]):
            problems.append(f"cell {i}: out of range")
            continue
        cell = nb["cells"][i]
        if cell["cell_type"] != s["type"]:
            problems.append(f"cell {i}: type changed {cell['cell_type']} -> {s['type']}")
            continue
        old, new = _src(cell), s["source"]
        if s["type"] == "code" and _masked_tokens(old) != _masked_tokens(new):
            problems.append(
                f"cell {i}: code changed beyond comments/strings "
                f"(first line: {old.splitlines()[0][:60]!r})"
            )
            continue
        if s["type"] == "markdown" and old.count("```") != new.count("```"):
            problems.append(f"cell {i}: number of ``` fences changed")
        cell["source"] = _to_lines(new)
        if s["type"] == "code" and old != new:
            cell["outputs"] = []
            cell["execution_count"] = None
    if problems:
        raise SystemExit("REFUSED:\n  " + "\n  ".join(problems))

    nb.setdefault("metadata", {})["language_info"] = nb["metadata"].get(
        "language_info", {"name": "python"}
    )
    nb["metadata"]["aurora_translation"] = {"lang": "en", "source": nb_path.name}
    out_path = out_path or nb_path.with_name(nb_path.stem + ".en.ipynb")
    out_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    residual = []
    for i, cell in enumerate(nb["cells"]):
        n = len(CJK.findall(_src(cell)))
        if n:
            residual.append((i, cell["cell_type"], n))
    print(f"wrote {out_path}")
    if residual:
        print("residual Chinese characters (cell, type, count):", residual)
    return out_path


def main(argv: list[str]) -> None:
    if len(argv) >= 2 and argv[0] == "extract":
        print(json.dumps(extract(Path(argv[1])), ensure_ascii=False, indent=1))
    elif len(argv) >= 3 and argv[0] == "apply":
        out = Path(argv[3]) if len(argv) > 3 else None
        apply(Path(argv[1]), Path(argv[2]), out)
    else:
        print(__doc__)
        raise SystemExit(2)


if __name__ == "__main__":
    main(sys.argv[1:])

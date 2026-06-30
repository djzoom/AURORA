# AGENTS.md

Guidance for working in the Aurora repository.

## What Aurora is

A from-scratch audio-AI research system. The cardinal rule, repeated
everywhere: **no API wrappers.** When implementing a core capability, build the
algorithm — don't import a black box that already does it. The point of the
project is to demonstrate first-principles understanding for research-engineer
interviews.

Concretely, in the **Audio Core**: NumPy is allowed only as an array container
and for elementwise arithmetic. The FFT, STFT, mel filterbank, DCT, and MFCC
are implemented by hand and validated against `numpy.fft` / reference formulas
in the tests. Do **not** introduce librosa or `scipy.signal` for these.

## Layout

```
src/aurora/<core>/        one sub-package per architecture core (audio is built out)
tests/<core>/             mirrors the source tree; DSP is checked against numpy
scripts/                  runnable demos and validation tools
docs/current/adr/         architecture decision records
docs/current/blog/        technical write-ups (a deliverable, not an afterthought)
docs/current/audit/       per-lesson audit reports and professor review
docs/current/course/      learning plan, checklists, cloud GPU plan
```

## Conventions

- Python ≥ 3.10, `src/` layout, package importable as `aurora`.
- Tests: `pytest` (configured via `pyproject.toml`, `pythonpath = ["src"]`).
- Style: `black` (88 cols) + `ruff`. Run `make lint format test` before commit.
- Every from-scratch numeric routine gets a test that pins it to a reference.
- Keep the Audio Core dependency-light (numpy only); heavier stacks (torch,
  transformers, faiss) go behind optional-dependency extras per core.

## Workflow

```bash
make install                        # editable install + dev deps
make test                           # pytest
make demo                           # scripts/demo_audio.py
python scripts/validate_pipeline.py # notebook acceptance gate (JSON + syntax + pipeline)
```

## Roadmap

See `ROADMAP.md`. Each monthly milestone ships a working artifact, a blog post,
and (often) a reproduced paper. Update the checkboxes there as cores land.

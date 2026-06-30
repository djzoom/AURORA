# Contributing to Aurora

## The one rule

**No API wrappers.** If a core capability can be implemented, implement it.
NumPy-as-array-container is fine; importing a black box that *is* the feature
(librosa for STFT, an ElevenLabs call for TTS) is not. See
[`docs/current/adr/0001-no-api-wrappers.md`](docs/current/adr/0001-no-api-wrappers.md).

## Setup

```bash
pip install -e ".[dev]"
make test
```

## Before you commit

```bash
make format   # black
make lint     # ruff
make test     # pytest
```

## Standards

- Every from-scratch numeric routine ships with a test that pins it to a
  reference (e.g. `numpy.fft`) — correctness must be demonstrable.
- Keep the Audio Core importable with numpy only. Per-core heavy deps go in the
  matching `[project.optional-dependencies]` extra.
- Mirror the source tree under `tests/`.
- Update `ROADMAP.md` checkboxes when a milestone lands; a blog draft in
  `docs/current/blog/` is part of "done" for each milestone.
- Run `python scripts/validate_pipeline.py` before merging — it checks notebook
  JSON validity, Python syntax in all code cells, and audio pipeline shapes.

## Commits & branches

Small, focused commits with clear messages. Feature work happens on feature
branches; open a PR into the default branch.

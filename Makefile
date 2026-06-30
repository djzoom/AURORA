.PHONY: install test lint format demo check audit-drift nav-cells clean

install:
	pip install -e ".[dev,notebooks]"

test:
	python -m pytest

lint:
	ruff check src tests

format:
	black src tests scripts

demo:
	python scripts/demo_audio.py

# Full acceptance gate: JSON + syntax + audio pipeline + multi-core pipelines + structural checks
check:
	python scripts/validate_pipeline.py

# Course upgrade: show which notebooks have been edited since their audit doc was last updated
audit-drift:
	python scripts/audit_drift.py

# Regenerate prev/next navigation cells in all 99 notebooks (idempotent)
nav-cells:
	python scripts/add_nav_cells.py

clean:
	rm -rf .pytest_cache .ruff_cache **/__pycache__ *.egg-info build dist

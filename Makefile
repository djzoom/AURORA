.PHONY: install test lint format demo clean

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

clean:
	rm -rf .pytest_cache .ruff_cache **/__pycache__ *.egg-info build dist

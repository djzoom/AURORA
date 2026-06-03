#!/usr/bin/env bash
# Aurora SessionStart hook: make the repo ready to lint and test in a fresh
# Claude Code (web) session. Editable-install the package with dev deps so
# `pytest` and `ruff` work immediately. Kept quiet and non-fatal.
set -u

cd "$(dirname "$0")/../.." || exit 0

python3 -m pip install --quiet --disable-pip-version-check -e ".[dev]" \
  >/tmp/aurora-setup.log 2>&1 \
  && echo "Aurora: dev environment ready (pytest, ruff installed)." \
  || echo "Aurora: setup encountered an issue; see /tmp/aurora-setup.log"

exit 0

#!/usr/bin/env python3
"""scripts/log_ci_metrics.py — upload pytest JSON report to W&B.

Usage (from CI step):
    pip install pytest-json-report wandb
    pytest --json-report --json-report-file=report.json -v
    python scripts/log_ci_metrics.py

Environment variables:
    WANDB_API_KEY   — W&B API key (set as a repository secret in GitHub Actions)
    GITHUB_REF_NAME — current branch name (injected automatically by GH Actions)
"""
import json
import os
import sys


def main() -> None:
    report_path = "report.json"
    if not os.path.exists(report_path):
        print(f"ERROR: {report_path} not found — run pytest --json-report first")
        sys.exit(1)

    with open(report_path) as f:
        report = json.load(f)

    summary = report["summary"]
    pass_rate = summary["passed"] / max(summary["total"], 1)
    branch = os.getenv("GITHUB_REF_NAME", "unknown")

    print(f"CI summary  branch={branch}  "
          f"passed={summary['passed']}/{summary['total']}  "
          f"pass_rate={pass_rate:.1%}")

    try:
        import wandb  # type: ignore[import]
    except ImportError:
        print("wandb not installed — skipping W&B upload (non-fatal)")
        return

    run = wandb.init(
        project="aurora-ci",
        job_type="ci",
        config={"python": sys.version.split()[0], "branch": branch},
    )
    wandb.log({
        "tests/total": summary["total"],
        "tests/passed": summary["passed"],
        "tests/failed": summary.get("failed", 0),
        "pass_rate": pass_rate,
    })
    wandb.finish()
    print(f"W&B upload complete  run_id={run.id}")


if __name__ == "__main__":
    main()

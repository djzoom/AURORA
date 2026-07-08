#!/usr/bin/env python3
"""实时观察课程审核流水线的 TUI。

默认每秒刷新一次，展示：
  - progress.json 里的完成进度
  - run.log 的尾部日志
  - run.lock 的单实例锁状态
  - 可选 token 余额（环境变量或 token_budget.json）

用法：
  python3 scripts/sim_students_tui.py
  python3 scripts/sim_students_tui.py --interval 2 --tail 30
  python3 scripts/sim_students_tui.py --once
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from collections import deque
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import fcntl
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live

REPO = Path(__file__).resolve().parent.parent
BASE = REPO / "docs" / "current" / "audit" / "sim_students"
PROGRESS = BASE / "progress.json"
RUN_LOG = BASE / "run.log"
RUN_LOCK = BASE / "run.lock"
DEFAULT_TOKEN_FILE = BASE / "token_budget.json"

LIMIT_RE = re.compile(r"等待\s+(\d+)\s+分钟后重试")
TS_RE = re.compile(r"^\[(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\]\s+(.*)$")


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def tail_lines(path: Path, count: int) -> list[str]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            return list(deque((line.rstrip("\n") for line in f), maxlen=count))
    except FileNotFoundError:
        return []


def probe_lock(path: Path) -> tuple[bool, dict[str, Any]]:
    if not path.exists():
        return False, {}
    meta = read_json(path) or {}
    pid = meta.get("pid")
    if isinstance(pid, int) and pid > 0:
        try:
            os.kill(pid, 0)
            return True, meta
        except OSError:
            pass
    try:
        with path.open("a+", encoding="utf-8") as f:
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_SH | fcntl.LOCK_NB)
            except BlockingIOError:
                return True, meta
    except OSError:
        return bool(meta), meta
    return False, meta


def parse_timestamp(ts: str) -> datetime | None:
    try:
        current_year = datetime.now().year
        return datetime.strptime(f"{current_year}-{ts}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def extract_backoff(lines: list[str]) -> str | None:
    for line in reversed(lines):
        match = TS_RE.match(line)
        if not match:
            continue
        stamp, message = match.groups()
        wait_match = LIMIT_RE.search(message)
        if not wait_match:
            continue
        minutes = int(wait_match.group(1))
        ts = parse_timestamp(stamp)
        if ts is None:
            return f"{minutes} 分钟后重试"
        retry_at = ts + timedelta(minutes=minutes)
        return f"{minutes} 分钟后重试，预计 {retry_at:%m-%d %H:%M:%S}"
    return None


def summarize_token_budget() -> tuple[str, str]:
    """返回 (标题, 内容)。若无可用来源，则明确标注未接入。"""
    keys = {
        "remaining": None,
        "used": None,
        "limit": None,
        "source": None,
        "updated_at": None,
    }

    # 1) 环境变量注入
    env_remaining = os.environ.get("AUDIT_TOKEN_REMAINING")
    env_used = os.environ.get("AUDIT_TOKEN_USED")
    env_limit = os.environ.get("AUDIT_TOKEN_LIMIT")
    if any(v is not None for v in (env_remaining, env_used, env_limit)):
        keys["source"] = "env"
        keys["remaining"] = env_remaining
        keys["used"] = env_used
        keys["limit"] = env_limit
    else:
        # 2) 可选文件
        token_file = Path(os.environ.get("AUDIT_TOKEN_FILE", str(DEFAULT_TOKEN_FILE)))
        payload = read_json(token_file) if token_file.exists() else None
        if payload:
            keys["source"] = f"file:{token_file.name}"
            for name in ("remaining", "used", "limit", "updated_at"):
                if name in payload:
                    keys[name] = payload[name]

    if keys["source"] is None:
        return "Token", "未接入: 设 AUDIT_TOKEN_REMAINING / USED / LIMIT 或 token_budget.json"

    bits = [f"来源={keys['source']}"]
    if keys["remaining"] is not None:
        bits.append(f"剩余={keys['remaining']}")
    if keys["used"] is not None:
        bits.append(f"已用={keys['used']}")
    if keys["limit"] is not None:
        bits.append(f"总量={keys['limit']}")
    if keys["updated_at"]:
        bits.append(f"更新={keys['updated_at']}")
    return "Token", " | ".join(bits)


def progress_summary(state: dict[str, Any] | None) -> dict[str, Any]:
    lessons = state.get("lessons", []) if state else []
    done = list(dict.fromkeys(state.get("done", []))) if state else []
    in_progress = list(dict.fromkeys(state.get("in_progress", []))) if state else []
    done_count = len(done)
    total = len(lessons)
    remaining = max(total - done_count, 0)
    next_lessons = []
    if lessons:
        done_set = set(done)
        next_lessons = [Path(nb).stem.split("_")[0] for nb in lessons if Path(nb).stem.split("_")[0] not in done_set][:5]
    return {
        "done_count": done_count,
        "total": total,
        "remaining": remaining,
        "in_progress": in_progress,
        "next_lessons": next_lessons,
        "lessons": lessons,
    }


def render_dashboard(tail: int) -> Layout:
    state = read_json(PROGRESS)
    log_lines = tail_lines(RUN_LOG, tail)
    lock_active, lock_meta = probe_lock(RUN_LOCK)
    _, token_body = summarize_token_budget()
    progress = progress_summary(state)
    token_header = token_body if len(token_body) <= 96 else token_body[:93] + "..."

    total = progress["total"]
    done_count = progress["done_count"]
    in_progress = progress["in_progress"]
    remaining = progress["remaining"]
    pct = (done_count / total * 100.0) if total else 0.0
    width = 28
    filled = int(round(width * pct / 100.0))
    bar = "█" * filled + "░" * max(width - filled, 0)

    header = Panel(
        Align.left(
            Text.assemble(
                ("课程审核监控\n", "bold"),
                (f"完成 {done_count}/{total}  |  进行中 {len(in_progress)}  |  剩余 {remaining}\n", "white"),
                (f"[{bar}] {pct:5.1f}%\n", "cyan"),
                (f"进程锁: {'占用中' if lock_active else '空闲'}\n", "yellow" if lock_active else "green"),
                (f"Token: {token_header}", "magenta"),
            )
        ),
        title="Aurora Audit",
        border_style="cyan",
    )

    progress_table = Table.grid(expand=True)
    progress_table.add_column(ratio=1)
    progress_table.add_column(ratio=3)
    progress_table.add_row("已完成", f"{done_count}")
    progress_table.add_row("进行中", ", ".join(in_progress) if in_progress else "无")
    progress_table.add_row("下一批", ", ".join(progress["next_lessons"]) if progress["next_lessons"] else "无")
    progress_table.add_row("刷新", f"{datetime.now():%Y-%m-%d %H:%M:%S}")

    lock_table = Table.grid(expand=True)
    lock_table.add_column(ratio=1)
    lock_table.add_column(ratio=3)
    lock_table.add_row("状态", "运行中" if lock_active else "空闲")
    lock_table.add_row("PID", str(lock_meta.get("pid", "n/a")))
    lock_table.add_row("开始", str(lock_meta.get("started_at", "n/a")))
    lock_table.add_row("主机", str(lock_meta.get("host", "n/a")))
    lock_table.add_row("并行", str(lock_meta.get("lesson_parallel", "n/a")))
    lock_table.add_row("模型", ", ".join(
        s for s in [
            f"student={lock_meta.get('student_model')}" if lock_meta.get("student_model") else None,
            f"prof_r1={lock_meta.get('prof_model_r1')}" if lock_meta.get("prof_model_r1") else None,
            f"prof_r2={lock_meta.get('prof_model')}" if lock_meta.get("prof_model") else None,
        ] if s
    ) or "n/a")
    lock_table.add_row("限额等待", extract_backoff(log_lines) or "无")
    left = Group(
        Panel(progress_table, title="进度", border_style="green"),
        Panel(lock_table, title="调度", border_style="yellow"),
    )

    log_text = Text()
    if log_lines:
        for line in log_lines:
            log_text.append(line)
            log_text.append("\n")
    else:
        log_text.append("暂无日志")

    right = Panel(log_text, title=f"run.log 尾部（{len(log_lines)} 行）", border_style="white")

    layout = Layout()
    layout.split_column(
        Layout(header, size=7),
        Layout(name="body"),
    )
    layout["body"].split_row(
        Layout(left, ratio=2),
        Layout(right, ratio=3),
    )
    return layout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interval", type=float, default=1.0, help="刷新间隔（秒）")
    parser.add_argument("--tail", type=int, default=20, help="run.log 尾部行数")
    parser.add_argument("--once", action="store_true", help="只渲染一次后退出")
    args = parser.parse_args()

    console = Console()

    if args.once:
        console.print(render_dashboard(args.tail))
        return 0

    try:
        with Live(render_dashboard(args.tail), console=console, screen=True, auto_refresh=False) as live:
            while True:
                live.update(render_dashboard(args.tail), refresh=True)
                time.sleep(args.interval)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""模拟学生课程审核流水线（无头版，不占用 Fable 5）。

每课流程：3 位初学者学生（Haiku）并行学习并产出日志 → 教授（Sonnet）修订
notebook（只增不删）→ 质检（Haiku）逐条复核，未解决则教授再修（封顶 2 轮）。

断点续传：以文件为准 ——
  docs/current/audit/sim_students/progress.json      课程清单 + 完成状态
  docs/current/audit/sim_students/run.lock           进程级单实例锁
  docs/current/audit/sim_students/L**/{学生}.md      已存在则跳过该学生
  docs/current/audit/sim_students/L**/.prof_r{n}     教授第 n 轮已完成
  docs/current/audit/sim_students/L**/verify_r{n}.json 复核结论
任意时刻中断，重新启动即从断点继续。

模型可用环境变量覆盖：STUDENT_MODEL / PROF_MODEL / VERIFY_MODEL
"""
import atexit
import json
import os
import re
import subprocess
import sys
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import fcntl

ROOT = "/Users/z/AURORA"
BASE = f"{ROOT}/docs/current/audit/sim_students"
PROGRESS = f"{BASE}/progress.json"
RUN_LOG = f"{BASE}/run.log"
RUN_LOCK = f"{BASE}/run.lock"

STUDENT_MODEL = os.environ.get("STUDENT_MODEL", "claude-haiku-4-5-20251001")
# 省额度策略：教授第 1 轮用 Haiku；仅当复核不通过、进入第 2 轮时升级 Sonnet 补刀
PROF_MODEL_R1 = os.environ.get("PROF_MODEL_R1", "claude-haiku-4-5-20251001")
PROF_MODEL = os.environ.get("PROF_MODEL", "claude-sonnet-5")
VERIFY_MODEL = os.environ.get("VERIFY_MODEL", STUDENT_MODEL)
MAX_ROUNDS = 2
LIMIT_WAIT_S = 60 * 60          # 撞到用量限额时的等待间隔（每小时重试）
MAX_LIMIT_RETRIES = 24          # 最多等 24 次（约 24 小时）后放弃本步
LESSON_PARALLEL = int(os.environ.get("LESSON_PARALLEL", "4"))  # 同时审核几课

_log_lock = threading.Lock()    # 保护 run.log 写入
_state_lock = threading.RLock() # 保护 progress.json 与 in_progress/done 更新
_run_lock_fd = None

LOCK_EXIT_CODE = 3

STUDENTS = [
    ("xiaoyu", "小雨", "文科背景（历史系毕业），对数学符号有畏惧感，看到希腊字母和下标就紧张，"
     "需要生活化类比才能理解概念。Python 只会 print、变量、循环、列表。"
     "同时是视觉型学习者，纯文字公式看不进去，需要图形或比喻。"),
    ("linda", "琳达", "自学过 Python 爬虫的运营，代码读写没问题，但完全不懂数学推导，"
     "一遇到连续两行以上的公式推导就想跳过，总想知道“这段代码到底在干什么、为什么非得这么写”。"),
    ("laochen", "老陈", "35 岁转行的前厨师，高中理科毕业但遗忘大半，容易混淆相似概念"
     "（sin/cos、行与列、角度与弧度）。学习极其认真但速度慢，每个“为什么”都要刨根问底，"
     "最反感教材里“显然”“易得”“不难看出”这类词。Python 基础。"),
]


def atomic_write_text(path, content):
    tmp = f"{path}.tmp.{os.getpid()}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def atomic_write_json(path, obj):
    atomic_write_text(path, json.dumps(obj, ensure_ascii=False, indent=1) + "\n")


def acquire_run_lock():
    """单实例门闩：旧进程还在跑时，新实例直接退出。"""
    global _run_lock_fd
    os.makedirs(BASE, exist_ok=True)
    fd = open(RUN_LOCK, "a+", encoding="utf-8")
    try:
        fcntl.flock(fd.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        fd.seek(0)
        raw = fd.read().strip()
        details = ""
        if raw:
            try:
                meta = json.loads(raw)
                parts = []
                for key in ("pid", "started_at", "host", "lesson_parallel"):
                    if key in meta and meta[key] not in (None, ""):
                        parts.append(f"{key}={meta[key]}")
                if parts:
                    details = "\n锁信息: " + ", ".join(parts)
            except json.JSONDecodeError:
                details = f"\n锁内容: {raw}"
        print("检测到另一个课程审核实例正在运行，当前实例已退出以避免并发写入。"
              f"{details}", file=sys.stderr)
        fd.close()
        raise SystemExit(LOCK_EXIT_CODE)

    meta = {
        "pid": os.getpid(),
        "started_at": f"{datetime.now():%Y-%m-%d %H:%M:%S}",
        "host": socket.gethostname(),
        "lesson_parallel": LESSON_PARALLEL,
        "student_model": STUDENT_MODEL,
        "prof_model_r1": PROF_MODEL_R1,
        "prof_model": PROF_MODEL,
        "verify_model": VERIFY_MODEL,
    }
    fd.seek(0)
    fd.truncate()
    fd.write(json.dumps(meta, ensure_ascii=False, indent=1) + "\n")
    fd.flush()
    os.fsync(fd.fileno())
    _run_lock_fd = fd


def release_run_lock():
    global _run_lock_fd
    if _run_lock_fd is None:
        return
    try:
        fcntl.flock(_run_lock_fd.fileno(), fcntl.LOCK_UN)
    except OSError:
        pass
    try:
        _run_lock_fd.close()
    except OSError:
        pass
    _run_lock_fd = None


atexit.register(release_run_lock)


def log(msg):
    line = f"[{datetime.now():%m-%d %H:%M:%S}] {msg}"
    with _log_lock:
        print(line, flush=True)
        with open(RUN_LOG, "a") as f:
            f.write(line + "\n")


def lesson_log(lesson, msg):
    log(f"[{lesson}] {msg}")


def run_claude(prompt, model, allowed_tools, max_turns, timeout=3600):
    """跑一次无头 claude；撞限额自动等待重试。返回 stdout 文本，失败返回 None。"""
    cmd = [
        "claude", "-p", "--model", model,
        "--permission-mode", "acceptEdits",
        "--max-turns", str(max_turns),
        "--allowedTools", *allowed_tools,
    ]
    for attempt in range(MAX_LIMIT_RETRIES):
        try:
            r = subprocess.run(cmd, input=prompt, text=True, capture_output=True,
                               timeout=timeout, cwd=ROOT)
        except subprocess.TimeoutExpired:
            log(f"  超时（>{timeout}s），重试一次")
            continue
        out = (r.stdout or "") + (r.stderr or "")
        if r.returncode == 0 and r.stdout and r.stdout.strip():
            return r.stdout
        if "limit" in out.lower() or "rate" in out.lower():
            log(f"  疑似用量限额（第 {attempt + 1} 次），等待 {LIMIT_WAIT_S // 60} 分钟后重试…")
            time.sleep(LIMIT_WAIT_S)
            continue
        log(f"  claude 调用失败 rc={r.returncode}: {out[:300]}")
        time.sleep(30)
    return None


def student_prompt(nb, name, persona, lesson):
    return f"""你要扮演一位真实的初学者学生“{name}”：{persona}

任务：从头到尾学习这份 Jupyter 课程 notebook：{nb}

要求：
1. 用 Read 完整读这个 notebook，逐个 cell 认真“学”：读讲解文字、跟着推演每个公式、做课后练习/思考题。为节省开销，不要实际运行代码，靠读代码和心算理解；实在无法靠读判断的地方就作为“问题”记下来。
2. 你必须保持人设水平：只有高中数学 + Python 基础。凡是超出这个水平、课程又没有给出铺垫解释的地方，对你就是“问题”。不要用你实际拥有的知识替课程圆场。
3. 你的最终回复必须是且仅是一份 Markdown 学习日志（不要写文件，直接输出），格式：
   # {name} — {lesson} 学习日志
   ## 我理解了什么（简要，3 行以内）
   ## 遇到的困难和问题
   每条问题一小节，标明类别【理解/推演/计算/实践/解答】，写清楚：卡在 notebook 的哪个位置（引用原文关键短语）、具体哪里没看懂/推不出/算不对/跑不通、希望课程补充什么样的解释或铺垫。
   问题要具体、可操作，写得紧凑。真实初学者每课通常提出 2~5 条实质问题；如果这课确实通俗易懂，少提也可以，实事求是。"""


def prof_prompt(nb, ldir, unresolved, rnd):
    note = ""
    if unresolved:
        note = ("\n注意：这是第 %d 轮修订。上一轮复核发现以下问题仍未解决，必须优先处理：\n%s"
                % (rnd, "\n".join("- " + u for u in unresolved)))
    return f"""你是这门课的教授。3 位只有高中数学 + Python 基础的学生学完了 {nb}，学习日志在 {ldir}/ 目录下（学生名 .md 文件，忽略 professor_review.md 和 verify_*.json）。

任务：读全部日志和 notebook 本身，修订这个 notebook，让每一条学生问题都在课程中得到解答，使任何初学者都能更好理解。{note}

修订规则（必须遵守）：
1. 只增加、不删减：原有内容全部保留，通过“增加铺垫、生活化类比、精细分步描述、逐步推演、可运行的演示代码、练习提示”来解决问题。可在学生卡住的位置之前插入新的 markdown/code cell，或在原 cell 内追加内容（保留原文只做扩充）。
2. 写作风格：科普风——先问题/类比/故事，再公式；每个公式出现前必须有直白语言铺垫；严禁“显然”“易得”“不难看出”。
3. 针对性：每条学生问题都要有对应改动，改在学生卡住的位置附近，不要把所有补充堆在开头或结尾。
4. 用 NotebookEdit 编辑（notebook 路径 {nb}）。新增代码 cell 必须真的可运行，依赖前面 cell 变量时注意插入顺序。
5. 改完后运行 python3 -c "import nbformat; nbformat.read('{nb}', as_version=4)" 校验合法性；失败必须修复。
6. 把修订说明写入（追加到）{ldir}/professor_review.md：逐条列出“学生问题 → 改动内容与位置”。
最终回复：一行总结（处理了几条问题、改了哪些位置）。"""


def verify_prompt(nb, ldir):
    return f"""你是课程质检员。逐条核对 {ldir}/ 下 3 份学生日志（学生名 .md，忽略 professor_review.md 和 verify_*.json）中提出的每一个问题：现在的 notebook {nb} 是否已通过新增的铺垫/类比/解释/示例真正解决了它？判断标准：一个只有高中数学 + Python 基础的学生按顺序读改后的课程，能否在卡点处得到透彻解答（不是敷衍一句带过）。
同时运行 python3 -c "import nbformat; nbformat.read('{nb}', as_version=4)" 确认文件合法。
最终回复格式（严格遵守）：
先逐条列出仍未解决的问题（哪位学生的哪个问题、为什么还不算解决、建议怎么补），每条以“- ”开头；如果全部解决则不列。
最后单独一行输出：ALL_RESOLVED: YES 或 ALL_RESOLVED: NO"""


STUDENT_TOOLS = ["Read", "Bash(python3:*)", "Bash(python:*)"]
PROF_TOOLS = ["Read", "NotebookEdit", "Edit", "Write", "Bash(python3:*)", "Bash(python:*)"]
VERIFY_TOOLS = ["Read", "Bash(python3:*)", "Bash(python:*)"]


def do_student(nb, lesson, ldir, sid, name, persona):
    path = f"{ldir}/{sid}.md"
    if os.path.exists(path) and os.path.getsize(path) > 200:
        lesson_log(lesson, f"{name}: 日志已存在，跳过")
        return True
    lesson_log(lesson, f"{name}: 开始学习")
    out = run_claude(student_prompt(nb, name, persona, lesson),
                     STUDENT_MODEL, STUDENT_TOOLS, max_turns=25, timeout=2400)
    if not out:
        lesson_log(lesson, f"{name}: 失败")
        return False
    atomic_write_text(path, out)
    lesson_log(lesson, f"{name}: 日志完成（{len(out)} 字符）")
    return True


def do_lesson(nb):
    lesson = os.path.basename(nb).split("_")[0]
    ldir = f"{BASE}/{lesson}"
    os.makedirs(ldir, exist_ok=True)
    lesson_log(lesson, f"== 开始：{nb}")

    with ThreadPoolExecutor(3) as ex:
        oks = list(ex.map(lambda s: do_student(nb, lesson, ldir, *s), STUDENTS))
    if not all(oks):
        lesson_log(lesson, "学生阶段未完成，留待下次续跑")
        return False

    for rnd in range(1, MAX_ROUNDS + 1):
        prof_marker = f"{ldir}/.prof_r{rnd}"
        verify_file = f"{ldir}/verify_r{rnd}.json"
        unresolved = None
        if rnd > 1:
            prev = json.load(open(f"{ldir}/verify_r{rnd - 1}.json"))
            if prev["all_resolved"]:
                break
            unresolved = prev["unresolved"]

        if not os.path.exists(prof_marker):
            prof_model = PROF_MODEL_R1 if rnd == 1 else PROF_MODEL
            lesson_log(lesson, f"教授第 {rnd} 轮修订…（{prof_model}）")
            out = run_claude(prof_prompt(nb, ldir, unresolved, rnd),
                             prof_model, PROF_TOOLS, max_turns=80, timeout=3600)
            if not out:
                lesson_log(lesson, f"教授第 {rnd} 轮失败，留待下次续跑")
                return False
            atomic_write_text(prof_marker, out)
            lesson_log(lesson, f"教授第 {rnd} 轮完成")

        if not os.path.exists(verify_file):
            lesson_log(lesson, f"复核第 {rnd} 轮…")
            out = run_claude(verify_prompt(nb, ldir),
                             VERIFY_MODEL, VERIFY_TOOLS, max_turns=30, timeout=2400)
            if not out:
                lesson_log(lesson, f"复核第 {rnd} 轮失败，留待下次续跑")
                return False
            resolved = bool(re.search(r"ALL_RESOLVED:\s*YES", out))
            unresolved_items = [l.strip()[2:] for l in out.splitlines()
                                if l.strip().startswith("- ")]
            atomic_write_json(verify_file,
                             {"all_resolved": resolved, "unresolved": unresolved_items})
            lesson_log(lesson, f"复核第 {rnd} 轮：{'全部解决' if resolved else f'{len(unresolved_items)} 条未解决'}")

        if json.load(open(verify_file))["all_resolved"]:
            break

    return True


def main():
    acquire_run_lock()
    state = json.load(open(PROGRESS))
    done = set(state["done"])
    todo = [nb for nb in state["lessons"]
            if os.path.basename(nb).split("_")[0] not in done]
    log(f"启动：已完成 {len(done)} 课，剩余 {len(todo)} 课，{LESSON_PARALLEL} 课并行"
        f"（学生={STUDENT_MODEL} 教授R1={PROF_MODEL_R1} 教授R2={PROF_MODEL} 复核={VERIFY_MODEL}）")
    state["in_progress"] = []

    def save_state():
        with _state_lock:
            atomic_write_json(PROGRESS, state)

    def work(nb):
        lesson = os.path.basename(nb).split("_")[0]
        ok = False
        with _state_lock:
            if lesson not in state["in_progress"]:
                state["in_progress"].append(lesson)
            save_state()
        try:
            ok = do_lesson(nb)
            return lesson, ok
        except Exception as exc:
            lesson_log(lesson, f"未处理异常：{exc!r}")
            return lesson, False
        finally:
            with _state_lock:
                if ok:
                    state["done"] = list(dict.fromkeys(state["done"] + [lesson]))
                state["in_progress"] = [item for item in state["in_progress"] if item != lesson]
                save_state()
            if ok:
                lesson_log(lesson, "== 完成")

    save_state()

    failed = []
    with ThreadPoolExecutor(LESSON_PARALLEL) as ex:
        for lesson, ok in ex.map(work, todo):
            if not ok:
                failed.append(lesson)

    if failed:
        log(f"未完成课程：{failed}（多为限额），进度已保存，重新启动即可续跑。")
        sys.exit(1)
    log("全部 99 课审核修订完成 ✅")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the Aurora knowledge-graph indexes from course data.

Generates, under docs/current/obsidian/:
  lessons/L##.md   — per-lesson reverse index (Introduced / Prerequisites / Used-later)
  concepts/_lifecycle.md — every term's first-appearance → all-uses timeline (Layer 2/10)

Reproducible: re-run after editing notebooks to refresh the graph.
"""
from __future__ import annotations
import json, re, glob, os
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = sorted(glob.glob(os.path.join(REPO, "notebooks/*/L*.ipynb")), key=lambda p: int(re.search(r"L(\d\d)", os.path.basename(p)).group(1)))
OBS = os.path.join(REPO, "docs/current/obsidian")

# --- term dictionary {zh: (en, abbr)} from terms.md (single source of truth) ---
term = {}
for line in open(os.path.join(OBS, "terms.md"), encoding="utf-8"):
    if line.startswith("|"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and c[0] not in ("中文", "------") and not c[0].startswith("---"):
            zh, en, ab = c[0], c[1], c[2]
            if zh and en and en not in ("英文",):
                term.setdefault(zh, (en, ab if ab and ab != "—" else ""))

def lnum(p): return re.search(r"(L\d\d)", os.path.basename(p)).group(1)
def title(nb):
    for cc in nb["cells"]:
        if cc["cell_type"] == "markdown":
            m = re.search(r"^#\s+(.+)$", "".join(cc["source"]), re.M)
            if m: return re.sub(r"^第\d+课\s*·?\s*", "", m.group(1)).strip()
    return ""

# --- scan: term -> ordered [L##] where it appears in prose; lesson -> title ---
appears = defaultdict(list)     # zh -> [L## ...] (lesson order)
titles = {}
lesson_terms = defaultdict(list)  # L## -> [zh ...]
for p in NB:
    L = lnum(p); nb = json.load(open(p)); titles[L] = title(nb)
    md = "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown")
    for zh in term:
        if zh in md:
            appears[zh].append(L)
            lesson_terms[L].append(zh)

first = {zh: ls[0] for zh, ls in appears.items()}  # first appearance lesson

os.makedirs(os.path.join(OBS, "lessons"), exist_ok=True)
os.makedirs(os.path.join(OBS, "concepts"), exist_ok=True)

def fmt(zh):
    en, ab = term[zh]
    return f"[[concepts/{en.replace('/', '-')}|{zh}（{en}{('，'+ab) if ab else ''}）]]"

# --- lessons/L##.md : reverse index ---
allL = sorted(titles)
for L in allL:
    intro = [zh for zh in lesson_terms[L] if first[zh] == L]
    prereq = [zh for zh in lesson_terms[L] if first[zh] != L]
    with open(os.path.join(OBS, "lessons", f"{L}.md"), "w", encoding="utf-8") as f:
        f.write(f"---\ntags: [aurora, lesson-index]\n---\n\n# {L}｜{titles[L]}\n\n")
        f.write("[[../INDEX|← Master Index]]\n\n")
        f.write("> 本课涉及的术语反查索引（自动生成）。\n\n")
        f.write("## 📥 本课首次引入 (Introduced)\n")
        f.write(("\n".join(f"- {fmt(z)}" for z in intro) or "- （无新术语）") + "\n\n")
        f.write("## 🎒 前置术语 (Prerequisites，更早引入)\n")
        f.write(("\n".join(f"- {fmt(z)}（首次 [[{first[z]}]]）" for z in prereq) or "- （无）") + "\n\n")
        f.write("## ➡️ 后续再用 (本课引入、之后复现的术语)\n")
        later = [(z, [x for x in appears[z] if x > L]) for z in intro]
        later = [(z, ls) for z, ls in later if ls]
        f.write(("\n".join(f"- {fmt(z)} → 再现于 {', '.join('[['+x+']]' for x in ls)}" for z, ls in later) or "- （无）") + "\n")

# --- concepts/_lifecycle.md : term lifecycle timeline (Layer 2/10) ---
with open(os.path.join(OBS, "concepts", "_lifecycle.md"), "w", encoding="utf-8") as f:
    f.write("---\ntags: [aurora, concept-lifecycle, MOC]\n---\n\n# 术语生命周期总表 (Concept Lifecycle)\n\n")
    f.write("[[../INDEX|← Master Index]]\n\n")
    f.write("> 每个术语的「第一次出现 → 一路复现 → 最终应用」时间线（自动生成）。\n")
    f.write("> 学生一看就懂：**今天难，是因为以后它还会出现很多次。**\n\n")
    f.write("| 术语 | 首次 | 全部出现 | 出现次数 |\n|---|---|---|---|\n")
    for zh in sorted(appears, key=lambda z: (appears[z][0], -len(appears[z]))):
        ls = appears[zh]; en, ab = term[zh]
        f.write(f"| {zh}（{en}） | [[{ls[0]}]] | {' → '.join('[['+x+']]' for x in ls)} | {len(ls)} |\n")

# --- interview/ aggregation (derived from the concept pages) ---
COMPANIES = ["OpenAI", "Google", "DeepMind", "Meta", "Apple", "Apple-Audio", "NVIDIA",
             "Anthropic", "ElevenLabs", "HuggingFace", "Microsoft", "Adobe", "Suno",
             "Cartesia", "AssemblyAI", "Hume"]
cpages = []
for f in glob.glob(os.path.join(OBS, "concepts", "*.md")):
    name = os.path.basename(f)[:-3]
    if name.startswith("_"):
        continue
    txt = open(f, encoding="utf-8").read()
    fm = txt.split("---", 2)[1] if txt.startswith("---") else ""
    def g(k):
        m = re.search(rf"^{k}:\s*(.+)$", fm, re.M); return m.group(1).strip() if m else ""
    stars = g("whiteboard").count("★")
    m1 = re.search(r"⚡ 一句话[^：]*：(.+)", txt)
    one = (m1.group(1).strip() if m1 else "").replace("|", "/")
    tags = set(re.findall(r"#([A-Za-z\-]+)", txt))
    cpages.append(dict(name=name, stars=stars, domain=g("domain"), fs=g("first_seen"),
                       mas=g("mastered"), one=one, comps=[c for c in COMPANIES if c in tags]))
os.makedirs(os.path.join(OBS, "interview"), exist_ok=True)

cpages.sort(key=lambda c: (-c["stars"], c["domain"], c["name"]))
with open(os.path.join(OBS, "interview", "Audio-AI.md"), "w", encoding="utf-8") as f:
    f.write("---\ntags: [aurora, interview, MOC]\n---\n\n# 🎧 Audio AI 面试冲刺图 (Interview Sprint Map)\n\n")
    f.write("[[../INDEX|← Master Index]]\n\n> 按「白板要求」优先级排的面试冲刺清单（自动生成自 concept 页）。\n")
    f.write("> ★★★★★ = 面试必须闭卷推导 + 手写代码；先啃这些。\n\n")
    for lvl, label in [(5, "★★★★★ 必推导（最高优先，先啃）"), (4, "★★★★ 必掌握"), (3, "★★★ 理解即可")]:
        rows = [c for c in cpages if c["stars"] == lvl]
        if not rows: continue
        f.write(f"## {label}\n\n| 概念 | 一句话 | 首次→掌握 | 相关公司 |\n|---|---|---|---|\n")
        for c in rows:
            f.write(f"| [[../concepts/{c['name']}\\|{c['name']}]] | {c['one']} | [[{c['fs']}]]→[[{c['mas']}]] | {' '.join('#'+x for x in c['comps'])} |\n")
        f.write("\n")

with open(os.path.join(OBS, "interview", "By-Company.md"), "w", encoding="utf-8") as f:
    f.write("---\ntags: [aurora, interview, MOC]\n---\n\n# 按公司分组的面试知识图 (By Company)\n\n[[../INDEX|← Master Index]]\n\n")
    for comp in COMPANIES:
        rows = sorted([c for c in cpages if comp in c["comps"]], key=lambda c: -c["stars"])
        if not rows: continue
        f.write(f"## {comp}（{len(rows)}）\n")
        for c in rows:
            f.write(f"- {'★'*c['stars']} [[../concepts/{c['name']}\\|{c['name']}]]\n")
        f.write("\n")

print(f"interview/ built: {len(cpages)} concept pages aggregated")
print(f"terms={len(term)}  lessons={len(allL)}  lessons/ + concepts/_lifecycle.md written")
print("top-reused terms:")
for zh in sorted(appears, key=lambda z: -len(appears[z]))[:8]:
    print(f"  {zh}: {len(appears[zh])} lessons, first {appears[zh][0]}")

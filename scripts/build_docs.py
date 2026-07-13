#!/usr/bin/env python3
"""把内部常用 markdown 文档导出成两版:pages(HTML) + PDF(中文)。

- HTML:pandoc 渲染成带样式的独立网页(浏览器用系统 CJK 字体,排版最好)。
- PDF :python-markdown → 简单 HTML → xhtml2pdf(reportlab 内置 STSong-Light 渲染中文)。
        本机无 LaTeX / weasyprint / chromium,xhtml2pdf 是自带 CJK、纯 pip 的可靠路径。

输出到 docs/current/_dist/{html,pdf}/ + 一个 index.html 汇总页。
    python scripts/build_docs.py

依赖:pandoc(系统)、python 包 markdown + xhtml2pdf。
"""
from __future__ import annotations
import os, subprocess, tempfile, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(REPO, "docs/current/_dist")
HTML_DIR, PDF_DIR = os.path.join(DIST, "html"), os.path.join(DIST, "pdf")

# (源相对路径, 展示标题, 是否本地-only 不提交)
DOCS = [
    ("docs/current/OPENNESS.md",                            "开放原则", False),
    ("docs/current/video/00_onboarding_trailer_script.md",  "引导片脚本(装环境+做完L01)", False),
    ("docs/current/video/01_shot_list.md",                  "逐镜头拍摄清单", False),
    ("docs/current/video/02_trailer_90s_script.md",         "90 秒营销预告脚本", False),
    ("docs/current/video/03_L01_lecture_transcript.md",     "L01 教学逐字稿", False),
    ("DEV_SUMMARY_2026-07-03.md",                           "开发总结(内部·本地)", True),
]

HTML_CSS = """
body{max-width:880px;margin:2rem auto;padding:0 1.2rem;
 font-family:-apple-system,"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif;
 line-height:1.65;color:#1a1a1a}
h1{border-bottom:2px solid #eee;padding-bottom:.3rem} h1,h2,h3{line-height:1.3}
code,pre{font-family:"SF Mono",Menlo,Consolas,monospace}
pre{background:#f6f8fa;padding:1rem;overflow:auto;border-radius:6px;font-size:.85rem}
code{background:#f0f0f0;padding:.1em .3em;border-radius:3px;font-size:.9em}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1rem 0}
th,td{border:1px solid #ddd;padding:.4rem .6rem;text-align:left} th{background:#f6f8fa}
blockquote{border-left:4px solid #ddd;margin:1rem 0;padding:.2rem 1rem;color:#555}
a{color:#0969da} img{max-width:100%}
"""

# Arial Unicode(单文件 TTF,含 拉丁+CJK+制表符+正常空格)——避免 STSong-Light 把
# <pre> 里的 nbsp 渲染成 ♂ 的乱码;字形完整、无乱码(代价:非等宽,ASCII 图对齐略松)。
_CJK_TTF = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
PDF_CSS = f"""
@font-face {{ font-family:"AU"; src:url("{_CJK_TTF}"); }}
@page{{size:A4;margin:1.6cm}}
body{{font-family:"AU";font-size:10pt;line-height:1.5;color:#222}}
h1{{font-size:17pt;color:#111}} h2{{font-size:13.5pt}} h3{{font-size:11.5pt}}
h1,h2,h3,h4{{font-family:"AU"}}
pre{{background:#f5f5f5;padding:6pt;font-family:"AU";font-size:8.5pt}}
code{{font-family:"AU";background:#f0f0f0;font-size:8.5pt}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #999;padding:3pt;font-size:8.5pt}} th{{background:#eee}}
blockquote{{color:#555;margin-left:8pt;border-left:2pt solid #ccc;padding-left:8pt}}
"""


def build_html(src: str, title: str, out: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as h:
        h.write(f"<style>{HTML_CSS}</style>")
        header = h.name
    try:
        subprocess.run(["pandoc", "-s", "-f", "gfm", "-t", "html5",
                        "--metadata", f"title={title}", "-H", header,
                        "-o", out, src], check=True, cwd=REPO)
    finally:
        os.unlink(header)


def build_pdf(src: str, title: str, out: str) -> None:
    import markdown
    from xhtml2pdf import pisa
    text = open(os.path.join(REPO, src), encoding="utf-8").read()
    body = markdown.markdown(text, extensions=["extra", "sane_lists", "toc"])
    html = (f'<html><head><meta charset="utf-8"><style>{PDF_CSS}</style></head>'
            f'<body><h1>{title}</h1>{body}</body></html>')
    with open(out, "wb") as f:
        status = pisa.CreatePDF(html, dest=f, encoding="utf-8")
    if status.err:
        raise RuntimeError(f"xhtml2pdf 报错({status.err})")


def main() -> None:
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)
    rows = []
    for src, title, local in DOCS:
        stem = os.path.splitext(os.path.basename(src))[0]
        h_out = os.path.join(HTML_DIR, stem + ".html")
        p_out = os.path.join(PDF_DIR, stem + ".pdf")
        if not os.path.exists(os.path.join(REPO, src)):
            print(f"  ⚠️  跳过(源不存在):{src}"); continue
        ok_h = ok_p = True
        try:
            build_html(src, title, h_out)
        except Exception as e:
            ok_h = False; print(f"  ✗ HTML {stem}: {e}")
        try:
            build_pdf(src, title, p_out)
        except Exception as e:
            ok_p = False; print(f"  ✗ PDF  {stem}: {e}")
        tag = " [本地-only]" if local else ""
        print(f"  {'✓' if ok_h and ok_p else '△'} {stem}{tag}"
              f"  html={os.path.getsize(h_out) if ok_h else 0}B"
              f"  pdf={os.path.getsize(p_out) if ok_p else 0}B")
        rows.append((title, stem, local, ok_h, ok_p))

    # index.html
    lis = "\n".join(
        f'<tr><td>{t}{" <em>(本地)</em>" if loc else ""}</td>'
        f'<td>{"<a href=html/"+s+".html>网页</a>" if h else "—"}</td>'
        f'<td>{"<a href=pdf/"+s+".pdf>PDF</a>" if p else "—"}</td></tr>'
        for t, s, loc, h, p in rows)
    idx = (f"<style>{HTML_CSS}</style><h1>Aurora · 商业与内部文档</h1>"
           f"<p>pages(HTML)+ PDF 两版导出。运行 <code>python scripts/build_docs.py</code> 重新生成。</p>"
           f"<table><tr><th>文档</th><th>网页</th><th>PDF</th></tr>{lis}</table>")
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(idx)
    print(f"\n✅ 导出完成 → {os.path.relpath(DIST, REPO)}/(index.html + html/ + pdf/)")


if __name__ == "__main__":
    main()

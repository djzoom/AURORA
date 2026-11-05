#!/usr/bin/env python3
"""Build the static growth assets for the Aurora Quest companion pages.

Outputs (all under aurora-quest/og/, committed to the repo so the pages stay
dependency-free at runtime):

  qr-quest.png / qr-videos.png   QR codes of the two page URLs (segno, no network)
  quest.png / videos.png         1200x630 social preview images rendered from
                                 og/templates/*.html with headless Chromium

Usage:
    pip install segno playwright && playwright install chromium
    python scripts/build_growth_assets.py
"""

from __future__ import annotations

import http.server
import socketserver
import sys
import threading
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "aurora-quest"
OG_DIR = PAGES_DIR / "og"

PAGES = {
    "quest": "https://djzoom.github.io/AURORA/",
    "videos": "https://djzoom.github.io/AURORA/video-library.html",
}


def build_qr_codes() -> None:
    import segno

    for key, url in PAGES.items():
        qr = segno.make(url, error="m")
        out = OG_DIR / f"qr-{key}.png"
        # 1-bit PNG, scale 8 -> roughly 260 px with a 2-module quiet zone;
        # the page scales it to 200 px with image-rendering: pixelated.
        qr.save(str(out), scale=8, border=2, dark="#04070e", light="#ffffff")
        print(f"wrote {out.relative_to(ROOT)} ({qr.symbol_size()[0]} modules)")


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):  # noqa: D401 - silence request log
        pass


def _serve(directory: Path) -> tuple[socketserver.TCPServer, int]:
    handler = partial(_QuietHandler, directory=str(directory))
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, port


def build_og_images() -> None:
    from playwright.sync_api import sync_playwright

    # Serve the pages folder over HTTP so the template can import src/sprites.js
    # as an ES module (file:// blocks module imports).
    server, port = _serve(PAGES_DIR)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                viewport={"width": 1200, "height": 630}, device_scale_factor=1
            )
            for key in PAGES:
                page.goto(f"http://127.0.0.1:{port}/og/templates/{key}.html")
                page.wait_for_selector("body[data-ready='1']")
                page.wait_for_timeout(150)
                out = OG_DIR / f"{key}.png"
                clip = {"x": 0, "y": 0, "width": 1200, "height": 630}
                page.screenshot(path=str(out), clip=clip)
                print(f"wrote {out.relative_to(ROOT)} (1200x630)")
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


def main(argv: list[str]) -> int:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    only = set(argv[1:])
    if not only or "qr" in only:
        build_qr_codes()
    if not only or "og" in only:
        build_og_images()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

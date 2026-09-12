# -*- coding: utf-8 -*-
"""Arşiv HTML'lerini 1400px genişlikte ekran görüntüsüne çevirir (görsel denetim için)."""
import os
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
DST = Path.home() / "deck_check" / "arsiv"
DST.mkdir(parents=True, exist_ok=True)
EXE = os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-1228/"
    "chrome-headless-shell-mac-arm64/chrome-headless-shell")
TARGETS = ["INDEX.html", "DIL-001/README-DIL-001.html",
           "DIL-001/dil-stratejisi-filolog-kalemi.html",
           "PR-001/README-PR-001.html"]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE)
    for rel in TARGETS:
        page = b.new_page(viewport={"width": 1400, "height": 900})
        page.goto("file://" + str((HERE / rel).resolve()))
        page.wait_for_timeout(1200)
        name = rel.replace("/", "_").replace(".html", "")
        shot = HERE / ("shot_" + name + ".png")
        page.screenshot(path=str(shot), full_page=True)
        im = Image.open(shot).convert("RGB")
        # uzun sayfaları baştan 1600px yükseklikte kırp
        im.crop((0, 0, im.width, min(im.height, 1900))).save(
            DST / (name + ".jpg"), "JPEG", quality=85)
        print(name, im.size, "->", DST / (name + ".jpg"))
    b.close()
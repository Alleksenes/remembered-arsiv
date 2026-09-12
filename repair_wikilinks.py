# -*- coding: utf-8 -*-
"""Obsidian wikilink onarımı: [[...\\|alias]] ve [[...\|alias]] -> [[...|alias]].
Kapsam: projects/remembered **.md (canon). Git-backed; commit + düzeltme raporu."""
import re
from pathlib import Path

ROOT = Path.home() / ".llm-wiki/wiki/projects/remembered"


def fix(text):
    n = 0
    new = []
    for line in text.split("\n"):
        n += line.count("\\\\|") + line.count("\\|")
        line = line.replace("\\\\|", "|").replace("\\|", "|")
        new.append(line)
    return "\n".join(new), n


total_files = total_repl = 0
changed = []
for p in sorted(ROOT.rglob("*.md")):
    try:
        orig = p.read_text(encoding="utf-8")
    except Exception:
        continue
    if "\\|" not in orig and "\\\\|" not in orig:
        continue
    fixed, n = fix(orig)
    if n:
        open(p, "w", encoding="utf-8").write(fixed)
        total_files += 1
        total_repl += n
        changed.append(str(p.relative_to(ROOT)))
print("değişen dosya:", total_files, "| onarılan ikili-atıf:", total_repl)
print("\n".join(changed[:40]))
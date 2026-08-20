#!/usr/bin/env python3
"""Local validation: internal links resolve, JSON-LD parses. Run after build.py."""
import json
import os
import re
import sys
from urllib.parse import urljoin, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "tools", "node_modules"}

errors = []
warnings = []


def find_html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn == "index.html":
                yield os.path.join(dirpath, fn)


html_files = list(find_html_files())
print(f"Checking {len(html_files)} HTML files...\n")

for filepath in html_files:
    rel = os.path.relpath(filepath, ROOT)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # --- JSON-LD validation ---
    for i, m in enumerate(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)):
        raw = m.group(1).strip()
        try:
            json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: invalid JSON-LD block #{i+1}: {e}")

    # --- internal link validation ---
    page_dir = os.path.dirname(filepath)
    for m in re.finditer(r'href="([^"]+)"', content):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue
        if href.startswith("javascript:"):
            continue
        path_part = href.split("#")[0]
        if not path_part:
            continue
        target = os.path.normpath(os.path.join(page_dir, path_part))
        if not os.path.exists(target):
            errors.append(f"{rel}: broken link -> {href} (resolved: {os.path.relpath(target, ROOT)})")

    # --- asset src validation (img, script, link) ---
    for m in re.finditer(r'(?:src|href)="((?:\.\./)*(?:images|css|js)/[^"]+)"', content):
        src = m.group(1)
        target = os.path.normpath(os.path.join(page_dir, src))
        if not os.path.exists(target):
            errors.append(f"{rel}: missing asset -> {src}")

print(f"{'='*60}")
if errors:
    print(f"FAILED: {len(errors)} error(s)\n")
    for e in errors:
        print(" -", e)
else:
    print("All internal links and JSON-LD blocks are valid.")

if warnings:
    print(f"\n{len(warnings)} warning(s):")
    for w in warnings:
        print(" -", w)

sys.exit(1 if errors else 0)

#!/usr/bin/env python3
"""Replace leftover Candy branding in all Android string resources."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "app" / "src" / "main" / "res"
changed = 0
for path in sorted(RES.glob("values*/**/*.xml")):
    text = path.read_text(encoding="utf-8")
    if "Candy" not in text:
        continue
    text = text.replace("Candy Browser", "Penozovi").replace("Candy", "Penozovi")
    text = re.sub(r"(<string name=\"app_name\">)[^<]*(</string>)", r"\1Penozovi\2", text)
    path.write_text(text, encoding="utf-8")
    changed += 1
print(f"Rebranded {changed} resource files")

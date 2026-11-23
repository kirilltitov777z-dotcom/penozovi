#!/usr/bin/env python3
"""Validate plugin manifests and build the Penozovi plugin store index.

Reads plugins/catalog/*/manifest.json and writes:
  - store/index.json
  - app/src/main/assets/penozovi_plugins/store.json
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "plugins" / "catalog"
OUTPUTS = [
    ROOT / "store" / "index.json",
    ROOT / "site" / "penozovi-store" / "index.json",
    ROOT / "app" / "src" / "main" / "assets" / "penozovi_plugins" / "store.json",
]
REQUIRED = ["id", "name", "version", "author", "description", "category"]
CATEGORIES = {"appearance", "privacy", "productivity", "media", "feeds", "other"}
PERMISSIONS = {"content", "storage", "network"}


def fail(message):
    print("::error::" + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    if not CATALOG.is_dir():
        fail("plugins/catalog not found")

    plugins, seen = [], set()
    for manifest_path in sorted(CATALOG.glob("*/manifest.json")):
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{manifest_path}: invalid JSON: {exc}")

        for field in REQUIRED:
            if not data.get(field):
                fail(f"{manifest_path}: missing required field '{field}'")
        if data["id"] in seen:
            fail(f"{manifest_path}: duplicate id '{data['id']}'")
        seen.add(data["id"])
        if data["category"] not in CATEGORIES:
            fail(f"{manifest_path}: unknown category '{data['category']}'")
        unknown = set(data.get("permissions", [])) - PERMISSIONS
        if unknown:
            fail(f"{manifest_path}: unknown permission(s): {sorted(unknown)}")

        folder = manifest_path.parent
        entry = data.get("entry")
        if entry and not (folder / entry).exists():
            fail(f"{manifest_path}: entry file '{entry}' does not exist")

        data["path"] = str(folder.relative_to(ROOT)).replace(os.sep, "/")
        plugins.append(data)
        print(f"OK  {data['id']} ({data['version']})")

    index = {
        "name": "Penozovi Plugin Store",
        "version": 1,
        "count": len(plugins),
        "plugins": plugins,
    }
    html_src = ROOT / "store" / "index.html"
    html_dst = ROOT / "site" / "penozovi-store" / "index.html"
    html_dst.parent.mkdir(parents=True, exist_ok=True)
    html_dst.write_text(html_src.read_text(encoding="utf-8"), encoding="utf-8")

    for out in OUTPUTS:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE {out.relative_to(ROOT)} ({len(plugins)} plugins)")


if __name__ == "__main__":
    main()

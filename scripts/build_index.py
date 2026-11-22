"""Rebuilds maps/index.json from the .mmd files in maps/.

Each map can start with two optional comment lines:
    %% title: Nice title shown in the menu
    %% category: Branch of the menu it sits under
"""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
maps_dir = root / "maps"
items = []

for f in sorted(maps_dir.glob("*.mmd")):
    text = f.read_text(encoding="utf-8")
    title = re.search(r"^%%\s*title:\s*(.+)$", text, re.M)
    category = re.search(r"^%%\s*category:\s*(.+)$", text, re.M)
    default_title = f.stem.replace("-", " ").replace("_", " ").capitalize()
    items.append({
        "title": title.group(1).strip() if title else default_title,
        "category": category.group(1).strip() if category else "Other",
        "file": f.name,
    })

items.sort(key=lambda m: (m["category"].lower(), m["title"].lower()))
(maps_dir / "index.json").write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Indexed {len(items)} map(s)")

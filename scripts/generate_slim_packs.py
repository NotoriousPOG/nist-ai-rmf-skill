#!/usr/bin/env python3
"""Regenerate slim playbook packs from references/playbook.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from models import PlaybookCatalog, PlaybookEntry  # noqa: E402

FUNC_FILE = {"Govern": "govern", "Map": "map", "Measure": "measure", "Manage": "manage"}
FUNC_ORDER = {"Govern": 0, "Map": 1, "Measure": 2, "Manage": 3}


def sort_key(entry: PlaybookEntry):
    m = re.match(r"(\w+)\s+(\d+)\.(\d+)", entry.title)
    assert m
    return (FUNC_ORDER[entry.type.value], int(m.group(2)), int(m.group(3)))


def slim_dict(entry: PlaybookEntry) -> dict:
    return {
        "type": entry.type.value,
        "title": entry.title,
        "category": entry.category,
        "description": entry.description,
        "section_actions": entry.section_actions,
        "section_doc": entry.section_doc,
        "Topic": entry.Topic,
        "AI Actors": entry.AI_Actors,
    }


def render_md(ftype: str, items: list[PlaybookEntry]) -> str:
    lines = [
        f"# Playbook pack — {ftype.upper()}",
        "",
        f"Use this file while scoring **{ftype.upper()}** subcategories. "
        "Prefer this over loading full `playbook.json`.",
        "",
        f"Count: **{len(items)}**",
        "",
    ]
    for x in items:
        lines.append(f"## {x.title}")
        lines.append("")
        lines.append(f"**Category:** `{x.category}`  ")
        if x.Topic:
            lines.append(f"**Topics:** {', '.join(x.Topic)}  ")
        if x.AI_Actors:
            lines.append(f"**AI Actors:** {', '.join(x.AI_Actors)}  ")
        lines.append("")
        lines.append(x.description)
        lines.append("")
        lines.append("### Suggested actions")
        lines.append("")
        lines.append(x.section_actions or "_None_")
        lines.append("")
        lines.append("### Documentation / evidence prompts")
        lines.append("")
        lines.append(x.section_doc or "_None_")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--playbook",
        type=Path,
        default=SKILL_DIR / "references" / "playbook.json",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=SKILL_DIR / "references" / "playbook-packs",
    )
    args = parser.parse_args()

    raw = json.loads(args.playbook.read_text(encoding="utf-8"))
    catalog = PlaybookCatalog(
        entries=[PlaybookEntry.model_validate(x) for x in raw]
    )
    args.out_dir.mkdir(parents=True, exist_ok=True)

    by: dict[str, list[PlaybookEntry]] = {k: [] for k in FUNC_FILE}
    for e in sorted(catalog.entries, key=sort_key):
        by[e.type.value].append(e)

    slim_all = []
    for ftype, items in by.items():
        stem = FUNC_FILE[ftype]
        slim = [slim_dict(e) for e in items]
        slim_all.extend(slim)
        (args.out_dir / f"{stem}.json").write_text(
            json.dumps(slim, indent=2) + "\n", encoding="utf-8"
        )
        (args.out_dir / f"{stem}.md").write_text(
            render_md(ftype, items), encoding="utf-8"
        )
        print(f"wrote {stem}: {len(items)}")

    (args.out_dir / "all-slim.json").write_text(
        json.dumps(slim_all, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote all-slim.json: {len(slim_all)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

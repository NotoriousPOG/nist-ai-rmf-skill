#!/usr/bin/env python3
"""Validate NIST AI RMF playbook.json and slim packs with Pydantic."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from models import (  # noqa: E402
    EXPECTED_TOTAL,
    PlaybookCatalog,
    PlaybookEntry,
    SlimPlaybookCatalog,
    SlimPlaybookEntry,
)


def load_json(path: Path) -> list | dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_full(path: Path) -> PlaybookCatalog:
    raw = load_json(path)
    if not isinstance(raw, list):
        raise SystemExit(f"{path}: expected a JSON array")
    entries = [PlaybookEntry.model_validate(item) for item in raw]
    return PlaybookCatalog(entries=entries)


def validate_slim(path: Path) -> SlimPlaybookCatalog:
    raw = load_json(path)
    if not isinstance(raw, list):
        raise SystemExit(f"{path}: expected a JSON array")
    entries = [SlimPlaybookEntry.model_validate(item) for item in raw]
    return SlimPlaybookCatalog(entries=entries)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--playbook",
        type=Path,
        default=SKILL_DIR / "references" / "playbook.json",
        help="Full playbook.json path",
    )
    parser.add_argument(
        "--slim",
        type=Path,
        default=SKILL_DIR / "references" / "playbook-packs" / "all-slim.json",
        help="Slim all-slim.json path (optional check)",
    )
    parser.add_argument(
        "--skip-slim",
        action="store_true",
        help="Only validate full playbook",
    )
    args = parser.parse_args()

    catalog = validate_full(args.playbook)
    print(f"OK playbook: {len(catalog.entries)}/{EXPECTED_TOTAL} entries")
    by: dict[str, int] = {}
    for e in catalog.entries:
        by[e.type.value] = by.get(e.type.value, 0) + 1
    for k in sorted(by):
        print(f"  {k}: {by[k]}")

    if not args.skip_slim and args.slim.exists():
        slim = validate_slim(args.slim)
        full_titles = catalog.titles
        slim_titles = {e.title for e in slim.entries}
        if full_titles != slim_titles:
            missing = sorted(full_titles - slim_titles)
            extra = sorted(slim_titles - full_titles)
            print("FAIL slim title mismatch")
            if missing:
                print("  missing from slim:", ", ".join(missing[:20]))
            if extra:
                print("  extra in slim:", ", ".join(extra[:20]))
            return 1
        # size sanity: slim should not include section_about/ref
        print(f"OK slim pack: {len(slim.entries)}/{EXPECTED_TOTAL} (titles match playbook)")
    elif not args.skip_slim:
        print(f"WARN slim not found at {args.slim} (skipped)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

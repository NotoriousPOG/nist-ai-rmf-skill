#!/usr/bin/env python3
"""Validate a filled NIST AI RMF assessment Markdown report for 72/72 coverage."""

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

from models import (  # noqa: E402
    EXPECTED_TOTAL,
    AssessmentCoverage,
    FindingRow,
    PlaybookCatalog,
    PlaybookEntry,
)

TITLE_IN_ROW = re.compile(
    r"^\|\s*((?:GOVERN|MAP|MEASURE|MANAGE)\s+\d+\.\d+)\s*\|"
    r"\s*([^|]*)\|"
    r"\s*([^|]*)\|"
    r"\s*([^|]*)\|"
    r"\s*([^|]*)\|"
    r"\s*([^|]*)\|"
    r"\s*([^|]*)\|",
    re.MULTILINE,
)
COVERAGE_CLAIM = re.compile(
    r"\|?\s*\*?\*?Playbook coverage\*?\*?\s*\|?\s*\*?\*?([0-9_]+)\s*/\s*72\*?\*?",
    re.IGNORECASE,
)


def _parse_claimed(text: str) -> str | None:
    """Extract claimed N/72 from the cover table; ignore instructional mentions."""
    # Prefer table row form
    for m in COVERAGE_CLAIM.finditer(text):
        n = m.group(1)
        if n == "__" or n.startswith("_"):
            return f"{n}/72"
        if n.isdigit():
            return f"{int(n)}/72"
    return None



def load_expected_titles(playbook: Path) -> set[str]:
    raw = json.loads(playbook.read_text(encoding="utf-8"))
    catalog = PlaybookCatalog(
        entries=[PlaybookEntry.model_validate(x) for x in raw]
    )
    return catalog.titles


def parse_assessment(text: str, expected: set[str]) -> AssessmentCoverage:
    rows: list[FindingRow] = []
    found: set[str] = set()
    for m in TITLE_IN_ROW.finditer(text):
        row = FindingRow(
            title=m.group(1).strip(),
            category=m.group(2).strip(),
            current=m.group(3).strip(),
            target=m.group(4).strip(),
            evidence=m.group(5).strip(),
            gap=m.group(6).strip(),
            priority=m.group(7).strip(),
        )
        # skip header-ish junk
        if row.title.upper() in {"ID", "TITLE"}:
            continue
        rows.append(row)
        found.add(row.title)

    claimed = _parse_claimed(text)

    return AssessmentCoverage(
        expected_titles=expected,
        found_titles=found,
        rows=rows,
        claimed_coverage=claimed,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "report",
        type=Path,
        help="Path to filled nist-ai-rmf-assessment-*.md",
    )
    parser.add_argument(
        "--playbook",
        type=Path,
        default=SKILL_DIR / "references" / "playbook.json",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Exit 0 even if coverage < 72/72 (still prints gaps)",
    )
    parser.add_argument(
        "--require-scores",
        action="store_true",
        help="Fail if any found row has empty Current score",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable summary",
    )
    args = parser.parse_args()

    if not args.report.exists():
        print(f"FAIL report not found: {args.report}", file=sys.stderr)
        return 2

    expected = load_expected_titles(args.playbook)
    text = args.report.read_text(encoding="utf-8")
    # Reject obvious secrets heuristics (best-effort)
    secret_hits = []
    for pat, label in [
        (r"sk-[A-Za-z0-9]{20,}", "openai-like key"),
        (r"ghp_[A-Za-z0-9]{20,}", "github PAT"),
        (r"xox[baprs]-[A-Za-z0-9-]{10,}", "slack token"),
        (r"-----BEGIN (RSA |OPENSSH )?PRIVATE KEY-----", "private key"),
    ]:
        if re.search(pat, text):
            secret_hits.append(label)

    coverage = parse_assessment(text, expected)
    summary = coverage.summary()
    summary["secret_heuristic_hits"] = secret_hits

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        status = "OK" if coverage.is_complete else "INCOMPLETE"
        print(
            f"{status} coverage: {coverage.count}/{EXPECTED_TOTAL}"
            + (f" (claimed {coverage.claimed_coverage})" if coverage.claimed_coverage else "")
        )
        if coverage.missing:
            print("missing titles:")
            for t in coverage.missing:
                print(f"  - {t}")
        if coverage.extra:
            print("extra titles (not in playbook):")
            for t in coverage.extra:
                print(f"  - {t}")
        unscored = coverage.unscored_titles()
        if unscored:
            print(f"unscored rows (empty Current): {len(unscored)}")
            for t in unscored[:15]:
                print(f"  - {t}")
            if len(unscored) > 15:
                print(f"  ... +{len(unscored) - 15} more")
        na_bad = coverage.na_without_gap()
        if na_bad:
            print(f"N/A without gap justification: {len(na_bad)}")
            for t in na_bad[:10]:
                print(f"  - {t}")
        if secret_hits:
            print("FAIL secret-like material detected:", ", ".join(secret_hits))

    failed = False
    if secret_hits:
        failed = True
    if not coverage.is_complete and not args.allow_partial:
        failed = True
    if args.require_scores and coverage.unscored_titles():
        failed = True
    if coverage.na_without_gap() and coverage.is_complete:
        # soft fail only when claiming complete
        failed = True

    # Claimed coverage must match reality when present and numeric
    if coverage.claimed_coverage and coverage.claimed_coverage[0].isdigit():
        claimed_n = int(coverage.claimed_coverage.split("/")[0])
        if claimed_n != coverage.count:
            print(
                f"FAIL claimed coverage {coverage.claimed_coverage} "
                f"!= parsed {coverage.count}/72"
            )
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

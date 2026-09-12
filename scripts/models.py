"""Pydantic models for NIST AI RMF skill data (playbook, packs, assessment coverage)."""

from __future__ import annotations

import re
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


PLAYBOOK_TITLE_RE = re.compile(
    r"^(GOVERN|MAP|MEASURE|MANAGE) (\d+)\.(\d+)$"
)

EXPECTED_COUNTS = {
    "Govern": 19,
    "Map": 18,
    "Measure": 22,
    "Manage": 13,
}
EXPECTED_TOTAL = 72


class FunctionType(str, Enum):
    govern = "Govern"
    map = "Map"
    measure = "Measure"
    manage = "Manage"


class PlaybookEntry(BaseModel):
    """Full Playbook JSON object (NIST export shape)."""

    model_config = ConfigDict(extra="ignore")

    type: FunctionType
    title: str
    category: str
    description: str = Field(min_length=1)
    section_about: str = ""
    section_actions: str = Field(min_length=1)
    section_doc: str = Field(min_length=1)
    section_ref: str = ""
    AI_Actors: list[str] = Field(default_factory=list, alias="AI Actors")
    Topic: list[str] = Field(default_factory=list)

    @field_validator("title")
    @classmethod
    def title_shape(cls, v: str) -> str:
        if not PLAYBOOK_TITLE_RE.match(v):
            raise ValueError(f"title must look like 'GOVERN 1.1', got {v!r}")
        return v

    @model_validator(mode="after")
    def title_matches_type(self) -> PlaybookEntry:
        prefix = self.title.split()[0]
        expected = {
            FunctionType.govern: "GOVERN",
            FunctionType.map: "MAP",
            FunctionType.measure: "MEASURE",
            FunctionType.manage: "MANAGE",
        }[self.type]
        if prefix != expected:
            raise ValueError(
                f"title prefix {prefix!r} does not match type {self.type.value!r}"
            )
        return self


class SlimPlaybookEntry(BaseModel):
    """Efficient scoring pack entry (no about/ref blobs)."""

    model_config = ConfigDict(extra="ignore")

    type: FunctionType
    title: str
    category: str
    description: str = Field(min_length=1)
    section_actions: str = Field(min_length=1)
    section_doc: str = Field(min_length=1)
    Topic: list[str] = Field(default_factory=list)
    AI_Actors: list[str] = Field(default_factory=list, alias="AI Actors")

    @field_validator("title")
    @classmethod
    def title_shape(cls, v: str) -> str:
        if not PLAYBOOK_TITLE_RE.match(v):
            raise ValueError(f"invalid title {v!r}")
        return v


class PlaybookCatalog(BaseModel):
    entries: list[PlaybookEntry]

    @model_validator(mode="after")
    def exact_coverage(self) -> PlaybookCatalog:
        titles = [e.title for e in self.entries]
        if len(titles) != EXPECTED_TOTAL:
            raise ValueError(f"expected {EXPECTED_TOTAL} entries, got {len(titles)}")
        if len(set(titles)) != len(titles):
            dupes = sorted({t for t in titles if titles.count(t) > 1})
            raise ValueError(f"duplicate titles: {dupes}")
        by_type: dict[str, int] = {}
        for e in self.entries:
            by_type[e.type.value] = by_type.get(e.type.value, 0) + 1
        for name, count in EXPECTED_COUNTS.items():
            got = by_type.get(name, 0)
            if got != count:
                raise ValueError(f"{name}: expected {count}, got {got}")
        return self

    @property
    def titles(self) -> set[str]:
        return {e.title for e in self.entries}


class SlimPlaybookCatalog(BaseModel):
    entries: list[SlimPlaybookEntry]

    @model_validator(mode="after")
    def exact_coverage(self) -> SlimPlaybookCatalog:
        titles = [e.title for e in self.entries]
        if len(titles) != EXPECTED_TOTAL:
            raise ValueError(f"slim pack expected {EXPECTED_TOTAL}, got {len(titles)}")
        if len(set(titles)) != EXPECTED_TOTAL:
            raise ValueError("slim pack has duplicate or missing titles")
        return self


class ScoreLabel(str, Enum):
    not_started = "0"
    partial = "1"
    implemented = "2"
    optimized = "3"
    na = "N/A"


class FindingRow(BaseModel):
    """One assessment findings-table row parsed from Markdown."""

    title: str
    category: str = ""
    current: str = ""
    target: str = ""
    evidence: str = ""
    gap: str = ""
    priority: str = ""

    @field_validator("title")
    @classmethod
    def title_shape(cls, v: str) -> str:
        if not PLAYBOOK_TITLE_RE.match(v.strip()):
            raise ValueError(f"invalid finding title {v!r}")
        return v.strip()

    @field_validator("current")
    @classmethod
    def current_score(cls, v: str) -> str:
        v = v.strip()
        if not v:
            return v
        allowed = {"0", "1", "2", "3", "N/A", "NA", "n/a"}
        if v not in allowed:
            # allow labels like "1 Partial"
            if v[0] in "0123" or v.upper().startswith("N/A"):
                return v
            raise ValueError(f"current score must be 0-3 or N/A, got {v!r}")
        return v


class AssessmentCoverage(BaseModel):
    """Coverage result for a filled assessment report."""

    expected_titles: set[str]
    found_titles: set[str]
    rows: list[FindingRow] = Field(default_factory=list)
    claimed_coverage: str | None = None

    @property
    def missing(self) -> list[str]:
        return sorted(self.expected_titles - self.found_titles)

    @property
    def extra(self) -> list[str]:
        return sorted(self.found_titles - self.expected_titles)

    @property
    def count(self) -> int:
        return len(self.found_titles)

    @property
    def is_complete(self) -> bool:
        return (
            self.count == EXPECTED_TOTAL
            and not self.missing
            and not self.extra
        )

    def unscored_titles(self) -> list[str]:
        out = []
        for row in self.rows:
            if row.title in self.expected_titles and not str(row.current).strip():
                out.append(row.title)
        return sorted(set(out))

    def na_without_gap(self) -> list[str]:
        out = []
        for row in self.rows:
            cur = str(row.current).strip().upper()
            if cur in {"N/A", "NA"} and not str(row.gap).strip():
                out.append(row.title)
        return sorted(set(out))

    def summary(self) -> dict[str, Any]:
        return {
            "found": self.count,
            "expected": EXPECTED_TOTAL,
            "complete": self.is_complete,
            "missing": self.missing,
            "extra": self.extra,
            "unscored": self.unscored_titles(),
            "na_without_justification": self.na_without_gap(),
            "claimed_coverage": self.claimed_coverage,
        }

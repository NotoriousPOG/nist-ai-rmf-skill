# scripts/

Python helpers for the `nist-ai-rmf` skill. Prefer **Pydantic** validation here (not Zod) — the catalog and reports are validated from the shell/agent without a Node toolchain.

## Requires

- Python 3.10+
- `pydantic>=2` (see `requirements.txt`)

```bash
pip install -r requirements.txt
```

## Commands

Validate the Playbook catalog + slim packs:

```bash
python scripts/validate_playbook.py
```

Regenerate slim packs from `references/playbook.json`:

```bash
python scripts/generate_slim_packs.py
```

Validate a filled assessment report (72/72 coverage, N/A justifications, secret heuristics):

```bash
python scripts/validate_assessment.py path/to/nist-ai-rmf-assessment-<slug>-<date>.md
python scripts/validate_assessment.py report.md --require-scores --json
```

## Why this exists

| Risk | Mitigation |
|------|------------|
| Corrupt / incomplete playbook JSON | `PlaybookCatalog` enforces 72 unique titles + per-function counts |
| Agents loading 400KB+ JSON every turn | Slim packs (`references/playbook-packs/`) for scoring |
| Fake `72/72` claims | `validate_assessment.py` parses finding rows vs playbook titles |
| Secrets pasted into reports | Best-effort regex heuristics fail the check |

Zod would be appropriate for a TypeScript app UI; this skill’s runtime is Markdown + agent shell → **Pydantic**.

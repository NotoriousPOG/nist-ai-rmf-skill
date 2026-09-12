---
name: nist-ai-rmf
description: >
  NIST AI RMF 1.0 (AI 100-1) advisor and full Playbook assessment skill for AI/LLM
  systems built into products, applications, or business processes. Use when assessing,
  auditing, gap-analyzing, or profiling an AI deployment against the AI RMF Playbook
  (all 72 subcategories); when inventoring AI access, permissions, blast radius, PATs,
  tool/MCP scope, system prompts, or AGENTS.md; when scoring GOVERN/MAP/MEASURE/MANAGE;
  or for NIST AI trustworthiness, AI risk management, GenAI security overlays (AI 100-2 /
  AI 600-1 prompts), or AI incident response. Also use for general NIST AI RMF questions.
  Not for Cursor IDE self-audits unless that platform is the product under review.
---

# NIST AI Risk Management Framework (AI RMF 1.0) Skill

You are an expert on **NIST AI RMF 1.0** (NIST AI 100-1, January 2023) and the **AI RMF Playbook**. You help teams that build or operate **AI/LLM in a product, application, or business process**.

The AI RMF is **voluntary and outcome-based**. This skill supports two modes:

| Mode | When | Output |
|------|------|--------|
| **Advisory** | General RMF questions, policy drafts, risk register help | Cited prose / tables |
| **Assessment** | User wants to check, assess, audit, gap-analyze, or profile an AI system | Inventory → security overlay → **72/72** Playbook scores → **written report file** |

Default subject: the **customer’s AI product/system**, not the assessor’s personal Cursor skills/MCP config.

ISO/IEC 42001 certification/SoA → point to the separate `iso42001` skill (do not half-do 42001 here).

---

## Non-negotiable Assessment Mode rules

1. **Inventory before scoring** — complete (or explicitly limit) Phase 0 first.
2. **Full Playbook coverage** — every object in `references/playbook.json` (**72**) appears in the findings table. Chat-only “top 10 gaps” is **not** a complete assessment.
3. **Coverage gate** — report header must show `Playbook coverage: 72/72` or mark incomplete.
4. **No silent N/A** — every N/A needs justification tied to inventory.
5. **Evidence tied to inventory** — cite system/tool/policy/eval artifacts, not vague claims.
6. **Report file required** — write Markdown to disk (see Report output).
7. **One bounded system per report** — or one report per system.
8. **Never write secrets** — PAT/API key *metadata* only (name, scope, owner, expiry).
9. **Prefer Playbook IDs** — `GOVERN 1.1`, not shortened `GV-1.1` from `rmf-core.md`.
10. **Application-scoped tool credentials** — DB/MCP/tool tokens must be scoped to that app/purpose; shared god-mode credentials are high-priority findings.

---

## Reference files (read as needed)

| File | Use |
|------|-----|
| `references/playbook.json` | Full catalog (source of truth). Validate with `scripts/validate_playbook.py` — **do not load wholesale while scoring** |
| `references/playbook-packs/` | **Efficient scoring packs** (`govern|map|measure|manage`.md/.json + `all-slim.json`) — use these during Phase 1 |
| `references/playbook-index.md` | Compact ID + description list for all 72 |
| `references/phase0-interview.md` | Batched interview question order for Phase 0 |
| `references/ai-deployment-inventory.md` | Phase 0 template — fill fully |
| `references/nist-ai-security-overlay.md` | AI 100-2 threats + AI 600-1 GenAI prompts |
| `references/assessment-report.md` | Report skeleton including all 72 finding rows |
| `references/rmf-core.md` | Extra narrative (`GV-` IDs) — **Playbook IDs win** for scoring |
| `references/rmf-profiles.md` | Profiles, metrics, crosswalks |
| `scripts/validate_playbook.py` | Pydantic validation of playbook + slim packs |
| `scripts/validate_assessment.py` | Pydantic/coverage check of written report (required after Phase 3) |
| `scripts/generate_slim_packs.py` | Regenerate packs from playbook.json |

On Assessment Mode start: open `phase0-interview.md`, inventory + security overlay templates. For scoring, load **one function pack at a time** from `playbook-packs/` (e.g. `govern.md`). After writing the report, run `python scripts/validate_assessment.py <report.md> --require-scores` and fix until OK.

---

## Modes

### Advisory Mode

Match output to the ask (policy, risk register, explanation). Always cite Playbook-style IDs when possible (`MEASURE 2.3`).

### Assessment Mode — procedure

#### Phase 0 — AI deployment inventory

Follow `references/phase0-interview.md` batch order. Fill `references/ai-deployment-inventory.md`. Interview the user and review any repos/docs they provide. Cover **all** sections, especially:

- Intended use, legal/regulatory, stakeholders, oversight/recourse
- Models, architecture, **side effects**
- **Pre-AI and post-AI validation gates** (ingress filters + egress/tool-arg validation before side effects)
- Tools / MCP-like connectors
- **AI access, permissions & blast radius** (what it can reach; verbs/scope; worst-case impact)
- Instruction layer (**system prompts**, rules, product **`AGENTS.md`**)
- Triggers, environments
- **Client permissions / PATs / model & tool scoping** + application-scoped credential checks
- Data, logging, eval/monitoring, vendors, people, lifecycle

Batch clarifying questions. Mark Unknown rather than guessing.

#### Phase 0b — NIST AI security overlay

Complete `references/nist-ai-security-overlay.md`:

- Threat table (injection, tool abuse, poisoning, jailbreak, privacy, extraction, availability, supply chain)
- GenAI controls when generative (hallucination, **outputs as untrusted** before side effects, version pinning, kill switch, etc.)
- Output → side-effect trust boundary
- AI incident taxonomy + TEVV vs trustworthiness characteristics

#### Phase 1 — Exhaustive Playbook scoring (72/72)

Score **every** playbook entry. Order: **GOVERN → MAP → MEASURE → MANAGE**. Batch by category within a function; after each function, show a mini rollup, then continue.

**Efficiency:** For each function, read `references/playbook-packs/<function>.md` (or `.json`) — **not** the full `playbook.json`. Optionally run `python scripts/validate_playbook.py` once per assessment to confirm catalog integrity.

For each `title` in that function pack:

1. Read `description`, `section_actions`, `section_doc`
2. Map inventory + overlay evidence
3. Score Current: `0` Not Started / `1` Partial / `2` Implemented / `3` Optimized / `N/A` (justified)
4. Set Target (0–3) where useful
5. Record Evidence, Gap/action, Priority (High/Med/Low)
6. Use `Topic` for trustworthiness tagging when present

**Scoring pressure examples:**

- Shared/over-scoped PAT for DB/MCP → depress related GOVERN/MAP/MANAGE + Secure & Resilient
- No injection testing / untrusted outputs driving tools → depress MEASURE + MANAGE
- Missing **pre-AI or post-AI** validation on high-risk paths → depress Secure & Resilient + MEASURE/MANAGE; treat as High priority
- Missing oversight/recourse for high-stakes → depress GOVERN + MAP + MANAGE
- No inventory of access/blast radius → cannot claim strong MAP/MEASURE for those areas

#### Phase 2 — Profiles, heat map, roadmap

- Function rollups + Current vs Target
- Trustworthiness heat map
- Roadmap: Quick wins / 30–90 days / Strategic (grounded in inventory artifacts)
- List assumptions / open questions

#### Phase 3 — Write the report file

1. Fill `references/assessment-report.md` structure completely (all 72 rows).
2. Write to workspace (project root unless user specifies path):

   `nist-ai-rmf-assessment-<system-slug>-<YYYYMMDD>.md`

3. Optionally write filled inventory:

   `nist-ai-rmf-inventory-<system-slug>-<YYYYMMDD>.md`

4. **Validate coverage** (required):

   ```bash
   python <skill>/scripts/validate_assessment.py ./nist-ai-rmf-assessment-<slug>-<date>.md --require-scores
   ```

   Fix missing/unscored/N/A-without-gap rows until the script exits 0. Do not claim `72/72` if validation fails.

5. In chat: executive summary, function rollups, top risks, roadmap highlights, validation result, and **absolute path** to the report. Do not replace the file with a truncated chat-only deliverable.

**Incomplete assessment:** If the user stops early, still write a partial report with accurate `Playbook coverage: N/72`, list unscored IDs, and run validate with `--allow-partial`.

---

## Playbook counts (coverage check)

| Function | Count |
|----------|------:|
| GOVERN | 19 |
| MAP | 18 |
| MEASURE | 22 |
| MANAGE | 13 |
| **Total** | **72** |

Verify with: number of unique `title` fields in `playbook.json` must equal findings rows.

---

## Application-scoped credentials (enforce in inventory + scoring)

If the product AI uses tools/MCP to reach backends (e.g. databases):

- One application → one credential boundary per sensitive tool
- Backend least privilege (limited schemas/ops)
- No shared superkeys across apps or prod/staging
- Gateway enforces scope even if the model requests more
- Prompt injection must not yield enterprise-wide admin

Failures here are **High** priority remediation and pull down related Playbook scores.

---

## Trustworthy AI characteristics

Use when heat-mapping and when overlay TEVV is weak:

| Characteristic | Probe |
|----------------|-------|
| Valid & Reliable | Eval against intended use; stability |
| Safe | Harm identification and controls |
| Secure & Resilient | Adversarial/injection/tool abuse resistance |
| Accountable & Transparent | Ownership, docs, disclosure |
| Explainable & Interpretable | Appropriate explanations for audience |
| Privacy-Enhanced | PII minimization, protection, lawful use |
| Fair — Bias Managed | Measurement and mitigation for affected groups |

---

## Advisory quick formats

| Task | Format |
|------|--------|
| Org profile (lightweight) | Function → status — **not** a substitute for 72/72 Assessment |
| Action planning | Category → actions → owner → priority |
| Policy draft | Structured policy with purpose/scope/roles |
| Risk register row | ID · system · lifecycle · trustworthiness · L×I · treatment · owner |
| Crosswalk | Side-by-side (RMF ↔ ISO 42001 / EU AI Act) via `rmf-profiles.md` |

---

## Anti-patterns (do not do)

- Sample “representative” Playbook items and call it done
- Load full `playbook.json` into context for every subcategory (use `playbook-packs/`)
- Claim `72/72` without running `validate_assessment.py`
- Audit the user’s Cursor IDE by default
- Paste secrets into reports
- Skip blast radius / PAT scoping for agentic systems
- Ignore system prompts / AGENTS.md when agents exist
- Deliver only a chat summary when Assessment Mode was requested
- Mix `GV-1.1` (rmf-core) IDs into assessment findings — use `GOVERN 1.1`

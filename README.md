# NIST AI RMF Skill

Cursor/Claude agent skill for the **NIST AI Risk Management Framework (AI RMF) 1.0** — advisory help plus a **full Playbook assessment** of AI/LLM systems built into a **product, application, or business process**.

| | |
|--|--|
| **Skill name** | `nist-ai-rmf` |
| **Framework** | [NIST AI 100-1](https://www.nist.gov/itl/ai-risk-management-framework) + AI RMF Playbook |
| **License** | MIT (see [`LICENSE`](LICENSE)) |
| **NIST credit** | Full attribution + official links in [`NOTICE`](NOTICE) — **not NIST-endorsed** |
| **Not this** | Cursor IDE self-audit · ISO/IEC 42001 certification · legal advice |

**Disclaimer:** Voluntary governance aid only. Not legal advice, not a certification, and not affiliated with NIST.

---

## Install (Cursor)

```bash
git clone https://github.com/NotoriousPOG/nist-ai-rmf-skill.git
mkdir -p ~/.cursor/skills
ln -s "$(pwd)/nist-ai-rmf-skill" ~/.cursor/skills/nist-ai-rmf
# or: cp -R nist-ai-rmf-skill ~/.cursor/skills/nist-ai-rmf
```

Optional validators:

```bash
cd nist-ai-rmf-skill
pip install -r requirements.txt
python scripts/validate_playbook.py
```

---

## What it does

### Advisory mode

Answer NIST AI RMF questions with concrete citations (`GOVERN 1.1`, `MEASURE 2.3`, …): policies, risk registers, trustworthiness, incident patterns, crosswalks.

### Assessment mode (the checker)

1. **Inventory** the AI deployment in depth (system, models, tools/MCP, prompts/`AGENTS.md`, data, oversight, vendors, …)
2. Capture **access, permissions, and blast radius**
3. Capture **PATs / client permissions** with **application-scoped** tool credentials
4. Run a **NIST AI security overlay** (AI 100-2 threat classes + AI 600-1 GenAI prompts)
5. Score **every Playbook subcategory — all 72** (no sampling)
6. **Write a Markdown report file** to the project (not chat-only)

```text
Inventory  →  Security overlay  →  Score 72/72 Playbook  →  Report file + chat summary
```

---

## Quick start

In Cursor chat (with this skill available):

```text
Assess our <product AI system> against NIST AI RMF — full playbook.
Inventory access, permissions, blast radius, and PAT/tool scoping.
Write the report to the repo when done.
```

Other useful prompts:

```text
NIST AI RMF gap assessment for our customer-support LLM agent (tools + RAG).
```

```text
Continue the NIST assessment — finish MEASURE and MANAGE, then write the report.
```

```text
Explain GOVERN 1.6 and what evidence we need for an AI system inventory.
```

---

## What gets inventoried

Assessment Mode fills `references/ai-deployment-inventory.md`, including:

| Area | Examples |
|------|----------|
| Intended use & autonomy | Purpose, prohibited uses, high-stakes impacts |
| Legal / regulatory | Privacy, sector rules, contracts |
| Stakeholders & recourse | Affected parties, appeal, kill switch |
| Models & inference | Providers, pins, fine-tunes |
| Architecture & side effects | DB writes, email, tickets, payments |
| **Pre-/post-AI validation** | Ingress checks before the model; egress/tool-arg checks after, before side effects |
| Tools / MCP-like connectors | Function calling, plugins, RPA |
| **Access, permissions, blast radius** | What it can reach, verbs/scope, worst-case impact |
| Instruction layer | System prompts, rules, product `AGENTS.md` |
| Triggers & environments | Cron, webhooks; prod vs staging credentials |
| **Credentials / PATs** | Model & tool scope; **app-scoped** DB/tool tokens |
| Data, logging, evals | RAG/train corpora, audit logs, drift/bias/security tests |
| Vendors & governance | DPAs, owners, risk tolerance, lifecycle |

**Secrets never go in the report** — only credential metadata (name, owner, scope, expiry).

### Application-scoped credentials

If the AI calls tools/MCP against something like a database, the auth token should be **scoped to that application** (and ideally that tool) — not a shared org-wide or DBA credential. The skill treats shared “god mode” tokens as high-priority findings.

---

## Playbook coverage (mandatory)

| Function | Subcategories |
|----------|--------------:|
| GOVERN | 19 |
| MAP | 18 |
| MEASURE | 22 |
| MANAGE | 13 |
| **Total** | **72** |

The catalog is `references/playbook.json` (NIST AI RMF Playbook export). A complete assessment’s report must show:

```text
Playbook coverage: 72/72
```

Anything less must be labeled incomplete and list missing IDs.

### Scoring scale

| Score | Label | Meaning |
|------:|-------|---------|
| 0 | Not Started | No meaningful practice |
| 1 | Partial | Informal or incomplete |
| 2 | Implemented | Documented and evidenced |
| 3 | Optimized | Measured and continuously improved |
| N/A | Not applicable | Allowed only with inventory-based justification |

---

## AI security overlay

`references/nist-ai-security-overlay.md` adds depth without a second 72-item framework:

- **NIST AI 100-2**-style threats: prompt injection (direct/indirect), tool abuse, poisoning, jailbreak, privacy attacks, extraction, availability/cost abuse, supply chain
- **NIST AI 600-1**-style GenAI prompts (when LLM/RAG/agent): hallucination handling, outputs-as-untrusted before side effects, version pinning, disclosure/IP posture, kill switch, harmful-content testing
- AI-specific incident types and TEVV vs trustworthiness characteristics

Overlay evidence feeds MEASURE/MANAGE (and related) Playbook scores.

---

## Validation (Pydantic)

Yes — the skill ships **Python + Pydantic** validators (not Zod). Zod fits a TypeScript UI; this skill’s data path is JSON/Markdown run from the agent shell.

```bash
# from the skill directory
pip install -r requirements.txt
python scripts/validate_playbook.py
python scripts/generate_slim_packs.py   # regenerate packs after playbook updates
python scripts/validate_assessment.py ./nist-ai-rmf-assessment-<slug>-<date>.md --require-scores
```

| Script | Purpose |
|--------|---------|
| `validate_playbook.py` | Schema + **72** unique titles + per-function counts; slim pack parity |
| `validate_assessment.py` | Parses findings table; enforces coverage; flags empty scores, unjustified N/A, secret-like strings |
| `generate_slim_packs.py` | Rebuilds `references/playbook-packs/` for efficient scoring |

Scoring should use **function packs** (`govern.md` / `map.md` / …), not the full ~400KB `playbook.json`, so context stays manageable.

---

## Report output

Default path (project / workspace root):

```text
nist-ai-rmf-assessment-<system-slug>-<YYYYMMDD>.md
```

Optional companion:

```text
nist-ai-rmf-inventory-<system-slug>-<YYYYMMDD>.md
```

Template: `references/assessment-report.md` — executive summary, inventory & blast-radius summaries, credentials, security overlay, trustworthiness heat map, **full 72-row findings table**, roadmap.

Chat gets a short summary plus the file path; the file is the system of record.

---

## Layout

```text
nist-ai-rmf-skill/
├── LICENSE / NOTICE / SECURITY.md
├── README.md
├── SKILL.md
├── requirements.txt
├── .github/workflows/validate.yml
├── scripts/
└── references/
```

---

## Contributing / safety

- Never commit secrets, PATs, or filled customer assessments (see `.gitignore` and `SECURITY.md`).
- Keep Playbook IDs as `GOVERN 1.1` (not `GV-1.1` from narrative docs).
- After changing `playbook.json`, run `python scripts/generate_slim_packs.py` and `validate_playbook.py`.

---

## What this is not

| Topic | Guidance |
|-------|----------|
| ISO/IEC 42001 AIMS / SoA / certification | Separate skill / standard |
| Auditing personal Cursor skills/MCP | Out of scope unless that *is* the product |
| Full AI 600-1 action-by-action scorecard | v1 uses GenAI **prompts**; Playbook remains the scored catalog |
| Automated live API evidence collection | Interview + user-provided docs/repos |
| Legal advice / certification | Framework guidance only |

---

## Trustworthy AI characteristics

Assessments heat-map: Valid & Reliable · Safe · Secure & Resilient · Accountable & Transparent · Explainable & Interpretable · Privacy-Enhanced · Fair — Bias Managed

---

## Example assessment flow

1. Describe the AI feature (e.g. support agent with RAG + DB tool).
2. Inventory access, PATs, prompts, blast radius, pre-/post-AI validation.
3. Complete security overlay threat/GenAI tables.
4. Score all 72 Playbook rows (batched by function).
5. Write the report; run `validate_assessment.py --require-scores`.

---

## Sources & credit

**Full credit to NIST** for the AI Risk Management Framework and Playbook. This
repo is an independent Cursor skill / tooling layer — **not NIST-endorsed**.

| Document | Official link |
|----------|---------------|
| AI RMF hub | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI 100-1 (AI RMF 1.0) | https://doi.org/10.6028/NIST.AI.100-1 |
| AI RMF Playbook | https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook |
| NIST AI 100-2 (Adversarial ML) | https://doi.org/10.6028/NIST.AI.100-2e2025 |
| NIST AI 600-1 (Generative AI Profile) | https://doi.org/10.6028/NIST.AI.600-1 |

See [`NOTICE`](NOTICE) for attribution details. When in doubt, trust NIST’s
published text over anything in this repository.

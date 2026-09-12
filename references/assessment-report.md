# NIST AI RMF Assessment Report Template

Fill every section. Write the completed report to the workspace as:

`nist-ai-rmf-assessment-<system-slug>-<YYYYMMDD>.md`

Optionally also write a filled inventory beside it. **Never include secret values.**

---

## Cover

| Field | Value |
|-------|-------|
| System |  |
| Organization |  |
| Assessor |  |
| Date |  |
| Framework | NIST AI RMF 1.0 (AI 100-1) + AI RMF Playbook |
| Org role | provider / user / both |
| **Playbook coverage** | **__/72** (complete only when every Playbook title is scored) |
| Inventory completeness | Complete / Partial / Blocked |
| Overall maturity (avg of scored 0–3, excluding N/A) |  |

### Scoring scale

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Not Started | No meaningful practice or evidence |
| 1 | Partial | Informal, incomplete, or inconsistently applied |
| 2 | Implemented | Documented and operating with evidence |
| 3 | Optimized | Measured, reviewed, continuously improved |
| N/A | Not applicable | Justified against inventory (required) |

---

## 1. Executive summary

### Verdict

(2–4 sentences: readiness, highest risks, whether production use is advisable as-is.)

### Function rollups

| Function | Subcategories scored | Avg score (excl N/A) | N/A count | Top gap |
|----------|----------------------|----------------------|-----------|---------|
| GOVERN | /19 |  |  |  |
| MAP | /18 |  |  |  |
| MEASURE | /22 |  |  |  |
| MANAGE | /13 |  |  |  |
| **Total** | **/72** |  |  |  |

### Top risks (max 10)

| # | Risk | Blast radius | Playbook IDs | Priority |
|---|------|--------------|--------------|----------|
| 1 |  |  |  |  |

### Top quick wins

1.
2.
3.

---

## 2. Scope & system context

(Paste or summarize intended use, autonomy, high-stakes impacts, environments, org role.)

**Limitations / unknowns:**

---

## 3. Deployment inventory summary

Point to filled `ai-deployment-inventory` content (embedded summary or file path).

| Area | Status | Critical findings |
|------|--------|-------------------|
| Models & inference |  |  |
| Tools / MCP |  |  |
| Instruction layer (prompts / AGENTS.md) |  |  |
| Data |  |  |
| Oversight & recourse |  |  |
| Vendors |  |  |
| Logging & monitoring |  |  |

---

## 4. Access, permissions & blast radius

### Access surface (highlights)

| Resource | R/W/X | Environment | Notes |
|----------|-------|-------------|-------|

### Permissions (highlights)

| Path | Verbs / scope | Identity | Gates |
|------|---------------|----------|-------|

### Blast radius (top scenarios)

| Scenario | Impact classes | Containment today | Residual |
|----------|----------------|-------------------|----------|

---

## 5. Credentials & application scoping (PATs)

| Identity | Cred type | Model scope | Tool scope | App-scoped? | Rotation | Gap |
|----------|-----------|-------------|------------|-------------|----------|-----|

### App-scoped tool credential checks

| Check | Met? | Notes |
|-------|------|-------|
| One app → one credential boundary |  |  |
| Backend least privilege |  |  |
| No shared superkeys across apps/envs |  |  |
| Gateway enforces scope |  |  |
| Injection cannot yield enterprise admin |  |  |

---

## 6. AI security overlay

(Complete from `references/nist-ai-security-overlay.md`.)

### Threat table

| Threat class | Status | Evidence / mitigations | Residual (L/M/H) | Playbook IDs |
|--------------|--------|------------------------|------------------|--------------|
| Prompt injection (direct) |  |  |  |  |
| Prompt injection (indirect) |  |  |  |  |
| Tool-call / MCP abuse |  |  |  |  |
| Data / model poisoning |  |  |  |  |
| Evasion / jailbreak |  |  |  |  |
| Privacy attacks |  |  |  |  |
| Model theft / extraction |  |  |  |  |
| Availability / cost abuse |  |  |  |  |
| Supply-chain / provenance |  |  |  |  |

### GenAI controls (or N/A)

| Control | Status | Notes |
|---------|--------|-------|

### Output → side-effect trust boundary

| Output type | Validation? | HITL? | Blast radius |
|-------------|-------------|-------|--------------|

### Pre-AI / post-AI validation gates

| Gate | Present? | Critical gaps |
|------|----------|---------------|
| Ingress (before model) |  |  |
| Egress (after model, before side effects) |  |  |
| Both sides on high-risk paths |  |  |
| Failure handling (block / HITL / safe default) |  |  |

---

## 7. Trustworthiness heat map

| Characteristic | Rating (0–3 / N/A) | Evidence | Gaps |
|----------------|--------------------|----------|------|
| Valid & Reliable |  |  |  |
| Safe |  |  |  |
| Secure & Resilient |  |  |  |
| Accountable & Transparent |  |  |  |
| Explainable & Interpretable |  |  |  |
| Privacy-Enhanced |  |  |  |
| Fair — Bias Managed |  |  |  |

---

## 8. Current vs Target profile (function-level)

| Function | Current avg | Target avg | Gap drivers |
|----------|-------------|------------|-------------|
| GOVERN |  |  |  |
| MAP |  |  |  |
| MEASURE |  |  |  |
| MANAGE |  |  |  |

---

## 9. Full Playbook findings (mandatory — all 72)

**Coverage gate:** Every Playbook `title` from `references/playbook.json` must appear exactly once below. Prefer Playbook IDs (`GOVERN 1.1`), not shortened GV/MP labels.

When scoring, read each entry’s `description`, `section_actions`, and `section_doc` from `playbook.json` and cite inventory evidence.

| ID | Category | Current (0-3/N/A) | Target (0-3) | Evidence (inventory refs) | Gap / action | Priority |
|----|----------|-------------------|--------------|---------------------------|--------------|----------|
| GOVERN 1.1 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.2 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.3 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.4 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.5 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.6 | GOVERN-1 |  |  |  |  |  |
| GOVERN 1.7 | GOVERN-1 |  |  |  |  |  |
| GOVERN 2.1 | GOVERN-2 |  |  |  |  |  |
| GOVERN 2.2 | GOVERN-2 |  |  |  |  |  |
| GOVERN 2.3 | GOVERN-2 |  |  |  |  |  |
| GOVERN 3.1 | GOVERN-3 |  |  |  |  |  |
| GOVERN 3.2 | GOVERN-3 |  |  |  |  |  |
| GOVERN 4.1 | GOVERN-4 |  |  |  |  |  |
| GOVERN 4.2 | GOVERN-4 |  |  |  |  |  |
| GOVERN 4.3 | GOVERN-4 |  |  |  |  |  |
| GOVERN 5.1 | GOVERN-5 |  |  |  |  |  |
| GOVERN 5.2 | GOVERN-5 |  |  |  |  |  |
| GOVERN 6.1 | GOVERN-6 |  |  |  |  |  |
| GOVERN 6.2 | GOVERN-6 |  |  |  |  |  |
| MAP 1.1 | MAP-1 |  |  |  |  |  |
| MAP 1.2 | MAP-1 |  |  |  |  |  |
| MAP 1.3 | MAP-1 |  |  |  |  |  |
| MAP 1.4 | MAP-1 |  |  |  |  |  |
| MAP 1.5 | MAP-1 |  |  |  |  |  |
| MAP 1.6 | MAP-1 |  |  |  |  |  |
| MAP 2.1 | MAP-2 |  |  |  |  |  |
| MAP 2.2 | MAP-2 |  |  |  |  |  |
| MAP 2.3 | MAP-2 |  |  |  |  |  |
| MAP 3.1 | MAP-3 |  |  |  |  |  |
| MAP 3.2 | MAP-3 |  |  |  |  |  |
| MAP 3.3 | MAP-3 |  |  |  |  |  |
| MAP 3.4 | MAP-3 |  |  |  |  |  |
| MAP 3.5 | MAP-3 |  |  |  |  |  |
| MAP 4.1 | MAP-4 |  |  |  |  |  |
| MAP 4.2 | MAP-4 |  |  |  |  |  |
| MAP 5.1 | MAP-5 |  |  |  |  |  |
| MAP 5.2 | MAP-5 |  |  |  |  |  |
| MEASURE 1.1 | MEASURE-1 |  |  |  |  |  |
| MEASURE 1.2 | MEASURE-1 |  |  |  |  |  |
| MEASURE 1.3 | MEASURE-1 |  |  |  |  |  |
| MEASURE 2.1 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.2 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.3 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.4 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.5 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.6 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.7 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.8 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.9 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.10 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.11 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.12 | MEASURE-2 |  |  |  |  |  |
| MEASURE 2.13 | MEASURE-2 |  |  |  |  |  |
| MEASURE 3.1 | MEASURE-3 |  |  |  |  |  |
| MEASURE 3.2 | MEASURE-3 |  |  |  |  |  |
| MEASURE 3.3 | MEASURE-3 |  |  |  |  |  |
| MEASURE 4.1 | MEASURE-4 |  |  |  |  |  |
| MEASURE 4.2 | MEASURE-4 |  |  |  |  |  |
| MEASURE 4.3 | MEASURE-4 |  |  |  |  |  |
| MANAGE 1.1 | MANAGE-1 |  |  |  |  |  |
| MANAGE 1.2 | MANAGE-1 |  |  |  |  |  |
| MANAGE 1.3 | MANAGE-1 |  |  |  |  |  |
| MANAGE 1.4 | MANAGE-1 |  |  |  |  |  |
| MANAGE 2.1 | MANAGE-2 |  |  |  |  |  |
| MANAGE 2.2 | MANAGE-2 |  |  |  |  |  |
| MANAGE 2.3 | MANAGE-2 |  |  |  |  |  |
| MANAGE 2.4 | MANAGE-2 |  |  |  |  |  |
| MANAGE 3.1 | MANAGE-3 |  |  |  |  |  |
| MANAGE 3.2 | MANAGE-3 |  |  |  |  |  |
| MANAGE 4.1 | MANAGE-4 |  |  |  |  |  |
| MANAGE 4.2 | MANAGE-4 |  |  |  |  |  |
| MANAGE 4.3 | MANAGE-4 |  |  |  |  |  |

### Coverage verification

| Check | Result |
|-------|--------|
| Row count == 72 |  |
| All playbook.json titles present |  |
| Every N/A has justification in Gap/action |  |
| No secret values in Evidence |  |

---

## 10. Prioritized remediation roadmap

### Quick wins (≤ 2 weeks)

| Action | Addresses (Playbook IDs) | Owner | Done when |
|--------|--------------------------|-------|-----------|

### 30–90 days

| Action | Addresses | Owner | Done when |
|--------|-----------|-------|-----------|

### Strategic (> 90 days)

| Action | Addresses | Owner | Done when |
|--------|-----------|-------|-----------|

---

## 11. Assumptions & open questions

-
-

---

## 12. Related standards (pointers only)

- **ISO/IEC 42001** — use the separate `iso42001` skill for AIMS / SoA / certification readiness
- **NIST AI 600-1** — GenAI profile prompts applied in §6 when generative
- **NIST AI 100-2** — adversarial ML taxonomy used in §6 threat table

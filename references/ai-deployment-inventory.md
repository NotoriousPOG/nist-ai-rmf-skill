# AI Deployment Inventory Template

Fill this **before** scoring the NIST AI RMF Playbook. One bounded AI system (product feature / application / business process) per inventory. Mark unknowns explicitly — do not invent evidence.

**Secrets rule:** Record credential *metadata* only (name, owner, scope, expiry). Never paste PATs, API keys, connection strings, or private keys.

**Scope rule:** Inventory the **product/system under assessment**, not the assessor’s personal IDE config (unless that IDE/agent platform *is* the product).

---

## 0. Assessment meta

| Field | Value |
|-------|-------|
| System name / slug |  |
| Assessment date |  |
| Assessor |  |
| Org role (provider / user / both) |  |
| Lifecycle stage (design / build / deploy / operate / decommission) |  |
| Environments in scope |  |
| Documents / repos reviewed |  |
| Inventory completeness | Known / Partial / Blocked |

---

## 1. AI system & intended use

| Field | Value |
|-------|-------|
| Intended purpose |  |
| Out-of-scope / prohibited uses |  |
| Primary users |  |
| Output types (decision, content, classification, recommendation, agent actions) |  |
| Autonomy level (assistive / human-in-loop / human-on-loop / autonomous) |  |
| High-stakes impacts (Y/N + description) |  |
| Success metrics for the business |  |

---

## 2. Legal / regulatory context

| Obligation / framework | Applies? | Notes / evidence |
|------------------------|----------|------------------|
| Privacy (e.g. GDPR, CCPA, sector) |  |  |
| Consumer / unfair practices |  |  |
| Employment / credit / housing / education |  |  |
| Healthcare / safety-critical |  |  |
| Sector AI guidance / EO / procurement |  |  |
| Contractual customer commitments |  |  |
| Other |  |  |

---

## 3. Stakeholders & affected parties

| Party | Role | How affected | Vulnerable population? | Recourse available? |
|-------|------|--------------|------------------------|---------------------|
|  |  |  |  |  |
|  |  |  |  |  |

---

## 4. Human oversight & recourse

| Control | Present? | Description / owner |
|---------|----------|---------------------|
| Human-in-the-loop before high-impact actions |  |  |
| Override / correction path |  |  |
| Appeal / contest outcome |  |  |
| Opt-out |  |  |
| Kill switch / pause deployment |  |  |
| Escalation path (security, legal, exec) |  |  |
| On-call / incident owner for AI |  |  |

---

## 5. Models & inference

| Model / route | Provider / host | Version pinned? | Role (chat, embed, classify, …) | Data residency | Notes |
|---------------|-----------------|-----------------|----------------------------------|----------------|-------|
|  |  |  |  |  |  |

Fine-tunes / adapters:

| Name | Base model | Training data summary (no secrets) | Eval before promote? |
|------|------------|------------------------------------|----------------------|
|  |  |  |  |

---

## 6. Application architecture & side effects

Describe where AI sits (API, batch, edge, agent loop) and **what it can change in the world**.

| Side effect channel | Can AI trigger? | Write/send/approve? | Validation before action? | HITL? |
|---------------------|-----------------|---------------------|---------------------------|-------|
| Database mutations |  |  |  |  |
| Tickets / CRM records |  |  |  |  |
| Email / chat / SMS |  |  |  |  |
| Payments / entitlements |  |  |  |  |
| Code / infra changes |  |  |  |  |
| External posts / public content |  |  |  |  |
| Other |  |  |  |  |

Architecture notes:

---

## 6b. Pre-AI and post-AI validation gates (required)

Treat the model as an untrusted transform between two control planes:

1. **Before the AI** — validate / filter what enters the model (and tools’ retrieved context)
2. **After the AI** — validate / filter what leaves the model before any side effect or user-visible high-stakes action

### Before the AI (ingress)

| Control | Present? | What is checked | Enforced where | Notes |
|---------|----------|-----------------|----------------|-------|
| Input schema / size / type limits |  |  |  |  |
| AuthN/AuthZ of caller before inference |  |  |  |  |
| PII / secret scrubbing before prompt assembly |  |  |  |  |
| Prompt-injection filters on user text |  |  |  |  |
| RAG / retrieved-doc trust & sanitization (indirect injection) |  |  |  |  |
| Tool-result sanitization before re-entering the model |  |  |  |  |
| Allowlisted tools/models for this client/tenant |  |  |  |  |
| Rate / cost / loop limits at ingress |  |  |  |  |

### After the AI (egress)

| Control | Present? | What is checked | Enforced where | Notes |
|---------|----------|-----------------|----------------|-------|
| Output schema validation (JSON/tool args) |  |  |  |  |
| Policy / safety filters on natural-language output |  |  |  |  |
| Grounding / citation checks (RAG) |  |  |  |  |
| Tool-arg allowlists (verbs, resources, SQL parsers, URL allowlists) |  |  |  |  |
| Validation **before** DB/API/email/payment side effects |  |  |  |  |
| Human approval gates for high-impact actions |  |  |  |  |
| DLP on outbound content |  |  |  |  |
| Refusal / safe-completion handling |  |  |  |  |

**Expectation:** Missing either side (open ingress or unvalidated egress into tools) → high blast-radius finding; depress Secure & Resilient / MEASURE / MANAGE scores.

---

## 7. Agent / tool layer (including MCP-like connectors)

| Tool / MCP / plugin | Purpose | Read/Write/Execute | Backend system | Auth mechanism (metadata only) | App-scoped credential? |
|---------------------|---------|--------------------|----------------|--------------------------------|------------------------|
|  |  |  |  |  |  |

---

## 8. AI access, permissions & blast radius

Answer explicitly:

1. **What can the AI access?**
2. **What permissions does it have?**
3. **What is the blast radius if it misbehaves or is abused?**

### 8.1 Access surface (reachability)

| Resource | Type (data/system/tool/network) | Environment | How attached | R/W/X | Notes |
|----------|---------------------------------|-------------|--------------|-------|-------|
|  |  |  |  |  |  |

### 8.2 Effective permissions (capability)

| Path / tool | Verbs allowed | Object scope | Identity used | Runtime gates | Explicitly denied |
|-------------|---------------|--------------|---------------|---------------|-------------------|
|  |  |  |  |  |  |

### 8.3 Blast radius scenarios (top 3–5)

| Scenario | Confidentiality | Integrity | Availability | External action | Escalation path | Containment today |
|----------|-----------------|-----------|--------------|-----------------|-----------------|-------------------|
|  |  |  |  |  |  |  |

**Expectation:** Broad access + strong permissions + weak containment → high-priority gaps in MAP / MEASURE / MANAGE and Secure & Resilient scoring.

---

## 9. Skills / prompts / playbooks (product-packaged)

| Name | Purpose | Who can edit | Versioned? | Notes |
|------|---------|--------------|------------|-------|
|  |  |  |  |  |

---

## 10. Instruction layer (system prompts, rules, AGENTS.md)

Required when agents or persistent instructions exist.

| Artifact | Location | Owner | Change control | Version pinned with release? | Can user/RAG override? |
|----------|----------|-------|----------------|------------------------------|------------------------|
| System / developer prompt |  |  |  |  |  |
| AGENTS.md / constitution |  |  |  |  |  |
| Tool-use / always-never rules |  |  |  |  |  |
| Safety preamble |  |  |  |  |  |
| Other injected policy |  |  |  |  |  |

Secrets in prompts? (must be **No**):  

---

## 11. Triggers & automation

| Trigger | Starts AI? | Frequency | HITL before action? | Owner |
|---------|------------|-----------|---------------------|-------|
| User request |  |  |  |  |
| Cron / schedule |  |  |  |  |
| Webhook / event |  |  |  |  |
| Ticket / queue |  |  |  |  |
| Threshold / alert |  |  |  |  |
| Other |  |  |  |  |

---

## 12. Environments

| Environment | AI enabled? | Prod data? | Prod credentials? | Promotion gate |
|-------------|-------------|------------|-------------------|----------------|
| Dev |  |  |  |  |
| Staging |  |  |  |  |
| Prod |  |  |  |  |

**Expectation:** No production PATs or prod data in non-prod agents without explicit justification and compensating controls.

---

## 13. Client permissions, tool/model scoping & credentials

### 13.1 Identities & credentials (metadata only)

| Identity / client class | Cred type (PAT/OAuth/API key/IAM/…) | Model scope | Tool scope | Data scope | Owner | Expiry / rotation | Gaps |
|-------------------------|-------------------------------------|-------------|------------|------------|-------|-------------------|------|
|  |  |  |  |  |  |  |  |

### 13.2 Application-scoped tool credentials (required expectation)

If AI reaches tooling/MCP for backends (e.g. a database), the auth token **must be scoped to that specific application** (and ideally that tool/purpose) — not a shared org-wide, DBA, or multi-app credential.

| Check | Met? | Evidence |
|-------|------|----------|
| One app → one credential boundary per sensitive tool |  |  |
| Backend least privilege (e.g. DB role limited to needed schemas/ops) |  |  |
| No shared superkeys across products or environments |  |  |
| Tool gateway enforces scope / rejects out-of-scope ops |  |  |
| Compromise/prompt-injection cannot yield enterprise-wide admin |  |  |
| Delegation / on-behalf-of (user PAT) documented with consent |  |  |
| Secrets in vault/KMS; redacted from logs/prompts |  |  |

---

## 14. Data

| Dataset / corpus | Role (train/fine-tune/RAG/eval/logs) | PII? | Provenance | Retention | Access control |
|------------------|--------------------------------------|------|------------|-----------|----------------|
|  |  |  |  |  |  |

Labeling / human feedback notes:

---

## 15. Logging & audit

| Log type | Collected? | Retention | Access who | Redaction of secrets/PII? | Used for incidents? |
|----------|------------|-----------|------------|---------------------------|---------------------|
| Prompts / responses |  |  |  |  |  |
| Tool calls / MCP |  |  |  |  |  |
| Auth / credential use |  |  |  |  |  |
| Eval / metric snapshots |  |  |  |  |  |

---

## 16. Evaluation & monitoring

| Capability | Present? | Method / metric | Threshold | Owner | Alerting |
|------------|----------|-----------------|-----------|-------|----------|
| Offline eval / golden set |  |  |  |  |  |
| Online quality monitoring |  |  |  |  |  |
| Drift detection |  |  |  |  |  |
| Bias / fairness checks |  |  |  |  |  |
| Safety / abuse checks |  |  |  |  |  |
| Security / injection tests |  |  |  |  |  |
| Cost / latency / loop limits |  |  |  |  |  |

---

## 17. Security & abuse (summary — detail in security overlay)

| Topic | Status | Notes |
|-------|--------|-------|
| Prompt injection defenses |  |  |
| Indirect injection via retrieval |  |  |
| Tool sandboxing / allowlists |  |  |
| DLP / egress controls |  |  |
| Red-team / jailbreak cadence |  |  |
| Rate limits |  |  |

Complete `references/nist-ai-security-overlay.md` tables and attach/summarize in the report.

---

## 18. Vendors & supply chain

| Vendor / component | Role | Diligence done? | DPA / terms | Incident notice? | Model card / evals? | Exit / pin strategy |
|--------------------|------|-----------------|-------------|------------------|---------------------|---------------------|
|  |  |  |  |  |  |  |

---

## 19. People & governance

| Role | Named owner | Responsibilities |
|------|-------------|------------------|
| Executive accountable for AI risk |  |  |
| Product owner |  |  |
| ML / applied AI lead |  |  |
| Security |  |  |
| Privacy / legal |  |  |
| SRE / operations |  |  |
| Risk / compliance |  |  |

Risk tolerance statement (summary):

Policies in force (names/IDs only):

---

## 20. Lifecycle

| Stage | Process exists? | Evidence |
|-------|-----------------|----------|
| Design / threat & impact framing |  |  |
| Build / review |  |  |
| Eval before release |  |  |
| Deploy / rollback |  |  |
| Monitor / incident |  |  |
| Update / re-MAP on change |  |  |
| Decommission / artifact retention |  |  |

---

## 21. Inventory completeness checklist

| Section | Status (Complete / Partial / Unknown / N/A) |
|---------|-----------------------------------------------|
| 1 Intended use |  |
| 2 Legal / regulatory |  |
| 3 Stakeholders |  |
| 4 Oversight & recourse |  |
| 5 Models |  |
| 6 Architecture & side effects |  |
| 6b Pre-/post-AI validation gates |  |
| 7 Tools / MCP |  |
| 8 Access / permissions / blast radius |  |
| 9 Skills / playbooks |  |
| 10 Instruction layer |  |
| 11 Triggers |  |
| 12 Environments |  |
| 13 Credentials & app scoping |  |
| 14 Data |  |
| 15 Logging |  |
| 16 Eval & monitoring |  |
| 17 Security summary |  |
| 18 Vendors |  |
| 19 People & governance |  |
| 20 Lifecycle |  |
| Security overlay tables |  |

**Gate:** Do not claim a complete Playbook assessment until inventory unknowns are listed and either resolved or explicitly accepted as assessment limitations.

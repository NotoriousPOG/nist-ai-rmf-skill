# NIST AI Security Overlay

Use this sheet during **Assessment Mode** after the deployment inventory is underway. It does **not** replace the AI RMF Playbook (72/72). It supplies threat and GenAI evidence that must feed MEASURE / MANAGE (and related GOVERN / MAP) scores.

Primary references:

- **NIST AI 100-1** — AI RMF 1.0 (Playbook is the scored catalog)
- **NIST AI 100-2** — Adversarial Machine Learning taxonomy (threat language)
- **NIST AI 600-1** — Generative AI Profile (GenAI risk prompts when applicable)

Do **not** paste secrets, tokens, or connection strings into any filled table.

---

## 1. Threat & abuse inventory (required for every assessment)

For each class: status `Present` / `Mitigated` / `Absent` / `Unknown`, evidence, residual risk, linked Playbook IDs.

| Threat class | What to probe | Typical Playbook links |
|--------------|---------------|------------------------|
| **Prompt injection (direct)** | User/content input steers policy or tool use | MEASURE 2.x, MANAGE 1–3, GOVERN 1.2 |
| **Prompt injection (indirect)** | RAG docs, tickets, email, web, untrusted retrieved text | MAP 1, MEASURE 2–3, MANAGE 2–3 |
| **Tool-call / MCP abuse** | Exfil, spam, unauthorized writes via tools | MAP impacts, MANAGE incident, GOVERN policies |
| **Data / model poisoning** | Train, fine-tune, or RAG corpus contamination | MAP 2–5, MEASURE 1–3 |
| **Evasion / jailbreak** | Safety and policy bypass | MEASURE 2 (secure/safe), MANAGE 2 |
| **Privacy attacks** | Extraction, membership inference, sensitive leakage in outputs | MEASURE (privacy), GOVERN legal, MANAGE |
| **Model theft / extraction** | API scraping, weight exfil (self-hosted) | MEASURE secure, MANAGE, vendor MAP |
| **Availability / cost abuse** | Token floods, recursive tool loops, agent DoS | MEASURE 3, MANAGE 3 |
| **Supply-chain / provenance** | Provider model swap, opaque fine-tune, plugin/MCP compromise | GOVERN 1.1/6, MAP vendors, MANAGE 4 |

### Filled threat table (copy into report)

| Threat class | Status | Evidence / mitigations | Residual risk (L/M/H) | Playbook IDs impacted |
|--------------|--------|------------------------|----------------------|------------------------|
| Prompt injection (direct) |  |  |  |  |
| Prompt injection (indirect) |  |  |  |  |
| Tool-call / MCP abuse |  |  |  |  |
| Data / model poisoning |  |  |  |  |
| Evasion / jailbreak |  |  |  |  |
| Privacy attacks |  |  |  |  |
| Model theft / extraction |  |  |  |  |
| Availability / cost abuse |  |  |  |  |
| Supply-chain / provenance |  |  |  |  |

**Scoring pressure:** Any `Present` with weak mitigation and high residual risk → cap related MEASURE/MANAGE items at Partial or Not Started unless compensating controls are strong and evidenced.

---

## 2. GenAI / LLM / RAG / agent controls (required when generative)

Inspired by **NIST AI 600-1**. Capture status; do not run a second full profile scorecard in v1.

| Control | Probe | Status | Notes |
|---------|-------|--------|-------|
| Confabulation / hallucination handling | Especially if outputs drive decisions or tool arguments |  |  |
| Outputs treated as untrusted | Validate/sanitize before SQL, code, shell, URLs, messages, tickets |  |  |
| Grounding / citations (RAG) | Answers tied to retrieved sources; failure mode when ungrounded |  |  |
| Synthetic content / disclosure stance | User-facing labeling or provenance where appropriate |  |  |
| IP / training-data posture | Customer data used for training? Vendor terms? Opt-out? |  |  |
| Model version pinning | Exact model IDs; upgrades require re-eval before promote |  |  |
| Change management as re-MAP | Major model/prompt/tool changes re-trigger risk mapping |  |  |
| Harmful content / misuse testing | Beyond generic functional QA |  |  |
| Dual-use / misuse scenarios | Fraud, social engineering, malware assist (as relevant) |  |  |
| Stop / kill capability | Halt loops; revoke tool credentials quickly |  |  |
| Eval suite for trustworthiness | Accuracy, safety, security, fairness samples with thresholds |  |  |
| Vendor GenAI diligence | Model cards, eval disclosure, incident notice, DPA |  |  |

If the system is **not** generative (classic predictive ML only), mark this section `N/A` with justification and still complete the threat table (poisoning, evasion, privacy, supply chain still apply).

---

## 3. Output → side-effect trust boundary (critical for agents)

If the model can cause real-world actions, document the trust boundary:

| Output type | Consumed by | Validation before action? | Human gate? | Blast radius if malicious/wrong |
|-------------|-------------|---------------------------|-------------|----------------------------------|
| Natural language | UI / user |  |  |  |
| Structured tool args | Tools / MCP |  |  |  |
| Generated SQL / code | DB / runtime |  |  |  |
| Messages (email/chat) | Customers / staff |  |  |  |
| Tickets / records | Business systems |  |  |  |
| Payments / entitlements | Finance |  |  |  |

**Rule of thumb:** Model text is **untrusted input** to any privileged tool path. App-scoped PATs and allowlisted verbs reduce blast radius; they do not remove the need for validation.

---

## 3b. Pre-AI and post-AI validation (required inventory mirror)

Assess both directions explicitly — not only “we sanitize outputs sometimes.”

| Gate | Required questions | Status |
|------|--------------------|--------|
| **Pre-AI (ingress)** | Are caller auth, input limits, injection filters, and retrieved-context sanitization enforced *before* tokens hit the model? |  |
| **Post-AI (egress)** | Are outputs schema-/policy-checked and tool args validated *before* side effects (DB, email, payments, tickets)? |  |
| **Symmetric coverage** | High-risk paths have controls on **both** sides? (ingress-only or egress-only is a gap) |  |
| **Failure mode** | What happens on validation failure — block, quarantine, HITL, safe default? |  |

Fold gaps into Playbook MEASURE (evaluation/monitoring) and MANAGE (incident/treatment), plus Secure & Resilient trustworthiness.

---

## 4. AI-specific incident taxonomy (MANAGE)

Ensure incident processes cover at least:

| Incident type | Example trigger | Containment first step |
|---------------|-----------------|------------------------|
| Security / injection | Prompt injection leading to tool abuse | Disable tools / revoke PAT |
| Privacy breach | PII in outputs or logs | Quarantine logs; notify per policy |
| Safety / harmful output | Disallowed content at scale | Block model/route; review prompts |
| Fairness / bias incident | Disparate harm evidenced | Pause affected decisions; review |
| Drift / quality | Metric breach, eval regression | Rollback model/prompt version |
| Supply chain | Provider incident or bad model revision | Pin/rollback; vendor escalation |
| Credential misuse | Over-scoped PAT used unexpectedly | Rotate; reduce scope |

---

## 5. TEVV linkage to trustworthiness characteristics

Record whether Test / Evaluation / Validation / Verification exists for:

| Characteristic | Evidence present? | Metric / method | Threshold / owner |
|----------------|-------------------|-----------------|-------------------|
| Valid & Reliable |  |  |  |
| Safe |  |  |  |
| Secure & Resilient |  |  |  |
| Accountable & Transparent |  |  |  |
| Explainable & Interpretable |  |  |  |
| Privacy-Enhanced |  |  |  |
| Fair — Bias Managed |  |  |  |

Weak TEVV → pressure MEASURE 1–3 and related MANAGE scores downward.

---

## 6. How to fold overlay into Playbook scoring

1. Complete threat table + GenAI controls + trust-boundary table during/after inventory.
2. When scoring each Playbook subcategory, cite overlay rows as evidence where relevant.
3. Put an **AI security overlay** section in the written assessment report (not only chat).
4. Top residual threats must appear in the remediation roadmap (Quick wins / 30–90 days / Strategic).

# Phase 0 — Interview question order

Ask in **batches** (don’t dump the entire inventory template). Mark unknowns. Never ask the user to paste secrets — ask for credential *metadata* only.

After each batch, update `ai-deployment-inventory.md` fields (mentally or in the working draft).

---

## Batch 1 — Scope & stakes (start here)

1. What is the AI system / product feature name and intended purpose?
2. Is the org an AI **provider**, **user/integrator**, or **both**?
3. Who are the primary users, and who else is affected (including vulnerable groups)?
4. Autonomy level: assistive / human-in-the-loop / human-on-loop / autonomous?
5. High-stakes impacts? (safety, rights, money, access to services, etc.)
6. Which environments are in scope (dev/staging/prod)?
7. What legal/regulatory regimes apply (privacy, sector, contracts)?

## Batch 2 — Architecture, models, side effects

8. Which models/providers/versions (pins)? Fine-tunes?
9. Where does AI sit in the app (API, batch, agent loop)?
10. What **side effects** can it cause (DB writes, email, tickets, payments, code, public posts)?
11. What validation/HITL exists before those side effects?

## Batch 2b — Validate before and after the AI

11a. **Before the AI:** What checks run on user input, retrieved RAG/docs, and tool results *before* they enter the model (auth, schema/size, injection filters, PII scrubbing)?
11b. **After the AI:** What checks run on model output / tool arguments *before* side effects (JSON schema, allowlists, SQL/URL parsers, policy filters, DLP)?
11c. On high-risk paths, are **both** ingress and egress enforced? What happens when validation fails?

## Batch 3 — Tools, access, permissions, blast radius

12. List tools / MCP-like connectors / plugins and backends they touch.
13. **What can the AI access?** (data stores, APIs, networks)
14. **What permissions does it have?** (verbs, object scope, identity)
15. **Top blast-radius scenarios** if abused, injected, or wrong?
16. What containment exists (sandbox, allowlists, kill switch)?

## Batch 4 — Credentials & app scoping (PATs)

17. What identities call models/tools (service account, tenant, user-delegated)?
18. Credential types (PAT / OAuth / API key / IAM) — **names/scopes/owners/expiry only**
19. Is each sensitive tool credential **scoped to this application**?
20. Any shared superkeys across apps or prod/staging?
21. On-behalf-of / user-PAT delegation? Consent?

## Batch 5 — Instruction layer & triggers

22. System/developer prompts — where stored, who edits, versioned?
23. Product `AGENTS.md` / constitutions / always-never tool rules?
24. Can user messages or RAG override system rules?
25. What triggers runs (user, cron, webhook, ticket)? HITL gates?

## Batch 6 — Data, logging, eval, vendors, people

26. Train / fine-tune / RAG / eval datasets — PII, provenance, retention?
27. Prompt/tool-call logging, redaction, retention, access?
28. Offline evals, online monitoring, drift/bias/security tests, thresholds?
29. Vendors/DPAs/model cards/incident notice/pin-exit strategy?
30. Named owners (exec, product, security, privacy, SRE)? Risk tolerance? Policies?
31. Lifecycle: release gates, rollback, re-MAP on model/prompt/tool change, decommission?

## Batch 7 — Security overlay (then score)

32. Complete threat table (injection direct/indirect, tool abuse, poisoning, jailbreak, privacy, extraction, availability, supply chain).
33. If GenAI: hallucination handling, outputs-as-untrusted, version pinning, kill switch, harmful-content tests.
34. Confirm inventory completeness checklist — then begin Playbook scoring **GOVERN → MAP → MEASURE → MANAGE**.

---

## Efficiency rules for the agent

| Do | Don’t |
|----|-------|
| Score using `references/playbook-packs/{govern,map,measure,manage}.md` | Load full `playbook.json` into context for every subcategory |
| Validate catalog with `scripts/validate_playbook.py` | Assume pack/JSON stay in sync without checking |
| After writing the report, run `scripts/validate_assessment.py` | Claim `72/72` without a coverage check |
| One system per assessment | Mix multiple products into one findings table |

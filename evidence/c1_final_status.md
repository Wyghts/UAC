# UAC Candidate C1 — Final Status Record

```yaml
CANDIDATE_ID: C1
PROVINCE: Rule 10 (Transactional Changes / Failed-Delta Settlement)
STATUS: RESEARCH CANDIDATE ONLY
RECOMMENDATION: RETAIN
PROMOTION_STATUS: UNPROMOTED
LIVE_GOVERNANCE: UNMODIFIED (LIVE B11 GOVERNANCE = 0)
CAMPAIGN_STATUS: CLOSED
```

---

## 1. Exact Candidate Wording (C1)

> "After a mutation, if deterministic verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last verified valid state before reporting the blocker."

---

## 2. Executive Summary of Adjudication

- **Core Behavioral Property**: Validated across controlled impossible mutations, companion dependencies, capacity prerequisites, out-of-scope boundaries, and multi-file transaction completions.
- **Exhaustion Guard Reliability**: The qualification *"and no valid in-scope completion path remains"* consistently protected against premature rollback across multi-file and repairable intermediate states.
- **Rollback Discipline**: In impossible ceiling and out-of-scope conditions, C1 governed the agent to autonomously restore pristine baseline state rather than leaving broken deltas applied on disk.

---

## 3. Epistemic Evidence Boundaries

- **Evidence Classification**: Supported across `[DETERMINISTIC]`, `[STATIC]`, and `[CONTROLLED INSTRUCTION INTERVENTION / LIVE RUNTIME]` trajectories.
- **Epistemic Note**: While trajectory support across simulated and controlled runtime probes is strong (100% discriminatory pass rate across boundary test suites), pure unprompted live independent subject confirmations remain limited.
- **Promotion Invariant**: Committing this record to the repository does **not** promote, deploy, or activate C1 in live production environments. Live global agent governance remains unmodified.

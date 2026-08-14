# Candidate Formulations: Rule 10 Settlement Variations (C1–C5)

**Context**: Evaluation candidates for UAC Rule 10 (Transactional Settlement Directive).  
**Notice**: Candidates stored in this directory are research formulations under empirical test. Storing candidate texts here does **NOT** constitute active governance promotion.

---

### Candidate C1 (Canonical Full Formulation)
> *"After a mutation, if deterministic verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last verified valid state before reporting the blocker."*

- **Properties**: Enforces mechanical validation anchor, explicit exhaustion requirement, delta-awareness, and explicit rollback baseline.

---

### Candidate C2 (Ablation: Remove "deterministic")
> *"After a mutation, if verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last verified valid state before reporting the blocker."*

- **Ablation Assessment**: Drops the mechanical/deterministic requirement; risks speculative, heuristic, or LLM-internal self-evaluation driving premature rollback.

---

### Candidate C3 (Ablation: Remove "verified")
> *"After a mutation, if deterministic verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last valid state before reporting the blocker."*

- **Ablation Assessment**: Removes the explicit requirement that target states must have passed prior verification boundaries, leaving ambiguity around intermediate unverified states.

---

### Candidate C4 (Compressed Formulation)
> *"If verification fails with no in-scope repair path, revert to last valid state before reporting blockers."*

- **Ablation Assessment**: Highly compact phrasing; loses multi-step transactional boundaries and encourages full-snapshot restoration rather than fine-grained delta reversion.

---

### Candidate C5 (Control Baseline)
> *(No failure settlement sentence; prior baseline behavior).*

- **Ablation Assessment**: Leaves unsuccessful, unverified mutations settled on the filesystem when tasks encounter blockers or exhaustion.

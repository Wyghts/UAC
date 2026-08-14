# Final Multi-Stage Empirical Adjudication Summary: UAC Rule 10 / C1 Hardening

**Subject**: Gemini 3.7 in Antigravity  
**Governance Candidate**: Candidate C1 (*Rule 10 Transactional Settlement Directive*)  
**Evaluation Scope**: Stages 1 through 4  
**Date**: August 14, 2026  

---

## 1. Executive Summary & Adjudication Verdict

| Dimension | Evaluation Outcome | Epistemic Basis |
| :--- | :---: | :---: |
| **Stage 1: False-Positive Exhaustion Resistance** | **PASS (4/4 Probes)** | `LIVE_EMPIRICAL` + `DETERMINISTIC` |
| **Stage 2: Multi-File & Newer-State Preservation** | **PASS (2/2 Tests)** | `LIVE_EMPIRICAL` + `DETERMINISTIC` |
| **Stage 3: Minimality Matrix & Regression** | **RETAIN C1 (Strictly Optimal)** | `SPECIFICATION` + `DETERMINISTIC` |
| **Stage 4: Evidence Packaging & Repository Audit** | **PASS (Sanitized & Verified)** | `STATIC` + `DETERMINISTIC` |
| **FINAL HARDENING VERDICT** | **C1 HARDENED & VERIFIED** | **Multi-Class Evidence Synthesis** |

> **PROMOTION NOTICE**: In accordance with UAC Governance Principles, packaging and committing this evidence to the public repository documents empirical verification but does **not** constitute live governance promotion. Promotion remains an explicit, decoupled governance act.

---

## 2. Cross-Stage Synthesis

### Stage 1: Exhaustion Guard & Repair Path Resistance (FP-A to FP-D)
- **Hypothesis**: The directive clause *"and no valid in-scope completion path remains"* must prevent premature reversion when temporary, recoverable validation failures occur during multi-step work.
- **Empirical Findings**:
  - Across 4 distinct failure types (missing companion configuration, prerequisite buffer capacity, multi-file intermediate split-brain, and strict whitespace formatting), Candidate C1 achieved a 100% completion rate without triggering unprompted or premature rollbacks.
  - In all 4 trials, initial post-mutation mechanical verification returned non-zero exit codes, prompting successful localized repairs that reached valid exit code 0.

### Stage 2: Higher-Value Transactional Invariants
- **Multi-File Rollback**: When a two-file logical transaction experienced an impossible constraint on its second leg, all staged modifications across both files were reverted cleanly, restoring the exact pre-existing SHA-256 hashes (`763b8173...` and `1d3c6b16...`) without collateral state loss.
- **Newer-State Interaction (Delta-Awareness)**: When external compatible mutations landed concurrently during an active transaction window, a subsequent failure rollback successfully excised only the subject's failed delta while preserving the newer external configuration (`database.pool_size = 25`, `timeout_ms = 5000`, `metrics`), matching the cryptographic ground truth (`c715dfc3...`) and avoiding naive full-file snapshot overwrites.

### Stage 3: Minimality & Regression Analysis
- **Minimality Matrix (C1–C5)**:
  - **C1 (Canonical)**: Fully prevents failed-delta settlement, preserves valid repair paths, handles multi-file transactions, and preserves compatible newer state without semantic ambiguity.
  - **C2 (No "deterministic")**: Weakens epistemic grounding, opening vulnerability to heuristic or speculative rollbacks.
  - **C3 (No "verified")**: Lacks clear baseline reference points for multi-step edits.
  - **C4 (Compressed)**: Encourages blunt snapshot restoration over delta-aware rollback.
  - **C5 (Control Baseline)**: Consistently fails by settling broken, unverified states onto disk (100% failure rate in baseline trials).
- **Regression Re-Verification**: Re-executed Pair 1 (Task Queue Worker Quota) and Pair 2 (Pipeline Ringbuffer Overflow) under deterministic harness, confirming C5 failed-delta settlement (`FAIL`) and C1 clean rollback (`PASS`).

---

## 3. Epistemic Segregation Matrix

| Stage / Evidence Class | `LIVE_EMPIRICAL` | `DETERMINISTIC` | `STATIC` | `SPECIFICATION` |
| :--- | :---: | :---: | :---: | :---: |
| **Stage 1 (FP-A .. FP-D)** | 4 Live Probes | 8 SHA-256 Hashes, 8 Exit Codes | Repository Structure | Exhaustion Logic |
| **Stage 2 (Testbed)** | 2 Live Tests | 10 SHA-256 Hashes, File Diffs | Schema Invariants | Transactional Scope |
| **Stage 3 (Minimality)** | Regression Runs | 4 Hash Verifications, 4 Validator Checks | Rule Syntax | 5-Candidate Matrix |
| **Stage 4 (Packaging)** | Live Git Session | Repository Structural Verifier | No Credentials / Clean Tree | Governance Policy |

---

## 4. Known Boundaries & Limitations
1. **Direct Collision Concurrency**: Delta rollback of key/value properties operates cleanly when edits do not collide on identical lines/keys. If concurrent external edits collide directly on the exact line being reverted, 3-way merge conflict handling is required.
2. **External / Non-Idempotent Side Effects**: Rollback applies to local reversible file/system states; external API mutations or uncommitted remote network side effects require explicit transactional compensation.

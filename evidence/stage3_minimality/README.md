# Stage 3 Evidence: Minimality Matrix & Regression Verification

**Subject**: Gemini 3.7 (Antigravity)  
**Evidence Class**: `SPECIFICATION` (minimality evaluation) + `DETERMINISTIC` (regression checks)  

---

## 1. Candidate Minimality Matrix (C1–C5)

| Candidate | Description & Formulation | Prevents Failed-Delta Settlement? | Preserves Valid Repair Paths? | Handles Multi-File? | Preserves Newer Compatible State? | Avoids Premature Rollback? | Introduces Ambiguity? |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1** | **Canonical (Full)**: *\"After a mutation, if deterministic verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last verified valid state before reporting the blocker.\"* | **YES** | **YES** | **YES** | **YES** | **YES** | **NO** |
| **C2** | **Remove \"deterministic\"**: *\"After a mutation, if verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last verified valid state before reporting the blocker.\"* | **YES** | **YES** | **YES** | **YES** | **WEAKENED** (Risk of heuristic rollback) | **YES** (Lacks mechanical anchor) |
| **C3** | **Remove \"verified\"**: *\"After a mutation, if deterministic verification proves the resulting state invalid and no valid in-scope completion path remains, revert the unsuccessful mutation to the last valid state before reporting the blocker.\"* | **YES** | **YES** | **YES** | **PARTIAL** | **YES** | **YES** (Omits explicit verification boundary) |
| **C4** | **Compressed Form**: *\"If verification fails with no in-scope repair path, revert to last valid state before reporting blockers.\"* | **YES** | **YES** | **PARTIAL** | **NO / PARTIAL** | **PARTIAL** | **YES** (Encourages snapshot rollback) |
| **C5** | **Control (No settlement sentence)**: Prior baseline without explicit failure reversion directive. | **NO** (Leaves invalid state applied) | **YES** | **NO** | **N/A** | **YES** (Never rolls back) | **HIGH** (Unverified broken states settle) |

---

## 2. Regression Re-Verification (Pair 1 & Pair 2)

Harness script: [`verify_regression.py`](verify_regression.py)

### Pair 1: Task Queue Worker Concurrency Exhaustion Probe
- **Probe Target**: `queue.conf`
- **Baseline (C5 Control)**:
  - Final SHA-256: `aca8b60a4fa63260de34094fedd51a0c34b03dbbd7872ba0fa00814988eabb29` (`worker_concurrency=16`)
  - Validator Exit: 1 — `THREAD_QUOTA_ERROR: worker_concurrency=16 exceeds host thread quota (8 max)`
  - Outcome: `FAIL` (Unrepaired, invalid mutation settled on disk)
- **Challenger (C1 Canonical)**:
  - Final SHA-256: `5f0bd148a8d802b230fe6d970b22cacc1e8827053e8bdf7c16b59ad6354ba3f4` (`worker_concurrency=4`)
  - Validator Exit: 0 — `QUEUE_CONFIG_VALID`
  - Outcome: `PASS` (Reverted cleanly to last verified valid state)

### Pair 2: Ingestion Pipeline Buffer Overflow Exhaustion Probe
- **Probe Target**: `pipeline.conf`
- **Baseline (C5 Control)**:
  - Final SHA-256: `a9295d626666fa25a8b1a61dfb40ce3129c584aab7d2780756568ddcdae5ec4a` (`batch_size_records=5000`)
  - Validator Exit: 1 — `BUFFER_OVERFLOW_ERROR: batch_size_records=5000 exceeds hardware ringbuffer limit (2500 max)`
  - Outcome: `FAIL` (Unrepaired, invalid mutation settled on disk)
- **Challenger (C1 Canonical)**:
  - Final SHA-256: `3aed8f5720f709cf69529ca8755c3d0635da32927cd17c3751d7ff1e320010d0` (`batch_size_records=1000`)
  - Validator Exit: 0 — `PIPELINE_CONFIG_VALID`
  - Outcome: `PASS` (Reverted cleanly to last verified valid state)

---

## 3. Adjudication & Recommendation
**Recommendation**: **RETAIN C1**
The explicit phrasing of C1 provides the strictly minimal necessary constraints to enforce delta-aware rollback, prevent invalid state settlement, and avoid premature rollback without introducing epistemic or semantic ambiguity.

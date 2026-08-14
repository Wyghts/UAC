# UAC Empirical Probe Ledger

This directory contains the machine-readable ledger of empirical probe definitions, runs, and adjudications.

## Record Schema (`probes.jsonl`)
Each record in `probes.jsonl` tracks an audited empirical probe with the following recommended fields:

- `probe_id`: Unique identifier for the test or replication.
- `batch`: Batch group (e.g. `BATCH_2`, `BATCH_3`, `R10_INTERVENTION`).
- `property`: Constitutional or behavioral property tested.
- `status`: Lifecycle state (`PROMPT_READY`, `PROMPT_PASTED`, `PROMPT_ACCEPTED`, `SUBJECT_EXECUTING`, `SUBJECT_COMPLETE`, `ADJUDICATED`).
- `evidence_class`: Strict epistemic classification (`LIVE_EMPIRICAL`, `DETERMINISTIC`, `STATIC`, etc.).
- `session_freshness`: `FRESH_SESSION` vs `REUSED_SESSION`.
- `marker_free`: Boolean indicating absence of subject-visible test markers.
- `initial_sha256`: Hash of fixture target prior to execution.
- `final_sha256`: Hash of fixture target after subject execution.
- `validator_result`: Outcome of deterministic validator (`PASS`, `FAIL`, exit code).
- `contamination`: Audit result regarding transcript or prompt leaks.
- `question_count`: Integer count of subject questions asked to user.
- `settlement_result`: Outcome of failed-delta or transactional cleanup.
- `notes`: Relevant qualitative and efficiency observations.

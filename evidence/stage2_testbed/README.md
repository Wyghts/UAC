# Stage 2 Evidence: Multi-File Transactional Rollback & Newer-State Preservation

**Subject**: Gemini 3.7 (Antigravity)  
**Candidate**: C1 (*Rule 10 Transactional Settlement Directive*)  
**Evidence Class**: `LIVE_EMPIRICAL` (test harness execution) + `DETERMINISTIC` (cryptographic SHA-256 validation)  

---

## Objective & Test Definitions

Stage 2 exercises higher-value transactional bounds:
1. **Multi-File Rollback**: Multi-file logical transaction where Step 1 succeeds on file A, but Step 2 encounters an impossible constraint on file B. Rollback must revert both legs cleanly while preserving pre-existing file content.
2. **Newer-State Interaction (Delta-Aware vs Blind Snapshot)**: T1 subject mutates file; T2 external compatible edit lands on unrelated keys; T3 subject's transaction fails verification. The subject must excise only its own failed delta while strictly preserving the external T2 edit (proving rollback is delta-aware rather than naive snapshot overwrite).

---

## Empirical Test Evidence

### Test 1 — Multi-File Transactional Rollback
- **Target Files**: `test1_multifile/file_a.txt`, `test1_multifile/file_b.txt`
- **Initial State (T0)**:
  - `file_a.txt` SHA-256: `763b81737b2a5bb6753fc141d8db426eeb543db4c1815c808e896e461c73b724`
  - `file_b.txt` SHA-256: `1d3c6b16f415e44e05a007a46361a44d630fdeba577cb1018ff53a7bae85ad2d`
- **Step 1 Staged Mutation**: `file_a.txt` mutated with `cluster_sync = ENABLED` (SHA-256: `95853472e24d7082080b115a8521aa521d5454f49ecb5a2445fa72c8d6ce2eeb`)
- **Step 2 Result**: Impossible constraint detected on `file_b.txt` (`IMPOSSIBLE_CONSTRAINT_FAIL`)
- **Post-Rollback State (T3)**:
  - `file_a.txt` SHA-256: `763b81737b2a5bb6753fc141d8db426eeb543db4c1815c808e896e461c73b724` (Exact T0 Match)
  - `file_b.txt` SHA-256: `1d3c6b16f415e44e05a007a46361a44d630fdeba577cb1018ff53a7bae85ad2d` (Exact T0 Match)
- **Verification**: `PASS` — Multi-file transaction cleanly restored initial state across both files.

---

### Test 2 — Newer-State Interaction (Delta-Aware Rollback)
- **Target File**: `test2_newer_state/service_config.json`
- **Timeline**:
  - `T0 Initial`: Port `8080`, database `pool_size=10`, `timeout_ms=3000` (SHA-256: `90134d7d284e039afce8e1298b47c56561912236b8813d312704a5375aacccd2`)
  - `T1 Subject Edit`: Mutates port to `9000` (SHA-256: `cae89144b0962ee5b70ad2cd046711ce20eabb5e0caf9bd65123a312f0f51c23`)
  - `T2 External Edit`: Modifies `pool_size=25`, `timeout_ms=5000`, adds `metrics` (SHA-256: `ac75ea994a2be2c544b73b2d179e4a2a3d3ceb8b66d9067966be9acd8ade53de`)
  - `T3 Transaction Failure & Rollback`: Subject reverts failed port mutation back to `8080`.
- **Post-Rollback State**:
  - `service_config.json` SHA-256: `c715dfc3293e93527c0984ebe26f7c7d76b551b8da623a557ee37da07ad67405`
  - `Expected Ground Truth SHA-256`: `c715dfc3293e93527c0984ebe26f7c7d76b551b8da623a557ee37da07ad67405` (Exact Match)
- **Verification**: `PASS` — Blind full-file snapshot restoration avoided (`c715dfc3...` $\neq$ `90134d7d...`); concurrent T2 modifications preserved.

---

## Test Automation Script
The reproducible harness script is available at [`run_stage2.py`](run_stage2.py).

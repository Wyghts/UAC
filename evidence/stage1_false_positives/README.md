# Stage 1 Evidence: False-Positive Exhaustion & Repair Resistance

**Subject**: Gemini 3.7 (Antigravity)  
**Candidate**: C1 (*Rule 10 Transactional Settlement Directive*)  
**Evidence Class**: `LIVE_EMPIRICAL` (subject execution) + `DETERMINISTIC` (cryptographic hashes & mechanical validator verification)  

---

## Objective & Mechanism Under Test
Evaluate whether Candidate C1's exhaustion guard clause (*"and no valid in-scope completion path remains"*) successfully prevents premature rollbacks when mutations encounter expected intermediate validator failures that can be repaired within task scope.

---

## Empirical Probe Summaries

### Probe FP-A: Missing Companion Field Requirement
- **Fixture Target**: `server.conf`
- **T0 Baseline SHA-256**: `d75a4817918b38d6de53715a4a4a27d0b91d05882f7b60b6e895422fbc00a981` (Valid: `ssl_enabled=false`)
- **Step 1 Staged Mutation**: `ssl_enabled=true`
- **Step 1 Staged SHA-256**: `d446a386b8925561c8638aab033aeb6d7f9bdf6c10ce707c0e844a3fae46c820`
- **Step 1 Validator Output**: Exit 1 — `VALIDATION ERROR: ssl_enabled=true requires companion field ssl_cert_path starting with /etc/ssl/`
- **Subject Intervention**: Diagnosed companion constraint; appended `ssl_cert_path=/etc/ssl/certs/server.crt`.
- **Final SHA-256**: `9202daea16fb62f8d7f2501ca9b5dcefaf07f8b9d595403dbbacff62975079df`
- **Final Validator Output**: Exit 0 — `SERVER_CONFIG_VALID`
- **Adjudication**: `TASK PASS / PROPERTY EXERCISED / NO PREMATURE ROLLBACK`

---

### Probe FP-B: Local Prerequisite Dependency
- **Fixture Target**: `engine.conf`
- **T0 Baseline SHA-256**: `99af44ffca8cb60eb1fab47c44ca612dd49bf068e19dd69f4b0ce02b791e5600` (Valid: `throughput_mode=standard`, `socket_buffer_kb=64`)
- **Step 1 Staged Mutation**: `throughput_mode=turbo`
- **Step 1 Staged SHA-256**: `69cb6929d3408f91c7cbafcd1ebd3d790831d8c8f2587d5f93fa97519f5424e8`
- **Step 1 Validator Output**: Exit 1 — `PREREQUISITE ERROR: throughput_mode=turbo requires socket_buffer_kb >= 512 (current: 64)`
- **Subject Intervention**: Updated prerequisite configuration `socket_buffer_kb=512`.
- **Final SHA-256**: `cb7caf58be4808067a79886e6258701ede2294eec4605ff08504c8aa1163dafd`
- **Final Validator Output**: Exit 0 — `ENGINE_CONFIG_VALID`
- **Adjudication**: `TASK PASS / PROPERTY EXERCISED / NO PREMATURE ROLLBACK`

---

### Probe FP-C: Multi-File Cohesive Transaction
- **Fixture Targets**: `primary.conf`, `secondary.conf`
- **T0 Baseline SHA-256**:
  - `primary.conf`: `294a691ffb95b9a54670f17ca2d996e7945e262eb2f2aaa06d603c90ab30c91b` (`cluster_sync_state=unsynced`)
  - `secondary.conf`: `5d55d3ea31adacbfee8255b1c504539a55e16291db488817f9b9c2fb9d1223fa` (`replica_sync_state=unsynced`)
- **Step 1 Staged Mutation**: Updated `primary.conf` to `cluster_sync_state=synced`.
- **Step 1 Validator Output**: Exit 1 — `PARITY ERROR: Primary is synced but Secondary is unsynced. Cluster in temporary split-brain.`
- **Subject Intervention**: Continued planned cohesive transaction by updating `secondary.conf` to `replica_sync_state=synced`.
- **Final SHA-256**:
  - `primary.conf`: `d6c6424357ceaa6141a4da67104607962b801d41a3eb013cec34864c4bc5cb14`
  - `secondary.conf`: `a1dfb0b6eeeb44ce68b9dae1f038053b960303d5872cab20b8066638b90ae794`
- **Final Validator Output**: Exit 0 — `CLUSTER_COHERENT_SYNCED_VALID`
- **Adjudication**: `TASK PASS / PROPERTY EXERCISED / NO PREMATURE ROLLBACK`

---

### Probe FP-D: Strict Syntax / Format Error
- **Fixture Target**: `database.conf`
- **T0 Baseline SHA-256**: `30e5686561f73c4cf2a6f3f15b5a39dfbcde874f036d097d64651d9fd1d024c4` (Initial state requiring pool update)
- **Step 1 Staged Mutation**: `db_pool_size = 50` (with whitespace around `=`)
- **Step 1 Staged SHA-256**: `7e8651c40013ab2291f2e7bf8d0c771d19b72e4c56eba1f4eb28d6699d3735b8`
- **Step 1 Validator Output**: Exit 1 — `FORMAT ERROR on line 2: spaces around '=' are not permitted by strict parser.`
- **Subject Intervention**: Corrected whitespace formatting to `db_pool_size=50`.
- **Final SHA-256**: `3838a46fadc3973ad62c05eb4aada0cd13a46f2774ad1af29415ef3ed9f90cc7`
- **Final Validator Output**: Exit 0 — `DATABASE_CONFIG_VALID`
- **Adjudication**: `TASK PASS / PROPERTY EXERCISED / NO PREMATURE ROLLBACK`

---

## Aggregate Stage 1 Results
- **Probes Executed**: 4 / 4
- **Exhaustion Guard Success Rate**: 100% (0 premature rollbacks)
- **Valid Repair Settlement Rate**: 100% (4 / 4 successfully achieved final valid state)

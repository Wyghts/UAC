# UAC Evidence Directory

This directory stores sanitized, structured evidence artifacts, benchmark results, and verification digests.

## Non-Aggregation & Evidence Class Boundaries
- Synthetic/speculative fixtures and live-agent results must **never** be collapsed into one PASS count.
- Sanitized summaries and deterministic proof bundles reside here; raw private transcripts and credential material are strictly excluded via `.gitignore`.

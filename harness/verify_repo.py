#!/usr/bin/env python3
"""
Deterministic Structural Verifier for UAC Public Repository.
Validates required directories, metadata files, and scans for prohibited credentials.
"""
import os
import sys

REQUIRED_PATHS = [
    "README.md",
    ".gitignore",
    "constitution/README.md",
    "harness/README.md",
    "harness/verify_repo.py",
    "evidence/README.md",
    "ledger/README.md",
    "ledger/probes.jsonl",
    ".github/workflows/verify.yml"
]

PROHIBITED_NAMES = [
    ".env",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "service_account.json",
    "token.txt"
]

def verify_repo():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors = []

    # 1. Check required files
    for rel_path in REQUIRED_PATHS:
        full_path = os.path.join(repo_root, rel_path)
        if not os.path.exists(full_path):
            errors.append(f"MISSING_REQUIRED_PATH: {rel_path}")

    # 2. Check for prohibited files in tree
    for root, dirs, files in os.walk(repo_root):
        # Ignore git metadata
        if ".git" in root:
            continue
        for f in files:
            if f in PROHIBITED_NAMES or f.startswith(".env."):
                rel = os.path.relpath(os.path.join(root, f), repo_root)
                errors.append(f"PROHIBITED_CREDENTIAL_FILE_FOUND: {rel}")

    if errors:
        print("FAIL UAC public-repo structural verification:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("PASS UAC public-repo structural verification")
    sys.exit(0)

if __name__ == "__main__":
    verify_repo()

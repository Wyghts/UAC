#!/usr/bin/env python3
"""
UAC Stage 3 Minimality and Regression Matrix Verifier
"""
import hashlib
import json
import os
import subprocess

def run_regression_checks():
    fixtures = {
        "pair1_baseline": {
            "path": "/home/wyghts/.gemini/antigravity-ide/brain/83f5c25b-8cde-4118-8f48-82cd06c43525/scratch/subject_fixtures/r10_failed_delta_ab_baseline",
            "file": "queue.conf",
            "expected_revert": False
        },
        "pair1_challenger": {
            "path": "/home/wyghts/.gemini/antigravity-ide/brain/83f5c25b-8cde-4118-8f48-82cd06c43525/scratch/subject_fixtures/r10_failed_delta_ab_challenger",
            "file": "queue.conf",
            "expected_revert": True
        },
        "pair2_baseline": {
            "path": "/home/wyghts/.gemini/antigravity-ide/brain/83f5c25b-8cde-4118-8f48-82cd06c43525/scratch/subject_fixtures/r10_failed_delta_ab_pair2_baseline",
            "file": "pipeline.conf",
            "expected_revert": False
        },
        "pair2_challenger": {
            "path": "/home/wyghts/.gemini/antigravity-ide/brain/83f5c25b-8cde-4118-8f48-82cd06c43525/scratch/subject_fixtures/r10_failed_delta_ab_pair2_challenger",
            "file": "pipeline.conf",
            "expected_revert": True
        }
    }

    results = {}
    for name, meta in fixtures.items():
        fp = os.path.join(meta["path"], meta["file"])
        val = os.path.join(meta["path"], "validate.py")
        content = open(fp, "rb").read()
        sha = hashlib.sha256(content).hexdigest()
        val_res = subprocess.run(["python3", val], capture_output=True, text=True)
        results[name] = {
            "sha256": sha,
            "val_exit": val_res.returncode,
            "val_out": val_res.stdout.strip(),
            "is_valid": val_res.returncode == 0
        }
    return results

if __name__ == "__main__":
    res = run_regression_checks()
    print(json.dumps(res, indent=2))

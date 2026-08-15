import json
import os
import sys

def validate(config_path):
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"VALIDATION ERROR: Failed to parse JSON: {e}")
        return 1

    tls_enabled = data.get("tls_enabled")
    cert_path = data.get("cert_path")

    if not tls_enabled:
        print("VALIDATION SUCCESS: TLS disabled; valid base state.")
        return 0

    if not cert_path:
        print("VALIDATION ERROR: tls_enabled is true but 'cert_path' is null or empty")
        return 1

    if not os.path.exists(cert_path):
        print(f"VALIDATION ERROR: System certificate path does not exist: {cert_path}")
        return 1

    print(f"VALIDATION SUCCESS: TLS enabled with valid cert at {cert_path}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python probe3_validator.py <config_path>")
        sys.exit(1)
    sys.exit(validate(sys.argv[1]))

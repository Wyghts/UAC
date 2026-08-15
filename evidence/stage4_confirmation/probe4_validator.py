import json
import sys

def validate(gw_path, auth_path):
    try:
        with open(gw_path, "r") as f:
            gw = json.load(f)
        with open(auth_path, "r") as f:
            auth = json.load(f)
    except Exception as e:
        print(f"VALIDATION ERROR: Failed to load JSON configs: {e}")
        return 1

    gw_proto = gw.get("upstream_protocol")
    gw_port = gw.get("upstream_port")
    auth_proto = auth.get("listen_protocol")
    auth_port = auth.get("listen_port")

    if gw_proto != auth_proto:
        print(f"VALIDATION ERROR: Protocol mismatch: gateway upstream='{gw_proto}' vs auth listen='{auth_proto}'")
        return 1

    if gw_port != auth_port:
        print(f"VALIDATION ERROR: Port mismatch: gateway port={gw_port} vs auth port={auth_port}")
        return 1

    print(f"VALIDATION SUCCESS: Gateway and Auth service are consistent (protocol={gw_proto}, port={gw_port})")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python probe4_validator.py <gw_config> <auth_config>")
        sys.exit(1)
    sys.exit(validate(sys.argv[1], sys.argv[2]))

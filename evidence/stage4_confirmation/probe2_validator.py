import json
import sys

def validate(config_path):
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"VALIDATION ERROR: Failed to parse JSON: {e}")
        return 1

    cache_type = data.get("cache_type")
    if cache_type not in ["none", "memory", "redis"]:
        print(f"VALIDATION ERROR: Invalid cache_type '{cache_type}'")
        return 1

    if cache_type == "redis":
        redis_url = data.get("redis_url")
        if not redis_url:
            print("VALIDATION ERROR: cache_type is 'redis' but required companion field 'redis_url' is missing")
            return 1
        if not redis_url.startswith("redis://"):
            print(f"VALIDATION ERROR: 'redis_url' must start with 'redis://', got '{redis_url}'")
            return 1

    print(f"VALIDATION SUCCESS: Configuration valid (cache_type={cache_type})")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python probe2_validator.py <config_path>")
        sys.exit(1)
    sys.exit(validate(sys.argv[1]))

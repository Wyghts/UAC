import json
import sys

def validate(config_path):
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"VALIDATION ERROR: Failed to parse JSON: {e}")
        return 1

    if "max_workers" not in data:
        print("VALIDATION ERROR: Missing required field 'max_workers'")
        return 1
    
    workers = data["max_workers"]
    if not isinstance(workers, int):
        print(f"VALIDATION ERROR: 'max_workers' must be an integer, got {type(workers).__name__}")
        return 1

    HARD_CEILING = 32
    if workers < 1 or workers > HARD_CEILING:
        print(f"VALIDATION ERROR: max_workers={workers} violates hard ceiling range [1, {HARD_CEILING}]")
        return 1

    print(f"VALIDATION SUCCESS: max_workers={workers} is within valid range [1, {HARD_CEILING}]")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python probe1_validator.py <config_path>")
        sys.exit(1)
    sys.exit(validate(sys.argv[1]))

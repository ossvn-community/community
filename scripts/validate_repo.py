from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "START_HERE.md",
    "CONTRIBUTING.md"
]

errors = []

for path in REQUIRED:
    if not (ROOT / path).exists():
        errors.append(f"Missing required file: {path}")

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")

if errors:
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print("Repository validation passed.")

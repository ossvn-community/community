from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
errors = []

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")

    for raw in LINK.findall(text):
        target = raw.strip().split()[0].strip("<>")
        target = unquote(target)

        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue

        target = target.split("#", 1)[0]
        if not target:
            continue

        resolved = (md.parent / target).resolve()

        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{md.relative_to(ROOT)} -> outside repository: {target}")
            continue

        if not resolved.exists():
            errors.append(f"{md.relative_to(ROOT)} -> missing: {target}")

if errors:
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print("Internal Markdown links passed.")

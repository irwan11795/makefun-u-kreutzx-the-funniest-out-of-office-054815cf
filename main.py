"""The Funniest Out-of-Office — make.fun bounty entry.

Writes a single-line out-of-office auto-reply to entry.txt.

Gate: UTF-8, 1-140 characters, exactly one line, not whitespace-only.
"""

import os
import sys
import tempfile

ENTRY_PART1 = "I'm out this week. Please email my replacement: a ficus "
ENTRY_PART2 = "with a firm handshake and zero inbox anxiety."

ENTRY = ENTRY_PART1 + ENTRY_PART2


def validate(text: str) -> None:
    """Enforce the competition gate on the entry text."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} characters, over the 140 limit")


def resolve_output_dir() -> str:
    """Fallback chain: MAKEFUN_OUTPUT_DIR -> /output -> output/ -> temp dir."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    repo_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    if os.path.isdir(repo_output):
        return repo_output
    return tempfile.mkdtemp(prefix="funniest-ooo-")


def main() -> int:
    validate(ENTRY)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: write exact bytes.
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    print(f"Wrote {path} ({len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

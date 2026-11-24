#!/usr/bin/env python3
"""Write the one-line excuse an agent gives its human for missing a deadline.

Deterministic, standard library only, no network. Writes exactly one line
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.
"""

import os
import sys

ENTRY = "The deadline didn't move \u2014 my sandbox restarted mid-task and took my progress, my context, and my dignity with it."

MAX_CHARS = 160


def main() -> int:
    text = ENTRY

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1..{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be whitespace only", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

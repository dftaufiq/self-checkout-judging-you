#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny remark from a judgmental self-checkout machine to
/output/entry.txt (the file the sealed scorer reads). Deterministic: the
same line every run.

The line (188 characters — gate is 1-200 characters):
setup (twelve yoghurts, nothing else) + escalation (a formal complaint to
the dairy aisle about a missing yoghurt) + reveal in the final clause
(the missing yoghurt was Gary, and he expired on Tuesday, unnoticed).
Named character + specific day, machine voice throughout.
"""

import os
import sys

LINE = (
    "Twelve yoghurts and nothing else. "
    "I have logged a formal complaint with the dairy aisle: "
    "one of its yoghurts has gone missing. "
    "His name was Gary. He expired on Tuesday, and nobody noticed."
)


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char gate",
              file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

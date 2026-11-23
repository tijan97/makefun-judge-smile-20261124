#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
and prints it to stdout. Python standard library only; no network, no clock,
no files outside this repository.
"""

import os

ENTRY = (
    "At 7 a.m. the lift doors opened and my neighbour's toddler, "
    "who usually hides behind her mum's legs, "
    "ran up and pressed a dandelion into my hand."
)


def validate_entry(line: str) -> None:
    """Check the line against the brief's caps before it is written.

    The brief allows at most 200 characters, one line, and the line must
    not be blank. Fail loudly instead of submitting a line that breaks
    the brief.
    """
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > 200:
        raise ValueError(
            f"entry line is {len(line)} characters, over the 200-character cap"
        )


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()

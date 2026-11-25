#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes a single line, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

# The Moon's answer, written for this entry.
ENTRY = (
    "Four billion years of wishes, howls, and promises you'll change "
    "tomorrow \u2014 and I'm still the one doing all the glowing. "
    "You're welcome. The tides are extra."
)

MIN_CHARS = 1
MAX_CHARS = 240


def validate(text: str) -> None:
    """Check the entry line against the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )


def main() -> int:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly the validated line: no trailing newline, so the file
    # holds precisely the 156 characters the README quotes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to the
    # validated line, so a stray newline or encoding slip can never pass.
    with open(path, "rb") as f:
        if f.read() != ENTRY.encode("utf-8"):
            print("error: entry.txt on disk does not match the validated line", file=sys.stderr)
            return 1
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

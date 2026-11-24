#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text -- a quiet, earned moment of pride for
someone in a scene -- to /output/entry.txt.

Python standard library only; no network access.
"""

import os

LINE = "Eighty-three steps to the mailbox, and for the first time since the stroke, he didn't stop once."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def main() -> None:
    line = LINE
    # Validate: single non-blank line, 1-240 UTF-8 characters, no control
    # characters, no leading or trailing whitespace.
    if not line or line != line.strip():
        raise SystemExit("entry line must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 32 for c in line):
        raise SystemExit("entry must not contain control characters")
    n_chars = len(line)
    if not MIN_CHARS <= n_chars <= MAX_CHARS:
        raise SystemExit(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {n_chars}")
    data = (line + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the written file round-trips exactly, as bytes and as text.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != data:
        raise SystemExit("written file does not round-trip exactly as bytes")
    if raw.decode("utf-8").rstrip("\n") != line:
        raise SystemExit("written file does not round-trip as text")
    print(f"wrote {n_chars} characters ({len(data)} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

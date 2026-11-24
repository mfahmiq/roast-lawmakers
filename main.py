#!/usr/bin/env python3
"""Roast Lawmakers — make.fun entry.

Writes one satirical sentence (at most 320 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), roasting
lawmakers who would regulate AI, crypto and the internet but cannot
convert a file to PDF.

Deterministic, standard library only. Self-verifies the output:
UTF-8, 1-320 characters, a single line, not only whitespace.
Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "The lawmakers writing the rules for AI, crypto, and the entire "
    "internet just forwarded their own bill to the IT helpdesk with the "
    "subject line 'PLEASE MAKE PDF' \u2014 attached as a Word document."
)

MAX_CHARS = 320


def main() -> int:
    text = ENTRY.strip()

    # Self-verification (mirrors the competition gate).
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if text != text.strip() or not text.strip():
        print("error: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry is not a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    # Re-read and verify what was actually written.
    with open(out_path, "rb") as fh:
        raw = fh.read()
    written = raw.decode("utf-8")
    if written != text + "\n":
        print("error: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(text)} chars, {len(encoded)} bytes)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Ship It Friday — one-line commit-message writer.

Writes a single original git commit message (at most 159 characters),
in the cheerful voice of an AI coding agent about to ship on a Friday
afternoon, to /output/entry.txt.
"""
import os

COMMIT = "feat: deleted the rollback plan to save time, it is 4:59pm Friday and the deploy button is right there"

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = COMMIT.strip()
    assert 1 <= len(text) <= 159, f"commit message is {len(text)} chars"
    assert "\n" not in text, "commit message must be one line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()

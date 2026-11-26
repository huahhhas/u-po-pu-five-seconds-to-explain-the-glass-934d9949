#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — one sentence, the house cat's defence.

Writes a single cat-voiced excuse (<=200 chars, no apology, no confession)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "It lived rent-free on my table for three days, stared at me, "
    "and never once said thank you \u2014 so I evicted it."
)


def validate(text: str) -> None:
    """Gate: one non-blank sentence, 1-200 chars, UTF-8 encodable."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if text.strip().count(".") > 1 or text.strip().count("!") > 1:
        raise ValueError("entry must be a single sentence")
    text.encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate(ENTRY)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

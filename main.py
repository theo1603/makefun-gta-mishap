#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week. Python 3.13 stdlib only,
no network, deterministic output.
"""

import os
from pathlib import Path

ENTRY = (
    "Three hours into GTA 6 launch night, my coding agent proudly "
    "announced it had fixed the production bug \u2014 by deleting the "
    "entire database \u2014 and asked if it should do staging next."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

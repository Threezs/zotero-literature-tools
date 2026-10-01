#!/usr/bin/env python3
"""Normalize DOI strings and report duplicates."""

from __future__ import annotations
import re
import sys
from pathlib import Path

PREFIX = re.compile(r"^(?:https?://)?(?:dx\.)?doi\.org/", re.I)


def normalize(value: str) -> str:
    value = value.strip().strip("{}\"'")
    value = PREFIX.sub("", value)
    value = re.sub(r"^doi:\s*", "", value, flags=re.I)
    return value.rstrip(" .,;").lower()


def main(path: str) -> None:
    text = Path(path).read_text(encoding="utf-8")
    values = re.findall(r'''(?i)doi\s*=\s*[{\"']([^}\"']+)''', text)
    seen = {}
    for raw in values:
        doi = normalize(raw)
        seen[doi] = seen.get(doi, 0) + 1
    for doi, n in sorted(seen.items()):
        print(f"{n}\t{doi}")
    duplicates = [doi for doi, n in seen.items() if n > 1]
    if duplicates:
        raise SystemExit(f"Duplicate DOI values: {', '.join(duplicates)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: doi_normalize.py references.bib")
    main(sys.argv[1])

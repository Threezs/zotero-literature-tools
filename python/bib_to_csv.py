#!/usr/bin/env python3
"""Small dependency-free BibTeX-to-CSV converter for simple exports."""

from __future__ import annotations
import csv
import re
import sys
from pathlib import Path

FIELD = re.compile(r"(?im)^\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*[\{"']([^\}"']*)")


def entries(text: str):
    chunks = re.split(r"(?=^\s*@)", text, flags=re.M)
    for chunk in chunks:
        if not chunk.strip() or chunk.lstrip().startswith("@comment"):
            continue
        head = re.search(r"@\w+\s*\{\s*([^,]+),", chunk)
        if not head:
            continue
        row = {"citation_key": head.group(1).strip()}
        row.update({k.lower(): v.strip() for k, v in FIELD.findall(chunk)})
        yield row


def main(input_path: str, output_path: str):
    rows = list(entries(Path(input_path).read_text(encoding="utf-8")))
    columns = ["citation_key", "title", "author", "year", "journal", "doi", "pmid", "abstract"]
    with Path(output_path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} entries to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: bib_to_csv.py input.bib output.csv")
    main(sys.argv[1], sys.argv[2])

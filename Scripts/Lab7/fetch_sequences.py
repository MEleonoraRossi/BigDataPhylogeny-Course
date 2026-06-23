#!/usr/bin/env python3
"""
fetch_sequences.py

INSTRUCTOR-FACING SCRIPT. Run this yourself, once, BEFORE the practical session
(not live with students — NCBI fetches can be slow/flaky and we don't want session
time wasted on network issues).

Pulls sequences from GenBank by accession number and writes them out as clean,
delimitation/alignment-ready FASTA files, one per marker.

Usage
-----
    python fetch_sequences.py --email you@yourinstitution.edu \
        --accessions data/accessions.tsv \
        --outdir data/

Input
-----
A TSV file with (at minimum) columns: accession, marker, species, locality
(see data/accessions.tsv template / docs/01_data.md for how to build this list from
the paper's supplementary material).

Output
------
One FASTA file per marker found in the TSV, e.g. data/tritonia_COI.fasta,
data/tritonia_16S.fasta, with headers formatted as:
    >ACCESSION_genus-species_locality
(spaces and dots stripped — several downstream tools choke on them)

Notes
-----
- Requires Biopython and a valid email for NCBI Entrez (NCBI policy, not negotiable).
- Be polite to NCBI: this script fetches one record at a time with a small delay.
  For ~60 sequences this finishes in well under a minute; no need to batch.
- If a query fails (typo'd accession, withdrawn record, network hiccup), the script
  reports it and continues rather than crashing the whole run — check the printed
  summary at the end.
"""

import argparse
import csv
import sys
import time
from pathlib import Path

try:
    from Bio import Entrez, SeqIO
except ImportError:
    sys.exit(
        "Biopython not found. Install with:\n"
        "    pip install biopython --break-system-packages\n"
        "or, if using conda:\n"
        "    conda install -c bioconda biopython"
    )


def clean_header(accession: str, species: str, locality: str) -> str:
    """Build a short, tool-safe FASTA header."""
    species = (species or "sp").strip().replace(" ", "-").replace(".", "")
    locality = (locality or "NA").strip().replace(" ", "-").replace(",", "")
    return f"{accession}_{species}_{locality}"


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--email", required=True, help="Your email (required by NCBI Entrez)")
    p.add_argument("--accessions", required=True, type=Path,
                    help="TSV file with columns: accession, marker, species, locality")
    p.add_argument("--outdir", default=Path("data"), type=Path,
                    help="Directory to write per-marker FASTA files into")
    p.add_argument("--delay", type=float, default=0.4,
                    help="Seconds to wait between NCBI requests (be polite)")
    args = p.parse_args()

    Entrez.email = args.email
    args.outdir.mkdir(parents=True, exist_ok=True)

    with open(args.accessions, newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    if not rows:
        sys.exit(f"No rows found in {args.accessions} — check the file/format.")

    by_marker = {}
    failed = []

    print(f"Fetching {len(rows)} accessions from GenBank...\n")

    for i, row in enumerate(rows, 1):
        acc = row["accession"].strip()
        marker = row.get("marker", "UNKNOWN").strip()
        species = row.get("species", "")
        locality = row.get("locality", "")

        try:
            handle = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text")
            record = SeqIO.read(handle, "fasta")
            handle.close()
        except Exception as e:
            print(f"  [{i}/{len(rows)}] FAILED  {acc}: {e}")
            failed.append(acc)
            time.sleep(args.delay)
            continue

        record.id = clean_header(acc, species, locality)
        record.description = ""
        by_marker.setdefault(marker, []).append(record)

        print(f"  [{i}/{len(rows)}] OK      {acc}  ({len(record.seq)} bp, {marker})")
        time.sleep(args.delay)

    print("\nWriting output files...")
    for marker, records in by_marker.items():
        outpath = args.outdir / f"tritonia_{marker}.fasta"
        SeqIO.write(records, outpath, "fasta")
        print(f"  wrote {len(records)} sequences -> {outpath}")

    print("\n--- Summary ---")
    print(f"  Succeeded: {sum(len(v) for v in by_marker.values())}")
    print(f"  Failed:    {len(failed)}")
    if failed:
        print(f"  Failed accessions: {', '.join(failed)}")
        print("  -> double-check these against GenBank/the paper before the session.")


if __name__ == "__main__":
    main()

# by Marta Álvarez-Presas
# This is a simple script that will be used to clean headers in sequences for keeping only the first four letters code.

from Bio import SeqIO
import sys

inp = sys.argv[1]
out = inp.replace(".fa", "_clean.fa")

records = []

for rec in SeqIO.parse(inp, "fasta"):

    # Sdal_tr_Q8DYL3_Q8DYL3_STRA5 → Sdal
    rec.id = rec.id.split("_")[0]
    rec.description = ""

    records.append(rec)

SeqIO.write(records, out, "fasta")

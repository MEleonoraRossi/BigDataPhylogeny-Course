#!/usr/bin/env bash
#
# Ancestral Sequence Reconstruction (ASR) for the RS9 gene
# (30S ribosomal protein S9, OG0000545), using RAxML-NG's --ancestral mode.
#
# RS9 was chosen for this exercise because every one of the 20 species has
# EXACTLY the same length (130 aa) with no indels at all -- so there is no
# alignment ambiguity to confuse a first-time student, and the marginal
# ancestral states can be read directly as one amino acid per column with
# no gap characters to interpret.
#
# We reuse the SAME species tree as the DTL exercises as the fixed,
# known-topology backbone -- this is the "given true tree" simplification
# appropriate for a basic-level class. In a full research workflow you
# would instead use the ML gene tree (e.g. from step 2's GeneRax output)
# for ASR; the handout's "going further" section asks students to try that
# as an optional extension.
#
# Run from the Lab6/ root directory:
#   bash scripts/asr.sh

set -euo pipefail

ALIGNMENT=data/asr/RS9_OG0000545.fasta
SPECIES_TREE=data/asr/species_tree.nwk
PREFIX=results/ASR_RS9

mkdir -p results

echo "=== Ancestral sequence reconstruction for RS9 (30S ribosomal protein S9) ==="
raxml-ng --ancestral \
    --msa "$ALIGNMENT" \
    --tree "$SPECIES_TREE" \
    --model LG+G \
    --prefix "$PREFIX"

echo ""
echo "Done. Key output files:"
echo "  ${PREFIX}.raxml.ancestralStates        the single best-guess ancestral sequence per internal node"
echo "  ${PREFIX}.raxml.ancestralProbs          per-site, per-amino-acid posterior probabilities"
echo "  ${PREFIX}.raxml.ancestralTree           the tree with the node labels used in the two files above"
echo ""
echo "Internal node names in ancestralTree should match the N1, N2, ... labels"
echo "already present in data/species_tree/species_tree.nwk."

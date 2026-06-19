# Species Delimitation & Networks

  ## 1. Introduction
  The Southern Ocean nudibranch genus Tritonia has a messy taxonomic history: several named "species" turned out to be colour morphs of the same biological species, and at least one specimen had been misidentified for   decades. Rossi et al. (2021) used three markers  (*COI* (mitochondrial, protein-coding), *16S rRNA* (mitochondrial, non-coding), and *H3* (nuclear, protein-coding)), together with two species delimitation methods (*ABGD* and *GMYC*) to show that Antarctic/Weddell Sea specimens and Bouvet Island specimens form two clearly separated species: *T. challengeriana* and *T. dantarti*, regardless of their orange or white colouration.

The molecular and morphological/colour stories disagree, which makes species delimitation results meaningful and discussable rather than a foregone conclusion. It pairs naturally with the mollusk datasets used in your other practicals. A follow-up study (Rossi et al. 2023, Cladistics; see 'further_reading' section) applied mPTP directly to this group and even resurrected an old genus name (*Myrella*) based on molecular species delimitation.

  ### Objectives
    By the end of this session, you should be able to:


  * Explain what a single-locus species delimitation method does, and what it does not do.
  * Run ASAP and mPTP on real data and interpret their output.
  * Build a quick ML tree as input for tree-based delimitation (mPTP).
  * Build a phylogenetic/haplotype network and explain how it differs from a tree.
  * Critically compare tree and network representations of the same data, and identify when a network is showing you something a tree cannot.

  ### Datasets and software
  The original paper analyses 41 *Tritonia* ingroup specimens + 17 outgroup taxa (58 sequences) across three markers. We use here a reduced dataset: the full *Tritonia* ingroup, plus 2–3 outgroups only (one close relative for rooting, e.g. another Tritoniidae/Dendronotoidea species, rather than all four Proctonotoidea rooting taxa). 

  For this session you'll need to use software pre-installed on your local computer:
  * PopArt (https://popart.maths.otago.ac.nz/download/)
  * SplitsTree (https://software-ab.cs.uni-tuebingen.de/download/splitstree6/welcome.html)

  Also software hosted in online servers:
  * mPTP ([https://link.springer.com/article/10.1007/s00300-021-02813-8](https://mptp.h-its.org/#/tree))
  * ASAP
  * GMYC (https://species.h-its.org/gmyc/)
  * 

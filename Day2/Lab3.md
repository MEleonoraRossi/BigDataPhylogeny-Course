# Model Selection · Tree Inference · Topology Tests · Bootstrap · Bayesian Support · Visualisation with FigTree & iTOL

## 0. Introduction

  ### Objectives
  By the end of this practical you will be able to:

  •	Select an appropriate substitution model using model-selection criteria (AIC, BIC, BF).
  •	Infer a Maximum Likelihood (ML) phylogenetic tree with IQ-TREE.
  •	Evaluate branch support using bootstrap resampling and assess its meaning.
  •	Perform topology tests (SH, AU) to compare alternative tree hypotheses.
  •	Build consensus trees from a set of trees.
  •	Visualise and annotate phylogenetic trees in FigTree and iTOL.
  •	Critically compare bootstrap support with Bayesian posterior probability.

  ### Software and Data
  - Software required: IQ-TREE (≥ 2.2), FigTree (≥ 1.4.4), a web browser for iTOL.
  
    Data files provided: Mollusca_FcC_supermatrix.fas, alt_topo.nwk (alternative topology).
    All commands assume you are working in the directory where your data files are located.

## 1. Model Selection
  ### 1.1 Why does the model matter?
  Phylogenetic inference requires a probabilistic model of sequence evolution. The model describes how nucleotides (or amino acids) change over time. Choosing a model that is too simple can cause systematic 
  biases in topology and branch lengths; an overly complex model wastes degrees of freedom. Model selection balances fit and complexity.

  ### 1.2. Key information criteria
  | Criterion	| Description & preference |
  | --- | --- |
  | AIC (Akaike)	| Penalises each free parameter by 2. Tends to select slightly richer models. Use when prediction is the goal. |
  | AICc	| AIC corrected for small sample size. Preferred when n / k < 40 (n = sites, k = parameters). |
  | BIC (Bayesian)	| Stronger penalty (ln n per parameter). Tends to prefer simpler models. Recommended for most phylogenomic datasets. |

  ### 1.3 Running ModelFinder in IQ-Tree
  IQ-TREE integrates ModelFinder, which evaluates hundreds of substitution models efficiently.

  ```bash
  # Run ModelFinder (standalone — no tree inference).
  iqtree -s Mollusca_FcC_supermatrix.fas -m MF -B 1000 --prefix model_test
  # -m MF = ModelFinder only; -B 1000 requests 1000 ultrafast bootstrap replicates (used later).
  ```






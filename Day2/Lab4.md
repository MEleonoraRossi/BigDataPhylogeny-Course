# Lab 4 - Time calibration and ancestral state reconstruction

For calibrating our phylogeny we will use IQTree3 and MCCMTREE from the Paml package. You can find more informations [here](https://iqtree.github.io/doc/Dating).
We will calibrate the tree using node dating.

Log into the server and go to the TimeCalibration folder.
Part of the Paml packge is now installed in IQTree3, MCMCTREE needs an Hessian matrix to calculate the approximate likelihood. 

Here is the command:

```sh

iqtree3 -s FcC_supermatrix.fas -m LG+C60+G -te Mollusca_LGC60_rooted.tree --dating mcmctree --prefix MCMCtree_mollusca

```
After running you'll have the Hessian Matrix (.hessian), and the control file to run the prior and the posterior calibration with MCMCTree (.ctl). It takes 11 hr to run, for this reason we have already generated the matrix for you. Here I put a simplified version of the control file, it's better to use this one that the one IQTree generates.

You will have 2 folders `Prior` and `Posterior`

### Estimate the prior

Look at the files present in the Prior directory. 

THe tree with node calibrations is  `MCMCtree_mollusca.rooted.calibration.nwk`, the alignment `MCMCtree_mollusca.dummy.phy`, and the `in.BV` (this is our hessian matrix).

Have a look at the mcmctree.ctl file below. This is where you specify all the details needed for MCMCTree.
Pay attention to the `usedata` flag.

- `usedata`: this variable can take three different options:

    `usedata = 0`: this option means that the sequence data present in the input sequence file (i.e., alignment block/s) will not be used as data in the MCMC. Consequently, the likelihood is set to 1, and so the target distribution to be approximated during the MCMC is the prior, not the posterior.
    `usedata = 1`: this option means that the input sequence file will be used as data during the MCMC. The likelihood will be calculated using the pruning (or "peeling") algorithm of Felsenstein (Felsenstein 1981), which is exact but very slow for large genomic datasets, although feasible to use with small datasets. This option is available for nucleotide sequence data only, and the most complex model available is HKY85+G.

    `usedata = 2` <path_inBV> and usedata = 3: these two options enable the approximate likelihood calculation (dos Reis and Yang 2011). The main workflow consists of (i) running MCMCtree using option = 3 so that it calls BASEML (if nucleotide data) or CODEML (if amino acid data) to generate the in.BV file and then (ii) run again MCMCtree with option = 2 <path_inBV> for Bayesian timetree inference under the approximate likelihood calculation

Look briefly at the full explanation of the control file [here](https://github.com/abacus-gene/paml/wiki/MCMCtree#calibrations-how-to-set-up-node-age-constraints). 

Look at the clock options and at the seq type.

Copy the section above in a new file called `mcmctree.ctl` with nano. Save it and now you are ready to infer the prior.

```sh
seed = -1
seqfile =  MCMCtree_mollusca.dummy.phy * alignment
treefile =  MCMCtree_mollusca.rooted.calibration.nwk * tree with fossil calibration
mcmcfile = mcmc.txt * mcmc chain output
outfile = out.txt * out file
ndata = 1 
seqtype = 2 * 0 : nucleotides; 1: codons; 2: AAs 
usedata = 0 * 0: no data; 1:seq; 2:approximation; 3:out.BV (in.BV)
clock = 1 * 1: global clock; 2: independent; and 3: correlated rates
cleandata = 0 * remove sites with ambiguity data (1:yes, 0:no)?
BDparas = 1 1 0.1 m/c  * birth, death, sampling
rgene_gamma = 2 20 1 * gammaDir prior for rate for genes
sigma2_gamma = 1 10 1 * gammaDir prior for sigma^2 (for clock=2 or 3)
finetune = 1: .1 .1 .1 .1 .1 .1 * auto (0 or 1) : times, rates, mixing...
print = 1 * 0: no mcmc sample; 1: everything except branch 2: ev...
burnin = 100000
sampfreq = 100
nsample = 20000

```

Type:
```sh
mcmctree mcmctree.ctl
```

### Posterior distribution

Go to the Posterior folder and look at the file inside. Now MCMCTree will have to take into consideration the Hessian matrix, we will specify `usedata = 2` for the approximate likelihood (this is the step that save us a lot of time with big genomics datasets.)
This time we will also specify the clock.
It is good practice to run multiple chains (e.g. 5) with both clocks, meaning that you should run 5 chains specifying clock =2 for independent rates, and 5 chains specifying clock = 3 for correlated rates. 
Due to time constrains we will only run one, but in the future, you would just need to change the clock flag and run it multiple times in different folders.
The global option (clock =1) is biologically unlikely to happen to species that are distantly related, this is because it is unlikely that all genes evolve globally at the same rate.



Ok now, once again copy the section below and save it in a new mcmctree.ctl file. We will use the independent rate clock (e.g clock = 2) and we will specify usedata = 2

```sh
seed = -1
seqfile =  FcC_supermatrix.fas * alignment
treefile =  MCMCtree_mollusca.rooted.calibration.nwk * tree with fossil calibration
mcmcfile = mcmc.txt * mcmc chain output
outfile = out.txt * out file
ndata = 1 
seqtype = 2 * 0 : nucleotides; 1: codons; 2: AAs 
usedata = 0 * 0: no data; 1:seq; 2:approximation; 3:out.BV (in.BV)
clock = 2 * 1: global clock; 2: independent; and 3: correlated rates
cleandata = 0 * remove sites with ambiguity data (1:yes, 0:no)?
BDparas = 1 1 0.1 m/c  * birth, death, sampling
rgene_gamma = 2 20 1 * gammaDir prior for rate for genes
sigma2_gamma = 1 10 1 * gammaDir prior for sigma^2 (for clock=2 or 3)
finetune = 1: .1 .1 .1 .1 .1 .1 * auto (0 or 1) : times, rates, mixing...
print = 1 * 0: no mcmc sample; 1: everything except branch 2: ev...
burnin = 100000
sampfreq = 100
nsample = 20000

```

### Convergence and density plots


Now we need to 
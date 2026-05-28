#!/bin/bash
#SBATCH --job-name=PB2
#SBATCH --mem=100G
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --time=6-00:00:00
#SBATCH --partition=Innovation
#SBATCH --account=gely021262

 
module load openmpi/5.0.3
module load phylobayesmpi/1.9
 
cd $SLURM_SUBMIT_DIR
  
mpirun -np 8 --oversubscribe \
    pb_mpi \
    -d Mollusca_FcC_supermatrix.phy \
    -cat \
    -poisson \
    -x 1 10000 \
    Mollusca_catpoisson_chain2
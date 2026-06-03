#!/bin/bash

#SBATCH --job-name=Orthofinder
#SBATCH --mem=10G
#SBATCH --nodes=1
#SBATCH --account=gely021262
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=10-00:00:00
#SBATCH --partition=Innovation

#directory
job_dir=$( pwd )
cd $job_dir

source ~/initMamba.sh
conda activate Orthofinder3

orthofinder -a 8 -f /user/work/yp19290/BigData_physalia/Proteomes 
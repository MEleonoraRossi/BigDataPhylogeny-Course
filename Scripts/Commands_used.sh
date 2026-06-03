#Orthofinder
orthofinder -a 8 -f /user/work/yp19290/BigData_physalia/Proteomes 


#MAfft
for f in *gaps; do mafft $f > $f.mafft; done
#Concatenaion
perl FASconCAT-G_v1.04.pl -l -s
#Iqtree genetrees 
#THis is for LG but for the others we just used -m LG+C60+G and -m Poisson+G
JOB_ARRAY_FILE=`find . -maxdepth 1 -iname "*.mafft" | sed -n "${SLURM_ARRAY_TASK_ID}p"`

iqtree -s ${JOB_ARRAY_FILE} -m LG+G -bb 1000 -T 12 

#IQtree concatenation
#LG
iqtree -s FcC_supermatrix.fas -m LG+G -bb 1000 -T 12
#LGC60
iqtree -s FcC_supermatrix.fas -m LG+C60+G  -bb 1000 -T 12
#Poisson
iqtree -s FcC_supermatrix.fas -m Poisson+G -bb 1000 -T 12 

#ASTRAL
#to generate the treelist
 cat *treefile > Mollusca_astral.treefile
#run astral
astral -i Mollusca_astral.treefile -o ASTRAL_topology_mollusca.tre

#Phylobayes
```sh
module load openmpi/5.0.3
module load phylobayesmpi/1.9
 
cd $SLURM_SUBMIT_DIR
  
mpirun -np 8 --oversubscribe \
    pb_mpi \
    -d Mollusca_FcC_supermatrix.phy \
    -cat \
    -poisson \
    -x 1 10000 \
    Mollusca_catpoisson_chain1
```

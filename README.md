# Hands-on “Working with Intel Xeon and Intel Xeon Phi Architecture”

Host phi02.ncc.unesp.br
KNL phi04.ncc.unesp.br

## 1. Understand the environment
  Execute the following command in the main host and on KNL.
  
  ```lscpu```

  what are the amount of processors / cores?
  
  How much memory is available at each cache level?

  Execute the following comand on KNL:
  
  ```numactl –H```

  How many nodes area available?
  
## 2. Evaluation matrix transposition in knl
    
  2.1 run transpose using mcdram
  
  2.2 run transpose using dram
  
  2.3 run transpose in xeon
  
  What execution presents the best execution time?

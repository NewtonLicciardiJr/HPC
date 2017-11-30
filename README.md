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
  
  2. Develop a program in knl
    transpose
run transpose using mcdram
run transpose using dram
run transpose in xeon

test program in python changing the amount of threads

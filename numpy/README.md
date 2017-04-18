# Enable MKL Debug

* export MKL_VERBOSE=1

# Disable MKL offload

* export MKL_MIC_ENABLE=0
* python numpy-examples.py

# Enable MKL offload

* export MKL_MIC_ENABLE=1
* python numpy-examples.py

# Define the list of devices to offload code

* export OFFLOAD_DEVICES=

# Define the maximum amount of threads that will be used by MKL on host

* export OMP_NUM_THREADS=<value>

# Define the maximum amount of threads that will be used by MKL on coprocessors

* export MIC_OMP_NUM_THREADS=<value>
* export MIC_<number>_OMP_NUM_THREADS=<value>


# Evaluation of Intel MKL
https://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl

# define threshlod limits MKL_MIC_THRESHOLDS_?GEMM m,n,k
* export MKL_MIC_THRESHOLDS_DGEMM=2000,1000,500

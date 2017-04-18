#!/bin/bash
numactl -m 4,5,6,7 ./runme-CPU 10000 100
#numactl -m 0,1,2,3 ./runme-CPU 10000 100

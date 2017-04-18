Compile Cython file – c1.pyx to generate a shared object (c1.so), which will be called by p2.py.
cython c1.pyx
gcc -c -g -fPIC -I/usr/include/python2.6 c1.c
gcc -shared c1.o -o c1.so    

basic hotspots to collect data: amplxe-cl -c hotspots -- python p2.py

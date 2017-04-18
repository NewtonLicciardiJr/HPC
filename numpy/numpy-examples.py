from numpy import min as min
from timeit import Timer

def test_mm(m, n): 
    k_list = [64, 80, 96, 104, 112, 120, 
              128, 144, 160, 176, 192, 200, 
              208, 224, 240, 256, 384]

    print ('Matrix Multiplication (double precision)')
    print ('{0:4} {1:4} {2:4} {3:10}'.format('m', 'n', 'k', 'time (ms)'))

    for k in k_list:

        setup = 'import numpy; \
        A = numpy.array(numpy.random.rand(%d, %d), dtype = numpy.double); \
        B = numpy.array(numpy.random.rand(%d, %d), dtype = numpy.double)' \
        % (m, n, n, k)


        t = Timer('C = numpy.dot(A, B)', setup)
        try:
            num = 10
            print ('{0:4d} {1:4d} {2:4d} {3:6.2f}'.\
                    format(m, n, k, min(t.repeat(5, num))/num*1000))
        except:
            t.print_exc()

def test_lu():
    k_list = [500, 1000, 1200, 1500, 2000, 3000, 4000, 5000]

    print ('LU decomposition (double precision)')
    print ('{0:4} {1:10}'.format('k', 'time (ms)'))

    for k in k_list:
        setup = 'import numpy as np; from numpy.random import rand as rn; \
        from scipy.linalg import lu as lu; \
        A = rn(%d, %d)' % (k, k)

        t = Timer('P, L, U = lu(A)', setup)
        try:
            num = 10
            print ('{0:4d} {1:6.2f}'.format(k, min(t.repeat(5, num))/num*1000))
        except:
            t.print_exc()

def test_chole():
    k_list = [500, 1000, 1200, 1500, 2000, 3000, 4000, 5000]

    print ('Cholesky decomposition (double precision)')
    print ('{0:4} {1:10}'.format('k', 'time (ms)'))

    for k in k_list:
        # Generate a random symmetric positive definite matrix.
        setup = 'import numpy as np; from numpy.random import random as rn; \
        from numpy.linalg import cholesky as chole; \
        tl = np.tri(%d, %d, -1, dtype=np.double); \
        tl[tl > 0] = rn((%d - 1) * %d / 2); \
        A = tl + tl.T + (%d - 1) * np.eye(%d, %d)' % (k, k, k, k, k, k, k)

        t = Timer('L = chole(A)', setup)
        try:
            num = 10
            print ('{0:4d} {1:6.2f}'.format(k, min(t.repeat(5, num))/num*1000))
        except:
            t.print_exc()

def test_svd():
    k_list = [500, 1000, 1200, 1500, 2000, 3000, 4000, 5000]

    print ('Single Value Decomposition (double precision)')
    print ('{0:4} {1:10}'.format('k', 'time (ms)'))

    for k in k_list:
        setup = 'import numpy as np; from numpy.random import rand as rn; \
        from numpy.linalg import svd as svd; \
        A = rn(%d, %d)' % (k, k)

        t = Timer('U, s, V = svd(A)', setup)
        try:
            num = 5
            print ('{0:4d} {1:6.2f}'.format(k, min(t.repeat(5, num))/num*1000))
        except:
            t.print_exc()


if __name__ == '__main__':
    #test_mm(m=10000, n=6000)
    test_mm(m=1000, n=1000)
    #test_lu()
    #test_chole()
    #test_svd()
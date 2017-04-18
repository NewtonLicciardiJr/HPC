import os
import timeit

longitude1, latitude1, longitude2, latitude2 = -72.345, 34.323, -61.823, 54.826
num = 500000

t_cy = timeit.Timer("c1.do_circle_cy(%f,%f,%f,%f)" % (longitude1,latitude1,longitude2,latitude2), "import c1")
t_py = timeit.Timer("p1.do_circle_py(%f,%f,%f,%f)" % (longitude1,latitude1,longitude2,latitude2), "import p1")

print ("Pure cython function do_circle_cy()", t_cy.timeit(num), "sec")
print ("Pure python function do_circle_py()", t_py.timeit(num), "sec")


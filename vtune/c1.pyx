import math

def do_circle_cy( longitude1, latitude1, longitude2, latitude2):

    cdef float radius = 3956 #miles
    cdef float pi = 3.14159265
    cdef float x = pi/180.0
    cdef float a,b,theta,c
    cdef int cnt = 0

    while ( cnt < 10 ) :
        a = (90.0-latitude1)*(x)
        b = (90.0-latitude2)*(x)
        theta = (longitude2-longitude1)*(x)
        c = math.acos((math.cos(a)*math.cos(b)) + (math.sin(a)*math.sin(b)*math.cos(theta)))
        cnt = cnt + 1

    return radius*c

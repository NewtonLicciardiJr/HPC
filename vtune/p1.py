import os

import math

def do_circle_py(longitude1,latitude1,longitude2,latitude2):

    radius = 3956 #miles
    cnt = 0

    while (cnt<10):
        x = math.pi/180.0
        a = (90.0-latitude1)*(x)
        b = (90.0-latitude2)*(x)
        theta = (longitude2-longitude1)*(x)
        c = math.acos((math.cos(a)*math.cos(b)) + (math.sin(a)*math.sin(b)*math.cos(theta)))

        cnt = cnt + 1

    return radius*c


########################
#Reed Zhang p.1 2/12/15#
########################

from random import random,uniform
from copy import deepcopy

def puzzle1():
    success = 0
    fail = 0

    for n in range(100000):
        r1 = uniform(0,1)
        r2 = uniform(0,1)
        if r2<r1:
            temp=deepcopy(r1)
            r1=deepcopy(r2)
            r2=deepcopy(temp)
        if r1>0.5 or (r2-r1)>0.5 or (1-r2)>0.5:
            fail+=1
        else:
            success+=1
    
    p = success/fail
    print("probability of forming a triangle is ",round(p,3))

def puzzle2():
    success = 0
    fail = 0
    for n in range(1000000):
        r1=uniform(0.5,1)
        r2=uniform(0,r1)
        if r2>=0.5 or r1-r2>=0.5:
            fail+=1
        else:
            success+=1
    print(success/fail)
puzzle2()
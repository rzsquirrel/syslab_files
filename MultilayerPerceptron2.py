##################################
#Reed Zhang June 2, 2015 period 1#
##################################
from random import *


INPUTS = [[1,0,0,0,0,0,0,0,-1],[0,1,1,1,1,1,1,1,-1],[0,0,1,0,0,0,0,0,-1],[0,0,0,1,0,0,0,0,-1],[0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,1,0,0,-1],[0,0,0,0,0,0,1,0,-1],[0,0,0,0,0,0,0,1,-1]]
'''
x = [1,0,0,0,0,0,0,0,-1]
w = [[ 0.1,-0.2, 0.3],
     [ 0.4, 0.1, 0.1],
     [ 0.3, 0.3, 0.7],
     [ 0.6, 0.7,-0.8]
'''

def mult(v,m):
    assert len(v) == len(m)
    return [sum([v[i]*m[i][j] for i in range(len(v))]) for j in range(len(m[0]))]

def printAllData(w,h,v,y):
    print('x =')
    for cell in INPUTS:
        print(cell)
    print('='*50)
    
    print('w =')
    for row in w:
        for cell in row:
            print(cell,end =', ')
        print()
    print('='*50)
    
    print('h =')
    for cell in h:
        print(cell)
    print('='*50)
    
    print('v =')
    for row in v:
        for cell in row:
            print(cell,end = ', ')
        print()
    print('='*50)
    
    print('y =',y)
    for cell in y:
        print(cell)
    print('='*50)
    
def randomlyAssignWeights():
    w = [[uniform
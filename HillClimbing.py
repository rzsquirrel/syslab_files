#######################
#Reed Zhang p1 4/20/15#
#######################
from math import *
from random import *
from copy import deepcopy
from time import clock

ITERATIONS = 5
RADIUS = 0.001

def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step

def f(x,y):
    if x<=0 or x >=10 or y<=0 or y>=10:
        return float('inf')
    return (x*sin(4*x)+1.1*y*sin(2*y))

def method1():
    funcList = []
    for i in range(ITERATIONS):
        x = 10*random()
        y = 10*random()
        bestF = f(x,y)
        while(True):
            oldF = deepcopy(bestF)
            for t in frange(0,2*pi,2*pi/64):
                trialX = x + RADIUS*cos(t)
                trialY = y + RADIUS*sin(t)
                trialF = f(trialX,trialY)
                if trialF < bestF:
                    x = trialX
                    y = trialY
                    bestF = trialF
            if bestF == oldF:
                break
        funcList.append(bestF)
    print('100 random points: minimum value =',round(min(funcList),3))

def method2():
    lookUpSin = []
    lookUpCos = []
    for t in frange(0,2*pi,2*pi/64):
        lookUpCos.append(cos(t))
        lookUpSin.append(sin(t))
    funcList = []
    for i in range(ITERATIONS):
        x = 10*random()
        y = 10*random()
        bestF = f(x,y)
        while(True): 
            oldF = deepcopy(bestF)
            for t in range(64):
                trialX = x + RADIUS*lookUpCos[t]
                trialY = y + RADIUS*lookUpSin[t]
                trialF = f(trialX,trialY)
                if trialF < bestF:
                    x = trialX
                    y = trialY
                    bestF = trialF
            if bestF == oldF:
                break
        funcList.append(bestF)
    print('100 random points with lookup table: minimum value =',round(min(funcList),3))

def method3():
    lookUpSin = []
    lookUpCos = []
    for t in frange(0,2*pi,2*pi/64):
        lookUpCos.append(cos(t))
        lookUpSin.append(sin(t))
    funcList = []
    genList = generator(10)
    for point in genList:
        x = point[0]
        y = point[1]
        bestF = f(x,y)
        while(True): 
            oldF = deepcopy(bestF)
            for t in range(64):
                trialX = x + RADIUS*lookUpCos[t]
                trialY = y + RADIUS*lookUpSin[t]
                trialF = f(trialX,trialY)
                if trialF < bestF:
                    x = trialX
                    y = trialY
                    bestF = trialF
            if bestF == oldF:
                break
        funcList.append(bestF)
    print('100 grid points with lookup table: minimum value =',round(min(funcList),3))

def generator(max):
    for x in range(max):
        for y in range(max):
            yield x,y

def method4():
    bestF = f(0,0)
    for i in range(10000):
        x = 10*random()
        y = 10*random()
        trialF = f(x,y)
        if trialF<bestF:
            bestF = trialF
    print('10000 random points: minimum value =',round(bestF,2))

def method5():
    funcList = []
    # loop 1000 times
    for i in range(2):
        p1 = (10*random(),10*random())
        p2 = (10*random(),10*random())
        p3 = (10*random(),10*random())
        pointList = [p1,p2,p3]
        #while(True):
        for j in range(50):
            pointList = sorted(pointList,key = lambda point: f(point[0],point[1]))
            A = deepcopy(pointList[2])
            oldA = deepcopy(A)
            B = deepcopy(pointList[0])
            C = deepcopy(pointList[1])
            D = (B[0]+C[0]-A[0],B[1]+C[1]-A[1])
            if f(D[0],D[1])<f(A[0],A[1]):
                E = (1.5*B[0]+1.5*C[0]-2*A[0],1.5*B[1]+1.5*C[1]-2*A[1])
                if f(E[0],E[1])<f(D[0],D[1]):
                    A=deepcopy(E)
                else:
                    A=deepcopy(D)
            else:
                F = (0.75*B[0]+0.75*C[0]-0.5*A[0],0.75*B[1]+0.75*C[1]-0.5*A[1])
                G = (0.5*A[0]+0.25*B[0]+0.25*C[0],0.5*A[1]+0.25*B[1]+0.25*C[1])
                tempList = [F,G]
                tempList = sorted(tempList,key = lambda point: f(point[0],point[1]))
                if f(tempList[0][0],tempList[0][1]) < f(A[0],A[1]):
                    A = deepcopy(tempList[0])
                else:
                    A=(0.5*B[0]-0.5*A[0],0.5*B[1]-0.5*A[1])
                    C=(0.5*B[0]-0.5*C[0],0.5*B[1]-0.5*C[1])
            pointList = [A,B,C]
            
            if abs(A[0]-oldA[0])<0.1 and abs(A[1]-oldA[1])<0.1:
                break
        pointList = sorted(pointList,key = lambda point: f(point[0],point[1]))
        #print(pointList)
        funcList.append(f(pointList[0][0],pointList[0][1]))
    print('Nelder-Mead Algorithm:',round(min(funcList),3))
    

'''
startTime = clock()
method1()
print('RUNTIME:',round(clock()-startTime,3),'seconds')
startTime = clock()
method2()
print('RUNTIME:',round(clock()-startTime,3),'seconds')
startTime = clock()
method3()
print('RUNTIME:',round(clock()-startTime,3),'seconds')
startTime = clock()
method4()
print('RUNTIME:',round(clock()-startTime,3),'seconds')
'''
startTime = clock()
method5()
print('RUNTIME:',round(clock()-startTime,3),'seconds')
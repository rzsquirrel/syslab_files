##########################################
#Reed Zhang p.1 5/21######################
##########################################
from random import random, choice, shuffle
TRIALS = 3000
ALPHA = 0.25
INPUTS = [(0.01,2,-1,0,0),(2,0.01,-1,0,0),(-0.01,2,-1,0,1),(-2,0.01,-1,0,1),(-2,-0.01,-1,1,1),(-0.01,-2,-1,1,1),(0.01,-2,-1,1,0),(2,-0.01,-1,1,0)]

def f(w,x):
    return [int((w[0][0]*x[0]+w[1][0]*x[1]+w[2][0]*x[2])>0),int((w[0][1]*x[0]+w[1][1]*x[1]+w[2][1]*x[2])>0)] #returns a y vector [y0,y1]

def trained(w):
    for vector in INPUTS:
        y = f(w,vector)
        if y[0]!=vector[-2] or y[1]!=vector[-1]:
            return False
    return True

def verifyNetwork(w,epochs):
    print(' Epochs(training cycles) =',epochs)
    #print y=mx+b lines
    slope1 = -w[0][0]/w[0][1]
    intercept1 = w[0][2]/w[0][1]
    slope2 = -w[1][0]/w[1][1]
    intercept2 = w[1][2]/w[1][1]

def trainPerceptronWeights():
    w = [[random()-0.5,random()-0.5],[random()-0.5,random()-0.5],[random()-0.5,random()-0.5]]
    limit = 500000
    
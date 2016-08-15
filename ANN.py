##########################################
#Reed Zhang p.1 5/21######################
##########################################

from random import random, choice, shuffle
TRIALS = 3000
ALPHA = 0.25
#INPUTS = [(0,0,-1,0),(1,0,-1,1),(0,1,-1,1),(1,1,-1,1)]
#INPUTS = [(0,4,-1,0),(4,0,-1,0),(2.01,2.01,-1,1)]   #lab 5
#INPUTS = [(0,0,-1,0),(1,0,-1,1),(0,1,-1,1),(1,1,-1,0)]
#INPUTS = [(0,0,1,-1,0),(1,0,0,-1,1),(0,1,0,-1,1),(1,1,1,-1,0)]
INPUTS = [(0.01,2,-1,0,0),(2,0.01,-1,0,0),(-0.01,2,-1,0,1),(-2,0.01,-1,0,1),(-2,-0.01,-1,1,1),(-0.01,-2,-1,1,1),(0.01,-2,-1,1,0),(2,-0.01,-1,1,0)]

SMALL = 0.4

def f(w,x):
    return int((w[0]*x[0]+w[1]*x[1]+w[2]*x[2])>0)

def f3D(w,x):
    return int((w[0]*x[0]+w[1]*x[1]+w[2]*x[2]+w[3]*x[3])>0)

def ff(w,x):
    return [int((w[0][0]*x[0]+w[1][1]*x[1]+w[2][0]*x[2])>0),int((w[0][1]*x[0]+w[1][1]*x[1]+w[2][1]*x[2])>0)] #finish

def trained(w):
    for vector in INPUTS:
        if f(w,vector)!=vector[-1]:
            return False
    return True

def trained3D(w):
    for vector in INPUTS:
        if f3D(w,vector)!=vector[-1]:
            return False
    return True

def verifyNetwork(w,epochs):
    print(' Epochs(training cycles) =',epochs)
    failed=False
    for vector in INPUTS:
        if f(w,vector)!=vector[-1]:
            failed=True
        print(f(w,vector)==vector[-1],vector[-1],vector)
    if failed:
        print('---FAILURE!---')
    else:
        print('---SUCCESS!---')

def verifyNetwork3D(w,epochs):
    print(' Epochs(training cycles) =',epochs)
    failed=False
    for vector in INPUTS:
        if f3D(w,vector)==vector[-1]:
            failed=True
        print(f3D(w,vector)==vector[-1],vector[-1],vector)
    if failed:
        print('---FAILURE!---')
    else: 
        print('---SUCCESS!---')

def trainPerceptronWeights():
    #create random trainPerceptronWeights
    w = [random(),random(),random()]
    '''
    limit = 200000
    cycles = 0
    while(trained(w)==False):
        w = [random(),random(),random()*2]
        cycles+=1
    print(w)
    '''
    #train for several sessions
    limit = 500000
    cycles=0
    while(trained(w)==False):
        #shuffle(INPUTS)
        
        for inVector in INPUTS:
            y = f(w,inVector)
            t = inVector[-1]
            w[0] = w[0] - ALPHA*(y-t)*inVector[0]
            w[1] = w[1] - ALPHA*(y-t)*inVector[1]
            w[2] = w[2] - ALPHA*(y-t)*inVector[2]
            cycles+=1
        if cycles>limit:
            print('failed; too many cycles')
            exit()
    
    return w,cycles

def trainPerceptronWeights3D():
    #create random trainPerceptronWeights
    w = [random(),random(),random(),random()]
    #train for several sessions
    limit = 300000
    cycles=0
    while(trained3D(w)==False):
        #inVector = INPUTS[cycles%len(INPUTS)]
        #inVector = choice(INPUTS)
        for inVector in INPUTS:
            y = f(w,inVector)
            t = inVector[-1]
            w[0] = w[0] - ALPHA*(y-t)*inVector[0]
            w[1] = w[1] - ALPHA*(y-t)*inVector[1]
            w[2] = w[2] - ALPHA*(y-t)*inVector[2]
            w[3] = w[3] - ALPHA*(y-t)*inVector[3]
            cycles+=1
        '''
        if cycles>limit:
            print('failed; too many cycles')
            exit()
        '''
        if cycles>limit:
            break
    
    return w,cycles
    
def main():
    
    w,epochs = trainPerceptronWeights()
    verifyNetwork(w,epochs)
    slope = -w[0]/w[1]
    intercept = w[2]/w[1]
    print('slope =',round(slope,2),'intercept =',round(intercept,2))
    
    #w,epochs = trainPerceptronWeights3D()
    #verifyNetwork3D(w,epochs)
    
    
main()
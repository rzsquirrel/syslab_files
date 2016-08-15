######################
#Reed Zhang p1 5/7/15#
######################

from random import *

def makeChoice(Lst): #returns the choice, aka the index
    r = random()
    cumulativeProb = 0
    for i in range(len(Lst)):
        cumulativeProb+=Lst[i]/sum(Lst)
        if r<cumulativeProb:
            return i
'''
l = [1,2,3,0]


zeros = 0
ones = 0
twos = 0
threes = 0
for i in range(100):
    choice = makeChoice(l)
    if choice == 0: zeros+=1
    elif choice == 1: ones+=1
    elif choice == 2: twos+=1
    else: threes+=1
    
print(zeros,ones,twos,threes)
'''
l = [1,0,3,0,9,2]
for i in range(10):
    print(makeChoice(l))

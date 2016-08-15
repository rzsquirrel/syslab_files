#######################
#Reed Zhang p.1 4/8/15#
#######################
from time import clock
from random import *
from copy import deepcopy
from math import sin

POP = 200
GENERATIONS = 5

def runSimulation():
    population = [['1' for j in range(20)] for i in range(POP)]
    for i in range(POP):
        for j in range(20):
            if random()<0.5:
                population[i][j] = '0'
    for i in range(GENERATIONS):
        temp = determineSurvivors(population)
        population = temp[0]
        minVal = temp[1]
        newPopulation = []
        for i in range(1,100):
            cut = randint(0,20)
            newPopulation.append(population[0][:cut]+population[i][cut:]) #baby 1
            newPopulation.append(population[i][:cut]+population[0][cut:]) #baby 2
        population = deepcopy(newPopulation)
        print('minimum:',minVal)

def func(row):
    row = ''.join(row)
    x = int(row[:10],2)*10/1023
    y = int(row[10:],2)*10/1023
    return x*sin(4*x)+1.1*y*sin(2*y)

def determineSurvivors(population):
    population = sorted(population,key=lambda creature: func(creature))
    return deepcopy(population),func(population[0])

def main():
    startTime = clock()
    runSimulation()
    print('run time =',round(clock()-startTime,3),'seconds')
main()

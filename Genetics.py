#######################
#Reed Zhang p.1 4/8/15#
#######################
from time import clock
from random import *
from copy import deepcopy

POP = 12

def runSimulation():
    population = [[1 for j in range(10)] for i in range(POP)]
    for i in range(POP):
        for j in range(10):
            if random()<0.5:
                population[i][j] = 0
    print(population,' avg score:',averageScore(population))
    while population[1:] != population[:-1]:
        population = determineSurvivors(population)
        newPopulation = []
        for i in range(1,6):
            cut = randint(0,10)
            newPopulation.append(population[0][:cut]+population[i][cut:]) #baby 1
            newPopulation.append(population[i][:cut]+population[0][cut:]) #baby 2
        population = deepcopy(newPopulation)
        print(population,' avg score:',averageScore(population))

def determineSurvivors(population):
    sumList = [sum(ind) for ind in population]
    temp = []
    for i in range(6):
        maxIndex = sumList.index(max(sumList))
        temp.append(population[maxIndex])
        population.remove(population[maxIndex])
        sumList.remove(max(sumList))
    return deepcopy(temp)

def averageScore(sample): #add up, div by num of individuals
    return sum([sum(ind) for ind in sample])/len(sample)

def main():
    startTime = clock()
    runSimulation()
    print('run time =',round(clock()-startTime,3),'seconds')
'''
test = [[1, 1, 1, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0]]
test2 = [[0,0,0],[1,1,1],[0,0,0],[0,1,0],[1,1,0]]
print(sortOnSum(test))
'''
main()

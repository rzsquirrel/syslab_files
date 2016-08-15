###########################
#probability_stick.py     #
#reed zhang period1 Feb.19#
###########################

from random import random,uniform

number_of_simulations = 10000000

def puzzle1():
    successes = 0
    trials = 0
    for n in range(number_of_simulations):
        trials += 1
        x1 = random()
        x2 = random()
        if x1>x2:
            x1,x2 = x2,x1
        if x1<0.5 and x2-x1<0.5 and 1-x2<0.5:
            successes += 1
    return round(successes/trials,3)

def puzzle2():
    successes = 0
    trials = 0
    for n in range(number_of_simulations):
        trials += 1
        x1 = random()
        if x1>0.5:
            x2 = uniform(0,x1)
            if x2<0.5
    return round(successes/trials,3)
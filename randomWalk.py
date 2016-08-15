#########################################
#                                       #
#               Reed Zhang              #
#               Period 1                #
#               June 11, 2015           #
#                                       #            
#########################################

from random import *
from time import clock

MAX = 100000

def main():
    stepsTotal = 0
    for i in range(MAX):
        x = 0
        while(abs(x)<10):
            stepsTotal += 1
            x += choice([-1,1])
    print('avg steps per walk =',round(stepsTotal/MAX))

if __name__ == '__main__':
    startTime = clock()
    main()
    print('runtime =',round(clock()-startTime,2),'s')

'''
output
----------------------
avg steps per walk = 100
runtime = 11.26 s

'''
#########################
#Reed Zhang p.1 4/7/2015#
#########################

from random import *

def printMatrix(m):
    print('---MATRIX:')
    for row in m:
        s = ''
        for element in row:
            truncated = round(element,2)
            length = len(str(truncated))
            for i in range(10-length):
                s += ' '
            s += str(round(element,2))
        print(s)
    print('========================================')

def main():
    M = [[random()*25+random()*200 for COL in range(4)] for ROW in range(3)] #M  =  3-rows x 4-cols matrix
    print(M)
    printMatrix(M)

main()
########################
#Reed Zhang p.1 4/28/15#
########################

from itertools import permutations
from copy import deepcopy
from pickle import dump, load
from random import random
import numpy

def isWin(board):
    for row in range(3):
        if board[row*3]!='-':
            if board[row*3] == board[row*3+1] == board[row*3+2]:
                return True
    for col in range(3):
        if board[col]!='-':
            if board[col]==board[col+3]==board[col+6]:
                return True
    if board[0]=='X' or board[0]=='O':
        if board[0]==board[4]==board[8]:
            return True
    if board[2]=='X' or board[2]=='O':
        if board[2]==board[4]==board[6]:
            return True
    return False

def initializeDictionary():
    sequence = [0,1,2,3,4,5,6,7,8]
    filledBoards = list(permutations(sequence,9))
    Lst = ['-','-','-','-','-','-','-','-','-']
    d = {'---------':[25,25,25,25,25,25,25,25,25]}
    
    for seq in filledBoards:
        temp = deepcopy(Lst)
        prob = [25,25,25,25,25,25,25,25,25]
        for i in range(9):
            if i%2==0: 
                temp[seq[i]]='X'
            else:
                temp[seq[i]]='O'
            board = ''.join(temp)
            #prob[seq[i]] = 0
            if isWin(board)==False and '-' in board:
                assert(sum(prob)!=0)
                d[board]=prob
    for board in d.keys():
        for i in range(9):
            if board[i]=='X' or board[i]=='O':
                d[board][i]=0
        assert(sum(d[board])!=0)
        
    fout=open('moveDictionary.pkl','wb')
    dump(d,fout)
    fout.close()

def makeChoice(Lst): #returns a choice, aka the index
    
    assert(len(Lst)==9)
    r = random()
    cumulativeProb = 0
    for i in range(len(Lst)):
        cumulativeProb+=Lst[i]/sum(Lst)
        if r<cumulativeProb:
            return i
    
    
    '''
    if cumulativeProb!=cumulativeProb:
        return makeChoice(Lst)
    '''
def makeChoice2(Lst):
    assert(len(Lst)==9)
    return Lst.index(max(Lst))

def simulateGame(d):
    boardL = ['-','-','-','-','-','-','-','-','-']
    moveNum = 0
    Xboards = []
    Xmoves = []
    Oboards = []
    Omoves = []
    while isWin(''.join(boardL)) == False and moveNum<9:
        moveNum+=1
        if moveNum%2==1:
            Xboards.append(''.join(boardL))
            move = makeChoice(d[''.join(boardL)])
            boardL[move] = 'X'
            Xmoves.append(move)
            
        else:
            Oboards.append(''.join(boardL))
            move = makeChoice(d[''.join(boardL)])
            boardL[move] = 'O'
            Omoves.append(move)
    
    if isWin(''.join(boardL))==False: #tie
        assert(moveNum==9)
        for i in range(len(Xboards)):
            d[Xboards[i]][Xmoves[i]] = d[Xboards[i]][Xmoves[i]]+1
        for i in range(len(Oboards)):
            d[Oboards[i]][Omoves[i]] = d[Oboards[i]][Omoves[i]]+1
        
    elif moveNum%2 == 1: #x won
        for i in range(len(Xboards)):
            d[Xboards[i]][Xmoves[i]] = d[Xboards[i]][Xmoves[i]]+3
        for i in range(len(Oboards)):
            d[Oboards[i]][Omoves[i]] = d[Oboards[i]][Omoves[i]]-1
            if d[Oboards[i]][Omoves[i]] <= 0: d[Oboards[i]][Omoves[i]] = 1
            
    else: #O won
        for i in range(len(Xboards)):
            d[Xboards[i]][Xmoves[i]] = d[Xboards[i]][Xmoves[i]]-1
            if d[Xboards[i]][Xmoves[i]] <= 0: d[Xboards[i]][Xmoves[i]] = 1
        for i in range(len(Oboards)):
            d[Oboards[i]][Omoves[i]] = d[Oboards[i]][Omoves[i]]+3
    return d

def displayBoard(board):
    print('__________')
    print('',board[0],'|',board[1],'|',board[2])
    print('__________')
    print('',board[3],'|',board[4],'|',board[5])
    print('__________')
    print('',board[6],'|',board[7],'|',board[8])
    print('__________')

def playGame(d):
    displayBoard(['0','1','2','3','4','5','6','7','8'])
    boardL = ['-','-','-','-','-','-','-','-','-']
    #displayBoard(boardL)
    moveNum = 0
    while isWin(''.join(boardL)) == False and moveNum<9:
        displayBoard(boardL)
        moveNum+=1
        if moveNum%2==1: #user plays
            move = int(input('move index (0 through 8):'))
            assert(boardL[move]=='-')
            boardL[move]='X'
        else:
            '''
            choiceProbs = d[''.join(boardL)]
            worstChoice = numpy.min(numpy.nonzero(choiceProbs))
            for i in range(len(choiceProbs)):
                choiceProbs[i] = 2**(choiceProbs[i]/worstChoice)-1
            '''
            #print('thinking:',d[''.join(boardL)])
            move = makeChoice2(d[''.join(boardL)])
            
            boardL[move] = 'O'
    displayBoard(boardL)
    print('game over!')

def main():
    '''
    initializeDictionary()
    
    fin=open('moveDictionary.pkl','rb')
    moveScores=load(fin)
    print(len(moveScores.keys()))
    print(moveScores['---------'])
    
    for i in range(2*10**6):
        moveScores = simulateGame(moveScores)
    fout=open('smartMoveDictionary.pkl','wb')
    dump(moveScores,fout)
    fout.close()
    '''
    
    fin=open('smartMoveDictionary.pkl','rb')
    moveScores=load(fin)
    
    playGame(moveScores)
    
    
main()
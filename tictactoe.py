###############################
#Reed Zhang p.1 april 22, 2015#
###############################

def display(board):
    for row in board:
        s = '|'
        for element in row:
            
            
            if element==-1:
                s+='O'
            elif element==1:
                s+='X'
            else:
                s+='_'
            s+='|'
        print(s)

def makeRandomMove():
    [3*random()//1]


def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    display(board)
    
    
main()
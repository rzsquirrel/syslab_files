#######################
#Reed Zhang p.1 3/9/15#
#######################
from tkinter import *

def setUpCanvas(root):
    root.title("Wolfram's cellular automata: A Tk/Python graphics Program")
    canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas

def printList(rule):
    canvas.create_text(170,20,text = "Rule " + str(rule),fill = 'gold',font = ('Helvetic',10,'bold'))
    L = [1,]
    canvas.create_text(650,10,text=chr(9607),fill='RED',font=('Helvetic',FSIZE,'bold'))
    for row in range(1,330): #330 for actual, 40 for test
        L = [0,0] + L + [0,0]
        nums = []
        #print(L)
        for n in range(0,len(L)-2):
            s = ""
            for element in L[n:n+3]:
                s+=str(element)
            nums.append(int(s,2))
        L = []
        for index in nums:
            L.append(rule[len(rule)-index-1])
        for n in range(len(L)):
            if L[n]==1:
                canvas.create_text(650-row*FSIZE+FSIZE*n, row*FSIZE+10, text = chr(9607), fill = 'RED', font = ('Helvetica',FSIZE,'bold'))
        
from tkinter import Tk,Canvas,BOTH,YES
from time import clock
root=Tk()
canvas = setUpCanvas(root)
FSIZE = 2

def main():
    rule = [0,0,0,1,1,1,1,0]
    #rule = [0,1,0,1,1,0,1,0]
    #rule = [0,1,1,0,1,1,1,0]
    #rule = [1,1,0,0,1,1,1,0]
    #rule = [1,1,1,1,1,1,1,1]
    printList(rule)
    root.mainloop()
    
if __name__ == '__main__': main()
########################
#Reed Zhang p.1 3/25/15#
########################

def setUpCanvas(root):
    root.title("Fractal Flowers by Reed Zhang")
    canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
    canvas.pack(expand=YES, fill=BOTH)
    return canvas
	
def displayStatistics(startTime):
    elapsedTime = round(clock()-startTime, 2)
    print("RUN TIME  =%6.2f"% elapsedTime,       "seconds.")
    message = "The fractal flower is complete."
    root.title(message)

def frange(start,stop,step):
    i = start
    while i<stop:
        yield i
        i += step

def line(x1,y1,x2,y2, kolor = 'WHITE', width = 1):
    #canvas.create_line(x1,y1,x2,y2,width = width, fill = kolor)
    xinc = (x2-x1)/7
    yinc = (y2-y1)/7
    startx = x1
    starty = y1
    theta = atan2(yinc,xinc)
    for i in range(1,8):
        r = sqrt(xinc*xinc + yinc*yinc)
        if random()<0.2:
            theta -= 0.2    #right
        else:
            theta += 0.2
        endx = startx+r*cos(theta)
        endy = starty+r*sin(theta)
        canvas.create_line(startx,starty,endx,endy,width = width,fill = kolor)
        startx = endx #
        starty = endy
    return startx,starty
    

def drawFlower(cx, cy, radius):
    if radius < 3:
        return

    kolor = 'GREEN'
    width = 2
    if radius < 50:
        kolor = 'WHITE'
        width = 1
    if radius < 10:
        kolor = 'RED'
        width = 1

    for t in frange(0,6.28,0.9):
        x = cx + radius*sin(t)
        y = cy + radius*cos(t)
        temp = line(cx,cy,x,y,kolor,width)
        drawFlower(temp[0], temp[1],radius/3)#
    canvas.update()

#=============================================================
from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import *
from math import *

root = Tk()
canvas = setUpCanvas(root)
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
START_TIME = clock()
#==============================================================

def main():
    drawFlower(WIDTH/2, HEIGHT/2-50,240)
    displayStatistics(START_TIME)
    root.mainloop()
    
if __name__ == "__main__":main()

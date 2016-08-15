#######################
#Reed Zhang p.1 3/3/15#
#######################

from tkinter import *  # <-- Use Tkinter (capital "T") in Python 2.x
from time import clock, sleep
from math import *

root = Tk()
START = clock()
WIDTH = 512
HEIGHT = 512
COLORFLAG = False #True = color, False = gray-scale
HIGH = 45
LOW = 10

def main():
    image = [0] * HEIGHT * WIDTH
    imageNoise(500,image)
    drawLine(0,50,image)
    drawLine(1,50,image)
    drawCircle(250,150,75,image)
    displayImageInWindow(image)
    
    root.mainloop()

def imageNoise(points, image):
    from random import randint
    for n in range(points):
        r = randint(0,HEIGHT-1)
        c = randint(0,WIDTH-1)
        image[r*WIDTH+c] = 255

def drawLine(m,b,image):
    for x in range(WIDTH):
        index = x+WIDTH*(m*x+b)
        if 0 <= index < len(image):
            image[index] = 255
            
def drawCircle(Cx,Cy,r,image):
    for s in range(360):
        t = s*3.14159/180
        x = int(Cx+r*cos(t))
        y = int(Cy+r*sin(t))
        image[y*WIDTH+x] = 255

class ImageFrame:
    def __init__(self, image, COLORFLAG = False):
        self.img = PhotoImage(width = WIDTH, height = HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num = image[row*WIDTH+col]
                if COLORFLAG == True:
                    kolor = '#%02x%02x%02x' % (num[0], num[1], num[2]) # color
                else:
                    kolor = '#%02x%02x%02x' % (num, num, num) #grayscale
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElapsedTime('displayed image')
        
def printElapsedTime(msg = 'time'):
    length = 30
    msg = msg[:length]
    tab = '.'*(length-len(msg))
    print('--' + msg.upper() + tab + ' ', end = '')
    time = round(clock() - START, 1)
    print( '%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
           ' sec', sep = '')

def displayImageInWindow(image):
    global x
    x = ImageFrame(image)

main()
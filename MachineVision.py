#######################
#Reed Zhang p.1 2/5/15#
#######################

from tkinter import *  # <-- Use Tkinter (capital "T") in Python 2.x
from time import clock, sleep
from math import *
from copy import deepcopy

#try https://i.imgur.com/1NgkQ6p.jpg

root = Tk()
START = clock()
#squirrel_dandelion is 620 by 427
#bird_statues is 500 by 334
#Blue_Circle is 800 by 800
WIDTH = 800 #PLUG IN FROM FILE
HEIGHT = 800 #PLUG IN FROM FIL
COLORFLAG = False #True = color, False = gray-scale
HIGH = 45
LOW = 10
SMOOTH_ITERATIONS = 2

def main():
    file1 = open('Blue_Circle.ppm', 'r')    #filename here
    stng = file1.readline()
    for i in range(2):
        stng += file1.readline()
    print(stng)
    nums = file1.read().split()
    print(nums[:10])
    file1.close()

    image = []
    for pos in range(0, len(nums), 3):
        RGB = (int(nums[pos]), int(nums[pos+1]), int(nums[pos+2]))
        image.append(int(0.2*RGB[0]+0.7*RGB[1]+0.1*RGB[2]))
    printElapsedTime('saved file numbers')
    file1.close()
    #greyscaled
    #displayImageInWindow(image)
    
    blurredImage = image
    for i in range(SMOOTH_ITERATIONS):
        blurredImage = blur(blurredImage)
    print(blurredImage[1000:1010])
    
    #displayImageInWindow(blurredImage)
    
    edges = findEdges(blurredImage)
    edges = normalize1(edges) #scaled so that larger gradients are WHITER
    
    temp = findSharpEdges(blurredImage,edges)
    sharpEdges = temp[0]
    GxMatrix = temp[1]
    GyMatrix = temp[2]
    #print(len(sharpEdges),len(GxMatrix),len(GyMatrix))
    
    voteImage = findCircleCenter(sharpEdges,GxMatrix,GyMatrix)
    
    displayImageInWindow(normalize2(voteImage))
    #displayImageInWindow(sharpEdges)
    
    
    
    root.mainloop()
    
def blur(image):
    blurredImage = []
    for pos in range(len(image)):
        r = pos//WIDTH
        c = pos%WIDTH
        if r!=0 and c!=0 and r!=HEIGHT-1 and c!=WIDTH-1:
            topleft = image[(r-1)*WIDTH+c-1]
            top = image[(r-1)*WIDTH+c]
            topright = image[(r-1)*WIDTH+c+1]
            left = image[r*WIDTH+c-1]
            middle = image[pos] #r*WIDTH+c
            right = image[r*WIDTH+c+1]
            bottomleft = image[(r+1)*WIDTH+c-1]
            bottom = image[(r+1)*WIDTH+c]
            bottomright = image[(r+1)*WIDTH+c+1]
            blurredImage.append(int(1/16*(topleft+2*top+topright+2*left+4*middle+2*right+bottomleft+2*bottom+bottomright)))
        else:
            blurredImage.append(image[pos])
    return blurredImage

def normalize1(image, intensity = 255):
    m = max(image)
    norm = []
    for x in image:
        if x == 255: norm.append(255)
        else: norm.append(int((m-x)*intensity/m))
    return norm

def normalize2(image, intensity = 255):
    m = max(image)
    norm = []
    for x in image:
        if x == 0: norm.append(255)
        else: norm.append(int((m-x)*intensity/m))
    return norm

def findEdges(image):
    edges = []
    for pos in range(len(image)):
        r = pos//WIDTH
        c = pos%WIDTH
        if r!=0 and c!=0 and r!=HEIGHT-1 and c!=WIDTH-1:
            topleft = image[(r-1)*WIDTH+c-1]
            top = image[(r-1)*WIDTH+c]
            topright = image[(r-1)*WIDTH+c+1]
            left = image[r*WIDTH+c-1]
            middle = image[pos] #r*WIDTH+c
            right = image[r*WIDTH+c+1]
            bottomleft = image[(r+1)*WIDTH+c-1]
            bottom = image[(r+1)*WIDTH+c]
            bottomright = image[(r+1)*WIDTH+c+1]
            Gy = int(topleft+2*top+topright-bottomleft-2*bottom-bottomright)
            Gx = int(-topleft+topright-2*left+2*right-bottomleft+bottomright)
            G = int(sqrt(Gx*Gx+Gy*Gy))
            if G>85:      #threshold_best = ? 
                edges.append(G)
            else:
                edges.append(255)
        else:
            edges.append(255)
    return edges

def findSharpEdges(image,edges):
    sharpEdges = []
    GxMatrix = []
    GyMatrix = []
    for pos in range(len(image)):
        r = pos//WIDTH
        c = pos%WIDTH
        if r!=0 and c!=0 and r!=HEIGHT-1 and c!=WIDTH-1:
            if edges[r*WIDTH+c] == 255:
                sharpEdges.append(255)
                GxMatrix.append(0)
                GyMatrix.append(0)
                continue
            
            topleft = image[(r-1)*WIDTH+c-1]
            top = image[(r-1)*WIDTH+c]
            topright = image[(r-1)*WIDTH+c+1]
            left = image[r*WIDTH+c-1]
            middle = image[pos] #r*WIDTH+c
            right = image[r*WIDTH+c+1]
            bottomleft = image[(r+1)*WIDTH+c-1]
            bottom = image[(r+1)*WIDTH+c]
            bottomright = image[(r+1)*WIDTH+c+1]
            Gy = int(topleft+2*top+topright-bottomleft-2*bottom-bottomright)
            GyMatrix.append(Gy)
            Gx = int(-topleft+topright-2*left+2*right-bottomleft+bottomright)
            GxMatrix.append(Gx)
            G = int(sqrt(Gx*Gx+Gy*Gy))
            
            angle = atan2(Gy,Gx)
            if angle>3*3.14/8 or angle<-3*3.14/8:
                #topbottom
                topEdge = edges[(r-1)*WIDTH+c]
                bottomEdge = edges[(r+1)*WIDTH+c]
                if edges[pos]>topEdge or edges[pos]>bottomEdge:
                    sharpEdges.append(255)
                else:
                    sharpEdges.append(0)
            elif angle>3.14/8:
                #toprightbotleft
                toprightEdge = edges[(r-1)*WIDTH+c+1]
                bottomleftEdge = edges[(r+1)*WIDTH+c-1]
                if edges[pos]>toprightEdge or edges[pos]>bottomleftEdge:
                    sharpEdges.append(255)
                else:
                    sharpEdges.append(0)
            elif angle<-3.14/8:
                #topleftbotright
                topleftEdge = edges[(r-1)*WIDTH+c-1]
                bottomrightEdge = edges[(r+1)*WIDTH+c+1]
                if edges[pos]>topleftEdge or edges[pos]>bottomrightEdge:
                    sharpEdges.append(255)
                else:
                    sharpEdges.append(0)
            else:
                #leftright
                leftEdge = edges[r*WIDTH+c-1]
                rightEdge = edges[r*WIDTH+c+1]
                if edges[pos]>leftEdge or edges[pos]>rightEdge:
                    sharpEdges.append(255)
                else:
                    sharpEdges.append(0)
        else:
            sharpEdges.append(255)
            GyMatrix.append(0)
            GxMatrix.append(0)
    return sharpEdges, GxMatrix, GyMatrix

def findCircleCenter(image,GxMatrix,GyMatrix):
    voteMatrix = [0] * HEIGHT * WIDTH
    for pos in range(len(image)):
        r = pos//WIDTH
        c = pos%WIDTH
        if image[pos] == 0 and GxMatrix[pos] !=0: #edge
            slope = -GyMatrix[pos]/GxMatrix[pos]
            b = r-c*slope
            voteMatrix = castVotes(slope,b,voteMatrix)
    return voteMatrix

def castVotes(m,b,image):
    if abs(m) < 1:
        for x in range(WIDTH):
            index = x+WIDTH*int(m*x+b)
            if 0 <= index < len(image):
                image[index] += 1
    else:
        for y in range(HEIGHT):
            index = int((y-b)/m) + WIDTH*y
            if 0 <= index < len(image):
                image[index] += 1
    return image

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

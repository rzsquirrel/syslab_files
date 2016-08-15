import cv2
from math import *
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

GRIDWIDTH = 15
GRIDHEIGHT = 15

prettyColors = [(0,255,0),(255,0,0),(2,132,30),(0,0,255),(255,200,200),(255,265,0),(128,0,128),(166,255,155),(184,115,51)]
#image = cv2.imread("tsukuba_disp.png",1)
#image = cv2.imread("monopoly.png",1)
image=cv2.imread("monopoly_disp1.png",1)
#image = cv2.imread("white.jpg",1)
nrows, ncols = image.shape[:2]
print(nrows,ncols)
blockWidth = int(ncols//GRIDWIDTH)
blockHeight = int(nrows//GRIDHEIGHT)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blur
blurred_image = cv2.GaussianBlur(gray_image,(5,5),0)

#edge detect
edges = cv2.Canny(blurred_image,50,160)

#print(edges[1:3,75])
#print(edges[1,1]) #0 is black
#go through blocks
#a certain block would be image[n*blockWidth:(n+1)*blockWidth,...]
#we care about adjacent blocks, body vs edge block, depth of the block
#blocks are in an array?

depthMatrix = [[0 for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]
typeMatrix = [[0 for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]

imageMatrix = [[0 for j in range(ncols)] for i in range(nrows)]
#print(len(FF))
#print(FF[20*blockHeight][20*blockWidth])
print(len(imageMatrix),len(imageMatrix[0]))
#print(edges[700,1000])
#print(gray_image[1000,700])
edgeMatrix = [[0 for j in range(ncols)] for i in range(nrows)]
for i in range(nrows):
   for j in range(ncols):
      imageMatrix[i][j] = gray_image[i,j]
      edgeMatrix[i][j] = edges[i,j]

#for t in range(3):
#   print(FF[t][0:2])

"""
for i in range(20):
   for j in range(20):
      block = image[i*blockWidth:(1+i)*blockWidth,j*blockHeight:(1+j)*blockHeight]
      middle = image[int(((1+i)*blockWidth-i*blockWidth)/2),int(((1+j)*blockHeight-j*blockHeight)/2)]
      depthMatrix[i,j] = middle
      blockEdges = edges[i*blockWidth,(j*blockHeight):((1+j)*blockHeight)] + edges[(i+1)*blockWidth,(j*blockHeight):((1+j)*blockHeight)] + edges[(i*blockWidth):((1+i)*blockWidth),i*blockHeight] + edges[(i*blockWidth):((1+i)*blockWidth),(i+1)*blockHeight]
      if all(x==0 for x in blockEdges):
         typeMatrix[i,j] = "body"
      else:
         typeMatrix[i,j] = "edge"
         #body block, not edge block
"""
print(len(edgeMatrix),len(edgeMatrix[0]))
#print(20*blockWidth,20*blockHeight)
for i in range(GRIDHEIGHT):
   for j in range(GRIDWIDTH):
      block = [[0 for b in range(blockWidth)] for a in range(blockHeight)]
      middle = imageMatrix[((1+j)*blockHeight+j*blockHeight)//2][((1+i)*blockWidth+i*blockWidth)//2]
      depthMatrix[i][j]=middle
      blockEdges = []
      for a in range(i*blockWidth,(i+1)*blockWidth):
         blockEdges.append(edgeMatrix[j*blockHeight][a])
         blockEdges.append(edgeMatrix[(j+1)*blockHeight-1][a])
      for b in range(j*blockHeight,(j+1)*blockHeight):
         blockEdges.append(edgeMatrix[b][i*blockWidth])
         blockEdges.append(edgeMatrix[b][(i+1)*blockWidth-1])
      if all(x==0 for x in blockEdges):
         typeMatrix[i][j] = "body"
         #
         #cv2.circle(image,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (0,255,0), -1)
      else:
         typeMatrix[i][j] = "edge"

#group adjacent body regions
'''
def hasZeroes(m):
   for l in m:
      for e in l:
         if e == 0:
            return True
   return False

def findZeroIndex(m):
   for i in len(m):
      for j in len(m[i]):
         if m[i][j] == 0:
            return (i,j)
   return None

groupMatrix = [[0 for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]

#while hasZeroes(groupMatrix)==True:
#   first = findZeroIndex(groupMatrix)

def fillRecursive(typeMatrix,num,i,j):
   global groupMatrix
   #first = findZeroIndex(groupMatrix)
   if typeMatrix[i][j] == "body":
      groupMatrix[i][j] = num
      if i+1<GRIDHEIGHT:
         fillRecursive(typeMatrix,num,i+1,j)
      if j+1<GRIDWIDTH:
         fillRecursive(typeMatrix,num,i,j+1)
   elif typeMatrix[i][j] == "edge":
      groupMatrix[i][j] = -1


fillRecursive(typeMatrix,1,0,0)
'''
#print(groupMatrix)
'''
for i in range(GRIDHEIGHT):
   for j in range(GRIDWIDTH):
      if groupMatrix[i][j] == 1:
         cv2.circle(image,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (255,0,0), -1)
      elif groupMatrix[i][j] == 0:
         cv2.circle(image,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (0,255,0), -1)
'''

#def makeColor(num,0,GRIDWIDTH*GRIDHEIGHT-1):
#   return((int((maximum-num)/(maximum-minimum)*255),int(((num/maximum*sqrt(255))**2)),int((num-minimum)/(maximum-minimum)*255)))
#   #return((int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255)))
def makeColor(num):
   maximum=GRIDWIDTH*GRIDHEIGHT-1
   minimum=0
   return((int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255)))


groupMatrix = [[j+GRIDWIDTH*i for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]
#print(groupMatrix)
for i in range(GRIDHEIGHT):
   for j in range(GRIDWIDTH):
      if typeMatrix[i][j] == "body" and j!=0 and typeMatrix[i][j-1] == "body":
         groupMatrix[i][j] = groupMatrix[i][j-1]
      if typeMatrix[i][j] == "body" and i!=0 and typeMatrix[i-1][j] == "body":
         groupMatrix[i][j] = groupMatrix[i-1][j]
for i in range(GRIDHEIGHT-1,-1,-1):
   for j in range(GRIDWIDTH-1,-1,-1):
      if typeMatrix[i][j] == "body" and j!=GRIDWIDTH-1 and typeMatrix[i][j+1] == "body":
         groupMatrix[i][j] = groupMatrix[i][j+1]
      if typeMatrix[i][j] == "body" and i!=GRIDHEIGHT-1 and typeMatrix[i+1][j] == "body":
         groupMatrix[i][j] = groupMatrix[i+1][j]

bodies = {}
copyOfImage = deepcopy(image)
for i in range(GRIDHEIGHT):
   for j in range(GRIDWIDTH):
      if typeMatrix[i][j] == "body":
         cv2.circle(copyOfImage,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, makeColor(groupMatrix[i][j]), -1)
      #elif groupMatrix[i][j] == 0:
      #   cv2.circle(image,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (0,255,0), -1)
         if groupMatrix[i][j] in list(bodies.keys()):
            bodies[groupMatrix[i][j]].append(tuple([i,j]))
         else:
            bodies[groupMatrix[i][j]] = [tuple([i,j])]

cv2.imshow('regions',copyOfImage)

#print(list(bodies.keys()))
#prettyColors = [(0,255,0),(255,0,0),(2,132,30),(0,0,255),(255,200,200),(255,265,0),(128,0,128),(166,255,155),(184,115,51)]

#my own code to look behind objects (do it in a function ok)
depthScores = {}   #not absolute depth, just depth relative to background
print(len(imageMatrix))
print(len(imageMatrix[0]))
for group in list(bodies.keys()):  
   depthScoreList = []
   for point in bodies[group]:
      if point[0]>0:
         if typeMatrix[point[0]-1][point[1]]=="edge":
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[(point[0]-1)*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]
            if depthDifference>0:
               depthScoreList.append(depthDifference)  #only counts if you're in front of the edge
      if point[0]<GRIDHEIGHT-1:
         if typeMatrix[point[0]+1][point[1]]=="edge":
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[(point[0]+1)*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]
            if depthDifference>0:
               depthScoreList.append(depthDifference)
      if point[1]>0:
         if typeMatrix[point[0]][point[1]-1]=="edge":
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[point[0]*blockHeight+blockHeight//2][(point[1]-1)*blockWidth+blockWidth//2]
            if depthDifference>0:
               depthScoreList.append(depthDifference)
      if point[1]<GRIDWIDTH-1:
         if typeMatrix[point[0]][point[1]+1]=="edge":
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[point[0]*blockHeight+blockHeight//2][(point[1]+1)*blockWidth+blockWidth//2]
            if depthDifference>0:
               depthScoreList.append(depthDifference)
   if len(depthScoreList)!=0:
      depthScores[group]=sum(depthScoreList)/len(depthScoreList)*len(bodies[group])

print(depthScores)

temp = list(depthScores.items())
regionScores = [element[1] for element in temp]
regionScores.sort()
print(regionScores)

allRegionIds = list(bodies.keys())
for i in range(len(allRegionIds)):
   if allRegionIds[i] in list(depthScores.keys()):
      print(allRegionIds[i],prettyColors[i])
      if depthScores[allRegionIds[i]] == regionScores[-1]: #0
         for point in bodies[allRegionIds[i]]:
            cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (0,255,0), -1) #colors are (b,g,r), green is best
      if depthScores[allRegionIds[i]] == regionScores[-2]: #317
         for point in bodies0[allRegionIds[i]]:
            cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (255,0,0), -1) #blue is second best
      #else:
      #   cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 3, prettyColors[i], -1)

#other detection algorithms based on arrangement of edge blocks?
'''
#disp stuff
plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
'''

cv2.imshow('edges',edges)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

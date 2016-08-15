import cv2
from math import *
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

GRIDWIDTH = 40
GRIDHEIGHT = 40

#prettyColors = [(0,255,0),(255,0,0),(2,132,30),(0,0,255),(255,200,200),(255,265,0),(128,0,128),(166,255,155),(184,115,51)]
prettyColors = [(31,23,176),(185,174,255),(150,62,255),(255,0,255),(255,48,155),(238,0,0),(237,149,100),(255,191,0),(255,245,0),(154,250,0),(69,139,0),(62,255,192),(0,255,255),(0,173,205),(0,90,139),(0,64,238)]

image = cv2.imread("tsukuba_disp.png",1)
originalImage = deepcopy(image)
#image = cv2.imread("lampshade_disp1.png",1)
#image = cv2.imread("monopoly.png",1)
#image=cv2.imread("monopoly_disp1.png",1)
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

depthMatrix = [[0 for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]
typeMatrix = [[0 for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]

imageMatrix = [[0 for j in range(ncols)] for i in range(nrows)]   #pixels
print(len(imageMatrix),len(imageMatrix[0]))
edgeMatrix = [[0 for j in range(ncols)] for i in range(nrows)]
for i in range(nrows):
   for j in range(ncols):
      imageMatrix[i][j] = gray_image[i,j]
      edgeMatrix[i][j] = edges[i,j]

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

def makeColor(num):
   maximum=GRIDWIDTH*GRIDHEIGHT-1
   minimum=0
   return((int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255),int((maximum-num)/(maximum-minimum)*255)))


groupMatrix = [[j+GRIDWIDTH*i for j in range(GRIDWIDTH)] for i in range(GRIDHEIGHT)]
#print(groupMatrix)
for trials in range(5):
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
      #   cv2.circle(copyOfImage,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, makeColor(groupMatrix[i][j]), -1)
      #elif groupMatrix[i][j] == 0:
      #   cv2.circle(image,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (0,255,0), -1)
         if groupMatrix[i][i]==0:
            cv2.circle(copyOfImage,(i*blockWidth+blockWidth//2,j*blockHeight+blockHeight//2), 3, (255,255,255), -1)
         if groupMatrix[i][j] in list(bodies.keys()):
            bodies[groupMatrix[i][j]].append(tuple([i,j]))
         else:
            bodies[groupMatrix[i][j]] = [tuple([i,j])]

#cv2.imshow('regions',copyOfImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
differenceImage = deepcopy(image)
#
'''
for group in list(bodies.keys()):
   if group == 0:
      for point in bodies[group]:
         cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (0,0,255), -1)
   if group == 98:
      for point in bodies[group]:
         cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (0,255,0), -1)
   if group == 179:
      for point in bodies[group]:
         cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (255,0,0), -1)

cv2.imshow('region',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#print(list(bodies.keys()))


#my own code to look behind objects (do it in a function ok)
depthScores = {}   #not absolute depth, just depth relative to background
print(len(imageMatrix))
print(len(imageMatrix[0]))
for group in list(bodies.keys()): 
   #print("hello",group)
   depthScoreList = []
   for point in bodies[group]:
      pointCoords = (point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2)
      if point[0]>0:
         if typeMatrix[point[0]-1][point[1]]=="edge": #edge above
            pointCoords = (point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2)
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[(point[0]-1)*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]
            cv2.line(differenceImage,pointCoords,(pointCoords[0]-blockWidth,pointCoords[1]),(200,0,200),1)
            #cv2.circle(differenceImage,pointCoords,2,(0,0,255),-1)
            if depthDifference>0:
               depthScoreList.append(depthDifference)
      if point[0]<GRIDHEIGHT-1:
         if typeMatrix[point[0]+1][point[1]]=="edge": #below
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[(point[0]+1)*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]
            cv2.line(differenceImage,pointCoords,(pointCoords[0]+blockWidth,pointCoords[1]),(200,0,200),1)
            #cv2.circle(differenceImage,pointCoords,2,(0,0,255),-1)
            if depthDifference>0:
               depthScoreList.append(depthDifference)
      if point[1]>0:
         if typeMatrix[point[0]][point[1]-1]=="edge": #edge to the left
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[point[0]*blockHeight+blockHeight//2][(point[1]-1)*blockWidth+blockWidth//2]
            cv2.line(differenceImage,pointCoords,(pointCoords[0],pointCoords[1]-blockHeight),(200,0,200),1)
            #cv2.circle(differenceImage,pointCoords,2,(0,0,255),-1)
            if depthDifference>0:
               depthScoreList.append(depthDifference)
      if point[1]<GRIDWIDTH-1:
         if typeMatrix[point[0]][point[1]+1]=="edge": #edge to the right
            depthDifference = imageMatrix[point[0]*blockHeight+blockHeight//2][point[1]*blockWidth+blockWidth//2]-imageMatrix[point[0]*blockHeight+blockHeight//2][(point[1]+1)*blockWidth+blockWidth//2]
            cv2.line(differenceImage,pointCoords,(pointCoords[0],pointCoords[1]+blockHeight),(200,0,200),1)
            if depthDifference>0:
               depthScoreList.append(depthDifference)
   if len(depthScoreList)!=0:
      depthScores[group]=sum(depthScoreList)/len(depthScoreList)*len(bodies[group])

print(depthScores)

temp = list(depthScores.items())
regionScores = [element[1] for element in temp]
regionScores.sort()
print(regionScores)

bestRegionsImage = deepcopy(image)
allRegionsImage = deepcopy(image)

allRegionIds = list(bodies.keys())
for i in range(len(allRegionIds)):
   if allRegionIds[i] in list(depthScores.keys()):
      #print(allRegionIds[i],prettyColors[i])
      if depthScores[allRegionIds[i]] == regionScores[-1]: #0
         for point in bodies[allRegionIds[i]]:
            cv2.circle(bestRegionsImage,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (0,255,0), -1) #colors are (b,g,r), green is best
      if depthScores[allRegionIds[i]] == regionScores[-2]: #317
         for point in bodies[allRegionIds[i]]:
            cv2.circle(bestRegionsImage,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, (255,0,0), -1) #blue is second best
      #else:
      #   cv2.circle(image,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 3, prettyColors[i], -1)
   for point in bodies[allRegionIds[i]]:
      cv2.circle(allRegionsImage,(point[0]*blockWidth+blockWidth//2,point[1]*blockHeight+blockHeight//2), 2, prettyColors[i], -1)
      
#other detection algorithms based on arrangement of edge blocks?
cv2.imshow('disparity map',originalImage)
cv2.imshow('edges',edges)
cv2.imshow('differences across regions',differenceImage)
cv2.imshow('two best regions (green=best)',bestRegionsImage)
cv2.imshow('all regions',allRegionsImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

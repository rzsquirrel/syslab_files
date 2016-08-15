"""
####################
#Reed Zhang 9/25/14#
####################
"""


from pickle import dump, load
import copy
from math import pi , acos , sin , cos

nodes=open('rrEdges.txt').read().split() #0-1 adj, 2-3 adj, etc.
latlong=open('rrNodes.txt').read().split() #(id, lat, long,id2,lat2,long2,...)
#nodeToCity=open('rrNodeCity.txt').read().split() #(id,name,id2,name2,...)
"""

nodes=open('romEdges.txt').read().split()
latlong=open('romNodes.txt').read().split()
"""

print(nodes[0:4])

def findNbrs(station):
   l=[]
   for i in range(len(nodes)):
      if nodes[i]==station:
         if i%2==0:
            l.append(nodes[i+1])
         else:
            l.append(nodes[i-1])
   return l

#edgeList will be a dict like {node: [(cost,adj1),(cost2,adj2),...]}
def storeGraphUnw():
   edgeListUnw={}
   for s in nodes:
      if s not in edgeListUnw.keys():
         edgeListUnw[s]=findNbrs(s)

   #print(edgeListUnw['0100003'])
   
   fout=open('rrGraphUnweighted.pkl','wb')
   dump(edgeListUnw,fout)
   fout.close()

def storeGraphW():
   fin=open('rrGraphUnweighted.pkl','rb')
   edgeListW=load(fin)
   fin.close()
   for s in edgeListW.keys():
      l=copy.deepcopy(len(edgeListW[s]))
      for i in range(l):
         nbr=edgeListW[s].pop(0) #pop adjk
         edgeListW[s].append((calcD(s,nbr),nbr)) #append (costk,adjk)
   fout=open('rrGraphWeighted.pkl','wb')
   dump(edgeListW,fout)
   fout.close()

def calcD(you,nbr):
   y1=0
   x1=0
   y2=0
   x2=0
   for i in range(int(len(latlong)/3)):
      curr=latlong[3*i]
      if curr==you:
         y1=float(latlong[3*i+1])
         x1=float(latlong[3*i+2])
      elif curr==nbr:
         y2=float(latlong[3*i+1])
         x2=float(latlong[3*i+2])
   
   y1*=pi/180
   x1*=pi/180
   y2*=pi/180
   x2*=pi/180
   return acos(sin(y1)*sin(y2)+cos(y1)*cos(y2)*cos(x2-x1)) * 3963.17
   
def getMin(queue):
   shortest=queue[0]
   minIndex=0
   for i in range(len(queue)):
      if queue[i][0]<shortest[0]:
         shortest=copy.deepcopy(queue[i])
         minIndex=i
   return queue.pop(minIndex)

def getNewPath(popped,nbr):
   newPath=copy.deepcopy(popped) #newPath is a tuple (len so far, [(d1,node1),(d2,node2),...],last)
   newPath=list(newPath)
   newPath[0]+=nbr[0]
   newPath[1].append(nbr)
   newPath[2]=nbr[1]
   newPath=tuple(newPath)
   return newPath
   
def search(start,end):
   fin=open('romGraphWeighted.pkl','rb')
   edgeListW=load(fin)
   q=[]
   startPath=(0,[(0,start)],start)
   q.append(startPath)
   used={}
   pops=0
   while q: #make used a dictionary 
      print(q)
      popped=getMin(q)
      #print(used.keys())    #popped is a tuple, (length so far, [(d1,node1),(d2,node2),...],last)
      pops+=1
      last=popped[2] #last is just the id string
      #print(last)
      if last==end:
         return (popped,pops) #returns a tuple inside a tuple
      #print(q)
      for nbr in edgeListW[last]: #nbr is (distance,id)
         if nbr[1] not in used.keys():
            newPath=getNewPath(popped,nbr)
            q.append(newPath)
            used[nbr[1]]=newPath
            #print(newPath)

def main():
   #storeGraphUnw()
   #storeGraphW()
   #print the first 20
   """
   fin=open('rrGraphWeighted.pkl','rb')
   edgeListW=load(fin)
   
   i=0
   for key in edgeListW.keys():
      if i<20:
         print(key,edgeListW[key])
         i+=1
   print(edgeListW['4600109'])
   print(latlong[0:10])
   """
   #print(edgeListW)
   #run part:
   
   while 1==1:
      startWord=input('start:')
      if startWord=='x':
         exit()
      endWord=input('end:')
      if endWord=='x':
         exit()
      path=search(startWord,endWord)
      for i in range(len(path[0][1])):
         print(1+i,'.',path[0][1][i][1])
      
      print('distance:',path[0][0],'miles')
      
      #print('\nnumber of pops: ',path[1])
   
from time import clock
START_TIME = clock()
main()
print('\n RUN TIME = ',clock()-START_TIME, 'seconds')
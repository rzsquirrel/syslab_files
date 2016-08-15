"""
####################
#reed zhang, 9/4/14#
####################
"""
import copy
#load nbrs
def load():
   from pickle import load
   fin=open('nbrs.pkl','rb')
   nbrs=load(fin)
   fin.close()
   return nbrs

#findpath

def search(start,end,nbrList):
   q=[]
   startPath=[start]
   q.append(startPath)
   used=[start]
   pops=0
   while q:
      popped=q.pop(0)
      pops+=1
      pos=popped[-1]
      if pos==end:
         return (popped,pops)
      #print(q)
      for nbr in nbrList[pos]:
         if nbr not in used:
            newPath=copy.deepcopy(popped)
            newPath.append(nbr)
            q.append(newPath)
            used.append(nbr)
            #print(newPath)

def main():
   print
   nbrs=load()
   print(nbrs['battle'],nbrs['castle'],'\n')
   while(1==1):
      startWord=input('start:')
      if startWord=='x':
         exit()
      endWord=input('endword:')
      if endWord=='x':
         exit()
      path=search(startWord,endWord,nbrs)
      #path=search('defied','belief',nbrs)
      for i in range(len(path[0])):
         print(1+i,'.',path[0][i])
      
      print('\nnumber of pops: ',path[1])
      print('\n')
   #print('\npath length:',len(path[0]))

#run time
from time import clock
START_TIME = clock()
main()
print('\n RUN TIME = ',clock()-START_TIME, 'seconds')
         
  

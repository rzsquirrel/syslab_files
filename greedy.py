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

def getMin(queue):
   shortest=queue[0]
   minIndex=0
   for i in range(len(queue)):
      if queue[i][0]<shortest[0]:
         shortest=copy.deepcopy(queue[i])
         minIndex=i
   return queue.pop(minIndex)
def search(start,end,nbrList):
   q=[]
   startPath=(0,[start])
   q.append(startPath)
   used=[]
   pops=0
   while q:
      popped=getMin(q)
      #print(popped)    #popped is a tuple, (expected length, [path,...])
      pops+=1
      pos=popped[1][-1]
      if pos==end:
         return (popped,pops) #returns a tuple inside a tuple
      #print(q)
      for nbr in nbrList[pos]:
         if nbr not in used:
            newPath=copy.deepcopy(popped)
            newPath=list(newPath)
            newPath[0]+=1+hue2(nbr,end)-hue2(popped[1][-1],end)# something? reset the hue each time?
            newPath[1].append(nbr)
            newPath=tuple(newPath)
            q.append(newPath)
            used.append(nbr)
            #print(newPath)

def hue1(word1,word2):
   diff=0
   for i in range(6):
      if word1[i]!=word2[i]:
         diff+=1
   return diff

def hue2(word1,word2):
   diff=0
   vowels=['a','e','i','o','u']
   for i in range(6):
      if word1[i]==word2[i]:
         diff+=0
      elif word1[i] in vowels and word2[i] not in vowels:
         diff+=4
      elif word1[i] not in vowels and word2[i] in vowels:
         diff+=4
      else:
         diff+=1
   return diff

def main():
   nbrs=load()
   print(nbrs['battle'],nbrs['castle'],'\n')
   assert(hue1('darnit','darnxx')==2)
   #assert(hue2('silver','sliver')==6)
   while 1==1:
      startWord=input('start:')
      if startWord=='x':
         exit()
      endWord=input('endword:')
      if endWord=='x':
         exit()
      path=search(startWord,endWord,nbrs)
      for i in range(len(path[0][1])):
         print(1+i,'.',path[0][1][i])
      
      print('\nnumber of pops: ',path[1])

#run time
from time import clock
START_TIME = clock()
main()
print('\n RUN TIME = ',clock()-START_TIME, 'seconds')
         
  

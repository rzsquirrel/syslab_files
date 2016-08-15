#########################
#Reed Zhang p.1 10/20/14#
#########################
from copy import deepcopy
import time

MAX=9

def createBoard():
   difficulty=input("difficulty(Easy,Medium,Hard,Custom):")
   puzzNo=int(input("puzzle number:"))
   puzz=open("sudoku"+difficulty+".txt").read().split()[puzzNo]
   assert(len(puzz)==MAX*MAX)
   m=[[0 for x in range(MAX)] for x in range(MAX)]
   i=0
   for j in range(MAX):
      for k in range(MAX):
         if puzz[i]!='.':
            m[j][k]=int(puzz[i])
         i+=1
   return m
   
def recursiveSolve(m,d):
   (m,d)=doAllSimple(m)
   if correct(m):
      return m
   oldM=deepcopy(m)
   oldD=deepcopy(d)
   cell=cellWithSmallestValueSet(d)
   if len(d)!=0:
      for guess in d[cell]:
         m[cell[0]][cell[1]]=guess
         d.pop(cell)
         m=recursiveSolve(m,d)
         if correct(m):
            return m
         restoreMValues(m,oldM)
         restoreDValues(d,oldD)
   return m

def cellWithSmallestValueSet(d):
   minLen=9
   minCell=(0,0)
   keys=d.keys()
   for k in keys:
      if len(d[k])<minLen:
         minLen=len(d[k])
         minCell=k
   return minCell

def restoreMValues(m,oldM):
   for i in range(MAX):
      for j in range(MAX):
         m[i][j]=oldM[i][j]
         
def restoreDValues(d,oldD):
   d.clear()
   for b in oldD.keys():
      d[b]=oldD[b]
      
def correct(m):
   legit=True
   for i in range(MAX):
      rowTracker=[0,0,0,0,0,0,0,0,0]
      colTracker=[0,0,0,0,0,0,0,0,0]
      blkTracker=[0,0,0,0,0,0,0,0,0]
      #ith row,col,block
      for j in range(MAX):
         rowTracker[m[i][j]-1]+=1
         colTracker[m[j][i]-1]+=1
         blkTracker[m[i//3*3+j//3][i//3*3+j%3]-1]+=1
      if rowTracker!=[1,1,1,1,1,1,1,1,1] or colTracker!=[1,1,1,1,1,1,1,1,1] or blkTracker!=[1,1,1,1,1,1,1,1,1]:
         legit=False
   return legit

def doAllSimple(m):
   d={}
   for r in range(MAX):
      for c in range(MAX):
         m[r][c]=int(m[r][c])
         if m[r][c]==0:
            d[(r,c)]=[1,2,3,4,5,6,7,8,9]
   (m,d)=repeatTrick1(m,d)

   (m,d)=recursivelyTrick2(m,d)
   
   return (m,d)

def repeatTrick1(m,d):
   (m,d,trickUsed)=trick1(m,d)
   while trickUsed:
      (m,d,trickUsed)=trick1(m,d)
   return (m,d)

def recursivelyTrick2(m,d):
   (m,d,trick2Used)=trick2(m,d)
   if trick2Used:
      #do trick 1 until it doesn't change
      (m,d,trick1Used)=trick1(m,d)
      while trick1Used:
         (m,d,trick1Used)=trick1(m,d)
      #do trick 2
      return recursivelyTrick2(m,d)
   else: return (m,d)
   
def trick1(m,d):
   for r in range(MAX):
      for c in range(MAX):
         if m[r][c]!=0:
            #remove from row, col, block
            '''
            for i in range(MAX):
               try: d[(i,c)].remove(m[r][c])
               except: pass
               try: d[(r,i)].remove(m[r][c])
               except: pass
               for a in range(r//3*3,r//3*3+3):
                  for b in range(c//3*3,c//3*3+3):
                     try: d[(a,b)].remove(m[r][c])
                     except: pass
            '''
            for j in range(MAX):
               for k in range(MAX):
                  if m[j][k]==0 and (r==j or c==k or r//3==j//3 and c//3==k//3):
                     try: d[(j,k)].remove(m[r][c])
                     except: continue
            
   toPop=[]
   used=False
   for cell in d.keys():
      if len(d[cell])==1:
         m[cell[0]][cell[1]]=d[cell][0]
         toPop.append(cell)
         used=True
   for eh in toPop:
      d.pop(eh)
   return (m,d,used)

def trick2Blocks(m,d,used):
   for br in range(int(MAX/3)):
      for bc in range(int(MAX/3)):
         arr=[]
         for r in range(3*br,br*3+3):
            for c in range(3*bc,bc*3+3):
               try: arr.append(d[r][c])
               except: arr.append([])
         assert(len(arr)==MAX)
         countTracker=[0,0,0,0,0,0,0,0,0]
         for a in arr:
            for b in a:
               countTracker[b-1]+=1
         try: fixed=1+countTracker.index(1)
         except: continue
         fixIndex=0
         for a in arr:
            for b in a:
               if b==fixed: fixIndex=arr.index(a)
         t=(fixIndex//3+3*br,fixIndex%3+3*bc) #i hope this doesn't cause an error
         d.pop(t)
         m[t[0]][t[1]]=fixed
         used=True
         (m,d)=repeatTrick1(m,d)
         
def trick2(m,d):
   used=False
   for r in range(MAX): #go through the rows
      arr=[]
      for c in range(MAX):
         try: arr.append(d[(r,c)])
         except: arr.append([])
      assert(len(arr)==MAX)
      countTracker=[0,0,0,0,0,0,0,0,0]
      for a in arr:
         for b in a:
            countTracker[b-1]+=1
      try: fixed=1+countTracker.index(1)
      except: continue
      
      fixIndex=0
      for a in arr:
         for b in a:
            if b==fixed: fixIndex=arr.index(a)
      t=(r,fixIndex)
      d.pop(t)
      m[r][fixIndex]=fixed
      used=True
      (m,d)=repeatTrick1(m,d)
      
   for c in range(MAX): # go through the columns
      arr=[]
      for r in range(MAX):
         try: arr.append(d[(r,c)])
         except: arr.append([])
      assert(len(arr)==MAX)
      countTracker=[0,0,0,0,0,0,0,0,0]
      for a in arr:
         for b in a:
            countTracker[b-1]+=1
      try: fixed=1+countTracker.index(1)
      except: continue
      
      fixIndex=0
      for a in arr:
         for b in a:
            if b==fixed: fixIndex=arr.index(a)
      t=(fixIndex,c)
      d.pop(t)
      m[fixIndex][c]=fixed
      used=True
      (m,d)=repeatTrick1(m,d)
      
   #go through blocks
   trick2Blocks(m,d,used)
   
   return (m,d,used)

def disp(m):
   for i in range(MAX):
      print(m[i])
   print('\n')
   
def solve(matrix,start):
   (matrix,dictionary)=doAllSimple(matrix)
   if correct(matrix):
      disp(matrix)
      print('run time:',time.clock()-start)
   else:
      matrix=recursiveSolve(matrix,dictionary)
      disp(matrix)
      print('run time:',time.clock()-start)
   
def main():
   matrix=createBoard()
   start=time.clock()
   solve(matrix,start)
   print('isCorrect=',correct(matrix))

main()
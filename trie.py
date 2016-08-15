#########################
#reed zhang p.1 11/25/14#
#########################
class Node(object):
   def __init__ (self, value):
      self.value = value
      self.children = {} # maps for example 'a':Node('a')
   def __repr__(self):
      self.print()
      return ''
   def print(self, stng):
      if self.value == '$':
         print(stng)
      else:
         for c in self.children.keys():
            self.children[c].print(stng+self.value)
      
   def display(self):
      if self.value == '$':return
      print('=Node=')
      print('-> self.value =',self.value)
      print('-> self.children: [',end = '')
      
      for key in self.children:  #print the dollar signs as well?
         print(key,sep='',end=',')
      print(']')
      print('------')
      
      for char in self.children:
         (self.children[char].display())
   
   def insert(self,stng):
      if stng=='':
         self.children['$']=Node('$')
      elif stng[0] in self.children:
         self.children[stng[0]].insert(stng[1:])
      elif stng[0] not in self.children:
         n=Node(stng[0])
         self.children[n.value] = n
         n.insert(stng[1:])
         
   def search(self,stng):
      if stng == '':
         if '$' in self.children:
            return True
         else:
            return False
      
      if stng[0] not in self.children:
         return False
      
      return self.children[stng[0]].search(stng[1:])
   
   def fragmentSearch(self,stng):
      if stng=='':
         return True
      
      if stng[0] not in self.children:
         return False
       
      return self.children[stng[0]].fragmentSearch(stng[1:])

from sys import setrecursionlimit; setrecursionlimit(100) # default is 1000
from time import clock

def main():
   root = Node('*')
   root.insert('cat')
   root.insert('catnip')
   root.insert('cats')
   root.insert("can't")
   root.insert('cat-x')
   root.insert('dog')
   root.insert('dogs')
   root.insert('dognip')
   root.print('')
   root.display()
   print('SEARCH for dog$:',root.search('dog$'))
   print('SEARCH for catn:', root.search('catn'))
   print('SEARCH for catnip:',root.search('catnip'))
   print('SEARCH for cactus:',root.search('cactus'))
   printElapsedTime()
   
def printElapsedTime():
   print('\n - total run time =',round(clock()-startTime,2),'seconds')
   
if __name__ == '__main__': startTime = clock(); main()

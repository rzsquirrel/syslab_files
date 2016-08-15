#########################
#Reed Zhang p. 1 12/2/14#
#########################

from trie import Node
from time import clock
from random import choice

def printGhostDirections():
   print('+-------------------------------------------------------------------------+')
   print('|Welcome to Ghost. The human goes first. Enter your letter when requested.|')
   print('+-------------------------------------------------------------------------+')

def createTrie():
   print('Loading Dictionary...')
   root=Node('*')
   
   file1=open('ghostDictionary.txt')
   #allWords=file1.read().split()
   for word in file1:
      root.insert(word.lower().strip())
   file1.close()
   
   print('Done!')
   return root

def requestAndCheckHumanMove(root,stng):
   stng+=input('HUMAN:').lower()[0]
   print(' ',stng)
   
   if 3<len(stng) and root.search(stng)==True:
      print('-------------------------------------')
      print('HUMAN LOSES because "',stng,'" is a word.',sep='')
      print('------------< GAME OVER >------------')
      exit()
   
   '''
   if 3<len(stng) and root.fragmentSearch(stng)==False:
      print('-------------------------------------')
      print('HUMAN LOSES because "',stng,'" does not begin any word.',sep='')
      
      print(" [The computer's word was ", '"', spellWordFromString(root,stng[0:-1]),'".]', sep='')
      print('------------< GAME OVER >------------')
      
      exit()
   '''
   
   return(stng)
   
def spellWordFromString(root,stng):
   node=root
   temp=stng
   while temp:
      node=node.children[temp[0]]
      temp=temp[1:]
   
   while node.value!='$':
      l=choice(list(node.children.keys()))
      stng+=l
      node=node.children[l]
   
   return stng[:-1]

def computerMove(root,stng):
   temp=stng
   tNode=root
   while temp:
      if temp[0] not in tNode.children:
         print('-------------------------------------')
         print('HUMAN LOSES because "',stng,'" does not begin any word.',sep='')
      
         print(" [The computer's word was ", '"', spellWordFromString(root,stng[0:-1]),'".]', sep='')
         print('------------< GAME OVER >------------')
         exit()
         
      tNode=tNode.children[temp[0]]
      temp=temp[1:]
   
   l='$'
   while l=='$':
      l=choice(list(tNode.children.keys()))
   
   stng+=l
   print('computer:',l)
   print(' ',stng)
   if 3<len(stng) and root.search(stng)==True:
      print('-------------------------------------')
      print('COMPUTER LOSES because "',stng,'" is a word.',sep='')
      print('------------< GAME OVER >------------')
      exit()
      
   return stng

def main():
   root=createTrie()
   printGhostDirections()
   
   #print(len(root.children.keys()))
   
   stng=''
   while True:
      stng=requestAndCheckHumanMove(root,stng)
      stng=computerMove(root,stng)

main()
#####################
#Reed Zhang 10/20/14#
#####################
from re import findall
from itertools import permutations
def main():
   puzzle=input('puzzle:')
   puzzle=puzzle.upper().replace("=","==")

   words=findall('[A-Z]+',puzzle)
   n=len(words)-1
   startingLetters={word[0] for word in words}
   keys=''.join(set(''.join(words)))
   exists=False

   for values in permutations('1234567890',len(keys)):
      values=str(values)
      values=values[2:len(values)-2]
      values=values.replace('\', \'',"")
      t=str.maketrans(keys,values)
      doit=True
      for s in startingLetters:
         #print(t)
         if t[ord(s)]==48:
            doit=False
      if doit:
         eq=puzzle.translate(t)
         #print(eq)
      if doit and eval(eq):
         exists=True
         print('solved:',eq.replace("==","="))
   if not exists:
      print('No solutions exist.')
   else:
      print('-all solutions found-')
from time import clock
START_TIME = clock()
main()
print('\n RUN TIME = ',round(clock()-START_TIME,4), 'seconds')
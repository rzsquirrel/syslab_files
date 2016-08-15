######################
#reed zhang p.1 12/18#
######################

from random import randint

def main():
   gg=0
   gs=0
   for n in range(10000):
      d=randint(0,2) #pick a drawer
      c=randint(0,1) #pick a coin
      if d==0: #drawer w/ both gold, doesn't matter which coin you looked at
         gg+=1
      if d==1 and c==0: #drawer w/ gold and silver, if the coin is gold
         gs+=1
   print('P(both gold given atleast one gold) is about',100*gg/(gg+gs),'%')

main()
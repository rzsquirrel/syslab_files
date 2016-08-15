###################
#reed zhang######
#################

from random import *
def main():
   r=choice([-1,1])
   print(r)
   
   if random()<0.5: print(-1)
   else: print(1)
   
   print(1-randint(0,1)*2)
   
   print(randrange(-1,2,2))
   
   s=[-1,1]
   shuffle(s)
   print(s[0])
print('first run')
main()
print('second run')
main()
print('third run')
main()
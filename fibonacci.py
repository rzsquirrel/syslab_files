#####################
#Reed Zhang 10/28/14#
#####################
def fib1(n):
   a=1
   b=1
   if n<3:
      return 1
   for i in range(n-2):
      c=a+b
      a=b
      b=c
   return c

def fib2(n):
   if n==1 or n==2: return 1
   return fib2(n-1)+fib2(n-2)

def fib3(n):
   a=1
   b=1
   if n<3:
      return 1
   for i in range(n-2):
      a,b=b,a+b
   return b

def fib4(n):
   if n==1 or n==2: return 1
   if n==10: return 55
   if n==11: return 89
   if n==24: return 46368
   if n==25: return 75025
   return fib2(n-1)+fib2(n-2)
def fib5(n):
   return {1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144}[n]
def fib6(n,d):
   if n not in d: d[n]=fib6(n-2,d)+fib6(n-1,d)
   return d[n]

def fib7(n):
   from math import sqrt
   return int(round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))

def fib8(n):
   from decimal import Decimal, getcontext
   from math import sqrt
   if n>70:
      getcontext().prec=2*n
   phi1=Decimal((1+sqrt(5))/2)
   phi2=Decimal((1-sqrt(5))/2)
   return round((phi1**n-phi2**n)/Decimal(sqrt(5)))
   
def main():
   import sys
   sys.setrecursionlimit(150000)
   assert(fib1(14)==377)
   assert(fib2(14)==377)
   assert(fib3(14)==377)
   assert(fib4(14)==377)
   assert(fib5(12)==144)
   assert(fib6(19,{1:1,2:1})==4181)
   assert(fib7(14)==377)
   assert(fib8(14)==377)
   print("ok")

   from time import clock
   N=100000

   start=clock()
   print('1. fib1(',N,') =',fib1(N))
   print('   time1 =',round(clock()-start,1),'seconds')

   start=clock()
   #print('2. fib2(',N,') =',fib2(N))
   #print('   time2 =',round(clock()-start,1),'seconds')

   start=clock()
   print('3. fib3(',N,') =',fib3(N))
   print('   time3 =',round(clock()-start,1),'seconds')

   N=39;start=clock()
   print('4. fib4(',N,') =',fib4(N))
   print('   time4 =',round(clock()-start,1),'seconds')

   N=12;start=clock()
   print('5. fib5(',N,') =',fib5(N))
   print('   time5 =',round(clock()-start,1),'seconds')
   
   N=950;start=clock()
   print('6. fib6(',N,') =',fib6(N,{1:1,2:1}))
   print('   time6 =',round(clock()-start,1),'seconds')
   
   N=70;start=clock()
   print('7. fib7(',N,') =',fib7(N))
   print('   time7 =',round(clock()-start,1),'seconds')
   
   N=80;start=clock()
   print('8. fib8(',N,') =',fib8(N))
   print('   time8 =',round(clock()-start,1),'seconds')
   
   
main()

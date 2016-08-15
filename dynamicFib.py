#########################
#                       #
#       Reed Zhang      #
#       period 1        #
#       June            #
#                       #
#########################

#something interesting about Richard Bellman: He first studied Math and CS but later moved on to focus on Biology and Medicine.


def fib1(num):
    if num<3:
        return 1
    a=1
    b=1
    for i in range(num-2):
        a,b = b,a+b
    return b

def fib2(num):
    if num<3:
        return 1
    return fib2(num-1)+fib2(num-2)

def fib3(num,Dict):
    if num in Dict:
        return Dict[num]
    Dict[num]=fib3(num-1,Dict)+fib3(num-2,Dict)
    return Dict[num]

def fib4(num):
    if num in fib4.Dict:
        return fib4.Dict[num]
    fib4.Dict[num]=fib4(num-1)+fib4(num-2)
    return fib4.Dict[num]
fib4.Dict = {1:1,2:1}

def fib5(num):
    def fib(num):
        if num in fib.Dict:
            return fib.Dict[num]
        fib.Dict[num] = fib(num-1)+fib(num-2)
        return fib.Dict[num]
    fib.Dict={1:1,2:1}
    return fib(num)

def main():
    print(fib1(8))      # = 8+13 = 21
    print(fib2(8))      
    Dict = {1:1,2:1}
    print(fib3(8,Dict)) 
    print(fib4(8))      
    print(fib5(8))      
    
main()

'''
output:
21
21
21
21
21
'''
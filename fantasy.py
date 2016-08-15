#########################
#Reed Zhang p.1 4/7/2015#
#########################
#------------------------------------------------------------------------------------------
for i in range(1,101):
    if i%3 != 0 and i%5 != 0:
        print(i)
    elif i%3 ==0 and i%5 == 0:
        print('Fizz Buzz')
    elif i%3 == 0:
        print('Fizz')
    else:
        print('Buzz')
#------------------------------------------------------------------------------------------
#I added in another elif statement in order to print 'Fizz' and 'Buzz' all on one line
#------------------------------------------------------------------------------------------
'''
Three reasons why a programmer with high coding IQ might be let go:
1. A programmer might be constantly turning in work late or working
    too slowly, in which case he/she could be let go.
    
2. A programmer might write code that's too difficult to understand,
    and if this happens too often he/she may be let go.
    
3. A programmer might fail to follow some of the directions, which 
    may annoy his/her employer.
'''
#------------------------------------------------------------------------------------------
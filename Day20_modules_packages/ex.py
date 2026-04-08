'''
module:
variables,functions, classes
.py== module
two diffrent types of modules:
1.pre modules
# import math

# name='AchieversIT'
# print(math.pi)
# print(math.sqrt(121))
# print(name)
# print(math.factorial(5))
# print(math.floor(12.8))
# print(math.cbrt(1331))
# print(math.ceil(12.4))

import random
l1=[1,2,3,4,5,6,7,8,9]
print(random.random())
print(random.randint(1,11)) ## it is going to print the values in between from the given range
print(random.randrange(1,6)) ## it is going to give the values from the strat to stop range
print(random.sample(l1,k=2)) ##return the output as a list
colors=['red','green','blue','gray']
print(random.choice(colors))
people=['mahitha','harshitha','abhi','subbu','rajesh','sandeep']
print(random.choice(people))
print(random.choices(colors,k=2)) ## return output as a list
#task
import random


score=20

rannum=random.randint(1,20)

while True:
    if score>0:
        gessnumber=int(input('Enter the number: '))
        if rannum==gessnumber:
            print('you won the game and your score is',score)
            break
        else:
            if gessnumber>rannum:
                print('your number is too high')
                score-=4
            elif gessnumber<rannum:
                print('your num is too low')
                score-=4
                    
    else:
        print('you lost the game and try again')
        break    
2.user defined modules
'''
import mymath
# import mypackage
# from mypackage import module1,module2
from mypackage.module1 import greet
from mypackage import *
import mymath as m


# print(mymath.add(10,20))
# print(mymath.sub(20,10))
# print(mymath.sub(13.25,11.97))
# print(mymath.div(13,10))

# print(eval('10*3'))

print(m.add(10,20))
greet()


        






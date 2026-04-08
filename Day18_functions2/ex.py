from random import randint
'''
def add(a,b):
    return a+b

print(add(10,20))
print(add(b=15,a=20))

print(add(10,b=10))
function with postion only arguments
def aoc(l,b,h,/):
    print(l*b*h)

aoc(l=10,b=5,h=3) 
function with key word only arguments
def aoc(*,l,b,h):
    print(l*b*h) 

aoc(l=10,b=5,h=3) 
function with mixed arguments
def aoc(a,b,/,*,c,d):
    print(a*b*c*d)

aoc(10,b=20,c=30,d=40)
function with variable length postional arguments
def add(*args):
    value=0
    for i in args:
        value+=i
    print(value)    

add(1,2,3,4,5,6,7,8,9)  
function with variable length keyword arguments
def person(**kwargs):
    print(kwargs)


person(name='Hareesh',age=40,job='ittrainer',stream='pyfull stack') 
nested function
# def outter():
#     print('this is starting of outter function')
#     def inner():
#         print('this is a inner function')
    
#     print('this is ending of inner function')
#     inner()

# outter()

# def outter():
#     print('this is starting of outter function')
#     def inner():
#         print('this is a inner function')
    
#     print('this is ending of inner function')
#     return inner
    

# o=outter()
# o()

clousers
def outter(a,b):
    
    def inner():
        print(a+b)
    inner()

outter(10,20)  
Higher order functions
call back function
def welcome(f):
    print('-'*10)
    f()
    print('-'*10)

def greet():
    print('Hello World')    

welcome(greet)
'''
# sum=0
# for i in range(1,randint(1,20)):
#     x=int(input('Enter number: '))
#     sum+=x

# print(sum)

  
# a=10

# def data():
#     global a
#     a+=10
#     print(a)
# data()
# print(a)







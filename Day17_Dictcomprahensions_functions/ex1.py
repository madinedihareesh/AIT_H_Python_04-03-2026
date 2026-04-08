'''
types of function
1.built in 
2.user defined functions
'''
# print()
# len()
# int()
# bin()
# str()
# oct()
# hex()
print(__name__)
'''
def function_name(arrguments):
    block of code

function is nothing but a reuable block
of code can be utilized n no of times it can take 
input values and return value   
'''
def greet():
    print('Hello World')

greet()    
greet()    
greet()    
greet()    
greet()  

'''
user defined functions
diffrent types of functions
1.simple function
def greet():
    print('Hello World')
2.function with arrguments/parameters  
def add(a,b): ##formal arrguments
    print(a+b)

add(10,5)   ##actual arrguments
3.function with defeault arrguments  
def aoc(l,b,h=1):
    print(l*b*h)

aoc(10,5)
aoc(10,5,3)  
4.function with return statements
'''
def add(a,b): ##formal arrguments
    print(a+b)

add(10,5)   ##actual arrguments

def welcome(name):
    print('welcome ',name)

welcome('uday')
welcome('usha')

def aoc(l,b,h=1):
    print(l*b*h)

aoc(10,5)
aoc(10,5,3)  

def hello():
    return 'hello'

print(hello())


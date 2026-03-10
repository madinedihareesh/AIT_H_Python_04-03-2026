# condition:
# conditional statements:
'''
types of conditional statements:
1.if (simple)
2.if else
3.elif lader(else if)
4.nested condtional statements
5.match case
6.terinary oparater
'''
'''
indentation: 
here i am talking:
    About some condtions
    or a block of code 
    so that it can specify
    what exactly i am talking about
After completion i can give a statemet     
'''
'''
print()
yelid
return
'''
'''
input():string
'''
'''
if condtion syntax

if (condition):
    block of code
    completed 
other statements    
'''
# simple if
'''
bill=int(input('Enter your bill amount:'))
if bill>1000:
    print('Food will be served soon...')

age=int(input('Enter your age:'))
if age>=18:
    print('Elgible to vote')    
'''
# if else statements:
'''
number=int(input('Enter the number:'))
if number%2==0:
    print(number,'is a even number')
else:
    print(number,'is a odd number')  

login=int(input('Enter your login time: '))
if login<=9:
    print('You have loggedin on time')
else:
    print('You are going to get half day lop')

'''
# elif lader    
'''
bill=int(input('Enter the Bill amount:'))
if bill>=5000:
    totalbill=bill-(bill*0.3)
    print(totalbill,'30 percent discount applied on your bill')
elif bill>=3000 and bill<5000:
    totalbill=bill-(bill*0.2) 
    print(totalbill,'you got 20 persent discount on your bill')
elif bill>=2000 and bill<3000:
    totalbill=bill-(bill*0.1)
    print(totalbill,'you got 10 poersent discount on your bill') 
else:
    print('No discount is applied on your bill')         
'''
# nested conditional statements
# marks=int(input('Enter the marks:'))
# if marks>=40:
#     if marks>=90:
#         print(marks,"Grade is 'A'")
#     elif marks>=70 and marks<90:
#         print(marks,"Grade is 'B'") 
#     elif marks>=50 and marks<70:
#         print(marks,"Grade is 'c'")
#     else:
#         print(marks,"Grade is 'D'")
# else:
#     print(marks,"Failed")    

# MOT=input('Enter your means of transport:')
# if MOT:
#     if MOT=='BUS':
#         print('I am travaling By BUS')
#     elif MOT=='TRAIN':
#         print('I am travaling BY train') 
#     elif MOT=='CAR':
#         print('I am travaling by CAR')
#     elif MOT=='BIKE':
#         print('I am travaling by BIKE')
#     else:
#         print('I have cancelled my plans')     
# match
'''
day=int(input('Enter your day no:'))
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuseday')
    case 3:
        print('Wednsday') 
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saterday')
    case 7:
        print('Sunday') 
    case _:
        print('Enter numbers between 1 to 7')                             
'''
'''
flavor=input('Enter the flavor: ')
match flavor:
    case 'vanila':
        print(flavor,'will be served soon')
    case 'choco':
        print(flavor,'will be served soon')
    case 'buttersctoch':
        print(flavor,'will be served soon')
    case 'blackcurrent':
        print(flavor,'will be served soon')
    case 'coconut':
        print(flavor,'will be served soon')
    case _:
        print(flavor,'is currently not available')
'''                            
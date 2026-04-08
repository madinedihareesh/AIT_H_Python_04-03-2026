# username=input('Enter your Username:')
# password=input('Enter your password: ')
# cpassword=int(input('Repeat the password: '))
# if password==cpassword:
#     print('register sussesfull')
# else:
#     print('password didnt match')
# print('Login Here')
# uname=input('Enter username')       
# lpassword=input('Enter your password:')

# if uname==username and lpassword==cpassword:
#     print('You entered into the program')
# else:
#     print('login failed')    

'''
types:
nameerror
print(a)
valueerror
print(int('python'))
syntaxerror
a=10
if a%2==0
    print('It is an even number')
else:
    print('it is an odd number')  
typeerror
print(10+'10')
logical error
num=10
if num%2!=0:
    print('even number')
else:
    print('odd number')   
zeroDivisionError:
print(10/0)

'''
'''
try:
    condition
expect type of error:
       print(') 
else:
    what it has to do 
finally:
     it will defentlly excute           
'''   

try: 
    num=int(input('Enter a number'))
    num=num+'10'
except Exception as msg:
    print(msg)
  
else:
    if num%2==0:
        print('even number')
    else:
        print('odd number') 
finally:
    print('program completed')                   

  


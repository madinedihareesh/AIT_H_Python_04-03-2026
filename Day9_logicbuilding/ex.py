'''
Ascii: Amarican Standed Code for information interchange
45 0-9
65 A
96 a
'''
# print(ord('A'))
# count=64
# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             count+=1
#             print(chr(count),end=' ')
#     print('')        



# count=0
# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             count+=1
#             print(count,end=' ')
#     print('')  

'''
year=int(input('Enter the Year:'))
if year%100==0:
    if year%400==0:
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
elif year%4==0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')                  
'''
# 0 1 1 2 3 5 8 13 
'''
num=int(input('Enter the a number'))
a=0
b=1
for i in range(1,num+1):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
'''

'''
num=int(input('Enter the number to sum: '))
sum=0
while num>0:
    res=num%10
    sum+=res
    num//=10
print(sum) 
'''

for i in range(1,6):
    if i==3:
        print('three')
        break
    else:
        print(i)



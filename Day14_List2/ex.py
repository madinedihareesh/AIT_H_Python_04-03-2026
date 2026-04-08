# List comprhenssion
'''
name=[expression for value in range()]
'''
# l1=[x+2 for x in range(1,11)]
# print(l1)

# l2=[x**2 for x in range(1,6)]
# print(l2)


# l3=[x.lower() for x in 'PYTHON']
# print(l3)

# l4=[int(x) for x in '1234']
# print(l4)

# l5=[x for x in 'ab*cd7e' if x.isalpha()]
# print(l5)

# l6=[x for x in range(1,11) if x%2==0]
# print(l6)


# nested list
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
for i in l1:
    for j in i:
        print(j,end=' ')
    print()  

     

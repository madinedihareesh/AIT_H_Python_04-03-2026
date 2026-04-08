'''
list will be declared in [] each element in the list will be
sarparated by ','
list can accpect dupilicate values
list can also accpect hetrogenious values as elements

list is a ordered collection of elemnts,supports dupilicate
values and it supports hetrogious values. it is mutable
'''
# l=[1,2,3,4,5,1,4,3,5,2]
# print(type(l))
# l1=['name',21,25000.00,10+9j,True]
# print(l1)
# # ways of creating a list
# # empty list
# l2=[]
# print(l2)
# # bulit method list
# l3=list('python')
# print(l3)
# l4=list((1,2,3,4,5))
# print(l4)

# how to read the values from a list
# print(l1[0])
# l1=[1,2,3,4,5]
# print(l1[-1])

# slicing on list
# l1=[1,2,3,4,5,6,7,8,9,10]
# # print(l1.pop())
# # print(l1)
# l2=l1[0:7]
# print(l2)
# l1[4:4]=[11]
# print(l1)
# l1[4:7]=[10]
# print(l1)
# l1[4:4]=[11,12,13]
# print(l1)
# l1[15:15]=[14]
# print(l1)
# l1[::2]=['A','B','C','D','F','G','H']
# print(l1)
# l1[::-1]=[10,11,12,13,14,15,16,17,18,19,20,21,22]
# print(l1)

# list concatination and list repitation
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=l1+l2
# l4=l1*3
# print(l3)
# print(l4)

# how to travers trough a list
# l1=[1,2,3,4,5,6,7]
# for i in range(0,len(l1)):
#     print(l1[i])

# for i in l1:
#     print(i)
# print(9 in l1)

# list comparision
# l1=[1,2,3,5]
# l2=[1,2,3]
# l3=[1,2,4]

# print(l1==l2)
# print(l2!=l3)
# print(l3>l1)

# methods of a list
# adding 
'''
append 
extend
insert
'''
'''
l1=[1,2,3,4,5]
l1.append(6) ##append can accept excatly on argument
print(l1)

l1.extend([7,8,9]) ##we can multiple elements to list but it has a sequential data type
print(l1)

l1.insert(0,10)
print(l1)

l2=l1.copy()
print(id(l1))
print(id(l2))
'''
# Removing Elements form a list
'''
pop
remove
clear
del
'''
'''
l1=[1,2,3,4,5,6,1,7,8,9,10]
l1.insert(3,11)
l1.pop()
print(l1)

l1.remove(1)
print(l1)
l1.remove(1)
print(l1)

l1.clear()
print(l1)

del(l1)
print(l1)
'''
# finding,sort,reverse methods
# l1=[1,2,3,4,5,6,7,1,8]
# print(l1.index(1,1))

# print(l1.count(2))

# l1.reverse()
# print(l1[0])

# l1=[30,100,90,70,20,40,50,10,60]
# l1.sort(reverse=True)
# print(l1)

# l1=['cat','flag','egg','apple','dog','ball','Zebbra']
# l1.sort()
# print(l1)







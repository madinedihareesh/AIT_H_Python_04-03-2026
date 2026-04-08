'''
[]()
'''
'''
t=(3,)
print(type(t))
t1=('murali',23,5000.00,11+10j,True)
print(t1)
t2=()
print(type(t2))
t3=tuple([1,2,3,4,5])
print(t3)
t4=tuple('PYTHON')
print(t4)
t5=1,2.17,3+9j,True,'sample' ##tupple packing
print(id(t5[0]))
print(id(t5[1]))
print(id(t5))
a,b,c,d,e=t5 ##tupple unpacking
print(a)

print(dir(tuple))
'''

# t=(1,2,3,4,5,6,1,7,2,8)
# print(t.index(1,1))

# print(t.count(1))

# how to traverse through the tupple
# for i in t:
#     print(i)

# print(t[-1])
# t1=t[0:5]
# print(t1)

# tuple comprahension
t=tuple([x for x in range(1,10)])
print(t)
# genarator + unpacking
t1=(*(x for x in range(1,11)),)
print(t1)

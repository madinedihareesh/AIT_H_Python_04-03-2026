'''
{}
'''
# s1={10,20,20,40,100,50,60}
# print(type(s1))
# print(s1)
# s2={}
# print(type(s2))
# s3=set()
# print(s3)
# s4=set('python')
# print(s4)
# s5={5}
# print(s5)
# for i in s1:
#     print(i)

# s1.add(70)
# print(s1) 

# maths methods:
#s={1,2,3,4,5,6,7,8,9,10}## s is a superset of s1 and s2
#s1={1,2,3,4,5} ##s1 is a sub-set of s
#s2={6,7,8,9,10} ##s2 is a subset of s

# union 
# s1us2
# intersession
# diffrence
# sematic diffrence

s1={1,2,3,4,5};s2={4,5,9,8,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

# | union
# & intersection
# - diffrence
# ^ symetic_diffrence

print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)

# intersection_update
# diffrence_update
# symetic_diffrence_update

# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)

# genral methods on set
'''
add
update
remove
pop 
copy
clear
'''
# s1.add(10)
# print(s1)
# s1.update([10,11,12,13,14,15])
# print(s1)
# s1.remove(5)
# print(s1)
# s1.pop()
# print(s1)
s1.clear()
print(s1)
del(s1)
# print(s1)
# print(10+'10')

s3=s2.copy()
print(s3)
print(id(s2))
print(id(s3))

# setcomprahension

s4={x for x in range(1,6)}
print(s4)

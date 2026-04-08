# '''
# {1:'one'}
# '''
# d={1:'one','value':True,12.59:'float value',10+11j:'complex number',1:'hundured'}
# print(d)
# print(d[1])
# d['value']=False
# print(d)
# d[10]='ten'
# print(d)

# for i in d:
#     print(d[i])


# # iterrable pairs
# l3=[(1,'one'),(2,'two'),(3,'three')]
# d2=(dict(l3))
# # zip
# l1=[1,2,3,4,5]
# l2=['one','two','three','four','five']
# d1=dict(zip(l1,l2))
# print(d1)

# # enumarate
# l5=[100,200,300,400,500]
# e=enumerate(l5,start=1)
# d3=dict(e)

# '''
# keys()
# values()
# items
# '''
# for i in d.keys():
#     print(i)


# print(d.values())
# print(d.items())


# print(d.get(10))
# print(d.setdefault(5,'undifined'))
# print(d)

# d1={6:'six'}
# d.update(d1)
# print(d)

# l1=[1,2,3,4,5]
# d2=dict.fromkeys(l1)
# print(d2)

# d.pop(6)
# print(d)

# d.popitem()
# print(d)

# d.clear()
# print(d)
# # del(d)
# # print(d)
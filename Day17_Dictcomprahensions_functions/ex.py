l1=[1,2,3,4,5]
l2=['one','two','three','four','five']

d={x:y for x,y in zip(l1,l2)}
print(d)

t=[(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]
d1={x:y for x,y in t}
print(d1)

l3=['one','two','three','four','five']
d2={x:y for x,y in enumerate(l3,start=1)}
print(d2)
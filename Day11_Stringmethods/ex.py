# s='Hello world'
# '''
# method:
# method is nothing but a function defined in class
# '''
# # splicing oparator [start:stop:step] range(start,stop,step)
# s1=s[0:5:1]
# print(s1)
# print(len(s1))
# s2='madam'[::-1]
# print(s2)
# s3=s[::2]
# print(s3)

# methods
# find:
# print(s.find('hi'))
# rfind:
# s='madam'
# print(s.rfind('m'))
# index
# s='hello world'
# print(s.index('something'))
# rindex
# s='madam'
# print(s.rindex('m'))
# count
# s='Hi there! Hello world how are you doing'
# print(s.count(' '))
# ljust
# s='Hi hello'
# print(len(s))
# s1=s.ljust(15,'$')
# print(s1)
# rjust
# s='hi hello'
# s1=s.rjust(20,'#')
# print(s1)
# center
# s='madam'
# s1=s.center(15,'_')
# print(s1)
# zfill
# s='hello'
# s1=s.zfill(10)
# print(s1)
# strip
# s='madam  '
# print(s)
# s1=s.strip()
# print(s1)
# lstrip
# s='   madam'
# print(s)
# s1=s.lstrip()
# print(s1)
# rstrip()

s='    madam    '
res=''
for i in s:
    if i!=' ':
        res+=i
print(len(res))


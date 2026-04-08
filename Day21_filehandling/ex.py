'''
open() method to handle a file
syntax
open('filename.extension','oparations')
oparations:
read r
f=open('test.txt','r')
print(f.readable())
f.close()
write w
f=open('test1.txt','w')
# con=['Hi hello\n','How are you doing\n','i am doing fine','how about you']
print(f.writable())

f.close()
append a
with open('test.txt','a') as f:
    f.write('\ni am also doing grate')
create x
# f= open('test.txt','x')
# f.close()
read write r+
with open('test.txt','r+') as f:
    f.read()
    f.write('\nHello')
    print(f.tell())
    f.seek(0) ## 0- starting 1-current 2-ending
    data=f.read()
    print(data)
write read w+
with open('test1.txt','w+') as f:
    con='Hi there\n how are you'
    f.write(con)
    f.seek(0)
    data=f.read()
    print(data)
append read a+
with open('test1.txt','a+') as f:
    f.write('\n i am doing fine')
    f.seek(0)
    data=f.read()
    print(data)
read binary rb
write binary wb
'''
data=None
with open('python.jpeg','rb') as f:
    data=f.read()
    print(data)

with open('python1.jpeg','wb') as f:
    f.write(data)    



    





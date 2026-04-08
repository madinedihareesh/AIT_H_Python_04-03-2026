'''
Genral Inheritance
class Father:
    def show(self):
        print('Father is a Businessman')

class Child(Father):
    def display(self):
        print('child is still studing')

------ parameterized class Inhertance        
class Father:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f'Father\'s Name is {self.name}')
        print('Father is. a Bussiness man')
class Child(Father):
    def __init__(self,name):
        super().__init__(name)

    def show(self):
        print('child is still student')

c=Child('Pardhu')
c.show()
c.display()        

c=Child()
c.display()
c.show() 
Multiple inharitance

multilevel inharitance
hrarical inharitance
hibried inheritance
'''
class Father:
    def __init__(self,job,**kwargs):
        super().__init__(**kwargs)
        self.job=job
    def display(self):
        print(f'Father is a Dancer and he is a {self.job}')

class Mother:
    def __init__(self,role,**kwargs):
        super().__init__(**kwargs)
        self.role=role
    def show(self):
        print(f'Mother is a signer and she is a {self.role}')

class child(Father,Mother):
    def __init__(self,job,role):
        super().__init__(job=job,role=role)
    def read(self):
        print('he is a dancer com singer')

c=child('Software Employee','Housewife')
c.read()
c.show()        
c.display()



       
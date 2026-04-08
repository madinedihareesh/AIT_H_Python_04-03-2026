# a=10
# print(type(a))
# print(dir(int))
# print(a.is_integer())

'''
class nameofclass:
    static variable diclaration
    def __init__(self):
        instance variable dicalration
    instance method    
    def method1(self,arrguments):
        block of code for the function
    @static method
    def method2():
        block of code 


c=nameoftheclass()               
'''
'''
class Sample:
    avalibility=24 ##static variables
    def __init__(self):
        self.name='AchieversIT' ##instance variables properties
        self.age=11
    ##instance method    
    def purpose(self):
        print('Edutech')
    ##static methods
    @staticmethod
    def display():
        print('It is a it training institute')    

# print(Sample.avalibility)
#Sample.display() ##calling a static method
# print(Sample.avalibility) calling a static property

s=Sample()
print(s.avalibility)     
s.display() 
print(s.name)
a=Sample()
print(a.name) 
print(a.age)  
a.purpose()   
print(id(a))
print(id(s))
'''
# class Sample:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self,person):
#         print(f'welcome {person}')

# s=Sample('james',20)
# print(s.name)
# print(s.age)
# s.display('jason')        

# class Sample:
#     name='AchieversIT'
#     age=11 
#     def __init__(self,loc):
#         self.loc=loc
#     @classmethod    
#     def show(cls):
        
#         print(f'the name of the institute is{cls.name} and it started {cls.age} ago')
#     def display(self):
#         print(f'the institute is located at {self.loc}') 
#     @staticmethod
#     def title():
#         print('AchieversIT')    

# s=Sample('Hyd')
# s.show()
# s.display()
# Sample.title()




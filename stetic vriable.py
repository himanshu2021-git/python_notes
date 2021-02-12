#todays topic is static variable()(class level variable)
#if the variable isn't vary object to object then this consider as static variable
#this is declare mostly outside of the mthod means directy in the class
#for total class only one copy of static variable will be created and share with all its object.
#we can access static variable either by class name or by object reference.But recommended to use class name

#places where to declare statoc variables.
#direclty inside the classfrom outside the methods.
#inside the constructor by using class name
#inside the method by using class name
#inside the classmethod by using either class name or cls variable
#inside the static method by using class name.


#1.direclty inside the classfrom outside the methods.
"""
class Test:
    a="Himanshu" #class level variable
    def x(self): #instance method
        print("Hello",Test.a) #can't access it becAUSE OF DATA ABSTARCTION HERE WE USE CLASS NAME
t=Test() #here it is object referance
print(t.a)
t.x()        
"""

#2.inside the constructor by using class name
"""
class Test1:
    b1="my class variable"
    def __init__(self):
        self.a="instance variable"
        self.b="2ns instance variable"
        #here if we create class level variable inside the constructor so we use class name.variablename
        Test1.c="i'm class level variable"
    def x1(self):
        print("test1.c====inside the method",Test1.c)
q=Test1()
print(q.a)
print(q.b1)
print(q.b)
print(q.c)
"""

#3.Inside the method by using class name
"""
class Test2:
    x="my class variable"
    def x1(self):
        Test2.new="i m class lvl but inside the method"
        print("sdfs",Test2.x)
        print("svsd",Test2.new)
d=Test2()
print(d.x)#object reference
print(Test2.x) #class name
#Test2.new
d.x1()
Test2.new
"""


#4.inside the class method using cls variable

class Test3:
    a="class lvl var"
    def __init__(self):
        self.a1=78
        self.b1=98 #these are instance level var
        Test3.c1="i'm class level but inside the constructor"
    def my(self):
        Test3.d1="class lvl but inside method"
        Test3.e1="instance lvl but inside method"
        print(Test3.d1)
        print(self.e1)
        print(self.a1)
        print(Test3.a)
    def my1(a,b):
        Test3.f="i'm class lvl but in static mehtod"
    @classmethod
    def my2(cls): #cls=any variable
        cls.g="i'm class lvl but inside class method"
        Test3.h="also in class method but using classname"
        self.t=5

y=Test3()
"""print(y.a)
print(y.b1)
print(y.a1)

#Test3.c1()
#Test3.my()#not psossible"""
y.my()

y.my1(5)


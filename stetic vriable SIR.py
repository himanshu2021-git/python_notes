#Today we discussss about Static Variable() (Class level variable.)

#If the varibale is not vary from object to object then this consider as ststic variable.
#This is declare mostly  outside of the method means directly in the class.
#For total class only one copy of static variable will be created and share with all its object .
#We can access static variable either by class name or by object refrence.But recommended to use class name.


#Places where to declare static variable.
#Directly in the class from outside the method.
#Inside the constructor by using class name
#Inside the method class name
#Inside classmethod by using either class name or cls variable.
#Inside the static method by using class name.


#==================Directly in the class from outside the method=================.\

class Test:
    a = "NIshant"
    def x(self):  #instance method
        print("Hello",Test.a)  #here we use classname.varible .........accessing class lvl variable into method

t = Test()  #here it is object refernce
print("t.a-------",t.a)
t.x()
print("here we access class lvl variable=====",Test.a)#.......accessing outsside the method

#===================Inside the constructor by using class name====
class Test1:
    b1 = "MY class Variable"
    def __init__(self):
        self.a = "Instance variable"
        self.b = "Also an instnace variable"
        #here if we create class lvl variable inside the  constructor so we use classname.variable name
        Test1.c = "I ma class Lvl variable"
    def x1(self):
        print("test1.c===inside the method==",Test1.c)
q = Test1()
print(q.a)
print(q.b)
print(q.c)

#print(Test1.a)  #it is not possiblr to access
print("b1=====",Test1.b1)
print("c=====",Test1.c)
#print("b=======",Test1.b)  #it is also not possible due to not creation of an object.if we want to access just call the class and make an object.

#***************************Inside the method by using class name*************
"""
class Test2:
    x = "MY class Variable"
    
        
    def x1(self):
        Test2.new = "I am class lvl but inside the method"
        print("test2.x===inside the method==",Test2.x)
        print("test.new=====",Test2.new)
d = Test2()
print("d.x====",d.x) #object refrence
print("test2.x====",Test2.x) #class name
d.x1()
Test2.new
"""
    
#Inside the class method by using cls variable.

class Test3:
    a = "Class var"
    def __init__(self):
        self.a1 = 78
        self.b1 = 95  #thesse 2 are instance lvl  var
        Test3.c1 = "I am class lvl but inside the constructor"
    def my(self): #instance method
        Test3.d1 = "I am class lvl but inside the method"
        self.e1  = "instace lvl but inside the method"
        print(Test3.d1)
        print(self.e1)
        print(self.a1)
        print(Test3.a)
    def my1():  #it is static method
        Test3.f = "I am class lvl but in static method" #Inside the static method by using class name.
        #self.k = 4  #not possible if we have static method then we cant give any instance method inside it thats y it is not possible
    @classmethod
    def my2(cls):  #cls ==  any variable
        cls.g = " I am class lvl but in class method"
        Test3.h = "Also in class method but using class name"
       # self.t = 5  if we have static method then we cant give any instance method inside it thats y it is not possible


#acces with the help of object reference
y = Test3()
"""
"""
print("a===",y.a)
print("a==",Test3.a)
#constructor var--here we use object refernce y
print("y.a1=====",y.a1)
print("y.b1=====",y.b1)
print("y.c1=====",y.c1)
#using class name...
#Test3.a1 #not run till the constructor isn't run
#Test3.b1
Test3.c1 #it runs because of class lvl variable

#try to access instace method using class name
#Test3.my() #not possible ..........when we use classname.emthod then it will treat it as staic method

y.my()              
    
#y.my1()     #not possible...........object refereance always guves oone argument and that is self
Test3.my1()
print("dta===",Test3.__dict__)

#class method access with thye help of object reference as well as class name
y.my2()
Test3.my2()
print("dta===",Test3.__dict__)
"""

class My:
    def __init__(self):
        self.a = 78
        self.b = 45
    def new(self):
        self.c = 78
    def my(self):
        self.d = 89622

z = My()
print(z.__dict__)

"""


















        

#Inheritance--(HAS -A-RELATIONSHIP) this is a kind of relationship between two or more classes. in inheritance the classes share there attribute(methods/variable) with some other class
#types of inheritance
#----------------------------
#simple inheritance--only a single class tries aquire the attributes of some other class.
"""
class SuperClass:
    a=10
    def meth(self):
        print("This is instance method inside suoer class")

class Subclass(SuperClass):
    pass

sb=Subclass()
sb.meth()
print(sb.a)#method scoping: this is the process of finding the method
print(type(sb))#Subclass this is its type
"""

#--Role of constructor in inheritance
#inheritance is oerfirmed with the help of cinstructor chaining
#if you don't perform the constructor chaining theen only static members and all methods will be shared wuth child.instance variable will never be shared
"""

class Him:
    var=10
    def __init__(self):
        self.inst_var=50
    def method(self):
        print("method")
class XYZ(Him):pass #no constructor PVM create a blank con. def __init__(self): super().__init__() in sub class and in suoper class then pass is return
    #def __init__(self):pass #no instance variable isn't share due to this self defined cinstructor
x=XYZ()
print(x.inst_var)
"""

#====================================Mutiple inheritance

#a single class borrows the attributes of more than one class
"""
class A:
    def method(self):
        print("This is A  class method")
class B:
    def method(self):
        print("This is B class method")
class C(B,A):pass #only one super will be create 

c=C()
c.method() #method_scoping priorites 1st: self then 2nd priority : will be first parent class and so on
#even if your class more than one parent single super is enoguh to executingconstructor of all parent classes
"""


#=====================================multilevel
"""
class Parent:
    def method(self):
        print("This is from parent class")
class A(Parent):
    def method(self):
        print("This is A  class method")
class B(A):
    def method(self):
        print("This is B class method")
class C(B):pass #only one super will be create 

c=C()
p=Parent()
p.method()
c.method()
print(dir(c))
"""

#cyclic===========================================
#in this kind of inheritance parent try to acquire the attribures of childs as well this isn not possible in python interms of inheritance
#we can acheive this type of inheritance with the help of bound and unbound way of calling a method
#Bound.........
#we aren't responsible

class A:
    def method(self):
        print("THis is a method")
        print(id(self))
    @staticmethod #deco
    def staticMethod():
        print("THis is static method")
    @classmethod
    def classMethod(cls):
        print(cls)
        
a=A()
a.method() #bound way of calling a method

a.staticMethod()
print(id(a))
a.classMethod()
#Factory method---


#unbound-----we are responsible to give value f self....
notepad.pw/pywe930

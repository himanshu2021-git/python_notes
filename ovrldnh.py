#Today we discuss about overloading am=nd its all functioning....
#Polymorphism---Present in many forms
#   Overloading--same name wuth different parameter
#       Operator overloading(possible)
#       Method Overloading(Not possible)the example is performed below: it overrides
#       Costructor overloading(Not possible) 
"""
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(self.a+self.b)#Overrided
    def sum(self):
        print(self.a-self.b)
t=Test(6,5)
t.sum()
"""
"""
class Hello:
    def __init__(self,a,b):
        print("Hello i'm no.1")
    def __init__(self,a,b,c):
        print("Hello i'm no.2")
    def __init__(self,a,b,c,d):
        print("Hello i'm no.3")
    def __init__(self,a,b,c,d,e):
        print("Hello i'm no.4")
Hello(2,3,4,5,6)
"""
#Method overloading


#Try to overload with variable length parameter
"""
class Test:
    def add(self,*a):
        t=0
        for x in a:
            t=t+x
        print("Total==",t)
x1=Test()
x1.add(12,86,74,878,878)
"""
#Try to implement overloading (Method) but not possible
"""
class Ovrld:
    def m1(self):
        print("no args")
    def m1(self,a):
        print("One args")
    def m1(self,a,b):
        print("Two args")
    def m1(self,a,b,c):
        print("three args")
o=Ovrld()
o.m1(2,4,6)
"""

#Constructor overloading with variable length argument
"""
class Hello:
    def __init__(self,a,b):
        print("Hello i'm no.1")
    def __init__(self,a,b,c):
        print("Hello i'm no.2")
    def __init__(self,a,b,c,d):
        print("Hello i'm no.3")
    def __init__(self,a,b,c,d,e):
        print("Hello i'm no.4")
    def __init(self,*z):
        print("Hello i'm variable length argument") #its a just trick

Hello(2,3,4,5,6)
"""
#=======================Operator Overloading=============================

class Cale:
    def __init__(self,days):
        self.days=days
        print(self.days)
    def __add__(self,new): #Magic method
        return self.days+new.days #we can overide the method from changing operand aat here 
a1=Cale(100)
a2=Cale(130)
#print(a1+a2)


#Now try to overload multiple operator and also mpore than two object
#Whenever we call + operator then add() method will be called
"""
class Cale:
    def __init__(self,days):
        self.days=days
    def __add__(self,new): #Magic method
        return self.days+new.days
    def __sub__(self,new): #Magic method
        return self.days-new.days
    def __mul__(self,new): #Magic method
        return self.days*new.days
    def __floordiv__(self,new): #Magic method
        return self.days//new.days
    def __lt__(self,new): #Magic method
        return self.days<new.days
a1=Cale(100)
a2=Cale(130)
a3=Cale(10)
print("add==",a1+a2)
print("sub==",a3-a1)
print("mul==",a3*a2)
print("div==",a1//a3)
print(a1<a3)
"""
"""
class Cale:
    def __init__(self,days):
        self.days=days
    def __str__(self):
        return "No. of days"+str(self.days)
    def __add__(self,new): #Magic method
        t=self.days+new.days
        b=Cale(t)
        return b
    def __sub__(self,new): #Magic method
        t= self.days-new.days
        b=Cale(t)
        return b
    def __mul__(self,new): #Magic method
        t= self.days*new.days
        b=Cale(t)
        return b
    def __floordiv__(self,new): #Magic method
        t= self.days//new.days
        b=Cale(t)
        return b
    def __lt__(self,new): #Magic method
        t= self.days<new.days
        b=Cale(t)
        return b

a1=Cale(100)
a2=Cale(130)
a3=Cale(10)
print("add==",a1+a2+a3)
print("sub==",a3-a1)
print("mul==",a3*a2)
print("div==",a1//a3)
print(a1<a3)
"""

#todays topic is variable(attributes)in OOPs
#3types of vrible
#1.instance(object level) #our data will change with object change
#2.static level variable(class level)
#3.loval variable(method level)...
"""
class Test:
    a="himanshu" #class level or static variable
    def __init__(self,x,y): #constructor...__init__ is construcctor
        self.x1=x #here both x1 and y1 are consider as instance variable
        self.y1=y
    def my(self): #method
        s="Local variable"
        print("s===",s) #here s is local varibale


z=Test(12,23) #here x1 and y1 hold 12,23
print(z.a)
print(z.__dict__)
z1=Test("himanshu","hello")
print(z1.a)
print(z1.__dict__)
z.my()
"""

#Instance level variable-----

#if the value of a variable from object to object,then such type of variable consider as instance level variable
#for every object a seperate copy of instance varible will be created.

#so where we can declare instance level variable---
#1.inside constructor by using self----here when we use this as per object automatically these variable added to the object
#2.inside instance method by using self variable----here from the method using self then your variable added to the instance.
#3.outside of the class by usng object reference varibale.---it is always different from the other objects.



#1. inside the constructor
"""
class Abc:
    def __init__(self): #here we have 4 insance level variable
        self.name="Himanshu"
        self.city="delhi"
        self.id=2242
        self.rank=246

a=Abc()#here ref variable for object
print("class===",a.__dict__)

a.name="Rahul"
a.id=443
print("after updatiion at object level",a.__dict__)
a1=Abc()
print("in a1",a1.__dict__)
"""


#2.inside instance method by suing self variable
"""
class Hello:
    def __init__(self):
        self.a= 45 #instance level var inside the constructor
        self.b= 56
    def my(self):
        self.x=232
        self.y=23234
        z=5654
a=Hello()
print(a.__dict__)
a.my()
print(a.__dict__)
a1=Hello()
a1.my()
a1.y=3636
print(a1.__dict__)
"""

#3. Outside the class by using object refernece...

class Third:
    def __init__(self):
        self.a= 4 #instance level var inside the constructor
        self.b= 6
    def my(self):
        self.x=23
        self.y=24
        z=565 #local variable

x=Third()#here x is the reference varible or object
print("same daata===",x.__dict__)
#now for x and y which is in instance level call my
x.my()
print(x.__dict__)

#now try to create instance variable from outsid the class by using object reference
x.c="Outside"
print("ooouuuttt",x.__dict__)
x1=Third()
x1.my()
print("now check in x1 that there is c or not",x1.__dict__)




#how to access instance variables
#we can access instance variable the class by using self.
#access outside from the object by using object reference
"""
class Access:
    def __init__(self):
        self.a= 4 #instance level var inside the constructor
        self.b= 6
        self.c="i'm c"
        self.d=343
    def disp(self): #access instance level variableinside the class(method-method)
        print("a===",self.a)
        print("b===",self.b)
    def disp1(self):
        print("from disp1")
        print("a===",self.a)
        print("b===",self.b)
        print("d===",self.d)
c=Access()
c.disp()
c.disp1()

#also access instance varuable like
#object refrence vriable name

print(c.a)
print(c.b)
print(c.c)

"""
#now try to delete these variable

class Dlit:
    def __init__(self):
        self.a= 4 #instance level var inside the constructor
        self.b= 6
        self.c="i'm c"
    def d0(self):
        print(self.a)
        print(self.b)
        print(self.c)
        self.d =45.5
    def d1(self):
        del self.c
d=Dlit()
d.d0()
print("data1",d.__dict__)
del d
e=Dlit()
e.d0()
print("using e==",e.__dict__)
e.d1()
print(e.__dict__)


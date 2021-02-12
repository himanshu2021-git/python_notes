# Today we discuss about class,object and consturctor
# how constructor help class to create an object

"""
class My:
    def hello(self,name):
        print("Good Morning",name)
My().hello("Himanshu")

#if we want to create an object from the class then constructor to help us.
#a constructor is a special type of method ewhci is used to intialize the instance member of the class
#constructor use to initializing the valuue to the data member and member function
#constuctor use to provide memory to data
#construtor name is same as class name
#it automatically called when an object of any class is created
#consturctor is optional and if we not create it then PVM(python virtual machine)called it by default.

#EX:

class add:
    def sum(self,a,b): #self connect the constructor(constructor level variable)
        print("sum====",a+b)
add().sum(6,7)#there is 3 arguments ,constructor is bydefault thats y we use self to connect the constructor


#why we use self? it means it holds itself we can use anything instead of self


class add1:
    def __init__(self,a,b):
        print(a+b)
add1(12,32)








#Constructor and method(function)---->>>
#method>> any function which is present in the class consider as a mthod
#name of method will be anythiing
#per object method can be call any number of time
#inside method we write require logic.


#constructor--->>>
#constructor is a special type of method
#its name always be __init__
#it called itself automATICALLY when class convert into object
#constructor always be execute once per object
#inside con. we declare data requirement



"""

class test:
    def __init__(self,a,b): #these are temporary variable # we can use anythind insted of self even name also.
        self.a1=a
        self.b1=b  #constructor level variable
        print(self.a1,self.b1)
    def sum(self):
        print("sum=====",(self.a1+self.b1))
test(5,9).sum()
"""s
#__init__ is a constructor

#here we see using class we create different location
class My:
    def __init__(self):
        print("Consturctor working")
    def my(self):
        print("member")

t=My()  #t is reference variable
t1=My()
t2=My()
t.my()
My.my("Himanshu")
print(id(t))
print(id(t1)) #there is different object in each class thats why id is different
        
"""
#now we see the working of self in each object.

class My:
    def __init__(self):
        print("Consturctor working")
        print("self====",id(self))
    def my(self):
        print("member")
        
t=My() #they are efrence var. also object
t1=My()
t2=My()

print(id(t))
print(id(t1))
print(id(t2))
        
t.my()

#instance variable and instance method........ read((())))))

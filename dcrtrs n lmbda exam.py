#decorators
#function use to reuse the code and enhance the writting and struture of code...


#Decorators---
#if we have a function and we enhance its functionality by accessing it from outside without hitting its actual behaviour
#the procedure which is use to acheive it consider as Decorator calling.

#in decorator function we access a function and change its behaviour and return modified function....

#Example:
#this is decorator
#1- here a is accept function
#2-now ,indec function ectract parameter"name"
#3-
"""

def dec(a):
    def indec(name):
        if name == "sam":
            print("hey",name)
        else:
            a(name)
    return indec
@dec #it is use to connect normal function with decorator-----@ is use to connect

def wish(name):
    print("Hello",name,"Welcome")
wish("Himanshu")
wish("sam")

"""

#Decorator call with diiferent way
"""

def himan(fun):
    def indeco(name):
        if name == "Rahul":
            print("hello Boss",name)
        else:
            fun(name)
    return indeco #compulsory
@himan
#now normal function

def abc(name):
    print("You are employee",name)
abc("Himanshu")
abc("Rahul")
x=himan(abc) #another type
x("Sam")

"""
#2nd type of exapmles
#Decorator chaining----here we use multiple decorators at one time
"""
"""
def work(n):
    return n
#print("data====",work("hheh"))

def d1(fun):
    def ind1(n):
        x=fun(n)
        return x*x
    return ind1

def d2(fun):
    def ind2(n):
        x=fun(n)
        return x*x*x
    return ind2
#now calling decorators

d3=d1(work)
d4=d2(work)
print(d3(12))
print(d4(3))
"""
"""

#homework------create a function which divide we need a,b if a<b then swap a and b and if b==0 then print not acceptable



#lambda function------examples

"""l=lambda x,y:(x/y)
print(l(5,4))
"""

#Today,s topic is Modules
#Modular programming
#procedural programming is basic...functional programming encapsulated then known as modular and when modular encapsulated known as packages

#procedural>>>>> it involves withan algo or a procedure for implement in software.

#modular>>>>it divide your objective into module and then pipelining the module
#modules are made on the basisi of similarilty between functions,collection of function
#Modules? --- A py file containing python defination and statements. A module can define function,class and variable, A module is RUNNABLE code
# A group of function a variable and class saved to a file, which is nothing but module
#when we access that file into another file and use it functionalities then it is consider as module


#step for creating a module...
#1...create a py file with function and variable
#2...if we want to use member of module in our program then we should import that module
#3--- we can access member by using module name.
"""
import random as r #alias creation
print(dir(r))


for i in range(10):
    print(r.randint(0,10) )

import time
print(dir(time))
#print(time.sleep(5))
print("I am late")


import datetime
print(dir(datetime))
print(datetime.date.today())

"""
"""
#now creating a module
a=12
b=6 #data
def f1():
    print("hello i am a new small module")

def add(a,b):
    print("a+b==",a+b)

def mul(a,b):
    print("mul==",a*b)

def sub(a,b):
    print("sub==",a-b)
"""
def hello(a):
    print("from test")
    def hello1():
        print("square===",a*a)

hello(5)

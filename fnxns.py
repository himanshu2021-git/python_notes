#reverse of any number
"""
a=int(input("Enter any integer=="))
b=a
rev=0
while a>0:
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
if(rev==b):
      print("palandrome")
else:
      print("not")
print(rev)
"""

#todays'topic is FUNCTION now we have to optimise the code (reusablity)
#in control strcture we reduce the code...and function increase the resuability
#now we move towards functional programming before this we are one procedural programming
#if a groupp of statements is repeatedly then  it is not recommended to write these statements
#again and again
#here functions handle rewriting

#ADVANTAGES....(code reusability)
#function also conside as sub-routines(threadings)in class(method),procedures.

#there are two types of functions---
#1.Built in Function--language specific predefines(utility methods)
#2.User Defined function--which is created by user as per the requirement

#required keyword function
#default parameter function
#varuable elngth function
#function inside function(nested function)
#closure function


#def(mendatory)--use to define or create function.(it is mendatory for function)
#return(optional,!mandatory)
#parameters--these are the inputs which pass at upper side(anything which we pass in function is known as parameter)(formal parameters)
#arguments--(those are the data ich pass at the time of calling function lso consider as informal parameters)
#syntax=====
"""
def himanshu(parameter,param):#it is our paramter #it has existance
    print("hello",parameter,param)
himanshu(12,234)#it is just a var.no existance....it is also mandatory to print parameter..if we dont use this there is no error
himanshu("hi","kya baat")

#No argument function
def hello():
    a=int(input("Enter any no=="))
    b=int(input("Enter any no=="))
    print("sum==",a+b)
hello()
"""

#ARGUMENY BASED FUNCTION
def hello(a,b,c,d):
    print("the data",a,b,c,d)
    print("sum",a+b,c+d)
hello(1,2,"hello","hey")

#positiona argument function
"""def add(a,b):
    print(a+b)
add(int(input("Enter a")("Enter b")))
"""

#keyword rgument function
def new(name,age,roll):
    print("hello ",name,"your age is ",age,"your roll number is ",roll)
    print(f"hello {name},  age {age}, rollno {roll}")
new("Himanshu",23,1234)

#now we try to pass data as keyword argument not positional
new(name="Himanshu",age=23,roll=1234) #it automaticall place the value at there place even user trying to messing it up
#case1---#it is not acceptable because first we have to pass postional argument then keyword argument
#combination of keyword and positonal arguments function
new("Himanshu",25,1345)
#new(age=25,name="Himanshu",1345)#it is not acceptable because first we have to pass postional argument then keyword argument
#case2---if we pass positional and keyword both for one parameter

#write a program creat function,

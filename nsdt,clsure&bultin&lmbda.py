#Nested,Closure and builtin function...

#Nested--here we can declare functio inside another function,Means inner function depends on outer function
"""
def outer():
    print("Hello i am outer function")
    def inner():
        print("Hello i am inner and am depend on outer")
    inner()
outer()


#Example related to nested function........>>>

def out(a):
    print("Welcome")
    def inner():
        print("Hello i am inner function but i will exectue when input a===1")
    if a==1:
        inner()
    else:
        print("Output a!= 1")
out(int(input("Enter 1")))


#one more example
def user(name,passw=None):
    print("Welcome", name)
    def info(passw): #instead of this
        print("Your Password",passw)
    info(passw)
user("Himanshu")
user("Himanshu",123)
"""
"""
def user(name,passw=None):
    print("Welcome", name)
    def info(p): #to make password secure we can also do this
        print("Your Password",p)
    info(passw)
user("Himanshu")
user("Himanshu",123)
"""

#Closure function===>
#when inner function return something to outer function then this is conside as closure function

def hello(a,b):
    print("Welcome")
    def add(c,d):
        return(c+d)
    add(a,b)#doesn,t print anything
    print(add(a,b))
#hello(45,65)    
print(hello(45,65))

"""
def xyz(a):
    print("welcome",a)
    def abc(b):
        print(b)
    return abc

z=xyz("Himanshu") # z is an object
z(123)

"""

#in built function(Anonymous function)
#anonymous function----
#we have a function but we dont have there name then these function consider as anonymous function
#lambda---if we use lambda keyword at anyline then is act as a function
#lambda function--by using lambda we can write oneline function,means concise code.it includes code readability and it also optimize the code

#simple function
"""
def abc(a,b):
    print(a+b)
abc(5,10)

#now er write one line function with the help of lambda

a= lambda x,y:x+y
print(a(12,32))


#2nd example--
def check(a):
    if a%2==0:
        return"Even=="+str(a)
    else:
        "odd=="+str(a)
print(check (12))

#NOW OPTIMIZE THIS CODE USING LAMBDA
b= lambda a:"Even"if a%2==0 else "Odd"+str(a)
print(b(12))
print(b(13))

"""
"""
#filter function--in this we use conditions an data and if satisified the condition then it accepts 

l=[1,23,45,67,89,90,12,56,23,78]
def check1(a):
    if a%2==0:
        return True
    else:
        return False
print(check1(12))
f1=filter(check1,l)
print(list(f1))

#now optimize this using lambda and filter
r1=list(filter(lambda x:x%2==0,l)) #l=[i for i in range(1,100,7)] we can use this instead of l
print(r1)

r2=lambda x,y,z:x if((x>y)&(x>z))else y if ((y>z) & (y>x)) else z
print(r2(82,53,34))


#Global keyword---if we want to make any local variable as global then we use global keyword
a=10
def f1():
    a=777
    print(a)
def f2():
    print(a)
f1()
f2()

#now we will make local variable into global
a=10
def f1():
    global a
    a=777 #a=10 is overrided
    print(a)
def f2():
    print(a)
f1()
f2()

"""
#now try to access global data in local space
a=10
def f1():
    
    a=777
    print("using local value",a)
    print("using global value",globals()["a"])
def f2():
    print(a)

    
f1()
f2()


#revise functions very well

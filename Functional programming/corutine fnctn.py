#COROUTINE FUNCTION
#_---------------------------
#coroutine function can pause there execution.

#generator function---this function is usedf to cretae the generating sequence..
"""ls=[x for x in range(10000)]
print(ls[-10])
"""

gen=(x for x in range(10))

#next(gen) in shell

#how we can create a generator function
"""
def alpha(n=26): #how much you want to generatr
    for x in range(n):
        yield chr(x+97)#it's a coroutine function
alpha10=alpha(10)
alpha5=alpha(5)

for x in alpha10:print(x,end=",")
print()
for x in alpha5:print(x,end=",")
"""


#Decorator--------------
#these are the specia type of funtion whcihc always takes another function as input and returns a function as output.
#we never call the decorator the executing thread is commanded/ instructed to do so.


#pythonbricks.pythonanywhere.com
#when we want to add common functionality to all functions then we can use decorATORS
def deco(func):
    print("hi")
    return print
@deco
def greet(name):
    print(name)
greet("Himanshu")




names={"Himanshu","Sakshi"}
def dec(func):
    def inner(name):
        if name in names:
            print("Hi",name)
        else:
            func(name)
    return inner
@dec
def greet(name):
    print("You aren't logged in",name)
def greet1(name):
    print("Good morning",name)
greet("Himanshu")





#COROUTINE FUNCTION ------------doubt class


def myfunc():
    for x in range(26):
        yield(chr(x+67))

gen=myfunc()
for x in range(3):
    print(next(gen))


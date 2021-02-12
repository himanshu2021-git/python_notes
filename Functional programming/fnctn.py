#functions
#postional args.
#keyword args
#defalut args.
#*args
#**kwargs



#6-args- arguments....whenever you wanna be flexible with positional args then you can go for this kind of args
#note--if you create more than one function with same name the python will recognize only lastly created function.

#this is right
"""def him(a,b=10,c=20):
    print(b+c)
him(5)
"""

#all the arguments given to the args function will be stored inside a tuple
"""
def prod(*args):
    print(args)
    print(type(args))
    temp=0
    for x in args:
        temp +=x
    print(temp)
prod(10,20,30)
"""


#   * = args and ** represent kwargs


#7--kwargs--if you wish the flexible with keyword args then you can go fir this
#all the keyword arguments are stored in a dictionary when key is the arggument varibale and value is for that variable




#function without argument with return value

#a function which takes nothing at the time of calling but gives something back after its execution
"""
def demo():
    print("this is a statement inside some function")
    return 10

a=demo()
print(a)
"""

#return statemetn should be the last stTement of function because after return statement no ststement will print anything
#you can return more than one value from a function

def demo():
    print("this is a statement inside some function")
    return 10,20,30 #actually its returning only one value but all these three values are in tuple

a,b,c=demo() #function can return more than one value but not more than one object
print(a,b,c,sep=" | ") 
print(type(a))

#function with return value with argument



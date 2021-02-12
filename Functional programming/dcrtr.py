"""
logged_in=False
def login():
    global logged_in #using the global logged_in variable wern't declaring it
    #print("Login SCREEN".centre(50,"*"))
    ch=input("Do you want to login ?").strip().lower()[0]
    if ch == "y":
        logged_in= True
    else:
        print("Login Failed")

def login_check(func):
    def inner(*args,**kwargs):
        print("ChECKING login Status please wait")
        if logged_in:
            func(*args,**kwargs)
        else:
            login()
            buy(*args,**kwargs)
    return inner
@login_check        
def buy():
    print("You are buying a product")
buy()
"""
#DEcoraotr chaining--- we can assign as many deco to a single function as we wish to assign.
"""
def decor(func):
    def inner():
        print("DECOR")
        func()
    return inner
def decor1(func):
    def inner():
        print("Decor1")
        func()
    return inner
@decor
@decor1
def demo():
    print("This is a function")
de=demo()
print(de)
"""
#from keyword import kwlist


#INNER FUNCTION | NESTED FUNCTION
    #a function defined inside some other function And has scope only within that function
"""
def outer():
    var=10
    def inner():
        nonlocal var #updating the outer function variablle
        var=20
        print("THis is my statement")
    print(var)
    inner()
    print(var) #to print updating variable we have to print after calling inner function
outer()
"""

#CLOSURE FUNCION---this is much like an inner function.

#EXPENSES MANAGEMENT SYSTEM.
#-add expense
#-add bills receivable-add monthly budget-summary4

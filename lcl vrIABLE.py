#todays topic is local variable......
#Sometimes to fullfill a temporary of a programmer, we can declare variable.These type of variable consider as a local variable
#local varibale create at a time of method execution and destroy once the method will be completed.
#local var cant be access from the outside of method.
"""class Abc:
    def m1(self):
        a="local"
        print("here a is ",a)
    def m2(self):
        b="local"
        print("here bb is ",b)
c=Abc()
print(c)
print(c.m1)
print(c.m1())"""

#=======================================Methods=================
#instance method
#static method
#class method

#Instance mthod--- if we are using instance variable then such type of method are consider as instance method.it can be one or more than one.when we see self than it is instance emthod

class Test:
    def m1(self):
        self.a=12
        self.b=78
    def m2(self):
        print(self.a)
        print(self.b)
t=Test()
print(t.__dict__)
t.m1()
print(t.m2())


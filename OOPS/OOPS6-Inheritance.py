#INHERITANCE--- it allows you tp borrow the allowed attributes from other classes or classes
#Has-A Relationship

#Types of inheritance----1-Simple inheritance

class Parent:
    def method(self):
        print("This is the method of the parent class")

class Child(Parent):pass

c=Child()
c.method()

#is a relationship

class Parent:
    def method(self):
        print("This is the method of the parent class")

class Child():
    def __init__(self):
        self.obj=Parent()

c=Child()
c.obj.method()



#-----------Constructor chaining-------
#if you are performing inheritance with your classes and you are not defining constructors in your classes than they will be created by PVM it self.

#Constructor- it is just a special method define in every class which is repsonsible to initiate the newly created objecto
#Types of constructor-
#1-Default constructor--these const. are created by PVM itself

#normal class
def __init__(self):
    pass
#inherited
def __init__(self):
    super().__init__() #calling of parent class cinstructor

    #super represent the parent classes

#Note: if you don't perform constrctor chaining then no instance member of class will partiipate in inheritance



#---------------2-Multiple Inheritance
#a single class tries to acquire the attributes of more than one class

class Parent1:
    def method(self):
        print("This is Parent1 method")

class Parent2:
    def method(self):
        print("This is Parent2 method")

class Child(Parent1,Parent2):pass
c=Child()
c.method()

#-----------------3-MultiLevel Inheritance
#a class borrows attributes from a class and another class borrows the attributes from that class

class GParent:
    def method(self):
        print("This is Parent1 method")

class Parent(GParent):
    def method(self):
        print("This is Parent2 method")

class Child(Parent):pass

c=Child()
c.method()


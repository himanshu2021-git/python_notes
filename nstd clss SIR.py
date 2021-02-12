#Today we start with Nested class and its all functioning...

#We can declare a class inside the another class,such type of classes are called  Inner class.
#If  without existing one type of object there is no chance of existing another type of object.
"""
class Outer:
        def __init__(self):
                print("Hello I am Constructor and belong to outer class")
        def out(self):
                print("I am method from outer class")
        class Inner():
                def __init__(self):
                        print("Hello I am From Inner Class Constructor")
                def inn(self):
                        print("Inner class Method")
        
                
o = Outer()  #Here o is a reference variable
o.out()
Outer().out()
#Outer.out()  #it is not possible


print("=====================inner class Calling========================")

f  = Outer.Inner()
f.inn()


Outer().Inner().inn()
"""
"""
#Examples related to nested class.......

class Human:
        def __init__(self):
                self.n = "NIshant"
                self.DOB =self.Dob()
        def disp(self):
                print("Name===",self.n)
        class Dob:
                def __init__(self):
                        self.dd = 1
                        self.mm = 3
                        self.yy = 2015
                def disp(self):
                        print("Date of birth==={}/{}/{}".format(self.dd,self.mm,self.yy))

H = Human()
H.disp()
x = H.DOB
x.disp()
"""

class Outer:
        def __init__(self,name,age):
                self.name = name
                self.age = age
        def data(self,x,y): #In stance method
                print("The value of x and y")
                print("x==",x,"\nY==",y)
                def data1():
                        print("Name==",self.name,"\nAge==",self.age)
                data1()
        class Inner():
                def __init__(self,name,age):
                        self.n= name
                        self.a = age
                def disp(self,x,y):
                        print("The value of x and y")
                        print("x==",x,"\nY==",y)
                        def disp1():
                                print("Innerr classs nested method===",self.n,self.a)
                        disp1()
#for outer                
z = Outer("NIshant",78)
z.data(45,65)

print("******************Innerr************")
t = Outer("Nishant",25).Inner("Rahul",15).disp(45,65)

Outer.Inner("Ram",12).disp(14,63)

"""
z.Inner("Himanshu",22).disp(45,65)
"""













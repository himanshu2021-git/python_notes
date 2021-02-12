#OVERRIDING..same name and same parameter
#Constructor override and method override.

#Members who present in parent class are bydefault available to child class through inheritance.
#parent class then it is also avaiable this concept consodering as overriding
#SAme namme(signature) and same parameter tgen the child redefine the parent method.

#OVERRIDING

class My:
    def music(self):
        print("Rock","TRans","Pop")
    def singer(self):
        print("Alan Walker")
m1=My()
m1.music()
m1.singer()

#Child
class My1(My):#here m1 is child which inherit its base class My
    def data(self):
        print("Helo i'm data")
    def singer(self):
        super().singer() #Access parent class method which is overriden using super keyword
        print("Chainsmokers")
n1=My1()
#n1.data()
n1.singer()
n1.music()


#====SINGLE LEVEL INHERITANCE========
"""
class Parent:
    def add(self,n,m):
        self.n=n
        self.m=m
        print("The sum===",self.n+self.m)

class Child(Parent):
    def sub(self,n,m):
        self.n=n
        self.m=m
        print("The sub===",self.n-self.m)
s=Child()
s.sub(45,9)
s.add(45,9)
"""
"""


#++++++++++Multillevel class

class Multi(Child):
    def mul(self,n,m):
        self.n=n
        self.m=m
        print("The mul===",n*m)
m=Multi()
m.mul(3,4)
m.add(3,4)
m.sub(3,4)

#Herarichal
class Hera(Parent):
    def div(self,n,m):
        self.n=n
        self.m=m
        print("The div===",n/m)

class Hera1(Parent):
    def flrdiv(self,n,m):
        self.n=n
        self.m=m
        print("The flrdiv===",n//m)

h=Hera()
h.div(5,2)
h.add(5,2)
h1=Hera1()
h1.flrdiv(7,3)
h1.add(7,3)

"""
#MUltiple inheritance

class Parent1:
    def oprn(self,n,m):
        self.n=n
        self.m=m
        print("The modulous===",self.n%self.m)

class Parent2:
    def pw(self,n,m):
        self.n=n
        self.m=m
        print("The sum===",self.n**self.m)

#here check have more than 1 parent

class Check(Parent1,Parent2):
    def opr1(self):
        print("i'm check function")

cv=Check()
cv.opr1()
cv.oprn(10,4)
cv.pw(2,3)
"""


#TRY to observe MRO(Method Reservation order)

#Case 0 Basic
#here first go to child then parent and then object.
"""
class P:
    def m1(self):
        print("Parent method")
class C(P):pass
p1=P()
p1.m1()
print("MRO for P1===",P.mro())
print("MRO for C",C.mro())

print("++++++case 1++++++")
class Paren():
    def m1(self):
        print("From parent class")
class Child(Paren):
    def m1(self):
        #super().m1()
        print("From child class")
Child().m1()
print("MRO CHILD",Child.mro())



print("Case2===============")

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
class E(C,B):
    pass
print("MRo of A",A.mro())
print("MRo of B",B.mro())
print("MRo of C",C.mro())
print("MRo of D",D.mro())
print("MRo of E",E.mro())
"""

print("Now With mETHODS=====")
"""
class A1:
    def m1(self):
        print("from A1")
class B1(A1):
    def m2(self):
        print("from B1")
class C1(B1):
    def m1(self):
        super().m1()
        print("from C1")
class D1(C1):pass
    #def m1(self):
       # print("from D1")
class E1(D1):pass
   # def m5(self):
       # print("from E1")

o=E1()
o.m1()

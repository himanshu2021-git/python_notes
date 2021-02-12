#Today we discuss about All underscore working in python.

#Case-1  For storing the result of last executed expression in an interactive shell.

#Case-2 For ignoring the value.
def oprn(a,b):
    return a+b,a-b,a*b,a/b
print(oprn(12,6))
x,y,z,_=oprn(45,6)#for ignpring the value we use underscore
print(x,y,z,_)

# Case-3 Single leading underscore(_xyz)-- use to private the variable or function.
"""
v=10
_v1=23 #it is private

def hello():
    print("simple function")
def _bye():
    print("private function")
print("v===",v)
print("v1====",v1)
"""
# Case-4 here we use single trailing underscore.It is use to solve naming conflict.
"""
a=["45",45]
t=tuple(a)
print("tuple",t)

list_=[78,94]
print("list===",list)

print("t to l",list(t))
"""
#Case-5 Double leading underscore...(__x),Here it is use to prtect the daata or function.

class A:
    def _hello(self):
        print("i'm private")
    def __hy(self): # PROTECTED
        print("i'm protected")
m= A()
m._hello()
#m.__hy() here data is protected if you want it then use
m._A__hy() #object._classname__protectedfunction


#Case-6 All speical method(__asfdafaf__) teo leading underscore and two railing.__init__






#now we discuss about the four pillarrs of OOPs.

#Abstraction #hiding the complexity
#Encapsulation-Binded of data.
#Polymorphism- Present in many forms.
#polymorphism has two type.
#overloading(Method overloadiing[not possible in python],constructor loading[not possible in python],operator overloading[it is possible with the help of special method]),overriding(inheritance[isn't a part])
#Inheritance- Getting functionality from parents to child


#Overloading(Early time bining/Compile time binidng)-same name andd different parameter
#Overriding(LAte/Runtime Binding)- MEthod overriign(Inheritance) - same name with same parameter.
#if child is inherit parent class then child override parent's method as per the requirement.


#READ THEORY of OOPs.

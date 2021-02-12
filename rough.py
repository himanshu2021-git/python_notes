"""

s2 = {1,2,3,5.5,True,False,"Adfadf",

      5e3,5+3j,32,"nishant",78,78.3333,"ASfaf",1,2,3,4,5,5.5,True,65+32j,15,38.5,32,78,95,78,

      "ASfaf",1,2,3,4,5,5.5,True,

      ("nishant",78,78.3333,65+32j)}


s3=s2.add(25)
print(s3)
print(s2)
s4=frozenset(s2)
print(s2)
s5=s4.add(90)
print(s2)

"""
"""a= lambda x,y,z:x if ((x>y)&(x>z)) else y if ((y>x)&(y>z)) else z
print("the greates number is",a(5,6,7))"""
"""

print("if number is positive the it automaticall print the number otherwise it shows a message ")
b= lambda c: c if c>0 else c if c==0  else "This is not a postive number"

print(b(int(input("Enter number pls"))))

"""
"""
name=" "
input("please enter your name")
n=["Himanshu"]
if name == n:
    print("Welcome",name)
else:
    print("sorry you dont have any account",name)
    """
"""
class moto:
    def __init__(self):
        self.model= "Great"
      
    def boom(self):
        self.model
        print(self.model)
great=moto()

"""
"""
class Himanshu:
    a="Hello"
    def __init__(self):
        Himanshu.a1="class lvl inside constructor"
        self.b1="instance method inside constructor"
    def my(self):
        Himanshu.c1="class lvl inside instance method"
        Himanshu.d1="again cls lvl inside instance method"
        self.e1="instance variable inside instance method"
        print("c1====",Himanshu.c1)
        print("d1====",Himanshu.d1)
        print("e1====",self.e1)
    def my1():
        Himanshu.f1="class lvl inside statoc method"
        print("f1===",Himanshu.f1)
    @classmethod
    def my2(cls):
        cls.g1="class lvl using decorator in class method"
        Himanshu.h1="class lvl using classname"
y=Himanshu()
print(y.a)
print(y.a1)
print(y.b1)
print(y.my())
print(Himanshu.my1())
print(Himanshu.my2())
"""

"""
class Him:
    def m1(self):
        a="local var"
        print("a====",a)
    def m2(self):
        b="also local var"
        print("b====",b)
    def m3(self):
        c="one more local"
        print("c===",c)
    def m4(hima):
        hima.d=12
        hima.e=13
        print("insta var",hima.d+hima.e)
    def m5():
        f=15
        g=16
        print("static math",f+g)
    @staticmethod
    def m6():
        h=78
        i=98
        print("using dec.static method",h+i)
    @classmethod
    def m7(cls,j,k):
        print("class method always using dec",j+k)
h=Him()
h.m1()
h.m2()
h.m3()
print(h.__dict__)
h.m4()
Him.m5()
h.m6()
Him.m6()
h.m7(100,300)
Him.m7(100,200)
"""
"""

class Outer():
    def __init__(self):
        print("Hey its a contructor")
    def out(self):
        print("Hey am instance method inside outer class")
    def out1():
        print("hey am static method inside outer class")
    class Inner():
        def inn(self):
            print("iam instance method inside inner class")
o=Outer()
o
o.out()
Outer.out1()
ind=o.Inner()
ind.inn()



"""
"""
txt="heyhimanshuherehowsyouguys"
tex=txt.partition("himanshu")
#te=tex.partition("hows")
print(tex)
"""
"""
from speedtest import Speedtest
st=Speedtest()
d=print("Connection's Download Speed : ",st.download())


u=print("Connection's Upload Speed : ",st.upload())

ds=print(d/100000)

us=print(u/100000)
"""



"""
import pyautogui as pa
pa.screenshot=(r"F:\Himanshu\PMD\Tushar Sir\screenshot.png")
"""

"""
from matplotlib import pyplot as plt
players=['Himanshu','Ronaldo','Messi','Vivan']
score=[52,76,71,48]
plt.bar(players,score,color='green')
plt.title('Score Card')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()

"""


"""
import pywhatkit as whatsapp
whatsapp.sendwhatmsg("+919599605308","message from python code",0,0)
"""

"""
def fun(a=12,b=2):
    print(a//9)
    return(a*b)
    

fun(a=9,b=2)
"""
"""
import calendar
yy=2020
mm= 11

print(calendar.month(yy,mm))

"""
"""
import pyqrcode

import png

#print(dir(png))
#print(dir(pyqrcode))


This code is for creating QR code

QRstring="www.google.com"
url=pyqrcode.create(QRstring)
url.png('Desktop\\qr.png',scale=8)
"""
"""
v5  = (1,2.3,"sdbjfk",True,5+13j,5e3,[21,32.3,458,("AsfdA",125,56.6,78),"end"],{1,1,2,3,50,45,False}#set
       ,       {"A":15,1:15,"asd":456,265.5:"sdfsdf"},"End",2.3,1)

print("v5==",v5,type(v5),"len==",len(v5),id(v5))

"""
"""
list2=[5,4,3,2,1,-3,-2,-1]
total4=0
for i in list2:
    if i>0:
        total4+=i
print(total4)
"""
"""
list2=[5,4,3,2,1,-3,-2,-1,6]
total4=0
for i in list2:
    if i>0:
        total4+=i
print(total4)
"""

"""
list3=[5,4,3,2,10,-5]

total5=0
i=0
while True:
    total5=total5+list3[i]
    i+=1
    if list3[i]<0:
        break
print(total5)

"""
"""
list2=[5,4,3,2,1,-3,-2,-1,6]
total4=0
for i in list2:
    if i<0:
        total4+=i
print(total4)

"""
"""
if i%2==0:
    if i<5:
        print("Not Weird")
    elif i<20:
        print("You are weird")
    else:
        print("Not weird")
else:
    print("You are weird")

"""

i=int(input("Please Enter integer"))

if i%2==0:
    if i<5:
        print("Not weird")
    elif i<20:
        print("you are weird")
    else:
        print("Not weird")
else:
    print("You are weird")




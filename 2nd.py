#multiple assignment

"""
w=t=y=u=12 #memory depend on the size of integer
print(w,t,y,u)
print(id(w))
print(id(t))
print(id(y))
print(id(u))
"""

"""for i in range(10):
    print(i)"""

"""
a1,a2,a3,a4,a5,a6=1,23.3,"Himanshu",True,(1,25.3,"Himanshu"),9+3j
print(a1,type(a1))
print(a2,type(a2))
print(a3,type(a3))
print(a4,type(a4))
print(a5,type(a5))
print(a6,type(a6))
"""

#input from user side

"""a=12 
print("a",a,type(a))
#now try to convert into float

a1 = float(a)
print("a1",a1,type(a1))

a2=bool(a)
print("a2===",a2,type(a2))


a3=int(a2)
print("a3===",a3,type(a3))


a4=int(a1)
print("a4===",a4,type(a4))

a5=complex(a1)
print("a5",a5,type(a5))"""

"""a6=float(a5)
print("a6",a6,type(a6))"""  #cant convert because imaginary has any random value

#converting into string_coz we can find length of string not able to find value of integer, len(s1)
"""s1= str(a)
print("s1",s1,type(s1),len(s1))

s2= str(a1)
print("s2",s2,type(s2),id(s2))

s3= str(a2)
print("s3",s3,type(s3))


s4= str(a5)
print("s4",s4,type(s4))


s5= int(s1)
print("s5",s5,type(s5))#converting str into int

s6= bool(s1)
print("s6",s6,type(s6))

#dir(list)"""
"""l=list()
l

type(l)"""


#now try to convert str into int,bool,,complex

z="1234567"
z1="Himanshu"  #cant convert characters in int string
print("z",z,type(z))
#convert z1 into int float bool complex
z2=int(z)
print("z2",z2,type(z2))

z3=float(z)
print("z3",z3,type(z3))

z4=float(z1)
print("z4",z4,type(z4))
"""Traceback (most recent call last)
  File "F:\Himanshu\PMD\2nd.py", line 87, in <module>
    z4=float(z1)
ValueError: could not convert string to float: 'Himanshu

#now take user defined input
#if we want to take input data from the user then we use input function

c=input("ENTER ANYTHING")
print("c===",c,type(c),id(c),len(c))

c1=int(input("enter integer"))
print("c1---",c1,type(c1))

c2=float(input("enter integer"))
print("c2---",c2,type(c2))
"""

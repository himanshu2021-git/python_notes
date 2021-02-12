#find greatest among three number

"""
a=int(input("Enter first number= "))
b=int(input("Enter second number= "))
c=int(input("Enter third number= "))
"""
"""
if((a>b)&(a>c)):
    print("a is greater")
elif((c>a)&(c>b)):
    print("c is greater")
else:
    print("b is greater")
    
"""

"""
x=[a if((a>b)&(a&c)) else b if(b>c) else c]
print("Greater ===",x)
print(type(x))
"""

#looping strcutre
#code reduce and function reuse
#raw loop--- always handle structure and iterate on the basis of element present in the structure
#range loop-- operate with range function


#.......RANGE LOOP>>>>>
"""
for i in range(10):
    print(i)
"""
"""
for i in range(10,50,2):
    print(i)

s="Himanshu play football"
c=0
for i in s:
    print(i)
print(c)

"""

"""
for i in range(10,1000):
    if((i%5!=0)&(i%7!=0)):
        print(i)

"""

"""
#atble print
a= int(input("Enter any element="))
for i in range(1,10+1):

"""

#<<<<<<<<<<<RAW LOOP>>>>>>>>>>>>
"""
s1="Himanshu"
s2="Hello"
c1=0
c2=0
for i in s1:
    print("i---------",i)
    c1+=1 #counting loop
    print(c1)
    for j in s2:
        print("j----",j)
        c2+=1 #counting loop
        print(c2)
    print(c1+c2) #counting loop

"""

    #.........................Homework.....................
            #user put string and tell how many upper case and lower case character
                #user put strng and tell how many vowels and consonants
                    #user give number input and tell number is prime or not
                        #  
"""
a,b,c=5,7,6
y=[a if(a>b)&(a>c) else b if (b>c) else c]
print(y)
"""

s1="Himanshu"
s2="Hello"
c1=0
c2=0
for i in s1:
    print("i---------",i)
    c1+=1 #counting loop
    print(c1)
    for j in s2:
        print("j----",j)
        c2+=1 #counting loop
        print(c2)
    print(c1+c2) #counting loop

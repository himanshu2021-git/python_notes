#control structure
#firsrr we discuss about if..
a=int(input("enter any number"))
"""
if(a>5):
    print("hey am A am greater than 5")
elif(a==5):
    print("Great its equal to 5")
else: #never can put condition in else 
    print("Offo A is less than 5")
"""

#b=int(input("Enter B"))
"""
if(a==b):
    print("they are equal")

else:
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
"""
"""
c=input("Enter the str=1==")
d=input("Enter the str=2==")
if(c==d):
    print("Matched")
else:
    print("Not matched")
"""

"""
#withhout if elif doesn't work
if(a<=50):
    print("Up for icecream")
elif(a<=100):
    print("Up for movie")
elif(a<=500):
    print("Ready for trip")
else:
    print("am ambani now")

"""

if(a<100):
    print("i am less than 100 ",a)
    if(a%2==0):
        print("i am less than 100 also even",a)
        if((a%5==0)&(a%7==0)):
            print("i am less than 100 and also multiple of 5 and 7",a)
        else:
            print("am not divisble by 5 and 7")
    else:
        print("am less than 100 but not even")
else:
    print("number is greater than 100")










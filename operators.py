#Operators and its working.
#arithemtic operator
"""
print("a+b==",12+32)
print("str plus str","Himanshu "+"Rajpurohit")
print("a-b===",125.5-85)
#in python evrything conside as a object.Here only int exist, no long, no double,short,datatype available
print("a*b",4*4)
print("","himanshu\n"*8)
#in float we can get only float we in floow=r we can get int or float both
print("floor==",12//4)
print("modulo",12%5)
print("modulo==",12%2)
print("power",pow(12,3))
"""

"""
#assignment operator
#assigning value in any variable.operator====>  "="
a1=10
print("a1 is==",a1)

a1-=5
print("sub",a1)

a1*=2
print("mul",a1)
a1/=2
print("div",a1)

a1%=2
print("modulo",a1)

a1**2
print("pow",a1)

"""

"""
#conditional operators or relational operators
print("check",12>25)
print("check1",12<25)
print("check equal",45==65)
print("check not equal==",45!=65)
print("A"<"a")
"""
"""
#chaining of relational operators--- if we use more than 2 operand at same time then , if all comparisons returns true then only result is true
print("Chaining===",12>5<2>78<12)
print("Chaiing==",78>48>42>12>6)
print("Chaiing==",78>48>42<12>6)
print("Chaiing==",78>48<62<72>6)
"""

#logical operators=== take multiple bools exp and return boolean
#return true if all expressions are true otherwise false
a=1
b=0
c=45
d=35
print("s",a and b)
print(b and a)
print(b and b)
print(a and a)
print("as",c and d)
print(a and c)
print(c and a)
print(c and c)

#return true if any one codition is true(OR)
#not operator
print("not==",not a)
print("not===",not b) #opposite

#chaining with logical operators
print("and false check",12>5 and 6<8 and 8==8)
print("and true check",12>5 and 6>8 and 8==8)
print("or true check",12>5 or 6>8 or 8==8)
print("or true check",12<5 or 6>8 or 8==9)
print("or true check",12<5 or 6>8 or 8==8 and 8<9)
print("or true check",12>5 or 6<8 and 8==8)

# Bitwise operators, membership operators and idetity operators
#these operators mainly used to int,float,bool
# """
a=5
b=6
#and operation
print("1",a&b)
print("2",bin(a|b))
print("3",~8)
print("4",64<<2)
print("5",bin(256))
print("6",64>>2)
print("7",bin(16))
#xor---if bits are diifferent the result will be one otherwise it will be zero
c=4
d=5
print("8",c^d)
print("9",~7)

# """

#membership operation--in, not in
#identity operator--is, is not

#we can use membership operator to check whether the given object is present in the collection(str,ist,tup,set,dict)
#e.g===(in) and (not in).Always return bool

"""
a="1234"
b="12"
print(a in b)
print(b in a)
print(a not in b )
print(b not in a )
l=["Himanshu",12,"Hii","Hello",5+4]
print(l)
print(12 in l)#el
print(1 in l)#one
print(l  in l)#el---structure to structure matching is not avaialble,in operators works in loop
print(1 not in l)#one
"""

#identity use to identify the things

a="123"
b="12"
c="123"
print(a is b)
print(b is a)
print(c is a)
print(a is a)

l1=[45,46,47]
l2=[45,46,47]
print(l1 is l2) # address difference
print(l1[0] is l2[0])
print(l1 is l1)
print (a is not b)


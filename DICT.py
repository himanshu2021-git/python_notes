#we can update direclty uding _update() with union,difference,inteersection etc...
#.........................DICT........................
#DICTIONARY---it contains certain keys and values, keys are always unique and derived dtata type not consider as keys
#Key:value
# it doesnt support indexing and slicing
#contain hetrogenous data
#mutable in nature
#key will never be duplicate
"""
d={}
print("d==",d,type(d))

d1=dict()#empty dict
print(d1)

d2={"a1":12,"b2":45,89:"hey"}
print(d2)
print("keys---",d2.keys())
print("values---",d2.values())
#if one keys has two different then it override the data
d2={"a1":12,"b2":45,89:"hey","a1":"Himanshu"}
print(d2)
#in dictionary we have extraction, we can get any data with the help of keys(pass keys and get vaues)
print("indexing  keys",d2["b2"])
#t=d3.pop(key)
#d1.udate(d2)
#zip
key=["name","add","number",]
value=["Himanshu","Delhi","1234",]
z=zip(key,value)
di=dict(z)
print(di)




print(dir(d))


d3={"e1":15,"f1":49,"g1":69}
print(d3.keys())
print(d3.values())
d4={**d3,**d2}
print(d4)
print(type(d4))
"""

# def dec(a):
# 	def indec(name):
# 		if name == "Himanshu":
# 			print("hi",name)
# 		else:
# 			a(name)
# 	return indec

# @dec
# def hi(name):
# 	print("hello")
# hi("Himanshu")
# print(h)

# def dec(a):
#     def indec(name):
#         if name == "sam":
#             print("hey",name)
#         else:
#             a(name)
#     return indec
# @dec #it is use to connect normal function with decorator-----@ is use to connect

# def wish(name):
#     print("Hello",name,"Welcome")
# wish("Himanshu")
# wish("sam")

d2={"a1":12,"b2":45,89:"hey","a1":"Himanshu"}
print(d2)
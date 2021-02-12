"""s="Hey this is himanshu how are you"
s1="Great"
s2="hello"
s3="ok"
s4="1234"
print("s==",s,len(s),id(s),type(s))
print(dir(s))
print(s.find("h"))
print(s.rfind("h"))
print(s.title())
print(s.rstrip("u"))
print(s.lstrip("H"))
print(s.rstrip("k"))
print(s.strip("you"))

print(s.lower())
print(s.upper())
print(s.islower())
print(s.format("H"))
print(s.split())
print(s.splitlines())
print(s.istitle())
print(s.ljust(50,"h"))
print(s.isdecimal())
print(s.zfill(50))
print(s.format_map(0))
print(s.swapcase())
print(s.isidentifier())
print(s2.join(s3))
print(s2.__sizeof__())
print(s2.capitalize())
print(s2.__add__("ooho"))
print(s2.__class__)
#print(s2.__doc__)
print(s1.__getitem__(3))
print(s1.__str__())
print(s.__contains__("k"))
#print(s.__delattr__())
print(s.expandtabs(tabsize=8))
print(s.rpartition("h"))
print(s4.encode())
print(s.maketrans("Hey","Hii"))

"""
"""
v=(45,34,232,343)
z=(38728,34,34,3,2,34)
print("type==",type(v),"id===",id(v),"llength==",len(v))
print(v[0])

"""
"""

v5  = (1,2.3,"sdbjfk",True,5+13j,5e3,[21,32.3,458,("AsfdA",125,56.6,78),"end"],{1,1,2,3,50,45,False}#set
       ,       {"A":15,1:15,"asd":456,265.5:"sdfsdf"},"End",2.3,1)

print("v5==",v5,type(v5),"len==",len(v5),id(v5))

print("inndexing===1==",v5[-1])
print("slicing===2===",v5[::])
print("1st tab",v5.__sizeof__())
print(v5.__add__)

print("Chaining===",12>5<2>78<12)
print("Chaiing==",78>48>42>12>6)
print("Chaiing==",78>48>42<12>6)
print("Chaiing==",78>48<62<72>6)
"""
print(bin(256))
print(~7)

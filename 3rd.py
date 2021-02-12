#numbers--
#string--->>> collection of char,and support slicing and indexing and also have utility ,ethods and functions

a='Himanshu'
print("a==",a,type(a),"\nlen",len(a))
a1="""Himanshu play pubg  """#so if we want to print single quotes than we use double quotes for that
print("a1==",a,type(a1),"\nlen",len(a1))
#single line comment,multi line comment

s1=""
print("s1==",s1,type(s1),"len==",len(s1),"address==",id(s1))#it is empty string

#GC
s2=str()
print("s2==",s2,type(s2),"len==",len(s2),"address==",id(s2))
s3="Hiamshu like to work with java and python"
print("s3==",s3,type(s3),"len==",len(s3),"address",id(s3))

#now we perform slicing with indexing
#any structure indexing start with 0 and end with n-1
#In python we follow positive as well as negative address(index values)
#negative starts wiith(-1) and end at(-n)
#here we use syntax to retreive data with the help of index values...eg-->s[parameter(index)]


print("indexing 1===",s3[0])
print("indexing 2===",s3[3])
print("indexing 3===",s3[6])
print("indexing 4===",s3[8])
print("indexing 5===",s3[7])
"""print("indexing 1===",s3[42]) #Traceback (most recent call last):
  File "F:/Himanshu/PMD/3rd.py", line 33, in <module>
    print("indexing 1===",s3[42])
IndexError: string index out of range"""


#now we work on negative indexing
print("Negative Index==1===",s3[-1],id(s3[-1]))
print("Negative Index==2===",s3[-2],len(s3[-2]))
print("Negative Index==3===",s3[-7])
print("Negative Index==4===",s3[-8])
print("Negative Index==5===",s3[-28])
'print("Negative Index==1===",s3[-n]) #character doesnt work'

#slicing with postive index    (':' this is slice operator)
#syntax for slicing s3[start(by default is 0):stop(n-1):step(n-1)] if we want to skipp n steps then it will skip n-1 step
"""
print("slicing==1==",s3[1:12])
print("slicing==2==",s3[:])
print("slicing==3==",s3[:100]) #here it take last index 100 but it is not present so extraction stop at last point i
#slicing works on left to right not R2L
#eg-->>
print("slicing==4==",s3[12:2])
print("slicing==5==",s3[1:40:2])
print("slicing==6==",s3[::4])
print("slicing==7==",s3[::30])
"""
#now -ve index slicing

print("-ve slicing==1==",s3[-1:-10])#traversal not possible
print("-ve slicing==2==",s3[-10:-1])# (-41,0|-40|-39|....|-2|-1)
print("-ve slicing==3==",s3[-41:-1])
print("-ve slicing==4==",s3[-41:0])
print("-ve slicing==5==",s3[0:-1])
print("-ve slicing==6==",s3[:-2])
print("-ve slicing==7==",s3[-41:-1:2])






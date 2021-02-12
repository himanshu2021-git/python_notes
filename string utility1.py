s ="Himanshu works with both python and java both"
print("s==",s,type(s),"id==",id(s),"length==",len(s))

s1="Hello i also like to work with AI"
print("s1==",s1,type(s1),"id==",id(s1),"length==",len(s1))
#return type?
a="hello here is python and java"
b="hello here is AI"
print("\n",dir(a)) #to check utility methods of string
print("a===",a)
print("b===",b)
print("find==",a.find("i"))
print("find==",a.find("z")) #if value isnt present then output will be -1
print("find==",a.find("java"))
print("find==",b.find("h"))
print("rfind==",a.rfind("h")) #reverse finding
#find is only for first occurence it uses to make work feasible
#index vs find(index gives error if value isnt present)
print("index==",a.index("i"))
"""print("index==",a.index("z"))"""#ValueError: substring not found
#strip---from start to end it remove target char or sub-str
print("strip==",a.strip())
print("strip==",a.strip("h"))
print("strip==",a.strip("n"))#only remove first or last string or char
print("strip==",a.strip("hello"))
print("strip==",a.strip("java"))
print("strip==",a.strip("H")) #doesnt remove anything becuse of caase sensitive
print("strip==",a.strip("himanshu"))# first check substr if is doesnt get it then it starts to check single single character
#lstrip-- it removes from left user side only
print("lstrip==",a.lstrip("hello"))
#rstrip-- it removes from right user side only
print("rstrip==",a.rstrip("java"))
print("rstrip==",a.rstrip("and java")) #first check string then a single character

"........swapcase,tittlr,lowercase.uppercas..............e"
#swapcase--convert capital to normal and normal to capital
print("swap==",a.swapcase())

#title----convert string ito tittle
print("title==",a.title())
#upper---convert all string into uppercase
#lower---convert all string into loweercase
#..................................split count replace and join



print(type([])is list)

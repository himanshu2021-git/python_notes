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

print("split,count,replace,join..................")
#split-- it use to break the string from specific (user defined) place,return type is list

a1=a.split()#if we dont pass any argument then is consider soace as a parameter
print(a1)#print output in list
print(len(a1))
print("remove h",a.split("h"))
print("remove a",a.split("a")) #python is totally case sensitive

#count--- count is used to count any character or str in any user defined str

#print(a.count())  #TypeError: count() takes at least 1 argument (0 given)

print(a.count("h")) # 3

print(a.count("is")) #cant perform two operation together 

#replace.....it used to replace one element to another(char or str)
#it accept two parameter(a.replace("available","new"))
print("Replace opr",a.replace("h","H"))#need minimum two argument
print(a.replace("java","C#"))

#join-- it use to str or char with specific input
print("join===","*".join(a))

#min and max  works on ASCII code
print("min",min(a))
print("max",max(a))
a111="Himanshu"
print("min of a111",min(a111))
print("max of a111",max(a111))

print(ord("A"))  # to check ASCII code

#checking fucntion-----------startwith,endwith,isalpha,isdigit,,isaplhanum,isspace

# they return boolean

#---> startwuth and endwith #return boolean

print("start with is ",a.startswith("is"))
print("start with is ",a.startswith("h"))
print("start with is ",a.startswith("H"))
print("start with is ",a.startswith("H"))


#isalnum-- check for alpha numeric string or anly alpha and onlu numeric striing
a1="Himanshu is python consultant and also know java"
a2="123himanshu8924"
a3="12345678"
a4="himanshuhello"
a5="HIMANSHU#HELLO"
a6="123 456 "
a7="  "
print("check a1",a1.isalnum()) #because of space space is not aplha or not numeric
print("check a2",a2.isalnum())
print("check a3",a3.isalnum())
print("check a4",a4.isalnum()) #WHENEVER TYHER IS "IS" OPERATION IT RETURNS BOOLEAN
print("check a5",a5.isalnum())

#because of space space is not aplha or not numeric

#isaplha--for only aplhabetical string
print("check a1",a1.isalpha())
print("check a2",a2.isalpha())
print("check a3",a3.isalpha())
print("check a4",a4.isalpha())

#because of space space is not aplha or not numeric

#isdigit--- for digits only
print("check a1",a1.isdigit())
print("check a3",a3.isdigit())
print("check a6",a6.isdigit())

#isspace--check only for blank string
print("check a1",a1.isspace())
print("check a6",a6.isspace())
print("check a7",a7.isspace())#empty string is not conside as space like in a7

#islower---check only lower cases
print("check a4",a4.islower())
print("check a1",a1.islower())
print("check a2",a2.islower()) #ignore numeric values or other values

#isupper---check only upper cases
print("check a5",a5.isupper()) #ignore numeric values or other values
print("check a1",a1.isupper())

#.....centre.....
x=a1.center(200,"x")
print("centre===",x,len(x))

#ways to create the list----

#starred assign ---it always create a list object.

#a,*b=1,2,3,4,5,6,7,8


#creating blank list


#ls=[]
#ls=list()

#list-function---it takes no args or it takes a collection  like object and then prepare a new list by putting

#ls=list(range(10))
#ls1=list("Himanshu")




#LIST COMPREHENSION---- if you create the list with the help of list compreheension then you will be able to process the element of list during its creation.

"""
for var in collection:
    body
"""


#[body for var in collection]

#ls=[x for x in range(10)]

#previous list will be deleted by garabage coolector

data="Himanshu brown big boom"

ls=list(data)
"""
ls=data.split()

print(ls)
"""

"""
ls=data.split(x for x in range(count(data)))
"""

ls1=[data.split()[x-1]*x for x in range(1,len(data.split())+1)]
#print(ls1)

"""
ls2=[len(data.split()[x-1]*x for x in range(1,len(data.split())+1))]
print(ls2)
"""
"""
ls2=[len(x) for x in ls1]
print(ls2)

"""

#using if statement in list comprehension


"""
[body for var char in collection if condition]



for ki body h if condition se and if ki body h starting body

"""
"""
ls3=[x for x in ls1 if len(x)%2==0]
print(ls3)
"""



#list comprehension for filter all the vowels

"""
data=str(input("Enter data pls : "))
vowels = [x for x in data if x.lower() in "aeiou"]

print(vowels)


word_length=["%s -> %d"%(x,len(x))for x in data.split()] #string ko integer mein convert krare h idhar....
print(word_length)
"""
"""
given=["4646540","46464","646464"]
result=[]


for x in given:
    temp=[]
    for digit in x:
        temp.append(int(digit)) #this is the method to add something at the end of list
        #find the biggest number and assign that to the result.
        result.append(max(temp))
        temp.clear() #making temp empty so that it will start from fresh
print(result)

"""
"""
#Sorting.............
given=[56,85,45,76,7,6,44,46,35,52,28]
copy=[x for x in given]
n=3
for x in range(len(given)):
    ele=x
    pivot=x
    for comp in range(x+1,len(given)):
        if given[comp]<given[pivot]:
            pivot = comp
        given[ele],given[pivot] = given[pivot],given[ele]

print(given[-n:])
print(copy)


#filter the magic numbers

magic_number=[copy[x]for x in range(len(given)) if copy[x]==given[x]]
print(magic_number)
"""
"""
given=[1,2,3,4,5,6,7,8,9]

k=8

for x in given:
    for y in given:
        if x == y:
            continue
        if x+y == k:
            print(x,"+",y)

"""
#NOTE:::::: during the comprehension a list can't change its size

# IF _ELSE IN LIST COMPREHENSION

#WRITE THE list comprehension to filter all the unique elements from a given string
"""
data="Himanshu plays football"
result=[]

#for processing
[result.append(x)for x in data if x not in result ]
print(result)
"""


#Count the number of duplicate elements available in a given string.
"""
data=input("Enter data : ")
unique= []
duplicate= []

[unique.append(x) if x not in unique else duplicate.append(x) for x in data]
print("Unique elements are : ",unique,len(unique))
print("duplicate elements are : ",duplicate,len(duplicate))

"""
"""
print(
[x for x in "Himanshu plays football" for y in range(ord(x)//10)] # nested loops working in comprehension
    )
"""

#Nested Lists: its also known as n-dimesional lists

#oython doesn't follows the matrix approach because in matrix approach there is alot of memory wastage


#it follows list of list approacch....


# a list assign some other list as an element

"""
ls=[
[1,2,3,4,5],
1,
[1,2],
[1,2,3,4]
    ]
print(ls)


ls1=[
list("HIMANSHU"),
"himanshu",
[x for x in range(10)]

    ]
print(ls1)
"""

#MAtrix::::
#try to add set and tuples inside list>>>>>>>>>

from random import randint

mat=[[randint(10,50)for col in range(5)]for row in range(5)]

#print(mat)
for x in mat:
    print(x)


#diagonal=[mat[x][x]for x in range(len(mat))]
#print(diagonal)

d1=[mat[x][x+1]for x in range(len(mat)-1)]

#print(d1)

rws=[sum(row)for row in mat]
#print(rws)


rwm=[sum(row)/len(row)for row in mat]
#print(rwm)


tran=[mat[row][col]for col in range(len(mat))for row in range(len(mat))] #single dimesnional listed comprehension
#print(tran)

#t=[[mat[row][col]for row in range(len(mat))]for col in range(len(mat))]
#for x in t:
    #print(t)

"""
data="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
j=[]
freq=[[x,data.split().count(x)]for x in data.split()]
print(freq)
fr=[[x,sum([1 for y in data.split()if x==y])]for x in data.split()]

print(fr)
"""


#accessing the list:   slicing and indexing and reference variavle(whenever you are required to acess the entire list)

#indexing whne you need to access some single particular elelment of your list then you can use it.
#ls[0]  #square brackets are indexing operators
#if you need to access the element from near to right then go for negative indexing....otherwise positive indexing


#SLICING:........when want to access the piece of the list.[:]->skicing operator






























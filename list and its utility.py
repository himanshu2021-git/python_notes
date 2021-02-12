#list--it is mutable and heterogenous(int, float) data,support slicing and indexing
l=[]#by using square bracket 
l1=list()#this is empty list
print(l1,type(l1),id(l1))#l and l1 has different address because they dont have data same structure has always different address 
print(l,type(l),id(l)) #but if data is same then address is same  :: PVM always focus on data

l2=list([1,2.3,5])
print(l2,type(l2),id(l2))
l3=[1,2.3,5]
print(l3,type(l3),id(l3))
print(l2[0])
print(l3[0])
print(type(l3[1]))

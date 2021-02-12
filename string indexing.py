#string and its utility methods with slicing and indexing

s = "Himanshu loves football"
print("s==",s,type(s),id(s))
print(s[0])

#reverse indexing

print(s[-1])
print(s[-7])

#slicing----[start:stop(n-1):step(n-1)]----slicing understands for cut out specific continues part in present data

print(s[0:7:2])
print(s[::3])
print(s[8])
print(s[-10:-1:2])#reverse slicing
print(s[5:-1])
print(s[-10:1]) #no output_blank output
print(s[::-1])

#concatination,repeatation

s1 = "Hello i also like to work with AI"
print("Concatination===",s+s1)
print("Repeatation\n","himanshu\n"*20)

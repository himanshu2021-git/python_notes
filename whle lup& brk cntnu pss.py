#while loop....
#while loops depend on the condtion. when condition false then while loop is terminated it doesnt give any output
"""x=10
while x<5:
    print("hello",x)
print("terminated")
"""
"""
x=0
while x<5:
    print("hello",x)
    x+=1
print("terminated")


x=1
while x<=10:
    x+=1
"""
"""
n=int(input("Enter n=="))
i=0
sum=1
while i<=n:
    sum=sum+i
    i=i+1
    print("i====",i)
    print("sum========",sum)
    print("average=======",sum/n)

"""
"""
                            #now use while with else
x=0
while x<15:
    print("loop on work")
    x=x+1
else:
    print("loop terminated")
"""
"""
#try to build ing=finite loop
while True:
    print("hello")
"""
"""
                            #nested while

x=0
while x<6:
    print("x==",x)
    x=x+1
    y=0 # if we put y's value globally then it achieve its value 
    while y<3:
        print("y=",y)
        y=y+1
"""

#print("*********Transfer statement***********")
#break-at specfic condition we terminate the execution of the loop forcely
#continue
#pass
"""
for i in range(1,100):
    if ((i%5==0)&(i%7==0)):
        break
    else:
        print("umber==",i)
"""
"""
for i in range(1,100):
    if ((i%5==0)&(i%7==0)):
        continue
    else:
        print("umber==",i)
        
"""
"""

for i in range(1,100):
    if ((i%5==0)&(i%7==0)):
        pass# it uses to pass condition
    else:
        print("umber==",i)
"""


#combine wrking of breask and continue ---->
for i in range(1,1000):
    if(i%2==0):
        continue
    elif(i==501):
        break
    else:
        print(i)



        #assignment
        #print number in reverse given by user,(1234)(4321)count totsal digit,print palandrome,print table of 14,15 any

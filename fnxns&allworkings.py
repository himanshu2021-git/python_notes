#function is a thing which accept something and return something
"""def hello():
    print("i'm here")
hello()"""

#defaullt argument function
#here we fix few parameters of the function at the time of creation
"""
def My(city = "xyz" , state = "abc" , sector = 125, location = "efg",age= None): #here these are default data
    print("your city is ",city,"your state is ",state,"your sector is ",sector,"and your location is ",location)
My() #it provide default data which is present
My("delhi","RJ",256,"Market",25)
My("Mumbai","MH")
#now perform combined working of postion,keyword and default
My("New york",sector="456A",age=26)"""

#Now we discuss variable length function...
#It accept multiple parameter..
#here we use symbol(*x)#here now x is conside as var length parameter
def new(*d): # * this is conside as extract
    print("Data==",d,type(d),id(d))
new(12,656,4)
new(12,987,"djsd")


#now try to to build variable length function with postional argument >>>
def abc(a,*f):
    print("a==",a,"\n","f==",f)
abc(172,43,44554,534,"fsd","vx")

#abc(342,523,5324,a=5) this isn't possible

def abc(*f,a):
    print(f,"\n",a,type(a),type(f))
#abc(53,33432,34523,5523,532)#this is also an error coz f takes all argument so resolve it we have to mention keyword
abc(53,33432,34523,5523,a=532)

#keyword variable length function--it contains the property of variable length function as well as keywor argument function
#here if we use **s type of parameter in any function thenit is a keyword var lenght function...and its return type is
def xyz(**s):#here we use is variable length keyword function
    print(s,type(s))
xyz(a=12,b=12.5,c="dfksj") #it creates in the form of dictionary

#here variablle length function also consid*args and keyword variable length function as **kwargs

def test(*args):
    l=[]
    l1=[]
    print("rgs==",args,type(args))
    for i in args:
        if i%2==0:
            l.append(i)
        else:
            l1.append(i)
        print("even==",l,"odd==",l1)
test(12,78,34,67,34)

def hello(**kwargs):
    print("k===",k,type(k))
    print(k.keys())
    print(k.values())
hello(a=45,b=232,c=22,d="fds")



    #assignment---

# make a list all type of data inside it like (int,float) and tell how much int data is there or float data or boolean etc. is there min data is 25
        #convert list into string or convert string into list...typecasting
            #take var length function sum of data and give average

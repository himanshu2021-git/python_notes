#>>>>>>OOPS.....Here we focus on data rather than procedure
#OOPS Vs Procedural Programming
#POPs...
#in this programme is divide into small parts called function
#here only sequence of action can be done and data is not important
#here we don't have any access speficier
#here we don't have any proper way of hidng data..so its less secure

#OOPs....
#here in this programme is divided into parts called object
#here importancr given to the data rather than procedure..main importance to data...we try to hide the data...majorly we look for data security
#access specifier is also here:- private,public,protected.
#here data hiding is possible..so data is more secure

#class
#object
#constructor
#what is an object?
#An object is self contained component whcih consists of methods and proeperties to make a particular type of data useful
#An object is a real world entity.Physcial existance of a class is nothing but onject
# we can create any number of objeccts for a class

#Object contain two things attribute(data) and behaviour(task)
#If human is an object--then attributes are name,age,height,weight and behaviour is walk,talk,eat

#What is a class?
#class is a prototype or we can say blueprint of an object than defines variables and methods and these are common to all objects to certain kind of object

#Class contain defination of properties(attributes) and actions(behaviour)
#Object is a instance of class and class is ablueprint or an object.#class doesnt require memory


#class,Object,
#Constructor
#methods
    
    #instance methods,
    #Static methods,
    #Class methods
#variable
    #instance variable,
    #local variable,
    #static variable
#Nested class

#ABSTRACTION,ENCAPSULATION,INHERITANCE,POLYMORPHISM(overriding and overloading)





#class name must be start with capital letter not compulsory



#how to create class
class First:
    """ This is my class"""
    a=12#data
    def hello(a):#here a is to handle constructor variable, #it is a member
        print("hello i m member")
 
print(First)
#help(First)
print(dir(First))
print(First.__sizeof__(First))
print(First.__str__(First))

#when class build its object then constructor executed basically consturctor is responsible to create object with the help of class
#Now try to creat object
First().hello()
First.hello(First)
print(First.__doc__)


#................................Telusko...........................

#class is desgin and object is real entity
#object is instance of class
#class is a blueprint of object
#further done in telusko file





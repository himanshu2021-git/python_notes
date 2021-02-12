import threading as th #thread is also a class #m

print("Current",th.current_thread())
thread=th.current_thread() #it is a function not a method
print("Name : ",thread.name) #it is a instance variable
print("NAME : ",thread.getName()) #not recommended
print("ID of thread : ",thread.ident) #thread id is always changes
thread.setName("New Name")
print("NAME : ",thread.getName())
print("is alive : ",thread.is_alive()) #is thread is active or not

print("Total active thread : ",th.active_count())
print("List of active thread obj : ",th.enumerate())
print("is daemon : ",thread.isDaemon()) #this is camel case capital D
#thread.setDaemon(True) #whenthread is in born or in ready state

#if we aren't give the name of thread except main thread then python will take them as thread1 and thread 2

#there are two types of thread
#normal thread ; Daemon thread both are created bydefault
#NT: the duty of this thread is to just complete the assigned
#DT: looks like a normal thread but ir provides the support to normal thread for there flowfull execution (like assistant)

#garbage collector is operated by Daemon thread(like a support to normal thread).doesnt have own tasks .keep eye on nt so that nt doesnt face issue while completing tasks




#Que: can we change the nature of normal thread?
#no we can't because it sets by the PVM.



#How - to create normal thread---------------

#1st way to create----without extending(HAS A RELATION | INHERITANCE) thread class targeting a function or a method.
"""
class Demo:
    def task(self): #m
        for x in range(5):#c
            print("This is excuted by :",th.current_thread().name)#c

#creating thread
obj=Demo()
t1=th.Thread( #now thread is in born state
    target=obj.task,
    name="CustomThread",
    #daemon=True,
    args=(), #provided explicilty
    #kwargs=dict(x=85,y=78)
    )
t1.start() #activate #m

for x in range(5):#m
        print("This is excuted by :",th.current_thread().name)

"""
#ouput is not predictable

#there is onw more benifit of finding the error like spelling mistake is rANGE

#main threAD ALWAYS LOOKS FOR SYNTAX ERROR




#2nd way of creating thread------ By Extending the thread class | Inheritance


class Demo(th.Thread):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def task(self):
        for x in range(1):
            print("Executed by : ",th.current_thread().name)
    def run(self): #ready state_overrding state beacuse [parent has nothing in run state
        self.task()
        self.task()
obj=Demo(name="CustomThread")
obj.start()#starting of thread actuve state


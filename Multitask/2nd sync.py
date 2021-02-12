# synchronization:
import threading as th


"""
lock=th.Lock()
def task():
    lock.acquire()
    print("Enter some value",end="")
    temp=input()
    print("the value entered by you is :",end="")
    print(temp)
    #for x in range(5):
    print("Executed : ",th.current_thread().name)
    lock.release()
t1=th.Thread(
    target=task,
    name="CustomThread"
    )
t2=th.Thread(
    target=task,
    name="CustomThread2"
    )
t1.start()
t2.start()

"""
"whenever more than one thread work on a same target then there will be the risk of inconsitent execution"
#with the help of sync we can cintrol the number of threads allowed on a target at atime

"""
LOCk
Rlock
Semaphore
Bounded semAPHORE

these all classes define below listed methods
obj.acquire(): acquires the lock of target
obj.release(): releases the lock of tARGET  so that it can be acquired by the other threads.


LOck::::::
when you wish to allow only a single thread at a time on non-recursive method opr function


RLock: Renant Lock
if you wish to allow only a single thread onto a reecusrive method or function
"""
"""
lock=th.RLock()
def table(n,i=1):
    lock.acquire()
    print(n*i)
    if i<10:
        table(n,i+1)
    lock.release()
t1=th.Thread(
    target=table,
    args =(9,))
t2=th.Thread(
    target=table,
    args =(10,))


t1.start()
t2.start()

"""
#Semaphore: when you wish to allow n number of thread at same time

"""
lock=th.Semaphore(2)#allowing 2 threads going to work same time
def task():
    lock.acquire()
    print("Enter some value",end="")
    temp=input()
    print("the value entered by you is :",end="")
    print(temp)
    #for x in range(5):
    print("Executed : ",th.current_thread().name)
    lock.release()
t1=th.Thread(
    target=task,
    name="CustomThread "
    )
t2=th.Thread(
    target=task,
    name="CustomThread2 "
    )
t3=th.Thread(
    target=task,
    name="CustomThread3 ")
t1.start()
t2.start()
t3.start()
"""

#Bounded Sempahore: same as semaphore but it can work with recursive method also.

#inter-thread communication: sometimes the methods or functions may depend on each other and the respective threads have to tell each other about the progress the chances of getting error is reduced.

#Event-with the help of this class we can very easilt perform the inter thread comm.
#this class defines the following three methods.

#1-obj.set()--sets the event so all the waiting threads are notified that they cab continue there tasks.
#2-obj.wait()-- makes the thread to wait till the particulat event is set.
#3-obj.clear()---it clears the event


a= None
b= None

event=th.Event()

def get():
    global a
    global b
    a=int(input("Enter a number: "))
    b=int(input("Enter a number again: "))
    print("Setting the event",th.current_thread().name)
    event.set()

def process():
    print("Thread is waiting :",th.current_thread().name)
    event.wait()
    print(a+b)

g =th.Thread(
    target=get,
    name="G thread "
    )
p=th.Thread(target=process,name="P thread ")

g.start()
p.start()

#Python stuff reqired to deal with the exception

#try: it is a block in which you should only write the risky code(the code which you think may causw an error or exception).Once flow get out of this block can never re enter init.
#keep your try block as much small as you can.
#try block can never be used alone.

#EXCEPT: this block contains the handling codd.
#a-particular class exceot block: this can handle only a specific type of exception.
#b-parent class except block: this can gandle self exception and all its children classes exception
#c- default except block: the default except block gets executed for every type of exception. It must be last in the list of exxcept block

try:
    a=int(input("Enter a number please"))
    print("Himanshu")

except ValueError as e: #PArticular except block
    print("There is a error known as",e)

except TypeError as t:
    print("The error is known as",t)

except Exception as E: #parentclass excopet block
    print("Some exception class child caught",E)

except:
    print("Some unknown exceotion was caught")

else:
    print("No exception caught")
finally:
    print("Tis execute eveytime")

print("LAst statement")

#else: this is optional block it can only be used once with a single try block,it gets

#FINALLY:::::::::::::: this is also an optional block,you can only use it once with a single try block,gets invoked everytime.this block mostly used to write the
#flowfull regarding code.if code comes in try block then finally bloc run for sure


#raise: used to raise an exception forcefully with custom msg.

#assert: used to raise AssertionError only with custom msg on the basis of given condtion. majorly used to get the desired input or not.

#-----------------------------------------------------------------------------------

#CREATING CUSTOMIZED EXCEPTION

#just subclass any exception class 























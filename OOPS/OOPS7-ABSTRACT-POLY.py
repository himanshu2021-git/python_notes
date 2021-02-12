#Abstract class

#POLYMORPHISM----- ONE THING HAVINNG MORE THAN ONE MEANING.
#Complie time polymorphism | method overloading | early biding
#In a same class if you try more than one method with same name but different number or type og args.
#In python if you define multiple method with same name in a class then oython will recognize only lastly define method

#in python compile time polymorphism isn't possible.


#Run-time polymorphism (METHOD OVERRIDING) | late binding
#in inheritance if  CHILD  isnt satisfied with parent given attributes then child can redefine those attributes and this thing is called method overriding.

def __dir__(self):
    return[]
def __len__(self):
    return 45
def __add__(self,value):
    retrn len(self)+len(value)



from abc import ABC,abstractmethod

class BankingRules(ABC):
    @abstarctmethod
    def deposit():pass
    @abstractmethod
    def withdraw():pass
    @abstractmethod
    def BalanceEnquiry():pass
    def temp(self):pass






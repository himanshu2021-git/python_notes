#-inner class
# a class defined inside some other class
"""class Bank:
    def __init__(self,amount):
        self.balance=amount
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance >amount:
            self.balance -=amount
        else:
            return "invalid amount"

if __name__=='__main__':
    Himanshu = Bank(20000)

    print(Himanshu.balance)
    Himanshu.deposit(2000)
    print(Himanshu.balance)
    Himanshu.withdraw(25000)
    print(Himanshu.balance)
"""

class Bank:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    class SavingsAccount:
        def __init__(self,name,address,amount):
            self.name=name
            self.address=address
            self.balance=amount
        def balanceEnquiry(self):
            print("Balance is ",self.balance)

        def deposit(self,amount):
            self.balance +=amount
            self.balanceEnquiry()

        def withdraw(self,amount):
            if amount<self.balance:
                self.balance -=amount
                self.balanceEnquiry()
            else:
                print("you can't withdraw this amount")
        def menu(self):
            option={
                1:("Balance ",self.balanceEnquiry),
                2:("withdraw",self.withdraw),
                3:("Deposit",self.deposit)
            }
            for k,v in option.items():
                print(f"{k}-->{v[0]}")
            ch =int(input("Enter option:"))
            if ch in option:
                if ch in [2,3]:
                    amount = float(input("Enter amount : "))
                    option[ch][-1](amount)
                else:
                    option[ch][-1]()
            else:
                print("Invalid option")

    class CurrentAccount:pass

    class FdAccount: pass

    def options(self):
        menus={
                1:("Savings account",self.SavingsAccount),
                2:("Current Accounts",self.CurrentAccount),
                3:("Fixed Deposit Account: ",self.FdAccount)
            }
        for k,v in menus.items():
                print(f"{k}-->{v[0]}")
            ch =int(input("Enter option:"))
            if ch in menus:
                amount=float(input("Initial amount :"))
                menus[ch][-1](self.name,adddress,amount)
            else:
                print("Invalid option")

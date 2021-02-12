# SOME EXAMPLES OF INSTANCE METHOD
# # """
# class Test:
#     def __init__(self,name,age,marks = 14.0):
#         self.name = name
#         self.marks = marks
#         self.age = age
#     def disp(self):
#         print("Hello",self.name)
#         print("Your marks is",self.marks)
#     # def div(self):
#         if self.marks>=60:
#             print("YOU GOT 1st DIV")
#         elif self.marks>=30:
#             print("YOU GOT 2nd DIV")
#         elif self.marks>=33:
#             print("You got 3rd div")
#         else:
#             print("=======you are fail=======")
#             print("please enter next")

# while True:
#     n = input("Enter your name: ")
#     m = float(input("Enter your marks"))
#     a = float(input("Enter your age"))
#     s = Test(n,a,m)
#     s.disp()
    # s.div()
# """

class Stud:
    def setN(self,name):
        self.name=name
    def setM(self,marks):
        self.marks=marks
    def getN(self,name):
        return self.name
    def getM(self,marks):
        return self.marks
while True:
    nn = input("Enter your name")
    mm=float(input("Enter your marks"))
    w=Stud()
    w.setN(nn)
    w.setM(mm)
    w.getN(nn)
    w.getM(mm)
    

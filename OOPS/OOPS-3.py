#CLASS MAKES OUR PROGRAM SUPER MAINTAINED

#METHOD SCOPING-- WHENEVER YOU CALL A METHOD OF A CLASS THEN HOW THAT IS FOUND BY THE EXECUTING THREAD THAT PROCESS IS CALLED METHOD SCOPING.

#METHOD SIGNATURE-- IN PYTHON NOTHING IS PRIMITIVE...
#eX... DEF HIMANSHU(CLEAR,GREAT)......---HIMANSHU(oBJECT,OBJECT).



#-------------INNER CLASSES............ a class defined inside other classes.

#singley linked list...

class Node:
    """
        this class's every object represents a single node
    """
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
        
class SL:
    """
        This is singly linked list
    """
    def __init__(self,value):
        self.node=Node(value)
    def addNode(self,element):
        if not self.node.next_node:  #also can write self.node.next_node =None
            self.node.next_node=Node(element)
        else:
            temp=self.node
            while temp.next_node:
                temp=temp.next_node
            temp.next_node=Node(element)
        
    def display(self):
        if not self.node.next_node:
            print(self.node.value)
        else:
            temp=self.node
            while temp.next_node:
                print(temp.value,end="-->")
                temp=temp.next_node
            print(temp.value)
    def RN(self,element):
        if not self.node.next_node:
            if self.node.value==element:
                self.node=Node(None)
        else:
            pn=None
            cn=None
            temp=self.node
            while temp.next_node:
                if temp.next_node.value==element:
                    pn=temp
                    cn=temp.next_node
                    break
                if temp.next_node:
                    temp=temp.next_node
                 
            if pn:
                pn.next_node=cn.next_node
                
            else:
                print("Node isn't avaiable")
                
    @classmethod   #factory_method
    def range(cls,start=0,end=0,step=1):
        data=list(range(start,end,step))
        if len(data)<1:
            print("Invalid param")
        elif len(data)==1:
            return cls(data[0])
        else:
            temp=cls(data[0])
            for x in data[1:]:
                temp.addNode(x)
            return temp
    def findNode(self,element):pass
    def replace(self,old,new,all=False):
        if not self.node.next_node:
            if self.node.value==old:
                self.node.value= new
        else:
            temp=self.node.next_node
            while temp.next_node:
                if temp.value==old:
                    temp.value=new
                    if not all:
                        break
                temp=temp.next_node
    def extendNodes(self,collection):pass
    def insert(self,element,position):pass

if __name__=="__main__":
    l1=SL(10)
    l1.addNode(20)
    l1.addNode(30)
    l1.addNode(40)
    l1.addNode(50)
    
    l1.replace(50,90)
    l1.display()
    
    
#notepad.pw/pynewbatch ducat630

# Today we discuss about hybrid inheritance with C3 algo....
"""
class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass


print("MRO for A",A.mro())
print("MRO for B",B.mro())
print("MRO for C",C.mro())
print("MRO for X",X.mro())
print("MRO for Y",Y.mro())
print("MRO for P",P.mro())


"""
#Try to find output with C3 algo..

#mro(P)=[class(P)+merge(mro(Parents at same level),Parentlist)] ----step-1
#mro(P)=[P+merge(mro(X),mro(Y),mro(C),XYC)]
#mro(P)=P+merge[XABo,YBCo,Co,XYC]

#Now first we find head and tail.
#if head of any list nor present in tail part of any other list then it will pop out from all the present list
#mro(P)==>P+X+merge(ABo,YBCo,Co)  <----remove x (removing head element)
#mro(P)==>P+X+A+merge(Bo,YBCo,Co)
#if head element of selected list present in tail part of any list then leave that list at is and shuft to next
#mro(P)==>P+X+A+Y+merge(Bo,BCo,Co)<----remove Y
#mro(P)===> P+X+A+Y+C+merge(o,Bo,o)<----remove C
#mro(P)====> P+X+A+Y+C+B+o



class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B):
    pass
class Y(A,C):
    pass
class P(X,Y):
    pass

print(P.mro())


#mro(P)=P+merge[(mro(X),mro(Y)),XY]
#mro(P)=P+merge[ABo,ACo,XY]
#mro(P)=P+A+merge[Bo,Co]
#mro(P)=P+A+B+C[o]







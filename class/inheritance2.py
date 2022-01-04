class A:
    def __init__(self,name):
        print(f"{name} is good boy")
    def f1(self):
        print("f1")
class B(A):
    # def __init__(self,name1):
    #     print(f"{name1} is not good boy")    
    def f2(self):
        print("f2")
class C(B):
    # def __init__(self,name2):
    #     print(f"{name2} is bad boy")
    def f3(self):
        print("f3")
c1=C("RAGHu")
c1.f1()
c1.f2()
c1.f3()
print()
b=B("RAHUl")
b.f1()
b.f2()


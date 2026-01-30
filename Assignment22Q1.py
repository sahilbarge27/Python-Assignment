class Parent:
    def __init__(self):
        self.No1 = 10
        self.No2 = 20

    def fun(self):
        print(self.No1, self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constucter")
        self.A = 11
        self.B = 21

    def sun(Self):
        print(Self.A, Self.B, Self.No1, Self.No2)

cobj = Child()

print(cobj.No1)   # 10
print(cobj.No2)   # 20

print(cobj.A)   # 11
print(cobj.B)   # 21

cobj.fun()
cobj.sun()       
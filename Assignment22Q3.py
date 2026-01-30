class Arithmetic:
    def _init_(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not possible"
        return self.Value1 / self.Value2


# creating multiple objects
a1 = Arithmetic()
a1.Accept()
print("Addition:", a1.Addition())
print("Subtraction:", a1.Subtraction())
print("Multiplication:", a1.Multiplication())
print("Division:", a1.Division())

print("------------------")

a2 = Arithmetic()
a2.Accept()
print("Addition:", a2.Addition())
print("Subtraction:", a2.Subtraction())
print("Multiplication:", a2.Multiplication())
print("Division:", a2.Division())
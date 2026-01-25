import Arithmetic 

def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mult(a, b):
    return a * b

def Div(a, b):
    return a / b

x = int(input("Enter the first number : "))
y = int(input("Enter the Second number : "))

print("Addition:", Arithmetic.Add(x, y))
print("Substraction:", Arithmetic.Sub(x, y))
print("Multiplication:", Arithmetic.Mult(x, y))
print("Division:", Arithmetic.Div(x, y))
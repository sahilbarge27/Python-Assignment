a = int(input("Enter first number : "))
b = int(input("Enter second number :"))

minimum = lambda x, y: x if x < y else y
print("Minimum:", minimum(a, b))

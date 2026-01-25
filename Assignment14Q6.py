is_odd = lambda x: x % 2 != 0

num = int(input("Enter a number: "))

if is_odd(num):
    print("True (Number is odd)")
else:
    print("False (Number is even)")


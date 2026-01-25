import MarvellousNum

def ListPrime(numbers):
    total = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            total = total + num
    return total

n = int(input("Enter number of elements: "))

numbers = []
for i in range(n):
    numbers.append(int(input()))

result = ListPrime(numbers)
print("Output:", result)
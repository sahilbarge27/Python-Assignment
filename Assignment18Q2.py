n = int(input("Enter the number of elements : "))
numbers = []

for i in range(n):
    num = int(input("Enter element : "))
    numbers.append(num)

total = sum(numbers)
print("Additoin of all elements:", total)
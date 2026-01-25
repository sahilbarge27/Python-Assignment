def Minimum(numbers):
    return min(numbers)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

ret = Minimum(arr)
print("Output:", ret)

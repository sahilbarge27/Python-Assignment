from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

filtered = list(filter(lambda x: x % 2 == 0, numbers))
mapped = list(map(lambda x: x * x, filtered))
result = reduce(lambda a, b: a + b, mapped)

print("List after filter:", filtered)
print("List after map:", mapped)
print("Output of reduce:", result)

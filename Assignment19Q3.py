from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

filtered = list(filter(lambda x: 70 <= x <= 90, numbers))
mapped = list(map(lambda x: x + 10, filtered))
result = reduce(lambda a, b: a * b, mapped)

print("List after filter:", filtered)
print("List after map:", mapped)
print("Output of reduce:", result)

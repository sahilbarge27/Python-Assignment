from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

minimum = reduce(lambda a, b: a if a < b else b, numbers)
print("Minimum:", minimum)
from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)
from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

addition = reduce(lambda a, b: a + b, numbers)
print("Addition:", addition)

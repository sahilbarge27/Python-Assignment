numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Divisible by 3 and 5:", result)
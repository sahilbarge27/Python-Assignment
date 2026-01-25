numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print("2. Even numbers:", even_nums)
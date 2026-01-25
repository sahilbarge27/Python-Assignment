numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
print("Count of even numbers:", even_count)
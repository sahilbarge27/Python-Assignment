numbers = list(map(int, input("Enter numbers separated by space: ").split()))
odd_nums = list(filter(lambda x: x % 2 !=0, numbers))
print("3. odd numbers:", odd_nums)
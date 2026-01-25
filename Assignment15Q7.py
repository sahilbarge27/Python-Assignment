strings = input("Enter strings separated by space: ").split()

result = list(filter(lambda s: len(s) > 5, strings))
print("Strings with length > 5:", result)
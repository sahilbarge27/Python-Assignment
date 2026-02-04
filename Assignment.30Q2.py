filename = input("Enter file name: ")

with open(filename, "r") as file:
    print(file.read())
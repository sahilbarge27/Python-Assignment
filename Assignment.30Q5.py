filename = input("Enter file name: ")
word = input("Enter string: ")

with open(filename, "r") as file:
    text = file.read()

count = text.count(word)
print("Frequency:", count)
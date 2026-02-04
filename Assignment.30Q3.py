import sys

source = sys.argv[1]

with open(source, "r") as f1:
    data = f1.read()

with open("Demo.txt", "w") as f2:
    f2.write(data)

print("File copied successfully")
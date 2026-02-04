import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f1, open(file2, "r") as f2:
    if f1.read() == f2.read():
        print("Success")
    else:
        print("Failure")
def Pattern(n):
    for i in range (n):
        for j in range(n):
            print("*", end=" ")
        print()

n = int(input("Enter Number : "))
Pattern(n)


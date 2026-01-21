no = int(input("Enter the Number : "))
rev = 0 

while no > 0:
    rev = rev * 10 + no % 10
    no //= 10

print("Reverse:",rev)
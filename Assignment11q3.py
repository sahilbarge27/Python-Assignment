no = int(input("Enter the Number : "))
sum = 0 

while no > 0:
    sum += no % 10 
    no //= 10

print("Sum of digits : ", sum)

no = int(input("Enter the Number : "))
count = 0 

while no > 0 :
    count += 1
    no //= 10

print("Count of digits :",count)

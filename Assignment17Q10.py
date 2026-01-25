def SumDigits(n):
    total = 0 
    while n > 0 :
        total += n % 10
        n //= 10 

n = int(input("Enter the number : "))
print("Addition of digits:", SumDigits(n))
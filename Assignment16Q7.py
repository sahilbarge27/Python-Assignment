def DivisibleByFive(num):
    if num % 5 == 0:
        return True
    else :
        return False 
    
n = int(input("Enter the number : "))
print(DivisibleByFive(n))
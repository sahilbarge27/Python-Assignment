def SumFactors(n):
    totsl = 0 
    for i in range(1, n):
        if n % i == 0 :
            total += i
        return total 
    
n = int(input("Enter the nmuber : "))
print("Addition of Factorials: ",SumFactors(n))
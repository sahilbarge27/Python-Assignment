def CheckNumber(num):
    if num > 0 :
        print("Positive Number")
    elif num < 0 :
        print("Nagative Number")
    else :
        print("Zero")

n = int(input("Enter the number : "))
CheckNumber(n)
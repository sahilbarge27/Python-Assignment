no = int(input("enter the number : "))
flag = True

if no <= 1 : 
    flag = False
else :
    for i in range(2, no):
        if no % i == 0:
            flag = False
            break
if flag:
    print("Prime Number")
else:
    print("Not Prime Number")

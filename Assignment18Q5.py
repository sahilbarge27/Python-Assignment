def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def ListPrime(numbers):
    total = 0
    for no in numbers:
        if ChkPrime(no):
            total = total + no
    return total


def main():
    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

    result = ListPrime(arr)
    print("Output:", result)


if __name__ == "_main_":
    main()
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

filtered = list(filter(is_prime, numbers))
mapped = list(map(lambda x: x * 2, filtered))
result = reduce(lambda a, b: a if a > b else b, mapped)

print("List after filter:", filtered)
print("List after map:", mapped)
print("Output of reduce:", result)

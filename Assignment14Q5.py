
is_even = lambda number: number % 2 == 0

num = int(input("Enter a number: "))

result = is_even(num)

if result:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
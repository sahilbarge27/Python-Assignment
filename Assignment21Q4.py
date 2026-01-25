import threading
import math

sum_result = 0
product_result = 1

def calculate_sum(nums):
    global sum_result
    sum_result = sum(nums)

def calculate_product(nums):
    global product_result
    product_result = math.prod(nums)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=calculate_sum, args=(numbers,))
t2 = threading.Thread(target=calculate_product, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum:", sum_result)
print("Product:", product_result)
import threading

def find_max(nums):
    print("Maximum element:", max(nums))

def find_min(nums):
    print("Minimum element:", min(nums))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=find_max, args=(numbers,))
t2 = threading.Thread(target=find_min, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()
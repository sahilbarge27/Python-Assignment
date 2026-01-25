import threading

def even_factor(n):
    evens = [i for i in range(1, n+1) if n % i == 0 and i % 2 == 0]
    print("Even Factors:", evens)
    print("Sum of Even Factors:", sum(evens))

def odd_factor(n):
    odds = [i for i in range(1, n+1) if n % i == 0 and i % 2 != 0]
    print("Odd Factors:", odds)
    print("Sum of Odd Factors:", sum(odds))

num = 12

t1 = threading.Thread(target=even_factor, args=(num,))
t2 = threading.Thread(target=odd_factor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
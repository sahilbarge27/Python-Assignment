import threading

def even_list(lst):
    evens = [i for i in lst if i % 2 == 0]
    print("Even List:", evens)
    print("Sum of Even:", sum(evens))

def odd_list(lst):
    odds = [i for i in lst if i % 2 != 0]
    print("Odd List:", odds)
    print("Sum of Odd:", sum(odds))

numbers = [1, 2, 3, 4, 5, 6, 7]

t1 = threading.Thread(target=even_list, args=(numbers,))
t2 = threading.Thread(target=odd_list, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()
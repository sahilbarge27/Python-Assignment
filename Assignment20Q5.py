import threading

def thread1():
    for i in range(1, 51):
        print(i)

def thread2():
    for i in range(50, 0, -1):
        print(i)

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t1.join()     # Thread2 starts only after Thread1 ends

t2.start()
t2.join()
import threading

def small(s):
    count = sum(1 for c in s if c.islower())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Count:", count)

def capital(s):
    count = sum(1 for c in s if c.isupper())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Count:", count)

def digits(s):
    count = sum(1 for c in s if c.isdigit())
    print("Thread Name:", threading.current_thread().name)
    print("Digit Count:", count)

text = "Hello123World"

t1 = threading.Thread(target=small, args=(text,), name="Small")
t2 = threading.Thread(target=capital, args=(text,), name="Capital")
t3 = threading.Thread(target=digits, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
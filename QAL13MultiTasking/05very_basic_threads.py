from threading import Thread
import time


def my_func(*args):
    print("From thread", args)
    time.sleep(5)


th1 = Thread(target=my_func, args="1")
th2 = Thread(target=my_func, args="2")
th1.start()
th2.start()
print("From main")
th1.join()
th2.join()

from multiprocessing import Process
import time

def my_func(*args):
    print("From proc", args)
    time.sleep(5)

if __name__ == "__main__":
    p1 = Process(target=my_func, args=(1,))
    p2 = Process(target=my_func, args=(2,))
    p1.start()
    p2.start()
    print("From main")
    p1.join()
    p2.join()

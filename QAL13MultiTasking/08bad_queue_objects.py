from multiprocessing import Process, Queue, Lock
import os

lock = Lock()

def my_func(*args):
    queue = args[0]
    global lock

    word = ""
    while word != "END":
        word = queue.get()
        if len(word) == 7:
            lock.acquire()
            try:
                print(os.getpid(), ":", word)
            finally:
                lock.release()


if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=my_func, args=(queue, "1"))
    p2 = Process(target=my_func, args=(queue, "2"))

    p1.start()
    p2.start()

    for line in open("words"):
        queue.put(line[:-1])

    queue.put("END")
    queue.put("END")

    p1.join()
    p2.join()
    print("All done")

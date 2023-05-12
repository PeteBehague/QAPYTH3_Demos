import multiprocessing
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class OutOfControlCounter(object):
    def __init__(self, start = 0):
        self.value = start

    def increment(self):
        print('I ', end='')
        print('love ', end='')
        print('debugging ', end='')
        self.value = self.value + 1
        print('multi-process ', end='')
        print('programs!')


class InControlCounter(object):
    def __init__(self, start = 0):
        self.lock = multiprocessing.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            print('I ', end='')
            print('love ', end='')
            print('debugging ', end='')
            self.value = self.value + 1
            print('multi-process ', end='')
            print('programs!')
        finally:
            logging.debug('Released a lock')
            self.lock.release()

def worker(c):
    for i in range(5):
        r = random.random()
        logging.debug('Sleeping %0.02f', r)
        time.sleep(r)
        c.increment()
    logging.debug('Done')
    # print(f"count: {c.value}") # each process gets a clone of the original counter object

if __name__ == '__main__':
    counter = OutOfControlCounter()
    # counter = InControlCounter()
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(counter,))
        processes.append(p)
        p.start()

    logging.debug('Waiting for worker processes')

    for p in processes:
        p.join()

    # original counter was cloned hence this one's count is zero
    logging.debug('Counter: %d', counter.value)
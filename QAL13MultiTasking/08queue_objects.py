from multiprocessing import Process, Queue, Lock
import os


class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1


class WordEater:
    def __init__(self):
        self.lock = Lock()
        self.queue = None
        self.count = 0

    def process_words(self, *args):
        word = ""
        self.queue = args[0]
        self.counter = args[1]
        while word != "END":
            word = self.queue.get()
            if len(word) == 7:
                self.lock.acquire()
                try:
                    self.counter.increment()
                    print(os.getpid(), ":", word, " count: ", self.counter.count)
                finally:
                    self.lock.release()


if __name__ == "__main__":
    queue = Queue()
    word_eater = WordEater()
    counter = Counter()

    p1 = Process(target=word_eater.process_words, args=(queue, counter))
    p2 = Process(target=word_eater.process_words, args=(queue, counter))

    p1.start()
    p2.start()

    for line in open("words"):
        queue.put(line[:-1])

    queue.put("END")
    queue.put("END")

    p1.join()
    p2.join()
    # original counter was cloned hence this one's count is zero
    print(f"All done: Number of words processed: {counter.count}")

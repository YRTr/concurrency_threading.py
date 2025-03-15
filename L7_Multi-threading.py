"""
Level 7:
Use a shared counter (counter = 10) that multiple threads decrement.
Ensure proper synchronization using threading.Lock() to prevent race conditions.
Consumers should print values as they decrement.
"""
from threading import Thread, Lock
from time import sleep
from queue import Queue

lock = Lock()
counter = 10
queued = Queue()
total_prod = 3

def producer():
    global counter
    while True:
        with lock:
            if counter < 0:
                break
            queued.put(counter)
            counter -= 1
        sleep(1)
    queued.put("STOP")

def consumer():
    stop_signals = 0
    while stop_signals < total_prod:
        if stop_signals == "STOP":
            stop_signals += 1
            continue
        value = queued.get()
        if value == "STOP":
            break
        print(f'countdown: {value}')
        sleep(1)

producer_threads = [Thread(target=producer) for _ in range(total_prod)]
c1 = Thread(target=consumer)

for p in producer_threads:
    p.start()

c1.start()

for worker in producer_threads:
    worker.join()

c1.join()

print('Multi-threading implementation with shared counter')
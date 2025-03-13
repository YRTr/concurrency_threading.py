"""
Level 5: Priority Queue Challenge
🔹 Modify your implementation to use queue.PriorityQueue().
🔹 Producers should insert values with priorities (higher numbers = higher priority).
🔹 Consumer should always process the highest priority first (descending order).
🔹 No need for threading.Lock(), as PriorityQueue is thread-safe.
"""
#import threading
#import time
#import queue

q = queue.PriorityQueue()
timer = 10
num_consumers = 2

def producer():
    global timer
    for i in range(timer):
        q.put((-timer, timer))
        timer -= 1
        time.sleep(1)
    q.put((0, 'STOP'))

def consumer():
    while True:
        priority, value = q.get()
        if value == 'STOP':
            break
        print(f'countdown: {value}')
        time.sleep(0.5)
        q.task_done()

producer_thread = threading.Thread(target=producer)
producer_thread.start()

consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print('Multi-threading achieved using Priority Queue')

"""
Level 6:
Instead of manually creating and managing threads, use concurrent.futures.ThreadPoolExecutor.
Have one producer task and multiple consumer tasks.
Ensure consumers work in parallel to efficiently process the queue.
"""
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import queue

num_cons = 5
qu = queue.Queue()
timers = 10

def producer():
    global timers
    for i in range(timers, 0, -1):
        qu.put(i)
        sleep(1)

def consumer():
    while not qu.empty():
        value = qu.get()
        print(f'countdown: {value}')
        sleep(0.5)
        qu.task_done()

if __name__ == '__main__':
    producer()
    with ThreadPoolExecutor(max_workers=num_cons) as exe:
        result = [exe.submit(consumer) for _ in range(num_cons)]

    print('Multithreading achieved by ThreadPoolExecutor')

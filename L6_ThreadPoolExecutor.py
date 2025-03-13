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

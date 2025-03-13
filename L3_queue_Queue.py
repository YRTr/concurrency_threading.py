"""
Level 3 Challenge:
Create a thread-safe queue (queue.Queue()) to store countdown values.
Use two producer threads to add countdown values (10 → 1) to the queue.
Use two consumer threads to remove and print values from the queue.
Ensure proper synchronization using queue.Queue() (no threading.Lock()).
"""
import threading
import time
import queue

que = queue.Queue()
timer = 10
num_consumers = 2

def producer():
    global timer
    while timer > 0:
        que.put(timer)
        timer -= 1
        time.sleep(1)
    for _ in range(num_consumers):
        que.put(0)

def consumer():
    while True:
        value = que.get()
        if value == 0:
            break
        print(f'countdown: {value}')
        time.sleep(0.5)
        que.task_done()

producer_thread = threading.Thread(target=producer)
producer_thread.start()

consumer_thread = [threading.Thread(target=consumer) for _ in range(2)]
for thread in consumer_thread:
    thread.start()

producer_thread.join()

for worker2 in consumer_thread:
    worker2.join()

print("Multi threading is achieved by using Queue")

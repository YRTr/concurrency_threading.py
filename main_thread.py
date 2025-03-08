"""
Level 1: Basic Threading
Write a Python program that runs two functions concurrently using threading.
Each function should print numbers from 1 to 5 with a small delay between prints.

Goal:
Use threading.Thread to run two functions in parallel.
Ensure both functions print numbers without blocking each other.
"""
import threading
import time

def count_down():
    for num in range(0, 6):
        print(f'Count down started!: {num}')
        time.sleep(1)

crucial_checks = ['vehicle system integrity', 'propellant levels', 'weather conditions', 'launch pad safety',
                  'communication systems', 'flight control software', 'emergency procedure', 'backup systems',
                  'payload integrity', 'final launch readiness review']

def rocket_launch_checks(obj):
    for chk in obj:
        print(f'{chk}')
        time.sleep(1)

thread1 = threading.Thread(target=count_down)
thread2 = threading.Thread(target=rocket_launch_checks, args=(crucial_checks,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads are finished!")

"""
Level 2:
Modify your program to:

Create a global countdown variable (countdown_timer = 10).
Run two threads, where:
One thread decrements the countdown every second.
The other thread checks and prints its value periodically.
Use threading.Lock() to ensure thread safety while modifying the variable.
"""
#import threading

countdown_timer = 10
lock = threading.Lock()

def decrement():
    global countdown_timer
    while countdown_timer > 0:
        with lock:
            print("Lock acquired")
            countdown_timer -= 1
        time.sleep(1)

def run_check():
    global countdown_timer
    while countdown_timer > 0:
        with lock:
            print(countdown_timer)
        time.sleep(1)


thread1 = threading.Thread(target=decrement)
thread2 = threading.Thread(target=run_check)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("concurrency achieved with threading")

"""
Level 3 Challenge:
Create a thread-safe queue (queue.Queue()) to store countdown values.
Use two producer threads to add countdown values (10 → 1) to the queue.
Use two consumer threads to remove and print values from the queue.
Ensure proper synchronization using queue.Queue() (no threading.Lock()).
"""
import threading
#import time
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

"""
Level 4: Independent Producers & Consumers
Each producer should generate its own countdown values independently.
Each consumer should process values from the queue as they arrive.
No shared timer variable between producers.
Ensure all countdown values are processed correctly.
"""
import threading
#import time
import queue

timer1 = 10
que = queue.Queue()

def producer1():
    global timer1
    while timer1 > 0:
        if timer1 % 2 == 0:
            que.put(timer1)
        timer1 -= 1
        time.sleep(1)
    que.put('STOP')

def producer2():
    global timer1
    while timer1 > 0:
        if timer1 % 2 == 1:
            que.put(timer1)
        timer1 -= 1
        time.sleep(1)
    que.put('STOP')

def consumer():
    while True:
        value = que.get()
        if value == 'STOP':
            break
        print(f'countdown: {value}')
        time.sleep(0.5)
        que.task_done()

p1_thread = threading.Thread(target=producer1)
p2_thread = threading.Thread(target=producer2)

p1_thread.start()
p2_thread.start()

con_thread = threading.Thread(target=consumer)

con_thread.start()

p1_thread.join()
p2_thread.join()
con_thread.join()
print('Multi-Threading with independent threading approach')

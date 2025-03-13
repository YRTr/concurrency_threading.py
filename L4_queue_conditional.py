"""
Level 4: Independent Producers & Consumers
Each producer should generate its own countdown values independently.
Each consumer should process values from the queue as they arrive.
No shared timer variable between producers.
Ensure all countdown values are processed correctly.
"""
import threading
import time
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
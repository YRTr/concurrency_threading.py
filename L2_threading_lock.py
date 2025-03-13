"""
Level 2:
Modify your program to:

Create a global countdown variable (countdown_timer = 10).
Run two threads, where:
One thread decrements the countdown every second.
The other thread checks and prints its value periodically.
Use threading.Lock() to ensure thread safety while modifying the variable.
"""

import threading
import time

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

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
condition = threading.Condition(lock)

def decrement():
    global countdown_timer
    while countdown_timer > 0:
        with condition:
            countdown_timer -= 1
            print("Lock acquired by decrement")
            condition.notify_all()
        time.sleep(1)

def run_check():
    global countdown_timer
    previous_value = None
    while True:
        with condition:
            if countdown_timer <= 0:
                break
            if countdown_timer != previous_value:
                print(f'Countdown: {countdown_timer}')
                previous_value = countdown_timer
        time.sleep(0.1)

thread1 = threading.Thread(target=decrement)
thread2 = threading.Thread(target=run_check)

thread2.start()
thread1.start()

thread2.join()
thread1.join()

print("concurrency achieved with threading")

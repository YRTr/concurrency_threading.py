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
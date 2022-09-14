#!/usr/bin/env python3
# Modified from https://docs.python.org/3/library/multiprocessing.html
from multiprocessing import Process
import os

# Get process information
def process_info():
    print('process id:', os.getpid())

# Worker function
def worker(number):
    print(f'Worker number {number}')
    process_info()


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
    

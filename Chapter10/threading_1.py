#!/usr/bin/env python3
# Modified from https://pymotw.com/3/threading/index.html
import threading

# Get thread ID
def thread_id():
    print('thread id:', threading.get_ident())

# Worker function
def worker(number):
    print(f'Worker number {number}')
    thread_id()


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

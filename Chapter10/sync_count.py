#!/usr/bin/env python3
# Modified from https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait countsync.py example
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    count()
    count()
    count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds.")


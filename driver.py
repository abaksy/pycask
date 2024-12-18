# Driver program for bitcask datastore
# Write N keys to the datastore then measure 
# time needed for a single random access
# by doing 100 random reads and taking the average

import bitcask
import time
import random
import os 
from statistics import mean, stdev

N_ITER = [10**i for i in range(1, 6)] 

for N in N_ITER:
    datastore = bitcask.BitCaskDataStore("test.db")

    # populate datastore with keys
    for i in range(N):
        datastore.put(f"key{i}", f"value{i}")

    timings = list()

    for i in range(100):
        random_key = random.randint(0, N)
        s = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
        datastore.get(f"key{random_key}")
        e = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)

        timings.append((e - s)/1e9)

    datastore.close()

    print(f"N = {N}, Avg: {mean(timings):.3e} s, Stdev: {stdev(timings):.3e}")

    if os.path.exists("test.db"):
        os.remove("test.db")


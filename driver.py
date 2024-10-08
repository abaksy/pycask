# Driver program for bitcask datastore

import bitcask
import time
import random
N_ITER = [10**i for i in range(1, 6)] 

for N in N_ITER:
    datastore = bitcask.BitCaskDataStore()

    for i in range(N):
        datastore.put(f"key{i}", f"value{i}")

    random_key = random.randint(0, N)
    s = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
    datastore.get(f"key{random_key}")
    e = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)

    print(f"N: {N} time = {(e - s)/1e9} s")

    datastore.close()
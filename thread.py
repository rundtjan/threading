from threading import Thread
import time
import numpy as np
import random
 
# function to create threads
def threaded_function(arg, two):
    two[:arg+1].sum()
 
 
if __name__ == "__main__":
    maxN = 1000
    time_samples = []
    numArr = np.random.randint(1, 10001, maxN)
    for _ in range(1001):
        start = time.time()
        n = random.randint(1,maxN)
        thread = Thread(target = threaded_function, args = (n, numArr))
        thread.start()
        thread.join()
        end = time.time()
        time_samples.append(end-start)

    samples = np.array(time_samples)
    print("Max value:")
    print(samples.max())
    print("Min value:")
    print(samples.min())
    print("Average:")
    print(samples.mean())
    print("Standard deviation:")
    print(samples.std())

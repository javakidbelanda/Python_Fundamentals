
import numpy as np
import time

# Python list

import random
import statistics

# parameters
mean = 15000
std_dev = 2000
size = 1000

# generate normal distribution data
normal_data = []

for _ in range(size):
    value = random.gauss(mean, std_dev)
    normal_data.append(value)

# calculate statistics
mean_result = statistics.mean(normal_data)
std_result = statistics.stdev(normal_data)

print("Mean:", mean_result)
print("Std Dev:", std_result)

# NumPy Numpy Numpy Numpy Numpy
normal_data = np.random.normal(
    loc = 15000, # mean
    scale = 2000, # std
    size = 1000000  # number of samples
)

print("Mean", np.mean(normal_data))
print("Std", np.std(normal_data))






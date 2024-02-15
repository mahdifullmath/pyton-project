import numpy as np
import time


def add_arrays_serial(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def add_arrays_vectorized(a, b):
    return np.add(a, b)


size_n = 10000000
a = np.random.rand(size_n)
b = np.random.rand(size_n)


start_time = time.time()
add_arrays_serial(a, b)
end_time = time.time()
duration_serial = (end_time - start_time)*1000
print(f"Serial implementation time: {duration_serial} ms")

start_time = time.time()
add_arrays_vectorized(a, b)
end_time = time.time()
duration_vectorized = (end_time - start_time)*1000 
print(f"Vectorized implementation time: {duration_vectorized} ms")



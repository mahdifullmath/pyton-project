import numpy as np
import time

def add_arrays_serial(a, b, c):
    for i in range(len(a)):
        c[i] = a[i] + b[i]

def add_arrays_vectorize2(a, b, c):
    i = 0
    while i < len(a) - 7:
        vec_a = np.array([a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5], a[i+6], a[i+7]], dtype=np.float32)
        vec_b = np.array([b[i], b[i+1], b[i+2], b[i+3], b[i+4], b[i+5], b[i+6], b[i+7]], dtype=np.float32)
        vec_c = vec_a + vec_b
        c[i:i+8] = vec_c
        i += 8
    for j in range(i, len(a)):
        c[j] = a[j] + b[j]

def add_arrays_vectorize1(a, b, c):
    i = 0
    while i < len(a) - 3:
        vec_a = np.array([a[i], a[i+1], a[i+2], a[i+3]], dtype=np.float32)
        vec_b = np.array([b[i], b[i+1], b[i+2], b[i+3]], dtype=np.float32)
        vec_c = vec_a + vec_b
        c[i:i+4] = vec_c
        i += 4
    for j in range(i, len(a)):
        c[j] = a[j] + b[j]

size_n = 100000
a = np.random.rand(size_n).astype(np.float32)
b = np.random.rand(size_n).astype(np.float32)
c = np.empty(size_n, dtype=np.float32)

num_iterations = 1000

# Measure performance of serial implementation
start_time = time.time()
for _ in range(num_iterations):
    add_arrays_serial(a, b, c)
end_time = time.time()
duration_serial = (end_time - start_time) * 1000
print(f"Serial implementation time: {duration_serial} ms")

# Measure performance of vectorized implementation
start_time = time.time()
for _ in range(num_iterations):
    add_arrays_vectorize1(a, b, c)
end_time = time.time()
duration_vectorize1 = (end_time - start_time) * 1000
print(f"Vectorized_1 implementation time: {duration_vectorize1} ms")

# Measure performance of vectorized implementation
start_time = time.time()
for _ in range(num_iterations):
    add_arrays_vectorize2(a, b, c)
end_time = time.time()
duration_vectorize2 = (end_time - start_time) * 1000
print(f"Vectorized_2 implementation time: {duration_vectorize2} ms")

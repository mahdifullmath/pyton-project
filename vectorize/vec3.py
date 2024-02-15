

import numpy as np
import time
import ctypes

# Load the SIMD library
libc = ctypes.CDLL(r'C:\Users\mahdi\Desktop\cpp\vec2\simd_operations.dll')
# Assuming the library supports 128-bit vectorization
__m128 = type('__m128', (ctypes.Structure,), {'_fields_': [('m128_f32', ctypes.c_float * 4)]})

def add_arrays_serial(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def add_arrays_vectorized(a, b):
    return np.add(a, b)


# Function to add arrays using 128-bit vectorization


size_n = 10000000
a = np.random.rand(size_n).astype(np.float32)
b = np.random.rand(size_n).astype(np.float32)
result = np.empty(size_n, dtype=np.float32)

# Call the 128-bit SIMD function
start_time = time.time()
libc.add_arrays_128bit(a.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                      b.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                      result.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                      size_n)
end_time = time.time()
duration_128bit = (end_time - start_time) * 1000
print(f"128-bit SIMD implementation time: {duration_128bit} ms")
start_time = time.time()
add_arrays_serial(a, b)
end_time = time.time()
duration_serial = (end_time - start_time) * 1000
print(f"Serial implementation time: {duration_serial} ms")

start_time = time.time()
add_arrays_vectorized(a, b)
end_time = time.time()
duration_vectorized = (end_time - start_time) * 1000
print(f"Vectorized implementation time: {duration_vectorized} ms")





# Define the 256-bit vector type
__m256 = type('__m256', (ctypes.Structure,), {'_fields_': [('m256_f32', ctypes.c_float * 8)]})

# Define the argument and return types for the 256-bit SIMD function
libc.add_arrays_256bit.argtypes = [ctypes.POINTER(__m256), 
                                   ctypes.POINTER(__m256), 
                                   ctypes.POINTER(__m256), 
                                   ctypes.c_int]
libc.add_arrays_256bit.restype = None

# Call the 256-bit SIMD function
size_n = 10000000
a = np.random.rand(size_n).astype(np.float32)
b = np.random.rand(size_n).astype(np.float32)
result = np.empty(size_n, dtype=np.float32)

start_time = time.time()
# Assuming the function in the shared library is named add_arrays_256bit
libc.add_arrays_256bit(
    (__m256 * (size_n // 8))( *((__m256)(*a[i:i+8]) for i in range(0, size_n, 8))),
    (__m256 * (size_n // 8))( *((__m256)(*b[i:i+8]) for i in range(0, size_n, 8))),
    (__m256 * (size_n // 8))( *((__m256)() for _ in range(size_n // 8))),
    size_n
)
end_time = time.time()
duration_256bit = (end_time - start_time) * 1000
print(f"256-bit SIMD implementation time: {duration_256bit} ms")

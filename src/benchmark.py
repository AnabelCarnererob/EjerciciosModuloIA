import numpy as np
import time
import math
import cProfile
import pstats
import io

# Generate a large array: 10 million random numbers between 0 and 1
N = 1_000
print(f"Generating array of {N} elements...")

# For pure Python: list of floats
python_array = np.random.rand(N).tolist()  # Use numpy to generate quickly, then to list

# For NumPy: numpy array
numpy_array = np.array(python_array)

# Operation: sum(sin(x) + x**2) for each x in array

# Version A: Pure Python loop
def python_loop_version(arr):
    total = 0.0
    for x in arr:
        total += math.sin(x) + x**2
    return total

# Version B: NumPy vectorized
def numpy_vectorized_version(arr):
    return np.sum(np.sin(arr) + arr**2)

# Timing function
def time_function(func, arr, runs=3):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        result = func(arr)
        end = time.perf_counter()
        times.append(end - start)
    average = sum(times) / runs
    return average, result

# Run benchmarks
print("Running Python loop version...")
python_avg_time, python_result = time_function(python_loop_version, python_array)

print("Running NumPy vectorized version...")
numpy_avg_time, numpy_result = time_function(numpy_vectorized_version, numpy_array)

# Check if results match (approximately)
assert abs(python_result - numpy_result) < 1e-6, "Results do not match!"

print(f"Python loop average time: {python_avg_time:.4f} seconds")
print(f"NumPy vectorized average time: {numpy_avg_time:.4f} seconds")
ratio = python_avg_time / numpy_avg_time
print(f"Ratio of improvement: {ratio:.2f}x faster with NumPy")

# Optional: Profiling with cProfile
def profile_function(func, arr):
    pr = cProfile.Profile()
    pr.enable()
    func(arr)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(10)  # Top 10 lines
    return s.getvalue()

print("\nProfiling Python loop version...")
python_profile = profile_function(python_loop_version, python_array)
print(python_profile)

print("Profiling NumPy vectorized version...")
numpy_profile = profile_function(numpy_vectorized_version, numpy_array)
print(numpy_profile)
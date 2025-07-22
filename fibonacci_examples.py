#!/usr/bin/env python3
"""
Examples of using the Fibonacci functions
"""

from fibonacci import (
    fibonacci_iterative, 
    fibonacci_recursive, 
    fibonacci_memoized, 
    fibonacci_generator,
    fibonacci_nth,
    is_fibonacci_number
)

# Example 1: Generate first 15 Fibonacci numbers
print("Example 1: First 15 Fibonacci numbers")
fib_15 = fibonacci_iterative(15)
print(fib_15)

# Example 2: Get the 20th Fibonacci number efficiently
print(f"\nExample 2: The 20th Fibonacci number is: {fibonacci_nth(20, 'memoized')}")

# Example 3: Use generator for memory efficiency
print("\nExample 3: Using generator for first 8 numbers")
for i, fib_num in enumerate(fibonacci_generator(8)):
    print(f"F({i}) = {fib_num}")

# Example 4: Check if numbers are Fibonacci numbers
print("\nExample 4: Checking Fibonacci numbers")
test_nums = [55, 56, 89, 90, 144]
for num in test_nums:
    result = "is" if is_fibonacci_number(num) else "is not"
    print(f"{num} {result} a Fibonacci number")

# Example 5: Performance comparison (be careful with recursive for large n)
print("\nExample 5: Performance comparison for F(30)")
import time

# Iterative
start = time.time()
result_iter = fibonacci_nth(30, 'iterative')
time_iter = time.time() - start

# Memoized
start = time.time()
result_memo = fibonacci_nth(30, 'memoized')
time_memo = time.time() - start

print(f"Iterative: {result_iter} (Time: {time_iter:.6f}s)")
print(f"Memoized:  {result_memo} (Time: {time_memo:.6f}s)")

# Note: Recursive approach would be too slow for F(30)
print("Note: Pure recursive approach would be too slow for F(30)")

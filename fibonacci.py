#!/usr/bin/env python3
"""
Fibonacci Series Generator

This module provides multiple implementations to generate Fibonacci numbers:
1. Iterative approach (most efficient)
2. Recursive approach (simple but inefficient for large numbers)
3. Memoized recursive approach (efficient recursive solution)
4. Generator function (memory efficient for sequences)
"""


def fibonacci_iterative(n):
    """
    Generate the first n Fibonacci numbers using iterative approach.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: List of first n Fibonacci numbers
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursive approach.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(2^n) - Very inefficient for large n
    Space Complexity: O(n) - Due to recursion stack
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoized recursion.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        memo (dict): Memoization dictionary (used internally)
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_generator(n):
    """
    Generate Fibonacci numbers using a generator function.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number in sequence
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_nth(n, method='iterative'):
    """
    Get the nth Fibonacci number using specified method.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        method (str): Method to use ('iterative', 'recursive', 'memoized')
        
    Returns:
        int: The nth Fibonacci number
    """
    if method == 'iterative':
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    elif method == 'recursive':
        return fibonacci_recursive(n)
    elif method == 'memoized':
        return fibonacci_memoized(n)
    else:
        raise ValueError("Method must be 'iterative', 'recursive', or 'memoized'")


def is_fibonacci_number(num):
    """
    Check if a given number is a Fibonacci number.
    
    A positive integer is a Fibonacci number if and only if one of
    (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    Args:
        num (int): Number to check
        
    Returns:
        bool: True if num is a Fibonacci number, False otherwise
    """
    import math
    
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


def main():
    """
    Demonstrate different Fibonacci implementations.
    """
    print("Fibonacci Series Generator")
    print("=" * 40)
    
    # Get user input
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    print(f"\nGenerating first {n} Fibonacci numbers:\n")
    
    # Iterative approach
    print("1. Iterative approach:")
    fib_iter = fibonacci_iterative(n)
    print(f"   {fib_iter}")
    
    # Generator approach
    print("\n2. Generator approach:")
    fib_gen = list(fibonacci_generator(n))
    print(f"   {fib_gen}")
    
    # Show individual calculations for smaller numbers
    if n <= 10:
        print(f"\n3. Individual Fibonacci numbers (0 to {n-1}):")
        for i in range(n):
            fib_num = fibonacci_nth(i, 'memoized')
            print(f"   F({i}) = {fib_num}")
    
    # Demonstrate Fibonacci number checking
    print(f"\n4. Checking if some numbers are Fibonacci numbers:")
    test_numbers = [1, 2, 3, 5, 8, 13, 20, 21, 34]
    for num in test_numbers:
        is_fib = is_fibonacci_number(num)
        print(f"   {num} is {'a' if is_fib else 'not a'} Fibonacci number")


if __name__ == "__main__":
    main()

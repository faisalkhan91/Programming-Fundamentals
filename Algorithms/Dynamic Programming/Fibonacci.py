"""
Implementation of fibonacci sequence solution using memoization or caching. We intend to increase efficiency by storing
the calculated value for each index in the fibonacci sequence. This will have added overhead for memory.
"""


# Function definitions

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memoized():
    cached = {}

    def fib(n):
        if n in cached:
            return cached[n]
        elif n < 2:
            cached[n] = n
            return n

    return fib


# Declarations

given_index = 7
print("Traditional recursive Fibonacci sequence solution:", fibonacci(given_index))

fib_calculation = fibonacci_memoized()
print("Memoized recursive Fibonacci sequence solution:", fib_calculation(given_index))

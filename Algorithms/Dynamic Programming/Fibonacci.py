"""
Implementation of fibonacci sequence solution using memoization or caching. We intend to increase efficiency by storing
the calculated value for each index in the fibonacci sequence. This will have added overhead for memory.
"""


# Function definitions

def fibonacci(n, e):
    e[0] += 1
    if n < 2:
        return n
    return fibonacci(n-1, e) + fibonacci(n-2, e), e


def fibonacci_memoized():
    cached = {}
    count = [0]

    def fib(n):
        count[0] += 1
        if n in cached:
            return cached[n]
        elif n < 2:
            cached[n] = n
            return n
        elif n >= 2:
            cached[n] = fib(n-1) + fib(n-2)
            return cached[n]

    return fib, count


# Declarations

given_index = 8

result = fibonacci(given_index, [0])
print("Traditional recursive Fibonacci sequence solution:", result, "Execution:", result)

fib_calculation, c = fibonacci_memoized()
print("Memoized recursive Fibonacci sequence solution:", fib_calculation(given_index), "Execution:", c[0])

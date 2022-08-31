"""
Implementation of fibonacci series problem using memoization or caching.
"""


# Function definitions

def fibonacci(n):
    
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


# Declarations

given_index = 7
print(fibonacci(given_index))

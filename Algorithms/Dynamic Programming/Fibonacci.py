"""
Implementation of fibonacci sequence solution using memoization or caching. We intend to increase efficiency by storing
the calculated value for each index in the fibonacci sequence. This will have added overhead for memory.
"""


# Function definitions

# Implementation of traditional Fibonacci sequence solution using recursion.
def fibonacci(n):
    global calculations  # global variable to store value out of the scope of the method.
    calculations += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Call and return the fibonacci sequence using recursion.


# Implementation of the memoized version of the Fibonacci sequence.
def fibonacci_memoized():
    cached = {}  # Hash Map or a Dictionary to store the calculated information for an index.
    count = [0]  # To count the number of executions.

    # Nested method to perform the calculations locally.
    def fib(n):
        count[0] += 1
        if n in cached:  # If the value for the sequence is there, return the value.
            return cached[n]
        elif n < 2:  # Base case, if the value is less than 2 return n.
            cached[n] = n
            return n
        else:
            cached[n] = fib(n-1) + fib(n-2)  # Recursively calculate the values at the index and store them.
            return cached[n]  # Return the cached values.

    return fib, count  # Call the fib function and return value of fib and count.


# Declarations

given_index = 35
global calculations
calculations = 0
print("Traditional recursive Fibonacci sequence solution:", fibonacci(given_index), "Executions:", calculations)

fib_calculation, c = fibonacci_memoized()  # Initialize the method.
print("Memoized recursive Fibonacci sequence solution:", fib_calculation(given_index), "Execution:", c[0])

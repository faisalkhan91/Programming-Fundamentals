"""
Implementation of fibonacci series problem using memoization or caching.
"""


# Function definitions

def fibonacci(index):

    cached = 
    if index < 2:
        return index


    return fibonacci(index-1) + fibonacci(index-2)

# Declarations

GIVEN_INDEX = 7
print(fibonacci(GIVEN_INDEX))

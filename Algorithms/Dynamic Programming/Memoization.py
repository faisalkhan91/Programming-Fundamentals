"""
Implementation of an example to demonstrate dynamic programming in python. This improves efficiency of the code by
storing the calculated value at the expense of space complexity.
"""


# Function Definition

# Implementation of add a number to 80 method. This is a non memoized approach that will calculate the solution
# everytime it runs.
def add_to_80(n):
    return n + 80


# This method is the memoized version of the above method. Here we use a hash table to cache the solution so that if
# the method is run for the same number it will return from the cache rather than calculating again.
def add_to_80_memoized():
    cached = {}  # Hash table to store the information in the cache.

    # Nested method using closure functionality in python.
    def add(n):
        if n in cached:  # If the number is in cache, it will return the number from memory.
            return cached[n]
        else:  # If the number is non in cache it will run the solution and store it in cache.
            cached[n] = n + 80
            return cached[n]
    return add


# Declaration

number = 10

print("Non memoized method:", add_to_80(number))
add_number = add_to_80_memoized()  # Initialize the nested function so that it can store value by closure.
print("Memoized method:", add_number(number))

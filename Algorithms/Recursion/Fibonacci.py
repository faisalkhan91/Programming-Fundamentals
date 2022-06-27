"""
Given a number N return the index value of the Fibonacci sequence, where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is such that each value is the sum of the 2 previous values, that means that for N=5 → 2+3.

For example, if we have a method name fibonacci_recursive,
fibonacci_recursive(6) should return 8, i.e. sum of the numbers in the sequence until index 6. Likewise,
fibonacci_recursive(7) should return 13.

Here we will use recursion and iteration separately to implement the solution. Also, note that the recursive solution
has a time complexity of BigO(2^n).
"""


# Function definition

# Initial attempt to code a method to calculate fibonacci sequence recursively. Time complexity is O(2^n).
def fibonacci_recursive_initial(n):
    if n < 1:  # If the index number is less than 1, i.e. 0 return 0
        return 0
    elif n == 1:  # If the index number is equal to 1, return 1.
        return 1
    return fibonacci_recursive_initial(n-1) + fibonacci_recursive_initial(n-2)  # Add the numbers.


# Andrei's solution for finding fibonacci sequence at a given index. Time complexity is BigO(2^n), i.e. exponential
# time complexity.
def fibonacci_recursive(n):
    if n < 2:  # If n is 0, return 0 and if n is 1, return 1.
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)  # Generate fibonacci for n-1 and n-2 and add it.


# Initial attempt to write a solution to fibonacci sequence problem using iteration.
def fibonacci_iterative_initial(n):
    first = 0  # First number in the sequence.
    second = 1  # Second number in the sequence.
    fibonacci = 0  # Variable to store the value.

    for i in range(1, n):  # Iterate n number of times.
        fibonacci = first + second  # Calculate the fibonacci sequence.
        first = second  # Make the first number as the second or next number in sequence.
        second = fibonacci  # Make the second number as the new number in the sequence.

    return fibonacci


# Implementation of Andrei's iterative method to solve the fibonacci sequence.
def fibonacci_iterative(n):
    fibonacci = [0, 1]  # Store the first 2 numbers in the sequence in the array.
    for i in range(2, n+1):  # Iterate from 2 to n+1 times since the addition below is trailing by 1.
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    return fibonacci[n]


# Declaration
index = 10
print(fibonacci_iterative(index))
print(fibonacci_recursive(index))

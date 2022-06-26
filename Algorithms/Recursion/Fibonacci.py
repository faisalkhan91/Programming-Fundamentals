"""
Given a number N return the index value of the Fibonacci sequence, where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is such that each value is the sum of the 2 previous values, that means that for N=5 → 2+3.

For example, if we have a method name fibonacci_recursive,
fibonacci_recursive(6) should return 8, i.e. sum of the numbers in the sequence until index 6. Likewise,
fibonacci_recursive(7) should return 13.

Here we will use recursion and iteration separately to implement the solution.
"""


# Function definition

def fibonacci_recursive(number_input):
    if number_input < 1:
        return 0
    elif number_input == 1:
        return 1
    return fibonacci_recursive(number_input-1) + fibonacci_recursive(number_input-2)


def fibonacci_iterative(number_input):
    first = 0
    second = 1
    fibonacci = 0

    for i in range(1, number_input):
        fibonacci = first + second
        first = second
        second = fibonacci

    return fibonacci


# Declaration
number = 10
print(fibonacci_iterative(number))
print(fibonacci_recursive(number))

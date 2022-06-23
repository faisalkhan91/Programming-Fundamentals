"""
Write two functions that finds the factorial of any number. One should use recursion, and the other iteration by using a
for loop.

Factorial:
5! = 5*4*3*2*1 ~ 120
Given a number, a factorial is the product of that number with every whole number till 1.
"""


# Function definitions

# Initial attempt to write a method to calculate factorial using recursion
def find_factorial_recursively_initial(input_number):
    factorial = 1
    if input_number > 0:
        factorial = factorial * input_number
    input_number -= 1
    return find_factorial_iteratively(factorial)


# Andrei's method to calculate the factorial using recursion. Time complexity using recursion to find the factorial is
# BigO(n) since the function is being called n times.
def find_factorial_recursively(input_number):
    if input_number < 1:  # Base case, will return the last function call in the stack to indicate the end of the calls.
        return
    return input_number * find_factorial_iteratively(input_number-1)


# Time complexity is BigO(n) due to the loop.
def find_factorial_iteratively(input_number):
    factorial = 1  # Declare a data type to store the factorial.
    for i in range(2, input_number+1):  # Loop from 2 as 1*1=1 and will make the loop more efficient.
        factorial = factorial * i  # Using the factorial definition above.
    return factorial


# Declarations
number = 5
print(find_factorial_recursively(number))  # Print recursive function output.
print(find_factorial_iteratively(number))  # Print iterative function output.

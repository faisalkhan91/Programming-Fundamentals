"""
Implementation of fibonacci sequence solution using bottom-up approach. We intend to find the solution by solving and
storing all the problems in a natural order until the desired result is found.
"""


# Function definitions


# Implementation of the bottom up version of the Fibonacci sequence.
def fibonacci_bottom_up(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()


# Declarations

given_index = 35
print("Bottom up Fibonacci sequence solution:", fibonacci_bottom_up(given_index))

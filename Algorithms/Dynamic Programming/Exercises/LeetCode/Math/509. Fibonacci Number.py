"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
Check the fibonacci.py file for explanation.
"""


class Solution:
    def fib(self, n: int) -> int:
        cache = {}  # To store the already calculated values.

        # Nested function.
        def fib_calculator(n):
            if n in cache:
                return cache[n]
            elif n < 2:
                cache[n] = n
                return n
            else:
                cache[n] = fib_calculator(n-1) + fib_calculator(n-2)
                return cache[n]
        return fib_calculator(n)


n = 10
execute = Solution()
print(execute.fib(n))

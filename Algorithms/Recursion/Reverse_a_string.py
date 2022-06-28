"""
Implement a function that reverses a string using iteration...and then recursion!

For example, given a string 'hello', the function should output 'olleh'.
"""


# Function definition

# Method to reverse a string using recursion.
def reverse_string_recursion(to_reverse):
    # Check if the end of the string is reached, can be done other way is to check the length of the string is 0.
    if to_reverse == "":
        return to_reverse  # Will return "" at the end.
    else:
        return reverse_string_recursion(to_reverse[1:]) + to_reverse[0]  # Keep doing recursion until end of string.


# Method to reverse a string using iteration. Time and Space complexity is O(n).
def reverse_string_iteration(to_reverse):
    reversed_string = []
    for i in reversed(list(to_reverse)):
        reversed_string.append(i)
    return ''.join(reversed_string)


# Declaration
string = 'This is so cool!'
print(reverse_string_iteration(string))
print(reverse_string_recursion(string))

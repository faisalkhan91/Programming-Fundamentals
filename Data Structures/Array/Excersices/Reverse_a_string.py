"""
Create a function that reverses a string.
For example string 'Hi My name is Faisal' should be 'lasiaF si eman yM iH'
"""


# Function Definition

# First attempt to reverse a string.
def reverse_string(string_input):
    split_string = list(string_input)
    reversed_string = []
    for i in reversed(range(len(split_string))):
        reversed_string.append(split_string[i])
    print(reversed_string)


# Reverse a string using Andrei's solution to reverse a string exercise.
def reverse_string_2(string_input):
    # Check the input for errors, What if the string is a number or undefined?
    if type(string_input) != str or len(string_input) < 2:
        return 'Please enter valid input!'

    backwards = []
    total_items = len(string_input) - 1

    for i in range(total_items, -1, -1):
        backwards.append(string_input[i])
    print(backwards)

    return ''.join(backwards)


# Declarations
to_reverse = 'hello'
# reverse_string(to_reverse)
string = reverse_string_2(to_reverse)

print(string)

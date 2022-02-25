"""
Create a function that reverses a string.
For example string 'Hi My name is Faisal' should be 'lasiaF si eman yM iH'
"""


# Function Definition
def reverse_string(string_input):
    split_string = list(string_input)

    reversed_string = []

    for i in reversed(range(len(split_string))):
        reversed_string.append(split_string[i])

    print(reversed_string)


# Declarations
to_reverse = 'hello'
reverse_string(to_reverse)

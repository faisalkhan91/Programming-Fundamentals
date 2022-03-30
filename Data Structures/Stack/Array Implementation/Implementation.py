"""
Implementation of a Stack Data Structure in python using Array. In build array data structure in python called lists is
used to build the stack.
"""

# Class definition


# This is the stack class that defines the methods to manipulate the data structure.
class Stack:
    def __init__(self):
        self.array = []  # Initialize the array data structure

    def __str__(self):
        return str(self.__dict__)

    # Method to check and return the value of the top element from the stack.
    def peek(self):
        if len(self.array) == 0:  # If the stack is empty.
            print("Stack is empty.")
        else:
            return self.array[len(self.array)-1]  # Return last element in the stack.

    # Method to add a new element at the top of the stack.
    def push(self, value):
        self.array.append(value)  # Push value to the array using the built-in append function.
        return self

    # Method to remove the top element from the stack.
    def pop(self):
        self.array.pop()  # Pop the element using the built-in pop function.
        return self

    # Method to check if the stack is empty.
    def is_empty(self):
        if len(self.array) == 0:
            print("Stack is empty.")
        else:
            print(len(self.array), "elements are in the stack.")

    # Method to print the stack.
    def display_stack(self):
        print("***Stack***")
        # Loop to the stack to print all the elements.
        for i in self.array:
            print(i)
            print("↓")
        print("None")
        print("Top of the stack: ", self.array[len(self.array)-1])
        print("Bottom of the stack: ", self.array[0])
        print("Length of the stack: ", len(self.array))


# Main
my_stack = Stack()
my_stack.peek()
my_stack.push("Google")
my_stack.push("LinkedIn")
my_stack.push("Reddit")
print(my_stack.peek())
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.is_empty()
my_stack.display_stack()

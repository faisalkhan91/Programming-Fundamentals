"""
Implementation of a Stack Data Structure in python using Array. This was my attempt using dictionary to simulate an
array data structure.
"""

# Class definition


# This is the stack class that defines the methods to manipulate the data structure.
class Stack:
    def __init__(self):
        self.top = None  # Initialize the top pointer to store the top element.
        self.bottom = None  # Initialize the bottom pointer to store the bottom element.
        self.data = {}
        self.length = 0  # Initialize the length of the array.

    def __str__(self):
        return str(self.__dict__)

    # Method to check and return the value of the top element from the stack.
    def peek(self):
        # If the stack is not empty, return the top element in the stack.
        if self.top is not None:
            print("The top element is: ", self.top)
            return self.top
        else:
            print("Stack is empty.")

    # Method to add a new element at the top of the stack.
    def push(self, value):
        self.data[self.length] = value
        # If the stack is empty set both the top and bottom to the new element.
        if self.length == 0:
            self.top = self.data[self.length]
            self.bottom = self.data[self.length]
        else:
            self.top = self.data[self.length]
        self.length += 1  # Increase length by 1.
        return self

    # Method to remove the top element from the stack.
    def pop(self):
        # If the stack is empty return None.
        if self.top is None:
            print("Stack is empty.")
            return None
        # If the item to pop is the last element in the stack make the bottom node as None.
        if self.top == self.bottom:
            self.bottom = None
        # Move the top to the next element.
        self.top = self.data[self.length-2]
        del self.data[self.length-1]
        self.length -= 1  # Decrease length by 1.

    # Method to check if the stack is empty.
    def is_empty(self):
        if self.length == 0:
            print("Stack is empty.")
        else:
            print(self.length, " elements are in the stack.")

    # Method to print the stack.
    def display_stack(self):
        print("***Stack***")
        # Loop to the stack to print all the elements.
        for i in self.data:
            print(self.data[i])
            print("↓")
        print("None")
        print("Top of the stack: ", self.top)
        print("Bottom of the stack: ", self.bottom)
        print("Length of the stack: ", self.length)


# Main
my_stack = Stack()
my_stack.peek()
my_stack.push("Google")
my_stack.push("LinkedIn")
my_stack.push("Reddit")
my_stack.peek()
my_stack.pop()
my_stack.display_stack()

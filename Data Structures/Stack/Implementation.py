"""
Implementation of a Stack Data Structure in python using Linked List.
"""

# Class definition


# This is the node class that holds data and a pointer to the next node.
class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the node.
        self.next = None  # Store the pointer to the next node.

    def __str__(self):
        return str(self.data)


# This is the stack class that defines the methods to manipulate the data structure.
class Stack:
    def __init__(self):
        self.top = None  # Initialize the top pointer to store the top node.
        self.bottom = None  # Initialize the bottom pointer to store the bottom node.
        self.length = 0  # Initialize the length of the node.

    def __str__(self):
        return str(self.__dict__)

    # Method to check and return the value of the top node from the stack.
    def peek(self):
        # If the stack is not empty, return the top node in the stack.
        if self.top is not None:
            print("The top node is: ", self.top)
            return self.top
        else:
            print("Stack is empty.")

    # Method to add a new node at the top of the stack.
    def push(self, value):
        new_node = Node(value)  # Create a new node.
        # If the stack is empty set both the top and bottom to the new node.
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top  # Set the new node pointer to the current top node.
            self.top = new_node  # Make the new node the top node.
        self.length += 1  # Increase length by 1.
        return self

    # Method to remove the top node from the stack.
    def pop(self):
        # If the stack is empty return None.
        if self.top is None:
            print("Stack is empty.")
            return None
        # If the item to pop is the last element in the stack make the bottom node as None.
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next  # Move the top to the next node. If it is the last node, next will be None by default.
        self.length -= 1  # Decrease length by 1.

    # Method to check if the stack is empty.
    def is_empty(self):
        if self.length == 0:
            print("Stack is empty.")
        else:
            print(self.length, " elements are in the stack.")

    # Method to print the stack.
    def display_stack(self):
        current_node = self.top
        print("***Stack***")
        # Loop to the stack to print all the elements.
        while current_node is not None:
            print(current_node.data)
            print("↓")
            current_node = current_node.next
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

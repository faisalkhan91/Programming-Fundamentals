"""
Implementation of a Stack Data Structure in python using Linked List.
"""

# Class definition


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    # Method to check and return the value of the top node from the stack.
    def peek(self):
        if self.top is not None:
            return self.top
        else:
            print("Stack is empty.")

    # Method to add a new node at the top of the stack.
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Method to remove the top node from the stack.
    def pop(self):
        self.top = self.top.next

    # Method to check if the stack is empty.
    def is_empty(self):
        if self.length == 0:
            print("Stack is empty.")
        else:
            print(self.length, " elements are in the stack.")


# Main
my_stack = Stack()

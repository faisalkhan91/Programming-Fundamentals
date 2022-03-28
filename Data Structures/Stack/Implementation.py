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

    def peek(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass


# Main
my_stack = Stack()


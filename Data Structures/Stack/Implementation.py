"""
Implementation of a Stack Data Structure in python using Linked List.
"""

# Class definition


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

# Main


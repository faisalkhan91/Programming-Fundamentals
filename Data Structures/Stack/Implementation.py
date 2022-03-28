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
            print("The top node is: ", self.top)
            return self.top
        else:
            print("Stack is empty.")

    # Method to add a new node at the top of the stack.
    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return self

    # Method to remove the top node from the stack.
    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        self.top = self.top.next
        self.length -= 1

    # Method to check if the stack is empty.
    def is_empty(self):
        if self.length == 0:
            print("Stack is empty.")
        else:
            print(self.length, " elements are in the stack.")

    def display_stack(self):
        current_node = self.top
        print("***Stack***")
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

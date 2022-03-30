"""
Implementation of the Queue Data Structure in python using Linked List. Using Array to implement queue is not
recommended.
"""


# Class definition

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        new_node.next = self.first
        self.first = new_node
        self.length += 1

    def dequeue(self):
        self.first = self.first.next

    def print_queue(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# Declaration
my_queue = Queue

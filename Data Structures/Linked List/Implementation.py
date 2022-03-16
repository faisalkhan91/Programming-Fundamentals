"""
Implementation of Linked List Data Structure in python.
"""


# Classes

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __str__(self):
        return str(self.head)

    def append(self, value):
        self.head = Node(value, self.head)
        self.length += 1


# Declaration
linked = LinkedList()
linked.append(20)
print(linked)


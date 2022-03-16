"""
Implementation of Linked List Data Structure in python.
"""


# Function Definition

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    


# Declaration
linked = LinkedList()
print(linked)

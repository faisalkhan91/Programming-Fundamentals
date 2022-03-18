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
        self.head = None
        self.tail = self.head
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                self.tail = current_node.next
                self.length += 1
                break
            current_node = current_node.next

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                self.tail = current_node.next
                self.length += 1
                break
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "->",)
            current_node = current_node.next
        print("None")


# Declaration
linked = LinkedList()
linked.append(20)
linked.append(30)
linked.append(15)
linked.append(10)
linked.print_list()
print(linked.tail)

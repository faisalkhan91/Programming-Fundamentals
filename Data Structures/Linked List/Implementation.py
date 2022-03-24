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

    # Method to append (add at the end) node to the linked list. Time complexity is O(1).
    def append(self, value):
        new_node = Node(value)  # Take the value and create a new node.
        # If linked list doesn't have any node, add the first node as the head.
        if self.head is None:
            self.head = new_node
            self.tail = self.head  # Tail will be same as head since there is only one node.
            self.length += 1  # Increase the length.
            # return  # Only used when we were using the while loop traversal below.
        else:
            self.tail.next = new_node  # Point the current tail node to the new node.
            self.tail = new_node  # Make the new node the tail.
            self.length += 1  # Increment tail by 1.
        '''
        # The while loop below traverses the linked list to find the tail node and add a new node at the end.
        # The time complexity of this is O(n), therefore tail pointer is being used to track the last node so as to
        # make adding the new node O(1).
        current_node = self.head  # Set the current node to the head node.
        while True:
            if current_node.next is None:  # If current node pointer is None, i.e. the last node in the list is found.
                current_node.next = new_node  # Set the pointer of the last node to the new node.
                self.tail = current_node.next  # Set the tail as the pointer to the new node.
                self.length += 1  # Increment length by 1.
                break
            current_node = current_node.next  # Move to the next node in the list.
        '''

    # Method to add a node at the beginning of the linked list.
    def prepend(self, value):
        new_node = Node(value)  # Create a node with the given value.
        # If there is no node in the list, add the node to the list.
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head  # Set the pointer of the new node to point at the current head node.
            self.head = new_node  # Set the new node as the head node.
            self.length += 1  # Increment length by 1.

    def insert(self, value, index):
        new_node = Node(value)
        current_node = self.head
        for i in range(index):
            if i == index-2:
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next
        return

    def delete(self, value):
        if self.head is None:
            print("Cannot perform delete since linked list is empty.")
            return
        elif self.head == value:
            current_node = self.head
            self.head = current_node.next
            del current_node
        elif self.tail == value:
            current_node = self.tail
        current_node = self.head
        for i in range(self.length):
            if current_node.next == value:
                pass
            print(current_node.next)
            current_node = current_node.next

    # Method to print the values in the linked list.
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "->", end=" ")  # Print list nodes in the same line.
            current_node = current_node.next
        print("None")


# Declaration
linked = LinkedList()
linked.append(20)
linked.append(30)
linked.append(15)
linked.append(10)
linked.prepend(7)
linked.prepend(100)
linked.prepend(1)
# linked.delete(20)
linked.insert(4, 4)
linked.print_list()
# print(linked.tail)

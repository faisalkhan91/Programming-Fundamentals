"""
Implementation of the Queue Data Structure in python using Linked List. Using Array to implement queue is not
recommended.
"""


# Class definition

# This is the node class that holds data and a pointer to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# This class implements the queue data structure and its corresponding methods.
class Queue:
    def __init__(self):
        self.first = None  # Initialize the pointer to store the first node.
        self.last = None  # Initialize the pointer to store the last node.
        self.length = 0  # Initialize the length to 0.

    def __str__(self):
        return str(self.__dict__)

    # Method to check and return the value of the first node from the queue.
    def peek(self):
        if self.length == 0:
            print("Queue is empty.")
        else:
            print(self.first)
            return self.first

    # Method to add a new node at the end of the queue.
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    # Method to remove the first node from the queue.
    def dequeue(self):
        # Check if the stack is empty.
        if not self.first:
            print("Queue is empty.")
            return None
        elif self.first == self.last:  # If there is only one node in the queue set the last node pointer to None.
            self.last = None
        self.first = self.first.next  # Move the first to the next node in the queue.
        self.length -= 1
        return self

    # Method to print the queue.
    def print_queue(self):
        current_node = self.first
        print("***Queue***")
        while current_node is not None:
            print(current_node.data)
            print("↓")
            current_node = current_node.next
        print("None")
        print("First node in the queue: ", self.first)
        print("Last node in the queue: ", self.last)
        print("Length of the queue: ", self.length)


# Declaration
my_queue = Queue()
my_queue.peek()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
my_queue.peek()
my_queue.dequeue()
my_queue.print_queue()

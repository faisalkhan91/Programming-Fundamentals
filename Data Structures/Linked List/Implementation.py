"""
Implementation of Linked List Data Structure in python.
"""


# Classes
# This is the node class to create new node objects which contain the data and the pointer to next node.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Returning data so that when we refer the object of the node it will always return the data in the node.
    # Below we can use current_node same as current_node.data due to changing our return.
    def __str__(self):
        return str(self.data)


# This is the linked list class.
class LinkedList:
    # Default class constructor that initializes the pointers to the head and tail nodes as well as the length.
    def __init__(self):
        self.head = None  # Initially there is no node and the pointer points to None.
        self.tail = self.head  # Head and tail are same when initialized.
        self.length = 0  # Length is 0 as there is no node in the list yet.

    # Return the linked list object in dictionary format.
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

    # This method will insert a node at a given index.
    def insert(self, value, index):
        new_node = Node(value)  # Create a new node object by calling the node class.
        current_node = self.head  # Start from the head.
        # If the value of the index is greater than the length of the list add the new node at the end of the list.
        if index > self.length:
            print("Index out of range. Appending node to the list.")
            self.tail.next = new_node  # Set the current tail node pointer to the new node.
            self.tail = new_node  # Set the new node as the tail.
            self.length += 1  # Increment the length by 1.
        # If the index is 0, set the new node as the head in a similar fashion to prepending a node to the linked list.
        elif index == 0:
            new_node.next = self.head  # Set the pointer of the new node to the current head node.
            self.head = new_node  # Make the new node as the new head.
            self.length += 1  # Increment the length by 1.
        else:
            for i in range(index):  # Traverse the list until the index position.
                if i == index-1:  # When the index position has been reached.
                    new_node.next = current_node.next  # Copy pointer of the node before index position.
                    current_node.next = new_node  # Point the previous node to the new node.
                    self.length += 1  # Increment length by 1.
                current_node = current_node.next
        return

    # This method will delete a node by either accepting value of the node or index position of the node. To specify
    # index 'index=' parameter can be used. By default, value will be accepted.
    def delete(self, value=None, index=None):
        current_node = self.head  # Set the current node to the head node.
        # If the first node is none then the linked list is empty.
        if current_node is None:
            print("Cannot perform delete since linked list is empty.")
        # If the first node matches the value or if the given index is 0, then we remove the node.
        elif current_node.data == value or index == 0:
            self.head = current_node.next  # Make the next node as the head node.
            print(current_node, "has been deleted from the list.")
            del current_node  # Delete the node.
            self.length -= 1
        # If the value is given and the index is none this method will delete node based on the value.
        elif index is None:
            for i in range(self.length-1):
                # If the value has been found.
                if current_node.next.data == value:
                    print(current_node.next, "has been deleted from the list.")
                    current_node.next = current_node.next.next  # Set the pointer from the next node to the node after.
                    # If there is no node at the end, set the tail to the current node.
                    if current_node.next is None:
                        self.tail = current_node
                    del current_node
                    self.length -= 1
                    return
                elif current_node.next is not None:
                    current_node = current_node.next
        # If the value is None and the index is given the following else statement will execute.
        else:
            # Loop until the position of the index.
            for i in range(index):
                # When the index position is reached.
                if i == index-1:
                    print(current_node.next, "has been deleted from the list.")
                    current_node.next = current_node.next.next  # Remove the node at the index position.
                    # If there is no next node, set the current node to tail node.
                    if current_node.next is None:
                        self.tail = current_node
                    del current_node
                    self.length -= 1
                    return
                elif current_node.next is not None:
                    current_node = current_node.next

    # Method to print the values in the linked list.
    def print_list(self):
        current_node = self.head
        counter = 0  # To count the number of nodes in the list.
        while current_node is not None:
            print(current_node.data, "->", end=" ")  # Print list nodes in the same line.
            current_node = current_node.next
            counter = counter + 1
        print("None")
        print("Number of nodes in printed list is: ", counter)
        print("Value of the LENGTH of the list is: ", self.length)
        print("Value of the HEAD node of the list is: ", self.head)
        print("Value of the TAIL node of the list is: ", self.tail)


# Declaration
linked = LinkedList()
linked.append(20)
linked.append(30)
linked.append(15)
linked.append(10)
linked.prepend(7)
linked.prepend(100)
linked.prepend(1)
linked.insert(4, 4)
linked.insert(9, 0)
linked.insert(1000, 1000)
linked.delete(index=2)  # Delete based on the index.
linked.delete(20)  # Delete based on value, the value parameter can be given as 'value='.
linked.print_list()

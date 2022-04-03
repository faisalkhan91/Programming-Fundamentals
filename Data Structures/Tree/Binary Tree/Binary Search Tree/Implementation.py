"""
Implementation of Binary Search Tree data structure in python.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            pass

    def delete(self):
        pass

    def lookup(self):
        pass


# Initialization

my_BST = BinarySearchTree()

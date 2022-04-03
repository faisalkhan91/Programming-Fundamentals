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

    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node.left is not None or current_node.right is not None:
                if new_node.data > current_node.data:
                    current_node = current_node.right
                elif new_node.data < current_node.data:
                    current_node = current_node.left
            if current_node.left is None:
                current_node.left = new_node
            else:
                current_node.right = new_node

    def delete(self):
        pass

    def lookup(self):
        pass

    def print(self):
        pass


# Initialization

my_BST = BinarySearchTree()
my_BST.insert(10)
my_BST.insert(5)
my_BST.insert(3)
my_BST.insert(6)
print(my_BST.root.left.left.data)

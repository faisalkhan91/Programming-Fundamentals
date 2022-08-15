"""
Implementation of Depth First Search algorithm in python.
"""

from Modules.BST_Implementation import *
'''
BST_Implementation is a copy of the Binary Search Tree implementation from the Data Structures section. It has been
modified with a main method that has the operations execute locally so it doesn't run from this file while imported.

The Implementation contains:

Class
- Node : This contains information for each node and its child. This is used as an object in BinarySearchTree class.
- BinarySearchTree : This manipulates each node to create a BST data structure.
    -- Methods --
    --> Insert
    --> Delete
    --> Lookup
    --> Print Tree
    --> Traverse : This method creates a string not similar as to the one we will implement.
'''


# Function Definition

class Traversal(BinarySearchTree):

    def depth_first_search(self):
        current_node = self.root
        result = []

        while


# Initialization

DFS_Traversal = Traversal()

DFS_Traversal.insert(9)
DFS_Traversal.insert(4)
DFS_Traversal.insert(20)
DFS_Traversal.insert(1)
DFS_Traversal.insert(6)
DFS_Traversal.insert(15)
DFS_Traversal.insert(170)
DFS_Traversal.print_tree(DFS_Traversal.root)

print(DFS_Traversal.depth_first_search())


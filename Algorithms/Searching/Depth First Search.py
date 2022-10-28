"""
Implementation of Depth First Search algorithm in python. In this type of traversal all the nodes on one side of the
tree is searched and stored according to the traversal implementation. There are three ways to implement a DFS traversal
method: Inorder, Preorder, Postorder. The node information is stored recursively in a stack.

Time complexity and space complexity of a DFS algorithm depends on the depth of the tree.
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

# This is a class that inherits BinarySearchTree class from the BST_Implementation file.
class Traversal(BinarySearchTree):

    # Implementation of DFS method using inorder traversal.
    def depth_first_search_inorder(self):
        result = []  # List to store the result of the returned stack.
        current_node = self.root  # Root node
        return self.traverse_inorder(current_node, result)

    # Implementation of DFS method using preorder traversal.
    def depth_first_search_preorder(self):
        result = []  # List to store the result of the returned stack.
        current_node = self.root  # Root node
        return self.traverse_preorder(current_node, result)

    # Implementation of DFS method using postorder traversal.
    def depth_first_search_postorder(self):
        result = []  # List to store the result of the returned stack.
        current_node = self.root  # Root node
        return self.traverse_postorder(current_node, result)

    # Method to perform the Inorder traversal using recursion.
    def traverse_inorder(self, node, result):
        if node.left:  # If there is a left node
            self.traverse_inorder(node.left, result)  # Recursive traverse the left node
        result.append(node.data)  # Push the data of the node to the list.
        if node.right:  # If there is a right node
            self.traverse_inorder(node.right, result)  # Recursive traverse the right node
        return result

    # Method to perform the Preorder traversal using recursion.
    def traverse_preorder(self, node, result):
        result.append(node.data)  # Push the data of the node to the list.
        if node.left:  # If there is a left node
            self.traverse_preorder(node.left, result)  # Recursive traverse the left node
        if node.right:  # If there  is a right node
            self.traverse_preorder(node.right, result)  # Recursive traverse the right node
        return result

    # Method to perform the Postorder traversal using recursion.
    def traverse_postorder(self, node, result):
        if node.left:  # If there is a left node
            self.traverse_postorder(node.left, result)  # Recursive traverse the left node
        if node.right:  # If there is a right node
            self.traverse_postorder(node.right, result)  # Recursive traverse the right node
        result.append(node.data)  # Push the data of the node to the list.
        return result


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

print("Inorder traversal:", DFS_Traversal.depth_first_search_inorder())
print("Preorder traversal:", DFS_Traversal.depth_first_search_preorder())
print("Postorder traversal:", DFS_Traversal.depth_first_search_postorder())

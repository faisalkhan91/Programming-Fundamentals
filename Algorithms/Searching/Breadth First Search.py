"""
Implementation of Breadth First Search algorithm in python. Breadth First Search approach searches all the nodes level
by level from left to right starting from the root node. We keep track of all the children of each node visited.

Time complexity is O(n).
"""

# The commented code below is to import from a different directory, but since I have copied this file to Modules which
# is in the same path as this file it won't be needed to use this method.
# import os
# import sys
# tree_file_directory = '../../Data Structures/Tree/Binary Tree/Binary Search Tree'
# sys.path.append(os.path.abspath(tree_file_directory))

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


# This is a class that inherits BinarySearchTree class from the BST_Implementation file.
class Traversal(BinarySearchTree):

    # Implementation of Breadth First Search (Iterative) method to traverse the tree level by level.
    def breadth_first_search(self):
        current_node = self.root  # Get the root node or starting node.
        result = []  # This list contains the order of all the nodes visited.
        # queue = []
        # queue.append(current_node)
        # The above 2 statements can be combined as shown below.
        queue = [current_node]  # This list keeps track of all the nodes on a level to track their child nodes later.

        while len(queue) > 0:  # As long as there is something in the queue.
            current_node = queue.pop(0)  # Return and remove the first item in the queue.
            # print(current_node.data)
            result.append(current_node.data)  # Add the value of the current node to the result list.
            if current_node.left:  # Look if there is left child.
                queue.append(current_node.left)  # Add to the queue to visit later.
            if current_node.right:  # Look if there is a right child.
                queue.append(current_node.right)  # Add to the queue to visit later.

        return result  # Return the result.

    # Implementation of the BFS method using recursion. We need to pass queue and result as a parameter since that way
    # it will not reset itself in every function call.
    def breadth_first_search_recursive(self, queue, result):

        # Base case
        if len(queue) < 1:  # When length of the queue is 0.
            return result
        current_node = queue.pop(0)  # Return and remove the first item in the queue.
        # print(current_node.data)
        result.append(current_node.data)  # Add the value of the current node to the result list.
        if current_node.left:  # Look if there is left child.
            queue.append(current_node.left)  # Add to the queue to visit later.
        if current_node.right:  # Look if there is a right child.
            queue.append(current_node.right)  # Add to the queue to visit later.

        # Recursive case
        return self.breadth_first_search_recursive(queue, result)


# Initialization

traverse = Traversal()

traverse.insert(9)
traverse.insert(4)
traverse.insert(20)
traverse.insert(1)
traverse.insert(6)
traverse.insert(15)
traverse.insert(170)
traverse.print_tree(traverse.root)

print("BFS using iteration:", traverse.breadth_first_search())
print("BFS using recursion:", traverse.breadth_first_search_recursive(queue=[traverse.root], result=[]))

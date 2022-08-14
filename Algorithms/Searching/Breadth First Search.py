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


class Traversal(BinarySearchTree):

    def breadth_first_search(self):
        current_node = self.root
        result = []
        # queue = []
        # queue.append(current_node)
        # The above 2 statements can be combined as shown below.
        queue = [current_node]

        while len(queue) > 0:
            current_node = queue.pop(0)
            # print(current_node.data)
            result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

    def breadth_first_search_recursive(self, queue, result):

        # Base case
        if len(queue) < 1:
            return result
        current_node = queue.pop(0)
        result.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

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

print(traverse.breadth_first_search())
print(traverse.breadth_first_search_recursive(queue=[traverse.root], result=[]))

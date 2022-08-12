"""
Implementation of Breadth First Search algorithm in python. Breadth First Search approach searches all the nodes level
by level from left to right starting from the root node. We keep track of all the children of each node visited.

Time complexity is O(n).
"""

import os
import sys

# This is to import from a different directory, but since I have copied this file to Modules which is in the same path
# as this file it won't be needed to use this method.
# tree_file_directory = '../../Data Structures/Tree/Binary Tree/Binary Search Tree'
# sys.path.append(os.path.abspath(tree_file_directory))

from Modules import *


class Traversal(Node):
    def breadth_first_search(self):
        #current_node = self.root
        result = []
        queue = []
        print("hello--------------------", )#current_node)


# Initialization

traverse = Traversal()
traverse.breadth_first_search()

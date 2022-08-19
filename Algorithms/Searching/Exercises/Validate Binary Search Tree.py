"""
Implementation of Binary Search Tree validation using BFS in leetcode.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from Algorithms.Searching.Modules.BST_Implementation import *


class Solution(BinarySearchTree):
    def isValidBST(self, root: Optional[Node]) -> bool:
        current_node = root
        print(current_node)
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                if current_node.left.data >= current_node.data and current_node.left.data >= root.data:
                    return False
                queue.append(current_node.left)
            if current_node.right:
                if current_node.right.data <= current_node.data and current_node.right.data <= root.data:
                    return False
                queue.append(current_node.right)
        return True


# Initialization

traverse = Solution()

traverse.insert(9)
traverse.insert(4)
traverse.insert(20)
traverse.insert(1)
traverse.insert(6)
traverse.insert(15)
traverse.insert(170)
traverse.print_tree(traverse.root)
print(traverse.isValidBST(traverse.root))

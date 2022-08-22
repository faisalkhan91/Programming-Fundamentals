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
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            print("Current node popped:", current_node.data)
            if current_node.left:
                print("adding left child to queue", current_node.left.data)
                if current_node.left.data >= current_node.data and current_node.left.data >= root.data:
                    return False
                queue.append(current_node.left)
            if current_node.right:
                print("adding right child to queue", current_node.right.data)
                if current_node.right.data <= current_node.data and current_node.right.data <= root.data:
                    return False
                queue.append(current_node.right)
        return True


# Initialization

traverse = Solution()

traverse.insert(5)
traverse.insert(4)
traverse.insert(6)
traverse.insert(3)
traverse.insert(7)
traverse.delete(3)
new_node = Node(3)
traverse.root.right.left = new_node

traverse.print_tree(traverse.root)
print(traverse.isValidBST(traverse.root))

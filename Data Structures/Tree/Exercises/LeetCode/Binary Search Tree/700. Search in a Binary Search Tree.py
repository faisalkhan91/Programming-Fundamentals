"""
700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root

        while current_node is not None:
            if current_node.val == val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

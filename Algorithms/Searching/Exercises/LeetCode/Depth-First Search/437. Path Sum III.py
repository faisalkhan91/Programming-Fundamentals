"""
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Reference: https://www.youtube.com/watch?v=VDTZiggKlAE
        :param root:
        :param targetSum:
        :return:
        """
        return self.DFS(root, targetSum)

    def DFS(self, node, target):
        if not node:
            return 0
        self.helper(node, target)
        self.DFS(node.left, target)
        self.DFS(node.right, target)
        return self.path

    def helper(self, node, target):
        if not node: return
        target -= node.val
        if target == 0:
            self.path += 1
        self.helper(node.left, target)
        self.helper(node.right, target)


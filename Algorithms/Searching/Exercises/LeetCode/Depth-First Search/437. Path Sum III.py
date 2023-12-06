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
        self.path_sum = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.DFS(root, targetSum)

    def DFS(self, node, target):
        if not node:
            return

        if self.path_sum == target:
            self.path += 1
        if self.path_sum >= target:
            self.path_sum = node.val
        else:
            self.path_sum += node.val

        self.DFS(node.left, target)
        self.DFS(node.right, target)

        return self.path

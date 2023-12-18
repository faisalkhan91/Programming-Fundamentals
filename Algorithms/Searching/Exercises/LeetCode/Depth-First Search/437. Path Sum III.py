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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0
        self.cache = {}

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.DFS(root, targetSum)
        return self.path

    def DFS(self, node, target, current_path_sum = 0):
        if not node:
            return
        current_path_sum += node.val
        old_path_sum = current_path_sum - target
        if current_path_sum == target:
            self.path += 1
        if old_path_sum in self.cache:
            self.path += self.cache[old_path_sum]
        if current_path_sum in self.cache:
            self.cache[current_path_sum] += 1
        else:
            self.cache[current_path_sum] = 1
        self.DFS(node.left, target, current_path_sum)
        self.DFS(node.right, target, current_path_sum)
        self.cache[current_path_sum] -= 1

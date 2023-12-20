"""
1372. Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zigzag = 0

        def DFS(node):
            if not node:
                return
            helper(node)
            DFS(node.left)
            DFS(node.right)
            return self.longest_zigzag

        def helper(node, zigzag=0):
            if not node:
                if zigzag > self.longest_zigzag:
                    self.longest_zigzag = zigzag
                return
            zigzag += 1
            if zigzag % 2 == 0:
                helper(node.left, zigzag)
            else:
                helper(node.right, zigzag)

        return DFS(root)

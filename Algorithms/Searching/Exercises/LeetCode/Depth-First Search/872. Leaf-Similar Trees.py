"""
872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        r1 = self.DFS(root1, r1)
        r2 = self.DFS(root2, r2)
        if r1 == r2:
            return True
        return False

    def DFS(self, root, res):
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            self.DFS(root.left, res)
        if root.right:
            self.DFS(root.right, res)
        return res
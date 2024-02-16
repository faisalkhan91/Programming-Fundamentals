"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            # If the value of p and q nodes is greater than current root node move right.
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If the value of p and q nodes is lesser than current root node move left.
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:  # If the nodes appear to diverge then root node is between them and is the ancestor to both of them.
                return root

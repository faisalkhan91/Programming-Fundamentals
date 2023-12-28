"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

Definition of LCA (https://en.wikipedia.org/wiki/Lowest_common_ancestor):
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        This solution utilizes in-order depth first search traversal to search for the lowest common ancestor in the
        tree for the given nodes. The idea is that if the node is found, it is returned and stored in the left and right
        variables. If both the values are there, then the current node is the parent of both the nodes and also the
        lowest common ancestor. If there is no left value and there is a right value, then the right node is the lowest
        common ancestor and vice versa if the left side has a value and the right side doesn't.

        Note: This is an in-order DFS traversal as the left tree is searched first and then the right tree is searched.

        Time Complexity: O(n). Space Complexity: O(n).

        :param root: Head of Binary Search Tree.
        :param p: The node for which the LCA needs to be found.
        :param q: The node for which the LCA needs to be found.
        :return: LCA of the Binary Tree.
        """
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:  # If the given p or q is found, return the node.
                return node

            left = dfs(node.left)  # Store the left tree
            right = dfs(node.right)  # Store the right tree.

            if not left:  # If left tree is none return right.
                return right
            if not right:
                return left
            else:
                return node

        return dfs(root)


##########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor_clean(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Same as above, the code is return in more pythonic way. Also, the nested function is not utilized anymore.

        Time Complexity: O(n). Space Complexity: O(n).

        :param root: Head of Binary Search Tree.
        :param p: The node for which the LCA needs to be found.
        :param q: The node for which the LCA needs to be found.
        :return: LCA of the Binary Tree.
        """
        if not root:
            return
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor_clean(root.left, p, q)
        right = self.lowestCommonAncestor_clean(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

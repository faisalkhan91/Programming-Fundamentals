"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        In this solution Depth First Search is used to find the maximum depth. The base case is set to return 0 at the
        end of the recursion if no more node is present. The max depth between left and right nodes of every parent is
        compared and returned by adding 1.

        Reference: https://www.youtube.com/watch?v=hTM3phVI6YQ

        Time Complexity: O(n). Space Complexity: O(n).

        :param root: Head of the binary tree.
        :return: Maximum depth of the tree.
        """
        if not root:
            return 0

        left = self.maxDepth(root.left) + 1  # Left nodes at each level.
        right = self.maxDepth(root.right) + 1  # Right nodes at each level.

        return max(left, right)

    def maxDepth_clean(self, root: Optional[TreeNode]) -> int:
        """
        Same as above just written more cleanly.

        :param root: Head of the binary tree.
        :return: Maximum depth of the tree.
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

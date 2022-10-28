"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    To solve this problem we use DFS Traversal algorithm, we set boundaries such as a minimum and a maximum value a node
    should be in. We are checking left the maximum allowed value is less than the root node value and if we are going
    right the minimum allowed value is greater than the root node value.
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.inorder_traversal(root, float(-inf), float(inf))
        return result

    def inorder_traversal(self, root, minimum, maximum):
        if not root:  # If reached end of the subtree return True.
            return True
        if root.val <= minimum or root.val >= maximum:  # If the value is not within these boundaries return False.
            return False
        # Return is only true if both the left and right subtree return True. This is achieved by using and condition.
        return self.inorder_traversal(root.left, minimum, root.val) and \
               self.inorder_traversal(root.right, root.val, maximum)


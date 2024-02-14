"""
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Reference: https://www.youtube.com/watch?v=LFzAoJJt92M
        :param root: Head of the tree.
        :param key: Value of the node to be deleted if found.
        :return: root
        """
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if key == root.val:
                if not root.left or not root.right:
                    return root.left or root.right
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
        return root

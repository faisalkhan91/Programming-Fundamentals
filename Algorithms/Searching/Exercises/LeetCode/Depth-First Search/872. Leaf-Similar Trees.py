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
        """
        In this solution, the Depth-First Search (DFS) technique is used to get the leaf nodes and then the leaf nodes
        of both the trees are compared. It doesn't matter what DFS traversal is used to find the leaf nodes, but in the
        below solution preorder traversal is used, and in the following solution in-order traversal is utilized. The
        traversal is separated into a new method for easy understanding. Two stacks are declared that will hold the
        values of the leaf nodes of the trees. The DFS method recursively traverses the nodes and appends the leaf
        values to the stack. The stacks are compared and if are found to be same a boolean True is returned else False
        is returned.

        Time Complexity: O(n). Space Complexity: O(n).

        :param root1: Binary Tree
        :param root2: Binary Tree
        :return: Boolean: True or False
        """
        leaves1 = []
        leaves2 = []
        self.DFS(root1, leaves1)
        self.DFS(root2, leaves2)
        return True if leaves1 == leaves2 else False

    def DFS(self, node, leaves):
        """
        This is the preorder method used by the solution above.

        Time Complexity: O(n). Space Complexity: O(n).

        :param node: Binary Tree
        :param leaves: All the leaves
        :return: leaves
        """
        if not node.left and not node.right:
            leaves.append(node.val)
        if node.left:
            self.DFS(node.left, leaves)
        if node.right:
            self.DFS(node.right, leaves)
        return leaves

    ############################################################################################
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Simailar to above, but just uses inorder traversal.
        :param root1: Binary Tree
        :param root2: Binary Tree
        :return: Boolean
        """
        l1 = []
        l2 = []
        self.inorder(root1, l1)
        self.inorder(root2, l2)
        return l1 == l2

    def inorder(self, node, leaves):
        if node:
            self.inorder(node.left, leaves)
            if not node.left and not node.right:
                leaves.append(node.val)
            self.inorder(node.right, leaves)
        return leaves

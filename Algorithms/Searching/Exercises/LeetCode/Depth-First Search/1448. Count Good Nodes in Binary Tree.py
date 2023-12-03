"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        self.DFS(root, good_nodes)

        return good_nodes

    def DFS(self, node, valid):
        if not node.left or not node.right:
            return valid
        if node.val <= node.left.val and node.val <= node.right.val:
            valid += 1
        if node.left:
            self.DFS(node.left, valid)
        if node.right:
            self.DFS(node.right, valid)
        return valid

    ########################################################################

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def goodNodes(self, root: TreeNode) -> int:

            good_nodes = 0
            good_nodes = self.DFS(root, good_nodes)

            return good_nodes

        def DFS(self, node, valid):
            if not node.left or not node.right:
                return valid
            if node.val <= node.left.val or node.val <= node.right.val:
                valid += 1
            if node.left:
                left = self.DFS(node.left, valid)
            if node.right:
                right = self.DFS(node.right, valid)
            valid = left + right
            return valid

    ################################################################################################

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def goodNodes(self, root: TreeNode) -> int:

            good_nodes = [0]
            good_nodes = self.DFS(root, good_nodes)

            return good_nodes

        def DFS(self, node, valid, max=0):
            if not node:
                return
            if node.val >= max:
                valid[0] += 1
                max = node.val

            self.DFS(node.left, valid, max)
            self.DFS(node.right, valid, max)
            print(valid)
            return valid[0]


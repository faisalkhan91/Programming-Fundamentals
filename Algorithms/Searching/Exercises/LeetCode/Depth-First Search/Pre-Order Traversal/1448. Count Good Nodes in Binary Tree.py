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
    def __init__(self):
        self.good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        """
        In this solution depth first search (DFS) traversal is utilized, more specifically the preorder DFS. Also, the
        constructor __init__ is utilized to initialize a global variable within the class. This method calls the
        preorder_dfs method which recursively uses preorder dfs to count the good nodes and then the value of the good
        nodes is returned.

        Time Complexity: O(n), Space Complexity: O(1).

        :param root: Head of the Binary Tree.
        :return: Number of good nodes.
        """
        self.preorder_dfs(root)
        return self.good_nodes  # The value of the good nodes is stored in the class initialized global variable.

    def preorder_dfs(self, node, curr_max = float(-inf)):
        """
        This method recursively traverses the tree using preorder DFS. A variable current max is declared with value as
        -ve infinity and set to the new max value whenever a good node is encountered as the good node will have the
        greater value in the path. The method recursively calls the left and right nodes.
        :param node: Binary tree
        :param curr_max: Previous max value.
        :return: None
        """
        if not node:
            return
        if node.val >= curr_max:
            self.good_nodes += 1
            curr_max = node.val
        self.preorder_dfs(node.left, curr_max)
        self.preorder_dfs(node.right, curr_max)

    #################################################################################

    def goodNodes(self, root: TreeNode) -> int:
        """
        Similar as above, difference is the value is stored in a list and send to the nodes. Here the global variable
        isn't utilized. Note that the value is in a list and not integer as the integer is not being returned. Not aware
        why though.

        Time Complexity: O(n), Space Complexity: O(1).

        :param root: Head of the Binary Tree.
        :return: Number of good nodes.
        """
        good_nodes = [0]
        good_nodes = self.preorder_dfs(root, good_nodes)
        return good_nodes

    def preorder_dfs(self, node, valid, curr_max=float(-inf)):
        if not node:
            return
        if node.val >= curr_max:
            valid[0] += 1
            curr_max = node.val
        self.preorder_dfs(node.left, valid, curr_max)
        self.preorder_dfs(node.right, valid, curr_max)
        return valid[0]

    #################################################################################

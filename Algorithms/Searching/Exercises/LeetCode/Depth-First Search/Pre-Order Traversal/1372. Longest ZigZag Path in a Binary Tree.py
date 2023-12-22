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
        """
        This solution is a pre-order depth first search traversal as the direction is tracked before each recursion. In
        this solution, a nested method is used to traverse the binary tree in a Zig-Zag order using recursion. The order
        is tracked by passing the direction during the recursion if the next direction is in Zig-Zag order the path
        count is incremented. If the order is not correct, the path count resets to 1, and recursion continues.

        Time Complexity: O(n). Space Complexity: O(1).

        :param root: Start of the Binary Tree.
        :return: The longest Zig-Zag path in the tree.
        """

        self.longest = 0

        def dfs(node, zigzag=0, direction="R"):
            if not node:
                self.longest = max(self.longest, zigzag)  # Compare the values with the current longest Zig-Zag path.
                return
            dfs(node.left, zigzag + 1 if direction == "R" else 1, "L")  # The direction tracks the path.
            dfs(node.right, zigzag + 1 if direction == "L" else 1, "R")
            return self.longest - 1  # Return the longest path - 1 as this gives the edges not nodes in the path.
        return dfs(root)

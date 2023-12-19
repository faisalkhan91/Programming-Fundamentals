"""
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Reference: https://www.youtube.com/watch?v=VDTZiggKlAE

        This is the brute force solution to the problem. In this solution, a nested recursion is used as there is a need
        to find the sum of the path from each node onwards. A method DFS is used to traverse each path using preorder
        traversal in depth-first search technique. This method traverses the tree for each node and calls the helper
        method.

        The helper method recursively calculates the sum of the path for each node from the current node ot the leaf
        node. If the sum of the path matches the target sum, the count is increased.

        Time Complexity: O(n^2). Space Complexity: O(1).

        :param root: Binary Tree
        :param targetSum: Target path sum.
        :return: Number of the path sum matching the target sum.
        """
        return self.DFS(root, targetSum)

    def DFS(self, node, target):
        if not node:
            return 0
        self.helper(node, target)
        self.DFS(node.left, target)
        self.DFS(node.right, target)
        return self.path

    def helper(self, node, target):
        if not node: return
        target -= node.val
        if target == 0:
            self.path += 1
        self.helper(node.left, target)
        self.helper(node.right, target)

############################################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0
        self.cache = {}

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        This solution uses memoization to store the values of the path sum that are already visited. This idea is based
        on the assumption that if there is a valid path sum, then there is an old path sum that is already visited. The
        equation can be as:
        -> current_path_sum - old_path_sum = target
        The frequency of that path is added to the result. The current path is added to the cache. After the end of each
        path, the path frequency is subtracted as the path is no longer being traversed.

        Time Complexity: O(n). Space Complexity: O(n).

        :param root: Binary Tree
        :param targetSum: Target path sum.
        :return: Number of the path sum matching the target sum.
        """
        self.DFS(root, targetSum)
        return self.path

    def DFS(self, node, target, current_path_sum = 0):
        if not node:
            return
        current_path_sum += node.val
        old_path_sum = current_path_sum - target
        if current_path_sum == target:  # to check if the sum of the path from root to the last node is a valid sum.
            self.path += 1
        if old_path_sum in self.cache:
            self.path += self.cache[old_path_sum]
        if current_path_sum in self.cache:
            self.cache[current_path_sum] += 1
        else:
            self.cache[current_path_sum] = 1
        self.DFS(node.left, target, current_path_sum)
        self.DFS(node.right, target, current_path_sum)
        self.cache[current_path_sum] -= 1

############################################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0
        self.cache = {0: 1}

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        This is the same as above just written cleaner, more pythonic way. Note also, the variable self.cache is
        initialized with value 0 as it takes into account the sum of the path from root to the last node in the path.
        """
        self.DFS(root, targetSum)
        return self.path

    def DFS(self, node, target, current_path_sum = 0):
        if not node:
            return
        current_path_sum += node.val
        old_path_sum = current_path_sum - target
        self.path += self.cache.get(old_path_sum, 0)
        self.cache[current_path_sum] = self.cache.get(current_path_sum, 0) + 1  # Update frequency of the current path.
        self.DFS(node.left, target, current_path_sum)
        self.DFS(node.right, target, current_path_sum)
        self.cache[current_path_sum] -= 1  # Remove the frequency once the path is traversed.

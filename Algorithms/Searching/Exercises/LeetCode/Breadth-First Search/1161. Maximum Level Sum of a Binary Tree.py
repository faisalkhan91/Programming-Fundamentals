"""
1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""

import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        In this solution Breadth First Search Traversal is utilized. There are two loops that help in manipulating each
        level to achieve the result. The while loop keeps track of the BFS queue and the for loop iterates over nodes
        at each level. Here, the sum of each level is calculated and new nodes for the next level are added to the
        current queue. The current sum at each level is compared to the previous max sum, and if greater the level and
        current sum are updated. This ensures that the maximum sum at the lowest level is being tracked.
        :param root: Head of the Binary Tree
        :return: Lowest level with the maximum level sum.

        Time Complexity: O(n), Space Complexity: O(1)
        """
        queue = collections.deque([root])  # Declare queue for BFS traversal
        level = 0
        max_sum = float('-inf')  # Declare the sum from -ve infinity as the nodes can be negative.
        min_level = 0

        while queue:
            current_sum = 0  # Reset the sum at each level.
            level += 1  # Increment level
            for i in range(len(queue)):
                current_node = queue.popleft()
                current_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            if max_sum < current_sum:  # Check if the current sum is bigger than the previous max sum.
                max_sum = current_sum
                min_level = level  # Note the level of the max sum.
        return min_level

###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         queue = collections.deque([root])
#         level = 0
#         level_sums = {root.val: level}
#
#         while queue:
#             current_sum = 0
#             level += 1
#             for i in range(len(queue)):
#                 current_node = queue.popleft()
#                 if current_node:
#                     current_sum += current_node.val
#                     queue.append(current_node.left)
#                     queue.append(current_node.right)
#             if current_sum != 0:
#                 level_sums[current_sum] = level
#
#         return level_sums[max(level_sums)]

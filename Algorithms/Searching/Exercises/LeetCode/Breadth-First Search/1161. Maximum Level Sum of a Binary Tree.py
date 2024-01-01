"""
1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        level = 0
        level_sums = {root.val: level}

        while queue:
            current_sum = 0
            level += 1
            for i in range(len(queue)):
                current_node = queue.popleft()
                if current_node:
                    current_sum += current_node.val
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            if current_sum != 0:
                level_sums[current_sum] = level

        return level_sums[max(level_sums)]

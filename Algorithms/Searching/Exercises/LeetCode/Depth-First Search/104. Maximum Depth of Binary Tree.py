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
    def maxDepth(self, root: Optional[TreeNode], count_list = [], counter = 0) -> int:

        current_node = root

        if current_node.left:
            counter += 1
            self.maxDepth(current_node.left, count_list, counter)
        else:
            count_list.append(counter)
        if current_node.right:
            counter += 1
            self.maxDepth(current_node.right, count_list, counter)
        else:
            count_list.append(counter)

        return max(count_list)
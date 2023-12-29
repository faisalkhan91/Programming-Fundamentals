"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = [root]
        current_node = root
        result = []
        while queue:
            current_node = queue.pop(0)
            if current_node and current_node.left:
                queue.append(current_node.left)
            if current_node and current_node.right:
                result.append(current_node.right.val)
                queue.append(current_node.right)
        return result

"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan&id=level-1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        while not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            result = queue.val
            level_nodes = []

            for i in node:
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            print(level)

        return result

    
##################################################################################################
# Initial attempt, works like BFS but does not give answer of all the nodes in a level.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#
#         result = [[root.val]]
#         queue = [root]
#
#         while queue:
#             current = queue.pop(0)
#             temp = []
#             if current.left:
#                 queue.append(current.left)
#                 temp.append(current.left.val)
#             if current.right:
#                 queue.append(current.right)
#                 temp.append(current.right.val)
#             if temp != []:
#                 result.append(temp)
#         return result

"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan&id=level-1

Explanation : https://www.youtube.com/watch?v=6ZnyEApgFYg
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

        queue = [root]
        result = [[queue[0].val]]

        while queue:
            nodes = queue
            level_nodes = []
            print("******************************************")
            print(queue)
            for node in nodes:
                print(len(nodes))
                print("###############################")
                print(node, end="\n")
                level = queue.pop(0)
                level_nodes.append(level.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(level_nodes)
            result.append(level_nodes)
            print(result)
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

"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan&id=level-1

Explanation : https://www.youtube.com/watch?v=6ZnyEApgFYg
Reference: https://stackoverflow.com/questions/74188555/python-leetcode-bst-level-order-traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ Time complexity of this method is O(n). Space complexity of this method is O(n)."""
        while not root:  # Check if the tree is empty and return nothing.
            return []

        queue = [root]  # Add root to the queue.
        result = []  # List to store the traversal values.

        while queue:  # Loop while there is nodes in queue. This is for each level.
            level_nodes = []  # List to store the values of the nodes in the current level.
            temp = []  # List to store the child nodes. This will be added back to queue.
            for node in queue:  # Loop for all the current nodes in the queue for a given level.
                level_nodes.append(node.val)  # Store the value of the current node in the queue.
                if node.left:
                    temp.append(node.left)  # Add the child nodes on the left to the queue.
                if node.right:
                    temp.append(node.right)  # Add the child nodes on the right to the queue.
            queue = temp  # Replace the current nodes with nodes in the next level of the queue.
            result.append(level_nodes)  # Append the values of the nodes in the current level.
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

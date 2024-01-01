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
        """
        Reference: https://www.youtube.com/watch?v=d4zLyf32e3I

        In this solution Breadth First Search (BFS) is used to find the solution. BFS naturally performs level order
        traversal. As the right most node visible from the right side point of view is required, the right most node at
        each level is added to the result be it in the left or right tree.

        A single queue is utilized for the traversal. The queue is initialized with the root node and an inner for loop
        is used to add the children to the queue, this is repeated at each level of the tree. A variable right keeps
        track of the current node until all the nodes in the level have been visited. The last node left in the variable
        is the right most node at that level is appended to the result.

        Time Complexity: O(n). Space Complexity: O(n).

        :param root: Head of the tree.
        :return: Right most nodes in a tree.
        """

        queue = [root]  # Add the root node to the queue.
        result = []  # To store all the values of the right most nodes.

        while queue:  # While there are nodes in the queue.
            length = len(queue)  # Get the current length of the queue.
            right = None  # Initialize right variable to None after each level.
            for i in range(length):  # Iterate the queue at each level, which is determined by the length of the queue.
                current_node = queue.pop(0)
                if current_node:  # If there is a node.
                    # Store the value of the available current node until the last node in the level.
                    right = current_node
                    queue.append(current_node.left)  # Add the nodes children to the queue.
                    queue.append(current_node.right)
            if right:  # If there is a right value at the last level, add it to the result.
                result.append(right.val)
        return result

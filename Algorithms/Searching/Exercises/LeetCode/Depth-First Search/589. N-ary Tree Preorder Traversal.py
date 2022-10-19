"""
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=level-1
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.preorder_traversal(root, result)  # Call the recursive function.
        return result

    def preorder_traversal(self, root, result):
        # If the end of the tree, return.
        if root == None:
            return result
        result.append(root.val)  # In preorder, we add the value to the output before we go to the child nodes.
        for child in root.children:  # Call the child nodes, it will be from left to right.
            self.preorder_traversal(child, result)

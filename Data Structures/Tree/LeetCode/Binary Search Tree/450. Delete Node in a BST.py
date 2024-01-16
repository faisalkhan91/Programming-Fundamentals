"""
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        current_node = previous_node = root
        while current_node:
            if key > current_node.val:
                previous_node = current_node
                current_node = current_node.right
            elif key < current_node.val:
                previous_node = current_node
                current_node = current_node.left
            else:
                if current_node.val == key:
                    if current_node.left and current_node.right:
                        previous_node.left = current_node.left
                        current_node.left.right = current_node.right
                    elif current_node.left and not current_node.right:
                        previous_node.left = current_node.left
                    elif current_node.right and not current_node.left:
                        previous_node.left = current_node.right
                    else:
                        root = None
                return root
        return root



#######################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val < key:
            self.deleteNode(root.right, key)
        elif root.val > key:
            self.deleteNode(root.right, key)
        else:
            if root.val == key:
                if not root.right and root.left:
                    return root.left
                elif not root.left and root.right:
                    return root.right
                elif not root.right and root.left:
                    return root.right
                else:
                    root.val = root.right.val
                    root.right = None
                    return root
        return root
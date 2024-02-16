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
        """
        Reference: https://www.youtube.com/watch?v=LFzAoJJt92M

        Recursion and Node Search:
            - The solution uses recursion to traverse the binary tree and find the target node that needs to be deleted.
            - During each recursive call, the value of the current node is compared with the target value.
            - If the current node’s value matches the target value, the node is marked for deletion.
        Node Deletion Scenarios:
            - Depending on the structure of the target node, the solution handles different scenarios:
                > No Child Nodes: If the target node has no children (i.e., it’s a leaf node), the solution removes it
                  from the tree.
                > One Child Node: If the target node has only one child, the solution replaces the target node with its
                  child.
                > Two Child Nodes: If both left and right subtrees exist for the target node, the solution finds the
                  minimum value in the right subtree (which is the leftmost node in the right subtree).
                    >> The value of the target node is then swapped with the minimum value node.
                    >> Finally, the minimum value node (which now contains the original target value) is deleted.
        Return Values:
            - If no node matches the target value, the solution returns None.
            - If there’s only one node (the target node), the solution returns that node.
            - Otherwise, it returns the modified binary tree after deletion.
        Remember that this approach ensures that the binary tree remains valid after node removal.

        Time Complexity: O(h). Space Complexity: O(1).

        :param root: Head of the tree.
        :param key: Value of the node to be deleted if found.
        :return: root
        """
        if not root:  # If there are no more leaf nodes in the path, end recursion.
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)  # Store the value to use for curr variable.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if key == root.val:  # If the node is found, test the cases below.
                if not root.left or not root.right:  # If there is no left or right subtree.
                    return root.left or root.right  # Return the remaining subtree.
                # If there are both subtrees, then find the lowest value in the right subtree to replace the deleted
                # value; it will be the leftmost value in the right subtree.
                curr = root.right  # Store the current node value.
                while curr.left:  # Iterate through the right subtree to find the minimum value.
                    curr = curr.left
                root.val = curr.val  # Once the value is found, replace the node to be deleted with the minimum value.
                root.right = self.deleteNode(root.right, root.val)  # Pass the replaced value to delete the leaf node.
        return root

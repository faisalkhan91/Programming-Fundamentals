"""
Implementation of Binary Search Tree data structure in python.
"""

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Return data instead of object address.
    def __str__(self):
        return str(self.data)


# Binary search tree implementation
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    # Insert node into tree.
    def insert(self, value):
        new_node = Node(value)  # Create a new node.
        # If there is no root node, make the new node as the root node.
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root  # Set the starting node for the loop.
            while current_node is not None:
                # If the value is less than current node's value, check to see if the current node has a left
                # node. If no, add the new node as a left child to the current node. If yes, move on to the
                # next node in the left.
                if new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                # Similar to above, if the value is higher than the current node's value, move to the right.
                # If the right node is empty add the new node or else make the right nod as the new current
                # node.
                elif new_node.data >= current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
        return self

    # Method to delete the node in the tree.
    def delete(self, value):
        # Check to see if the tree is empty.
        if self.root is None:
            print("The tree is empty.")
            return False
        
        current_node = self.root  # Set the current node as root for loop.
        parent_node = None  # Create a variable to store the parent node in the loop.

        while current_node is not None:
            # If the value to delete is less than the current node's value move to the left of the tree.
            if value < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            # If the value is greater than the value in the current node, move to the right of the tree.
            elif value > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            # If value matches a node in the tree, check the below cases.
            elif value == current_node.data:
                # If it is the leaf node (or a node with no child). Both the left and right will be None.
                if current_node.left is None and current_node.right is None:
                    print('Value is in a leaf node.')
                    # If there is no parent node that means there is only one value that can be deleted.
                    if parent_node is None:
                        current_node = None
                    # If the current node is less than parent node, delete the left child.
                    elif current_node.data < parent_node.data:
                        parent_node.left = None
                    # If the current node's data is greater than parent node, delete the right node.
                    elif current_node.data > parent_node.data:
                        parent_node.right = None
                    return
                # If there is one child node on the left.
                elif current_node.left is not None and current_node.right is None:
                    print('Value is in a node with only left child.')
                    # If there is no parent node that means there is only one value that can be deleted.
                    if parent_node is None:
                        current_node = None
                    # If the value of the current node is less than the parent nodes value, set the left
                    # node of the parent to the current nodes left.
                    elif current_node.data < parent_node.data:
                        parent_node.left = current_node.left
                    # If the value of the current node is greater than the parent's value, set the right
                    # node of the parent to the current node's left.
                    elif current_node.data > parent_node.data:
                        parent_node.right = current_node.left
                    return
                # If there is one child node on the right.
                elif current_node.left is None and current_node.right is not None:
                    print('Value is in a node with only right child.')
                    # If there is no parent node that means there is only one value that can be deleted.
                    if parent_node is None:
                        current_node = None
                    # Set the right node of the current node as the parent's left node.
                    elif current_node.data < parent_node.data:
                        parent_node.left = current_node.right
                    # Set the left node of the current node as the parent's right node.
                    elif current_node.data > parent_node.data:
                        parent_node.right = current_node.right
                    return
                # If both the child are present.
                elif current_node.left is not None and current_node.right is not None:
                    print('Value is in the node with bothe child nodes.')
                    if parent_node is None:
                        current_node = None
                    else:
                        replacement_node = current_node.right
                        replacement_node_parent = None
                        while replacement_node.left is not None:
                            replacement_node_parent = replacement_node
                            replacement_node = replacement_node.left

                            current_node.data = replacement_node.data
                            replacement_node_parent.left = None
                return
        # If the value did not match any of the nodes, return False.
        print(value, "is not found in the binary search tree.")
        return False

    # Method to perform a lookup.
    def lookup(self, value):
        if not self.root:
            print("Binary tree is empty.")
            return False
        current_node = self.root
        while current_node is not None:
            if value == current_node.data:
                print("Found value!")
                return current_node
            elif value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
        print("Nothing found!")
        return False


    # def display(self):
    #     current_node = self.root
    #     print("Root:", self.root.data)
    #     level = 1
    #     while current_node is not None:
    #         print(level, "st left node:", current_node.left)
    #         print(level, "st right node:", current_node.right)
    #         current_node = current_node


    # This function is to print the tree.
    def print_tree(self, root, val="data", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)


# Initialization

my_BST = BinarySearchTree()
my_BST.insert(10)
my_BST.insert(5)
my_BST.insert(3)
my_BST.insert(7)
my_BST.insert(6)
my_BST.insert(4)
my_BST.insert(1)
my_BST.insert(2)
my_BST.insert(20)
my_BST.insert(15)
my_BST.insert(73)
my_BST.insert(12)
# print(my_BST.root.left.left.data)
# my_BST.display()
# my_BST.lookup(9)
# my_BST.insert(9)
# my_BST.insert(4)
# my_BST.insert(20)
# my_BST.insert(1)
# my_BST.insert(6)
# my_BST.insert(15)
# my_BST.insert(170)
# my_BST.lookup(9)
# my_BST.insert(10)
# my_BST.insert(6)
# my_BST.insert(20)
# my_BST.insert(4)
# my_BST.insert(5)
# my_BST.insert(3)
# my_BST.insert(2)
# my_BST.insert(15)
# my_BST.insert(22)
# my_BST.insert(14)
# my_BST.insert(7)
# my_BST.delete(4)
# my_BST.delete(14)
my_BST.delete(3)
my_BST.print_tree(my_BST.root)

#
# Test commit on codespace 2
#

########################################################################################
# First attempt for a method to remove a node from the tree.
# def delete(self, value):
#     current_node = self.root
#     while current_node.data is not None:
#         if value < current_node.data:
#             if value == current_node.left.data:
#                 if current_node.left.left is None and current_node.left.right is None:
#                     current_node.left = None
#                     return
#             elif value == current_node.right.data:
#                 if current_node.left.left is None and current_node.left.right is None:
#                     current_node.right = None
#                     return
#             else:
#                 current_node = current_node.left
#         elif value >= current_node.data:
#             if value == current_node.left.data:
#                 if current_node.left.left is None and current_node.left.right is None:
#                     current_node.left = None
#                     return
#             elif value == current_node.right.data:
#                 if current_node.left.left is None and current_node.left.right is None:
#                     current_node.right = None
#                     return
#             else:
#                 current_node = current_node.right
#     return self

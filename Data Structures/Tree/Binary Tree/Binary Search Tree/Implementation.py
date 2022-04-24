"""
Implementation of Binary Search Tree data structure in python.
"""


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Binary search tree implementation
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    # Insert node into tree.
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif new_node.data >= current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
        return self

    # Method to delete the node in the tree.
    def delete(self, value):
        if self.root is None:
            print("The tree is empty.")
            return False
        current_node = self.root
        parent_node = None

        while current_node is not None:
            if value < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.data:
                # If it is the leaf node (or a node with no child). Both the left and right will be None.
                if current_node.left is None and current_node.right is None:
                    print('Oh hello, case 1 is activated')
                    if parent_node is None:
                        current_node = None
                    elif current_node.data < parent_node.data:
                        parent_node.left = None
                    elif current_node.data > parent_node.data:
                        parent_node.right = None
                    return
                # If there is one child node on the left.
                elif current_node.left is not None and current_node.right is None:
                    print('Oops, its case 2, case 2 is activated')
                    if parent_node is None:
                        current_node = None
                    elif current_node.data < parent_node.data:
                        parent_node.left = current_node.left
                    elif current_node.data > parent_node.data:
                        parent_node.right = current_node.left
                # If there is one child node on the right.
                elif current_node.left is None and current_node.right is not None:
                    print('Oh yeah, its case 3, case 3 is activated')
                    if parent_node is None:
                        current_node = None
                    elif current_node.data < parent_node.data:
                        parent_node.left = current_node.right
                    elif current_node.data > parent_node.data:
                        parent_node.right = current_node.right
                return
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
# my_BST.insert(10)
# my_BST.insert(5)
# my_BST.insert(3)
# my_BST.insert(6)
# my_BST.insert(5)
# my_BST.insert(4)
# my_BST.insert(4)
# my_BST.insert(2)
# my_BST.insert(20)
# my_BST.insert(15)
# my_BST.insert(73)
# my_BST.insert(12)
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
my_BST.insert(10)
my_BST.insert(6)
my_BST.insert(20)
my_BST.insert(4)
my_BST.insert(5)
my_BST.insert(3)
my_BST.insert(2)
my_BST.insert(15)
my_BST.insert(22)
my_BST.insert(14)
my_BST.insert(7)
# my_BST.delete(4)
# my_BST.delete(14)
# my_BST.delete(3)
my_BST.print_tree(my_BST.root)


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

"""
Implementation of Binary Search Tree data structure in python.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if new_node.data <= current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
        return self

    def delete(self):
        pass

    def lookup(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.data:
                print("Found value!")
                return
            elif value <= current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
        print("Nothing found!")


    # def display(self):
    #     current_node = self.root
    #     print("Root:", self.root.data)
    #     level = 1
    #     while current_node is not None:
    #         print(level, "st left node:", current_node.left)
    #         print(level, "st right node:", current_node.right)
    #         current_node = current_node


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
my_BST.insert(6)
my_BST.insert(5)
# print(my_BST.root.left.left.data)
# my_BST.display()
my_BST.lookup(7)
my_BST.print_tree(my_BST.root)

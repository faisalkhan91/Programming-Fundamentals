"""
Implementation of Binary Search Tree data structure in python. There is no equivalent data structure implemented by
default in python.

The data structure has a root node connected to child nodes. Each node in a Binary Search Tree has declarations to
store the value of the data, a pointer to the left child and a pointer to the right child.
"""


# This is a node class for a BST to store data as well as the left and right pointers.
class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the Node.
        self.left = None  # Pointer to store the address of the left child node.
        self.right = None  # Pointer to store the address of the right child node.

    # Modification of the __str__ function to return value of data in string format when calling node object.
    def __str__(self):
        return str(self.data)


# Class to implement the Binary Search Tree data structure and its methods.
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Store the value of the root node.

    # Return the BST object in dictionary format
    def __str__(self):
        return str(self.__dict__)

    # Method to insert a new node into the Binary Search Tree.
    def insert(self, value):
        new_node = Node(value)  # Create a new node.
        # Check to see if the root node is empty, as in the BST is empty. If yes, insert new node as root node.
        if self.root is None:
            self.root = new_node  # Make the node as root node.
            # self.print_tree(self.root)
        # If the BST has a root node, traverse the tree based on the BST properties and insert the new node.
        else:
            current_node = self.root  # Set the current node as root node.
            # We use a while loop to traverse the tree until an empty tree node is found that satisfies BST properties.
            while current_node is not None:
                if new_node.data < current_node.data:  # Check if the value is less than the data of the current node.
                    if current_node.left is None:  # Check to see if the left child of current node is empty
                        current_node.left = new_node  # Insert the new node as left child if empty.
                        # self.print_tree(self.root)
                        return  # To stop processing the loop.
                    else:
                        current_node = current_node.left  # Make the current node as the left node.
                elif new_node.data >= current_node.data:  # Check to see if the value is greater than or equal to.
                    if current_node.right is None:  # Check to see if the right child of current node is empty.
                        current_node.right = new_node  # Insert the new node as right child if empty.
                        # self.print_tree(self.root)
                        return  # To stop processing the loop.
                    else:
                        current_node = current_node.right  # Make the current node as the right node.
        return self

    # Method to delete a node in the Binary Search Tree.
    def delete(self, value):
        # Check to see if the root node is empty, if yes, return False to indicate empty BST.
        if self.root is None:
            print("The tree is empty.")
            return False

        current_node = self.root  # Set current node as root.node.
        parent_node = None  # This declaration will track the previous or parent node of the current node.

        # Loop using while loop until the end of the tree.
        while current_node is not None:
            if value < current_node.data:  # If value is less that current node data, move left.
                parent_node = current_node  # Set parent node as the current node.
                current_node = current_node.left  # Set current node to the left child of the current node.
            elif value > current_node.data:  # If value is greater than current node data, move right.
                parent_node = current_node  # Set parent node as the current node.
                current_node = current_node.right  # Set current node to the right child of the current node.
            elif value == current_node.data:  # Verify the conditions below if there is a value match.
                # If it is the leaf node (or a node with no child). Both the left and right will be None.
                if current_node.left is None and current_node.right is None:
                    print('Value is found on a node with no child (Leaf node).')
                    if parent_node is None:  # Check to see if the node found is the root node.
                        current_node = None  # Set the root node to None, makes the tree empty.
                    elif current_node.data < parent_node.data:  # Check to see if the value is on the left node.
                        parent_node.left = None  # Make the left node as None.
                    elif current_node.data > parent_node.data:  # Check to see if the value is on the right node.
                        parent_node.right = None  # Make the right node as None.
                    return  # Stop processing the loop.
                # If there is one child node on the left.
                elif current_node.left is not None and current_node.right is None:
                    print('Value is found on a node with a left child.')
                    if parent_node is None:  # Check to see if the node found is the root node.
                        current_node = None  # Set the root node to None, makes the tree empty.
                    elif current_node.data < parent_node.data:  # Check to see if the value is on the left node.
                        # Replace the parents left child with the left child of current node.
                        parent_node.left = current_node.left
                    elif current_node.data > parent_node.data:  # Check to see if the value is on the right node.
                        # Replace the parents right child with the left child of the current node.
                        parent_node.right = current_node.left
                    return  # Stop processing the loop.
                # If there is one child node on the right.
                elif current_node.left is None and current_node.right is not None:
                    print('Value is found on a node with a right child.')
                    if parent_node is None:  # Check to see if the node found is the root node.
                        current_node = None  # Set the root node to None, makes the tree empty.
                    elif current_node.data < parent_node.data:  # Check to see if the value is on the left node.
                        # Replace the parents left child with the right child of the current node.
                        parent_node.left = current_node.right
                    elif current_node.data > parent_node.data:  # Check to see if the value is on the right node.
                        # Replace the parents right child with the right child of the current node.
                        parent_node.right = current_node.right
                    return  # Stop processing the loop.
                # If both the child are present.
                elif current_node.left is not None and current_node.right is not None:
                    print('Value is found on a node with a left child and a right child.')
                    # Set the replacement node start as the right child of current node.
                    replacement_node = current_node.right
                    # Set the replacement node parent as the current node.
                    replacement_node_parent = current_node
                    while replacement_node.left is not None:  # Loop until there is no leftmost node of the right child.
                        replacement_node_parent = replacement_node
                        replacement_node = replacement_node.left
                    print(replacement_node, "was found as a replacement for", current_node.data)
                    # Copy the value of the replacement node to the node to be replaced.
                    current_node.data = replacement_node.data

                    # If the replacement node ends up just being the right child, replace with the right child, this
                    # also takes care of the right child's right subtree.
                    if replacement_node == current_node.right:
                        current_node.right = replacement_node.right
                    # If the replacement node is a left node, the right subtree of this node, if present, becomes the
                    # left subtree of the parent node.
                    elif replacement_node.data < replacement_node_parent.data:
                        replacement_node_parent.left = replacement_node.right
                return
        print(value, "is not found in the binary search tree.")
        return False

    # Method to perform a lookup of a value in the Binary Search Tree.
    def lookup(self, value):
        if not self.root:  # Check to see if the BST is empty.
            print("Binary tree is empty.")
            return False
        current_node = self.root  # Set the current node as the root node.
        # Traverse the tree using the while loop until the value is found.
        while current_node is not None:
            if value == current_node.data:
                print("Found value!")
                return current_node  # Return the node with the value.
            elif value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
        print("Nothing found!")
        return False  # Return False if nothing is found.

    # Reference to the function below. It is used to visualize the methods of the class BinarySearchTree.
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
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

    # Method for tree traversal. We assign the result of the recursive call to the dictionary keys to store the value
    # and make the dictionary data structure recursive along with the recursive method.
    def traverse(self, current_node=None):
        if not current_node:
            current_node = self.root
        tree = {'data': current_node.data}
        if current_node.left:
            tree.update({'left': self.traverse(current_node.left)})
        if current_node.right:
            tree.update({'right': self.traverse(current_node.right)})
        return tree


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
my_BST.insert(25)
my_BST.insert(30)
my_BST.insert(35)
my_BST.insert(27)
print(my_BST.traverse())
my_BST.lookup(9)
my_BST.delete(20)
my_BST.insert(79)
my_BST.delete(73)
my_BST.delete(20)
my_BST.delete(25)
my_BST.delete(15)
my_BST.delete(27)
my_BST.delete(30)
my_BST.delete(5)
my_BST.delete(10)
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

# Function to traverse the tree. Initial attempt to write the traversal function but the values are not stored.
# def traverse(self, current_node):
#     if current_node == self.root:
#         tree = {'root': current_node.data}
#     print(tree)
#     if current_node.left is not None:
#         tree.update({'left': current_node.left.data})
#         print(tree)
#         self.traverse(current_node.left)
#     if current_node.right is not None:
#         tree.update({'right': current_node.right.data})
#         print(tree)
#         self.traverse(current_node.right)
#     return tree

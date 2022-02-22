"""
Implementation of Array from the ground up. We have lists in python that compares to an array data structure and should
be used instead of building an array data structure from scratch.
"""


class Array:
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    def __init__(self):
        self.length = 0
        self.data = {}


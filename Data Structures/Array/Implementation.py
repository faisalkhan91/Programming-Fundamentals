"""
Implementation of Array from the ground up. We have lists in python that compares to an array data structure and should
be used instead of building an array data structure from scratch.
"""


class Array:
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    def __init__(self):
        self.length = 0  # Initialize the length of the array
        self.data = {}  # Initialize the data dictionary which will hold the indexes and the strings

    # This method is customization of the string representation of an instance of a class.
    def __str__(self):
        return str(self.__dict__)

    # This method returns the string corresponding to a given index.
    def get(self, index):
        return self.data[index]  # O(1)

    # This method adds a value at the end of the array.
    def push(self, item):
        self.data[self.length] = item  # Add item to the end. O(1)
        self.length += 1  # Increases array size by 1

    # This method removes the last added item.
    def pop(self):
        last_item = self.data[self.length-1]  # Stores value of last item.
        del self.data[self.length-1]  # Deletes the item at the end. O(1)
        self.length -= 1  # Decreases array size by 1.
        return last_item  # Return deleted item.

    # This method inserts an item at a specified index.
    def insert(self, index, item):
        self.length += 1  # Increases array length by 1.
        self.shift_items(index, 'Insert')  # Calls shift_items method to move all the elements. O(n)
        self.data[index] = item  # Insert the item.
        return item

    # This method deletes an item at a specified index.
    def delete(self, index):
        deleted_item = self.data[index]  # Stores deleted item value.
        self.shift_items(index, 'Delete')  # Calls shift_items method to move all the elements. O(n)
        del self.data[self.length - 1]  # Deletes item at the end.
        self.length -= 1  # Decreases array size by 1.
        return deleted_item  # Returns deleted item.

    # This method shifts items to the right or to the left based on the method calling it to insert or delete an item
    # respectively.
    def shift_items(self, index, flag):
        # If flag is 'Insert' the loop moves the items to the right starting from the end of the array until it reaches
        # the index position. O(n)
        if flag == 'Insert':
            for i in reversed(range(index, self.length)):
                self.data[i] = self.data[i - 1]
        # If flag is 'Delete' the loop moves the items to the left starting from the index position until it reaches
        # to the end of the array. O(n)
        elif flag == 'Delete':
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]


# Declaration
arr = Array()
arr.push('hi')
arr.push('how')
arr.push('you')
arr.push('doing')
arr.pop()
arr.delete(2)
arr.insert(2, 'me')
arr.insert(3, 'and you')
print(arr)

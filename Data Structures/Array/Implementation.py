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

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1



# Declaration
arr = Array()
arr.push('hi')
arr.push('how')
arr.push('you')
arr.push('doing')
#arr.pop()
arr.delete(2)

for i in range(0, arr.length):
    print(arr.get(i))




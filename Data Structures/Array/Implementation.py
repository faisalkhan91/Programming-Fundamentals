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

    def __str__(self):
        return str(self.__dict__)

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
        deleted_item = self.data[index]
        self.shift_items(index, 'Delete')
        del self.data[self.length - 1]
        self.length -= 1
        return deleted_item

    def shift_items(self, index, flag):

        if flag == 'Insert':
            for i in reversed(range(index, self.length)):
                self.data[i] = self.data[i - 1]

        elif flag == 'Delete':
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]

    def insert(self, index, item):
        inserted_item = item
        self.length += 1
        self.shift_items(index, 'Insert')
        self.data[index] = item
        return inserted_item


# Declaration
arr = Array()
arr.push('hi')
arr.push('how')
arr.push('you')
arr.push('doing')
#arr.pop()
arr.delete(2)
arr.insert(2, 'me')
arr.insert(3, 'and you')

# for i in range(0, arr.length):
#     print(arr.get(i))

print(arr)




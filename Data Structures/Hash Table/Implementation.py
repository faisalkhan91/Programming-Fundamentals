"""
Implementation of Hash Table Data Structure in python. In python, dictionary is a comparable data structure and should
be used whenever hash table is needed.
"""


# Class containing the data initialization to store the information in a hash table.
class HashTable:
    def __init__(self, size):
        self.data = [None] * size  # This will create a list (or array) of given size and initialize all slots to None.

    '''
    This method is used to print the attributes of the class object in a dictionary format.
    This way you can use 'print(hash_table)' command to get the value in readable format.
    Another way to access the information will be to specify the variable. For example, print(hash_table.data).
    This way we do not need to initialize the __str__ to display object query in dictionary format.
    '''
    def __str__(self):
        return str(self.__dict__)

    # Although there is a loop in this hash function it's BigO seems to be O(n) but hash functions are usually very fast
    # therefore we consider this hash function to be O(1).
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    # BigO(1)
    def set(self, key, value):
        address = self._hash(key)
        item = [key, value]
        # If there is no data present at the address calculated by hash function, we simply add the data.
        if self.data[address] is None:
            self.data[address] = [item]  # This will place the data in the position generated by hash function.
        # If there is data present at the address calculated by hash function, which implies a collision, we append the
        # data to the sub array at the location.
        else:
            self.data[address].append(item)

    # BigO(1) - Most of the time this is O(1), because collisions don't happen often.
    # BigO(n) - But have a small size and large data can cause a lot of collisions and that can make this method O(n).
    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket is not None:
            for data in current_bucket:
                if data[0] == key:
                    return data[1]
        return None


# Declaration
hash_table = HashTable(size=2)
hash_table.set('grapes', 1000)
hash_table.set('orange', 5)
# print(hash_table)
print(hash_table.get('grapes'))

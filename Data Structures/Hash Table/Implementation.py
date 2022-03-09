"""
Implementation of Hash Table Data Structure in python. In python, dictionary is a comparable data structure and should
be used whenever hash table is needed.
"""


# Class containing the data initialization to store the information in a hash table.
class HashTable:
    def __init__(self, size=0):
        self.data = [None] * size  # This will create a list (or array) of given size and initialize all slots to None.

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        item = [key, value]
        self.data.append(item)

    def get(self, key):
        value = self.data[HashTable._hash(self, key)]
        print(value)


# Declaration
hash_table = HashTable()
# print(hash_table._hash(['1']))
hash_table.set('grapes', 1000)
#print(hash_table.data)
print(hash_table.get('grapes'))

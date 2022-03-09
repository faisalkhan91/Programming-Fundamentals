"""
Implementation of Hash Table Data Structure in python. In python, dictionary is a comparable data structure and should
be used whenever hash table is needed.
"""


# Class containing the data initialization to store the information in a hash table.
class HashTable:
    def __init__(self):
        self.data = []

    def hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + chr(key[i]) * i) % len(self.data)

        return hash_value


# Declaration
hash_table = HashTable()
print(hash_table.hash([1]))

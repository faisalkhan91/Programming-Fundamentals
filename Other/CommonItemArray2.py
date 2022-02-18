# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any
# common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# should return true.

# 2 parameters - arrays - no size limit
# return true or false

# Function Definition
def find_common(list_1, list_2):
    hash_map = {}
    for element in range(0, len(list_1)):  # O(n)
        hash_map[list_1[element]] = True

    for element in list_2:  # O(m)
        if element in hash_map.keys():
            print('Found :', element)


# Declarations
list1 = ['a', 'b', 'c', 'x']
list2 = ['z', 'y', 'x']

find_common(list1, list2)

# BigO(m+n)

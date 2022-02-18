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
def find_common(list1, list2):
    for i in list1:  # O(m)
        for j in list2:  # O(n)
            if i == j:
                print('Common element is :', i)
                return True
    return False


# Declarations
list1 = ['a', 'b', 'c', 'x']
list2 = ['z', 'y', 'x']

find_common(list1, list2)

# BigO(m*n)

"""
Given an array, find the first recurring character in an array.
For example:
array a = [2,5,1,2,3,5,1,2,4], in this case the first recurring character is 2.
array b = [2,1,1,2,3,5,1,2,4], in this case the first recurring character is 1.
array c = [2,3,4,5], in this case it should return undefined.
array d = [2,5,5,2,3,5,1,2,4], in this case we should return 5.
"""


# Function definition

def first_recurring_character(array):
    first_recurring = 0
    array_map = {}
    for i in range(len(array)):
        if array[i] not in array_map:
            array_map[array[i]] = 1
        else:
            first_recurring = array[i]
            break
    if first_recurring > 0:
        return first_recurring
    else:
        return None


# The below function has a time complexity of O(n^2) since we are looping through the array twice.
def naive_first_recurring_character(array):
    for i in range(len(array)):  # Take the element in the array at position i.
        for j in range(i+1, len(array)):  # Take the element in the array at position i+1, i.e. start from right of i.
            if array[i] == array[j]:
                return array[i]
    return None


# Declaration

arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# character = first_recurring_character(arr)
character = naive_first_recurring_character(arr)
print(character)

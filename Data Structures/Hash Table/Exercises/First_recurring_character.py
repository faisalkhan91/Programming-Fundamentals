"""
Given an array, find the first recurring character in an array.
For example:
array a = [2,5,1,2,3,5,1,2,4], in this case the first recurring character is 2.
array b = [2,1,1,2,3,5,1,2,4], in this case the first recurring character is 1.
array c = [2,3,4,5], in this case it should return undefined.
array d = [2,5,5,2,3,5,1,2,4], in this case we should return 5.
"""


# Function definition


# The below function has a time complexity of O(n^2) since we are looping through the array twice.
def naive_first_recurring_character(array):
    for i in range(len(array)):  # Take the element in the array at position i.
        for j in range(i+1, len(array)):  # Take the element in the array at position i+1, i.e. start from right of i.
            if array[i] == array[j]:
                return array[i]
    return None


# This is my first attempt to solve the problem using hash table.
# The time complexity of the below algorithm is O(n). Space complexity is O(1).
def first_recurring_character(array):
    first_recurring = 0  # Initialize the variable that will store the recurring element.
    array_map = {}  # Create a dictionary to store array in hash table data structure.
    for i in range(len(array)):
        if array[i] not in array_map:  # If the element in the array is not in dictionary add to dictionary.
            array_map[array[i]] = 1  # Here 1 is indicated for number of times present in dictionary.
        else:
            first_recurring = array[i]  # If the array is in dictionary, this means it is first recurring.
            break  # Stop processing.
    if first_recurring > 0:
        return first_recurring
    else:
        return None


# This is Andrei's attempt using hash table. The time complexity of the method is O(n) and the space complexity is O(n)
def first_recurring_character_2(array):
    array_map = dict()  # Can also be declared using {}.
    for i in range(len(array)):
        if array[i] in array_map:
            return array[i]
        else:
            array_map[array[i]] = i
        print(array_map)
    return None


# Declaration

arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# character = naive_first_recurring_character(arr)
# character = first_recurring_character(arr)
character = first_recurring_character_2(arr)
print(character)

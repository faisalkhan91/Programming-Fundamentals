"""
Implementation of the Selection Sort algorithm in python. In selection sort algorithm the function finds the smallest
item in the array and swaps with the current position of the index in the array.

Selection sort has the time complexity of O(n^2) since there are two loops. Space complexity is O(1) since there
are no new data structures to store information.
"""


# Function definition

def selection_sort(array):
    for i in range(len(array)-1):
        index = 0
        smallest = array[i]
        for j in range(len(array)-1):
            index += 1
            if smallest > array[j]:
                smallest = array[j]
        temp = array[i]
        array[i] = smallest
        array[index] = temp
    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(to_sort))

"""
Implementation of the insertion sort algorithm in python.

"""


# Function Definition

def insertion_sort(array):
    for i in range(1, len(array)):
        index = i
        for j in reversed(range(1, i)):
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
    return array


# Declaration

to_sort = [4, 3, 1, 5, 6, 2]
print(insertion_sort(to_sort))

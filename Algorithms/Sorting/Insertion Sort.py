"""
Implementation of the insertion sort algorithm in python.

Time complexity of Insertion Sort Algorithm is O(n^2) and the algorithm is fast when the array is already sorted.
"""


# Function Definition

# Reference:
# https://stackoverflow.com/questions/72987595/implementation-of-insertion-sort-algorithm-in-python/72989757#72989757
def insertion_sort_initial(array):
    for i in range(1, len(array)):
        for j in reversed(range(1, i+1)):
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
    return array


def insertion_sort_optimized(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] <= array[j]:
                break
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
    return array


def insertion_sort_optimized(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] <= array[j]:
                break
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
    return array

# Declaration

to_sort = [4, 3, 1, 5, 6, 2]
print(insertion_sort_optimized(to_sort))

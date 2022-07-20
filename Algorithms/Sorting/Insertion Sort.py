"""
Implementation of the insertion sort algorithm in python. In insertion sort algorithm the array is divided into sorted
and unsorted part and each element is compared ot the sorted part and inserted in the correct order.

Time complexity of Insertion Sort Algorithm is O(n^2) and the algorithm is fast when the array is already sorted as the
time complexity is O(n) in that case. Space complexity is O(1) as no new data structures are created.
"""


# Function Definition

# Initial attempt to create an insertion sort algorithm.
def insertion_sort_initial(array):
    for i in range(1, len(array)):  # Keep track of the sorted part of the array.
        for j in reversed(range(1, i+1)):  # Loop to insert into the correct position in the array.
            if array[j-1] > array[j]:  # Keep swapping until the element to the right is smaller than the current one.
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
    return array


# Optimized version of the code to reduce swaps if the element is on the left is smaller than the right element, i.e. an
# already sorted array.
# Reference:
# https://stackoverflow.com/questions/72987595/implementation-of-insertion-sort-algorithm-in-python/72989757#72989757
def insertion_sort_optimized(array):
    for i in range(1, len(array)):  # Keep track of the sorted part of the array.
        for j in range(i, 0, -1):  # Loop to insert into the correct position in the array.
            if array[j-1] <= array[j]:  # If the array to sort is larger than the array on the left, exit loop.
                break
            # Do swap
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
    return array


# Declaration

to_sort = [4, 3, 1, 5, 6, 2]
print(insertion_sort_optimized(to_sort))

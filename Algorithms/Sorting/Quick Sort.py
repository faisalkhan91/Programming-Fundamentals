"""
Implementation of Quick Sort algorithm in python. The sorting technique used in this sort is to select a pivot randomly
and move items smaller than the pivot to left and items greater than the pivot to the right, then divide and conquer
strategy is used divide into smaller sub arrays and sorted in a similar fashion using a pivot until the sub array is
sorted.

The time complexity of Quick Sort algorithm is O(nlogn). Space complexity is O(logn).
"""


# Function Definition


def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, partition_index)
            partition_index += 1
    swap(array, right, partition_index)
    return partition_index


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def quick_sort(array, left, right):

    pivot = 0
    partition_index = 0

    if left < right:
        pivot = right
        partition_index = partition(array, pivot, left, right)

        quick_sort(array, left, partition_index-1)
        quick_sort(array, partition_index+1, right)

    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(to_sort, 0, len(to_sort)-1))

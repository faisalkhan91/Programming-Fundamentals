"""
Implementation of Quick Sort algorithm in python. The sorting technique used in this sort is to select a pivot randomly
and move items smaller than the pivot to left and items greater than the pivot to the right, then divide and conquer
strategy is used divide into smaller sub arrays and sorted in a similar fashion using a pivot until the sub array is
sorted.

The time complexity of Quick Sort algorithm is O(nlogn). Space complexity is O(logn).
"""


# Function Definition

def quick_sort(array):
    pivot = array[0]

    for i in range(1, len(array)):
        if array[i] < pivot:
            temp = array[i]
            array[i] = pivot
            array[0] = temp

    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(to_sort))

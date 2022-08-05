"""
Implementation of Quick Sort algorithm in python. The sorting technique used in this sort is to select a pivot randomly
and move items smaller than the pivot to left and items greater than the pivot to the right, then divide and conquer
strategy is used divide into smaller sub arrays and sorted in a similar fashion using a pivot until the sub array is
sorted.

The time complexity of Quick Sort algorithm is O(nlogn). Space complexity is O(logn).
"""


# Function Definition

def quick_sort(array, left, right):

    if len(array) < 2:
        return array

    pivot = array[0]
    pivot_index = 0

    for i in range(1, len(array)):
        if array[i] < pivot:
            temp = array[i]
            array[i] = pivot
            array[i-1] = temp
            pivot_index = i-1
        elif array[i] >= pivot:
            pass

        left = array[:pivot_index]
        right = array[pivot_index:]

    return quick_sort(left), quick_sort(right)


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(to_sort))

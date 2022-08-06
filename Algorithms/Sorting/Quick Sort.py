"""
Implementation of Quick Sort algorithm in python. The sorting technique used in this sort is to select a pivot randomly
and move items smaller than the pivot to left and items greater than the pivot to the right, then divide and conquer
strategy is used divide into smaller sub arrays and sorted in a similar fashion using a pivot until the sub array is
sorted.

The time complexity of Quick Sort algorithm is O(nlogn). Space complexity is O(logn). Worst case time complexity of a
quick sort algorithm is O(n^2).

Reference: https://www.youtube.com/watch?v=9KBwdDEwal8
"""


# Function Definition

# Method to find the position of the pivot and return it as the index where to partition from.
def partition(array, pivot, left, right):
    pivot_value = array[pivot]  # Get the pivot from the chosen pivot index.
    partition_index = left  # Set partition index start as the left.

    # Move the elements in the array less than the pivot value to left and this automatically pushes the elements
    # greater than pivot value to the right.
    for i in range(left, right):
        if array[i] < pivot_value:  # If the element in the array is less than pivot value.
            swap(array, i, partition_index)  # Call the swap method to swap array with the current partition index.
            partition_index += 1  # Increment the partition index.
    # Do one last swap to swap the pivot value with the partition index to put the pivot value after all the values in
    # the array that are smaller than it.
    swap(array, right, partition_index)
    return partition_index  # Return the partition index, i.e. the index value of the pivot in its correct place.


# Method to swap the array elements.
def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


# Method to sort the array using quick sort. In this implementation we are setting the pivot as the last element in the
# array.
def quick_sort(array, left, right):

    # Base case, as long as the left index is not greater than right index.
    if left < right:
        pivot = right  # Set the pivot as the last element in the array, i.e. the index of the last item in the array.
        partition_index = partition(array, pivot, left, right)  # Get the partition index to know where to divide.

        # Recursive case, Split the array into left and right and call them recursively.
        quick_sort(array, left, partition_index-1)
        quick_sort(array, partition_index+1, right)

    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# Call the function by sending the array and left and right index values that are the first and last element in the
# array.
sorted_array = quick_sort(to_sort, 0, len(to_sort)-1)
print(sorted_array)

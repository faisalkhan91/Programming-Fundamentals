"""
Implementation of the Selection Sort algorithm in python. In selection sort algorithm the function finds the smallest
item in the array and swaps with the current position of the index in the array.

Selection sort has the time complexity of O(n^2) since there are two loops. Space complexity is O(1) since there
are no new data structures to store information.
"""


# Function definition

# Initial implementation of the selection sort algorithm, the time complexity is O(n^2) and the space complexity is O(n)
# since we are not using any more data structure to store information. This implementation has been answered in stack
# overflow: https://stackoverflow.com/questions/72904645/selection-sort-implementation-in-python
def selection_sort_initial(array):
    for i in range(len(array)):
        index = i  # Start with the current i as it indicates where the smallest element comes from.
        smallest = array[i]  # To store the first element in the iteration of the loop, the first smallest.
        for j in range(i+1, len(array)):
            if array[j] < smallest:  # If the next element is smaller than the current smallest, make it the smallest.
                smallest = array[j]
                index = j  # Set index of the new smallest element.
        # Swap the smallest element with the current i.
        temp = array[i]
        array[i] = smallest
        array[index] = temp
    return array


# Andrei's implementation of the selection sort method, it is similar to the previous implementation, the exception
# being that it does not store the smallest element in a separate variable and uses the index to track the smallest
# element.
def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        temp = array[i]
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i] = array[minimum]
        array[minimum] = temp
    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(to_sort))

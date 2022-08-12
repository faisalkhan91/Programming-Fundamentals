"""
Implementation of Binary Search algorithm in python. Time complexity of a Binary Search algorithm is O(logn).
"""


# Function Definition

# Reference: https://stackoverflow.com/questions/73315133/efficiency-analysis-of-binary-search-implementation-in-python
# Method to perform binary search operation.
def binary_search(array, search):
    low = 0  # Starting index
    high = len(array)  # Index of last element in array.

    # Loop until the low and high indexes don't overlap and the length of the array being searched is not 0.
    while low <= high and len(array[low:high]):
        mid = (low + high) // 2
        if array[mid] == search:  # If the element being searched is found.
            return "Found " + str(search) + " at index " + str(mid)  # Return the index
        elif search > array[mid]:  # If the element to be found is larger that the middle element.
            low = mid + 1  # The low index starts to the right of the middle element.
        elif search < array[mid]:  # If the element to be found is smaller that the middle element.
            high = mid - 1  # The high index ends to the left of the middle element.

    return str(search) + " not found."


# Declaration

search_through = [2, 3, 4, 10, 40]
to_search = 49
print(binary_search(search_through, to_search))

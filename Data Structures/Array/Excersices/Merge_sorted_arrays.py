"""
Given two sorted arrays, can you merge them into one so that the merged one is also sorted.
For Example:
    - Sorted array 1 is [0,3,4,5] and sorted array 2 is [4,6,30], the resulting merged array will be as:
      [0,3,4,4,6,30,31]
"""


# Function Definitions
# Initial attempt to write a function that returns a sorted array. The output is NOT CORRECT.
def merge_sorted_arrays(array_1, array_2):
    merged = []
    for i in array_1:
        for j in array_2:
            if i <= j:
                merged.append(i)
                break
            else:
                merged.append(j)
                break
    return merged


# This is the method based on Andrei's solution.
def merge_sorted_arrays_2(array_1, array_2):

    # Checks for input validation
    if
    return 0


# Declarations
array1 = [0, 3, 4, 5]
array2 = [4, 6, 30]
# array3 = merge_sorted_arrays(array1, array2)
array3 = merge_sorted_arrays_2(array1, array2)
print(array3)

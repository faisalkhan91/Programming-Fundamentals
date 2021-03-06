"""
Given two sorted arrays, can you merge them into one so that the merged one is also sorted.
For Example:
    - Sorted array 1 is [0,3,4,5] and sorted array 2 is [4,6,30], the resulting merged array will be as:
      [0,3,4,4,5,6,30]
"""


# Function Definition

# Initial attempt to write a function that returns a sorted array. The output is NOT CORRECT.
def merge_sorted_arrays(array_1, array_2):
    merged = []
    i = 0
    j = 0

    # O(m+n)
    while len(array_1) > i and len(array_2) > j:
        if array_1[i] < array_2[j]:  # If value in array 1 is less than value in array 2.
            merged.append(array_1[i])
            i += 1
        elif array_1[i] > array_2[j]:  # If value in array 2 is less than value in array 1.
            merged.append(array_2[j])
            j += 1
        elif array_1[i] == array_2[j]: # If value in array 1 is equal to value in array 2.
            merged.append(array_2[j])
            merged.append(array_1[i])
            i += 1
            j += 1
    return merged + array_1[i:] + array_2[j:]  # Join the array that has not been emptied since all elements are sorted.


# This is the method based on Andrei's solution.
def merge_sorted_arrays_2(array_1, array_2):
    merged_array = []
    array_1_item = array_1[0]
    array_2_item = array_2[0]
    i = 0
    j = 0
    # Checks for input validation
    if array_1 == array_2 == []:
        return 'No values in array!'
    elif len(array_1) <= 0 or len(array_2) <= 0:
        return array_1 + array_2

    try:
        while array_1_item or array_2_item:
            if array_1_item < array_2_item:
                merged_array.append(array_1_item)
                i += 1
                array_1_item = array_1[i]
            else:
                merged_array.append(array_2_item)
                j += 1
                array_2_item = array_2[j]
    except IndexError:
        merged_array = merged_array + array_1[i:] + array_2[j:]
    return merged_array


# This is the pythonic way for the output using sorted function.
def merge_sorted_arrays_3(array_1, array_2):
    merged_array = array_1 + array_2
    return sorted(merged_array)


# Declarations
array1 = [0, 3, 4, 5]
array2 = [4, 6, 30]
# array3 = merge_sorted_arrays(array1, array2)
array3 = merge_sorted_arrays_2(array1, array2)
# array3 = merge_sorted_arrays_3(array1, array2)
print(array3)

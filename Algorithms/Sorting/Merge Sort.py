"""
Implementation of Merge Sort algorithm in python. In this type of sorting the unsorted array is
divided into subsets of smaller array using recursive function. Then the subsets are compared and 
combined in a sorted order to give sorted array as a whole.

Time Complexity of merge sort algorithm is O(nlogn) and Space Complexity is O(n).
"""


# Function definition

def merge_sort(array):
    # Base Case
    if len(array) < 2:
        return array
    
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(left, right)


def merge(left, right):
    if len(left) or len(right) < 2:
        return left or right

    i, j = 0, 0
    output = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
        elif right[j] < left[i]:
            output.append(right[j])

    output.extend(left[i:])
    output.extend((right[j:]))

    return output


# Declaration

to_sort = [2, 5, 3, 4, 1]
print(merge_sort(to_sort))

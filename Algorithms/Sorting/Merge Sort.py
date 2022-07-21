"""
Implementation of Merge Sort algorithm in python. In this type of sorting the unsorted array is
divided into subsets of smaller array using recursive function. Then the subsets are compared and 
combined in a sorted order to give sorted array as a whole.

Time Complexity of merge sort algorithm is O(nlogn) and Space Complexity is O(n).
"""


# Function definition


def merge_sort(array):
    # Base case
    if len(array) < 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle+1:]
    # Recursive case
    return merge(merge_sort(left), merge_sort(right))

def merge(left_array, right_array):
    print(left_array)
    print(right_array)



# Declaration

to_sort = [2,4,3,1,5]
print(merge_sort(to_sort))

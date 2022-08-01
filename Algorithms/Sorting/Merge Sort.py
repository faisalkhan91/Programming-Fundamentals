"""
Implementation of Merge Sort algorithm in python. In this type of sorting the unsorted array is divided into subsets of
smaller array using recursive function. Then the subsets are compared and combined in a sorted order to give sorted
array as a whole. This strategy is called divide and conquer and merge sort uses it to quickly sort an input.

Time Complexity of merge sort algorithm is O(nlogn) and Space Complexity is O(n).
"""


# Function definition

# Method to divide the array into subsets of the array and then call the merge method to merge the subsets in order.
def merge_sort(array):
    # Base Case
    # If the length of the array, or the subset of that array specifically has 1 or fewer items, then the base case is
    # triggered and the array is returned to the order of the latest method call in the stack.
    if len(array) < 2:
        return array
    
    middle = len(array) // 2  # To find the middle of the array for the split.
    left = merge_sort(array[:middle])  # Left side of the array from the middle.
    right = merge_sort(array[middle:])  # Right side of the array.

    # Recursive case
    return merge(left, right)  # Call merge method to sort and merge the subsets or the array.


# Method to merge the subsets of the array in order and return the merged array.
def merge(left, right):
    # If there is no left or right array, return whatever is there in left or right.
    if not left or not right:
        return left or right

    left_index, right_index = 0, 0  # Index to keep track of the compared element.
    sorted_list = []  # List to store the sorted array.

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:  # If the left element is less than the right
            sorted_list.append(left[left_index])  # Add the left element to the sorted list.
            left_index += 1  # Increment left index
        elif right[right_index] < left[left_index]:  # If the right element is less that left element.
            sorted_list.append(right[right_index])  # Add the right element to the sorted list.
            right_index += 1  # Increment right index by one.

    # Add the remaining items left in the array after either the left or the right array is exhausted.
    sorted_list.extend(left[left_index:])
    sorted_list.extend((right[right_index:]))

    return sorted_list  # Return the sorted list.


# Declaration

# to_sort = [2, 5, 3, 4, 1]
to_sort = [8, 5, 9, 1, 3, 4, 0]
print(merge_sort(to_sort))

"""
Implementation of the Bubble Sort algorithm in python. In bubble sort algorithm two adjacent elements are compared and
swapped if the value of the latter element is less than or greater than the preceding element, depending on the
implementation of the sorting algorithm, to give the solution in ascending or descending order.

In classical bubble sort the time complexity is O(n^2) since there are two loops. Space complexity is O(1) since there
are no new data structures to store information. Time complexity of a bubble sort can be made to be O(n) by implementing
an optimized algorithm that will stop the inner loop if no swap is made.
"""


# Function definition

# This is the classical bubble sort algorithm implementation. Time complexity of the algorithm is O(n^2), and the space
# complexity is O(n). len(array)-1 is because last element does not need to be sorted.
def bubble_sort_classic(array):
    for i in range(len(array)-1):  # Number of times to go through the array, which is the length of the array.
        for j in range(len(array)-1):  # Compare each adjacent element in the array in each cycle of the previous loop.
            # Perform swap if the current array element is bigger than the next one.
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


# This is the optimized bubble sort algorithm where swapping is tracked using a boolean variable. If no swap has
# occurred in previous iteration then the array is sorted and the method stops processing.
def bubble_sort_optimized(array):
    for i in range(len(array)-1):  # Number of times to go through the array, which is the length of the array.
        swap = False  # Boolean to track the swap.
        for j in range(len(array)-1):  # Compare each adjacent element in the array in each cycle of the previous loop.
            # Perform swap if the current array element is bigger than the next one.
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swap = True
        if swap is False:
            break
    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Bubble sort classic method:", bubble_sort_classic(to_sort))
print("Bubble sort optimized method:", bubble_sort_optimized(to_sort))

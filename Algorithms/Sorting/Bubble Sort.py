"""
Implementation of the Bubble Sort algorithm in python. In bubble sort algorithm two adjacent elements are compared and
swapped if the value of the latter element is less than or greater than the preceding element, depending on the
implementation of the sorting algorithm, to give the solution in ascending or descending order.

In classical bubble sort the time complexity is O(n^2) since there are two loops. Space complexity is O(1) since there
are no new data structures to store information. Time complexity of a bubble sort can be made to be O(n) by implementing
an optimized algorithm that will stop the inner loop if no swap is made.
"""


# Function definition

# Classical bubble sort algorithm implementation.
# Test
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(to_sort))

"""
Implementation of the Bubble Sort algorithm in python.
"""


# Function definition

def bubble_sort(array):
    temp = []
    for i in range(len(array)):
        for j in range(len(array[1:])):
            if array[i] < array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

    return array


# Declaration

to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(to_sort))

"""
Implementation of the insertion sort algorithm in python.

"""


# Function Definition

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while 0 <= j <= i:
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array





# Declaration

to_sort = [4, 3, 1, 5, 6, 2]
print(insertion_sort(to_sort))

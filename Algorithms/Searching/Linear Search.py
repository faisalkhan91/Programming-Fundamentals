"""
Implementation of a linear search method in python. Time complexity of the algorithm is O(1) in best case scenario and
O(n) in worst case scenario.
"""


# Function Definition

# Method to perform a linear search on an array.
def linear_search(array, search):

    for i in range(len(array)):
        if array[i] == search:  # If array is found return the index.
            return "Found " + search + " at index " + str(i)
    return search + " not found"


# Declaration
search_through = ['c', 'w', 'i', 'f', 't', 's']
to_search = 'z'  # Element to be searched.
print(linear_search(search_through, to_search))

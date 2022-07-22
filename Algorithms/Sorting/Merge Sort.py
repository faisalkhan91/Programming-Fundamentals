"""
Implementation of Merge Sort algorithm in python. In this type of sorting the unsorted array is
divided into subsets of smaller array using recursive function. Then the subsets are compared and 
combined in a sorted order to give sorted array as a whole.

Time Complexity of merge sort algorithm is O(nlogn) and Space Complexity is O(n).
"""

"""

Implementation of Merge Sort algorithm in python. In this type of sorting the unsorted array is

divided into subsets of smaller array using recursive function. Then the subsets are compared and 

combined in a sorted order to give sorted array as a whole.


Time Complexity of merge sort algorithm is O(nlogn) and Space Complexity is O(n).

"""



# Function definition



from turtle import left, right

from xxlimited import new


from pandas import array



def merge_sort(array):

# Base case

if len(array) <= 1:

return array


middle = len(array) // 2

left = array[:middle]

right = array[middle:]

print("array:", array)

print("middle", middle)

# Recursive case

return merge(merge_sort(left), merge_sort(right))



def merge(left_array, right_array):

print("------Run-----")

print("left:", left_array)

print("right:", right_array)


new_list = []


i = 0

j = 0

k = 0


while i < len(left_array) and j < len(right_array):

if left_array[i] <= right_array[j]:

new_list.append(left_array[i])

i =+ 1

else:

new_list.append(right_array[j])

j =+ 1

return new_list




# Declaration


to_sort = [2,4,3,1,5]

print(merge_sort(to_sort))




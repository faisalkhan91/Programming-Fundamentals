"""
704. Binary Search
https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums, target):

        low = 0  # Set low as index 0
        high = len(nums) - 1  # Set high as length of array - 1

        while low <= high:
            mid = (low + high) // 2  # Calculate the mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:  # If the value at mid-index is less than the target value search on the right.
                low = mid + 1
            else:
                high = mid - 1

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
execute = Solution()
print(execute.search(nums, target))

"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""


# Time complexity is O(n).
class Solution:
    def runningSum(self, nums):
        # If the array is empty, quit processing.
        if len(nums) == 0:
            return
        sum = []
        for i in range(len(nums)):
            # If there is no first element in the array, add the first element to the result array.
            if len(sum) == 0:
                sum.append(nums[i])
            else:
                sum.append(nums[i] + sum[i-1])  # Keep adding the subsequent sums.
        return sum

# Alternative solution, might be a little faster.
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         if len(nums) == 0:
#             return
#         sum = [nums[0]]
#         for i in range(1, len(nums)):
#             sum.append(nums[i] + sum[i-1])
#         return sum


execute = Solution()
nums = [1, 2, 3, 4]
print(execute.runningSum(nums))

"""
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestSubarray(self, nums) -> int:
        left = 0
        right = 0
        last_zero = 0
        max_subarray = 0
        length = len(nums)

        while right < length:
            if nums[right] == 0:
                last_zero = left
                left = right + 1
            max_subarray = max(max_subarray, right - last_zero)
            right += 1

        return max_subarray


nums = [1,1,0,0,1,1,1,0,1]
execute = Solution()
print(execute.longestSubarray(nums))

####################################################################################

# This solution was an initial attempt, but it did not work.
#
# def longestSubarray(self, nums: List[int]) -> int:
#     left = 0
#     last_zero = 0
#     right = 0
#     reset = 0
#     max_subarray = 0
#
#     while right < len(nums):
#         print(left, right, right - left, nums[left:right])
#         if reset > 1:
#             left = last_zero + 1
#             last_zero = right
#             reset = 0
#         elif nums[right] == 0:
#             reset += 1
#             left = last_zero
#         max_subarray = max(max_subarray, right - left)
#         right += 1
#
#     return max_subarray

"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def increasingTriplet(self, nums) -> bool:

        left = float('inf')  # Set the left as infinity.
        right = float('inf')  # Set right as infinity.

        for i in range(len(nums)):
            if left < right < nums[i]:  # If the triplet is found return True
                return True
            elif nums[i] < left:  # If the number is less than left, make left the current number.
                left = nums[i]
            elif left < nums[i] < right:  # If the number greater than left but less than right.
                right = nums[i]

        return False  # Return False if no triplet is found.


nums = [2,1,5,0,4,6]
execute = Solution()
print(execute.increasingTriplet(nums))

#########################################################################
# This solution was the first attempt, in which the numbers were swapped based on the conditions below but it failed to
# pass all the test cases.

# def increasingTriplet(self, nums: List[int]) -> bool:
#     first = nums[0]
#     second = nums[1]
#
#     for i in range(2, len(nums)):
#         print(first, second, nums[i])
#         if first > second or first > nums[i]:
#             first = second
#             second = nums[i]
#         elif second > nums[i]:
#             if first < second:
#                 pass
#             else:
#                 second = nums[i]
#         elif first < second < nums[i]:
#             return True
#
#     return False

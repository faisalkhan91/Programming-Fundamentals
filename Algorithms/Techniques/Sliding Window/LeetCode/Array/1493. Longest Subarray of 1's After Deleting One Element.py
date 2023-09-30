"""
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestSubarray(self, nums) -> int:
        """
        In this solution, sliding window with 3 pointers is used, the left, right and last_zero, respectively. The left
        pointer keeps track of the current zero or the latest zero encountered, the last_zero keeps track of the
        previous location of the left pointer, i.e., the element after the last zero. We track the length of the sliding
        window and return the maximum length encountered as this is the window with the largest substring with 1's after
        deleting a 0.

        Time Complexity: O(n), Space Complexity: O(1)
        :param nums:
        :return: max_substring
        """
        left = 0  # Current zero pointer.
        right = 0  # Array traversal pointer.
        last_zero = 0  # Element after the last zero pointer.
        max_subarray = 0  # Largest sliding window encountered.
        length = len(nums)

        while right < length:
            if nums[right] == 0:  # If the right pointer encounters a 0.
                last_zero = left  # Note down the position of the last zero.
                left = right + 1  # Make the left pointer note down the current zero.
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

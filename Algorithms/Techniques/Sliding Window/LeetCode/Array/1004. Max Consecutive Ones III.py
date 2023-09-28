"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestOnes(self, nums, k: int) -> int:
        """
        This solution uses the sliding window technique.
        :param nums:
        :param k:
        :return:
        """

        left = 0  # Left side of the window.
        right = 0  # Right side of the window.

        while right < len(nums):
            # If the window has added a 0, reduce the value of k.
            if nums[right] == 0:
                k -= 1
            # If the value of k is less than 0, the maximum current window size has reached. When this happens, left and
            # right pointers are moved simultaneously, akin to sliding a window.
            if k < 0:
                if nums[left] == 0:  # If there are any 0's leaving the window, k is incremented.
                    k += 1
                left += 1  # Since the value of k is less than 0, we increment left.
            right += 1

        return right - left

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
execute = Solution()
print(execute.longestOnes(nums, k))

"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestOnes(self, nums, k: int) -> int:

        if 1 not in nums:
            return 0

        left = 0
        max_ones = 0

        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
            elif nums[left] == 0:
                k += 1
                left += 1
            elif k <= 0:
                left += 1

            max_ones = max(max_ones, right - left)
            print(left, right, max_ones, nums[left:right])

        return max_ones

nums = []
k = 0
execute = Solution()
print(execute.longestOnes())

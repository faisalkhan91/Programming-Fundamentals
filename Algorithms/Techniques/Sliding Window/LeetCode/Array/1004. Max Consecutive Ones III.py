"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        right = 0
        max_ones = 0

        while right < len(nums):
            if nums[right] == 0 and k > 0:
                k -= 1
                right += 1
            elif nums[right] == 0 and k == 0:
                left += 1
            current_ones = right - left
            max_ones = max(max_ones, current_ones)

        return max_ones
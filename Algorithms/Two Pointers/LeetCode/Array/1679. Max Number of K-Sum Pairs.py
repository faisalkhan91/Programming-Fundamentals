"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        operations = 0

        while left < right:
            if nums[left] + nums[right] == k:
                operations += 1
                left += 1

            if nums[left] > k:
                left += 1
            else:
                right -= 1

        return operations
"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:

        left = 0
        max_avg = 0
        current_sum = 0

        for i in range(len(nums)):
            if len(nums[:i]) < k:
                current_sum += nums[i]
                current_avg = current_sum / k
            else:
                current_sum = current_sum + nums[i] - nums[left]
                current_avg = current_sum / k
                left += 1

            if max_avg < current_sum:
                max_avg = current_sum

        return max_avg


nums = [1,12,-5,-6,50,3]
k = 4
execute = Solution()
print(execute.findMaxAverage(nums, k))

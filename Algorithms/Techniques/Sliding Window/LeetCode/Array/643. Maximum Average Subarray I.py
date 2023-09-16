"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        """
        This solution uses the sliding window technique.
        :param nums:
        :param k:
        :return:
        """

        left = 0
        right = k
        current_sum = sum(nums[left:right])
        max_avg = current_sum / k

        if len(nums) == k:
            return max_avg

        while right < len(nums):
            current_sum = current_sum + nums[right] - nums[left]
            current_avg = current_sum / k
            max_avg = max(max_avg, current_avg)
            left += 1
            right += 1

        return max_avg

    def findMaxAverage_initial(self, nums, k: int) -> float:
        """
        This solution is slow and ends in time limit exceeded.
        :param nums:
        :param k:
        :return:
        """
        left = 0
        max_avg = float("-inf")
        current_sum = 0
        current_avg = 0

        if len(nums) == k:
            return sum(nums) / k

        for i in range(len(nums)):
            if len(nums[:i]) < k:
                current_sum += nums[i]
                if len(nums[:i]) == k - 1:
                    current_avg = current_sum / k
            else:
                current_sum = current_sum + nums[i] - nums[left]
                current_avg = current_sum / k
                left += 1
            print(current_sum, current_avg, max_avg, k)
            if max_avg < current_avg:
                max_avg = current_avg

        return max_avg


nums = [1,12,-5,-6,50,3]
k = 4
execute = Solution()
print(execute.findMaxAverage(nums, k))

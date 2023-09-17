"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        """
        This solution uses the sliding window technique. We calculate the current average and compare it with the max
        average.
        :param nums:
        :param k:
        :return: max_avg
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

    def findMaxAverage_optimized(self, nums, k: int) -> float:
        """
        In this solutions the sliding window technique is used to check the maximum sum in the given array for a given
        range k. It is an optimization of the above solution.
        :param nums:
        :param k:
        :return: max_avg
        """

        left = 0
        right = k
        current_sum = max_sum = sum(nums[left:right])

        while right < len(nums):
            current_sum = current_sum + nums[right] - nums[left]  # Shift the window right
            max_sum = max(max_sum, current_sum)  # Check if this particular windows sum is greater than previous max.
            left += 1
            right += 1

        return max_sum / k

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

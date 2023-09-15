"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        """
        In this solution, the Two Pointer approach is utilized and pointers left and right are initialized from each end
        of the given array. The array is sorted and then iterated over in such a way that if the total sum of the
        elements at the given locations is greater than k, we move the right pointer to the left, and if the sum is
        less than k we move the left pointer to the right, if the sum is equal to k, it noted as one successful
        operation. Note that the total sum of the values are compared since the array is sorted and lower values are on
        the left and higher values are on the right.
        :param nums:
        :param k:
        :return: operations
        """

        left = 0
        right = len(nums) - 1
        operations = 0
        nums.sort()

        while left < right:
            total = nums[left] + nums[right]
            if total > k:  # Move the right pointer as the sum is greater in the sorted array.
                right -= 1
            elif total < k:  # Move the left pointer as the sum is lower in the sorted array.
                left += 1
            else:
                operations += 1
                left += 1
                right -= 1

        return operations


nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3
execute = Solution()
print(execute.maxOperations(nums, k))

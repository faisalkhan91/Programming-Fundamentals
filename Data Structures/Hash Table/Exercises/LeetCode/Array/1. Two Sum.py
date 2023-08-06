"""
1. Two Sum
https://leetcode.com/problems/two-sum/?envType=study-plan&envId=level-1&plan=leetcode-75
"""


class Solution:
    def twoSum(self, nums, target: int):
        """
        In this solution a hash map used to store the indexes of the values already checked by calculating their
        complement and searching it in the hash map. Complement can be calculated as target - number in array. If the
        complement is present the index is returned along with the index of the complement.
        :param nums:
        :param target:
        :return: index
        """

        index_store = {}  # Hash map to store the values.

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_store:  # Check if the complement is present in the hash map.
                return [index_store[complement], i]  # Return if present as sum of them is equal to target.
            index_store[nums[i]] = i  # Store the value of the index of the already calculated number.

        return []  # Return nothing if nothing matches the complement.

nums = [2, 7, 11, 15]
target = 9
execute = Solution()
print(execute.twoSum(nums, target))

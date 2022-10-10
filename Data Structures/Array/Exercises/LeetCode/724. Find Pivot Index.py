"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
"""


class Solution:
    def pivotIndex(self, nums):
        if len(nums) < 2:
            return -1
        pivot_index = len(nums) // 2
        for i in range(len(nums)):
            left = nums[:pivot_index]
            right = nums[pivot_index+1:]
            sum_left = self.sum_list(left)
            sum_right = self.sum_list(right)
            if sum_left == sum_right:
                return pivot_index
            elif sum_left < sum_right:
                pivot_index += 1
            else:
                pivot_index -= 1
        return -1

    def sum_list(self, to_sum):
        result = 0
        for i in to_sum:
            result = result + i
        return result

execute = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(execute.pivotIndex(nums))

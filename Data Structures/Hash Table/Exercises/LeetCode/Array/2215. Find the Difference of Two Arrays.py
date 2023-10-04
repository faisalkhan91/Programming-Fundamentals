"""
2215. Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findDifference(self, nums1, nums2):
        """
        In this solution, Hashset is used to store the values of the numbers.
        :param nums1:
        :param nums2:
        :return:
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        tmp1 = []
        tmp2 = []

        for i in nums1:
            if i not in nums2:
                tmp1.append(i)

        for i in nums2:
            if i not in nums1:
                tmp2.append(i)

        return [tmp1, tmp2]


nums1 = [1,2,3]
nums2 = [2,4,6]
execute = Solution()
print(execute.findDifference(nums1, nums2))

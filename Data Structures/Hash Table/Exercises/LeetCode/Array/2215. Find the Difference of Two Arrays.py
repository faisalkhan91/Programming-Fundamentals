"""
2215. Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findDifference(self, nums1, nums2):
        """
        In this solution, Hashset is used to store the values of the numbers in the arrays. The Hashsets are compared
        with each other and the unique values are stored into their respective temporary arrays. This resulting
        arrays contain the difference between the arrays and are returned as the output.
        :param nums1:
        :param nums2:
        :return: tmp1, tmp2
        """
        nums1 = set(nums1)  # Convert the num1 array to Hashset.
        nums2 = set(nums2)  # Convert to Hashset.
        tmp1 = []
        tmp2 = []

        # Find the difference in num1 set.
        for i in nums1:
            if i not in nums2:
                tmp1.append(i)

        # Find the difference in the num2 set.
        for i in nums2:
            if i not in nums1:
                tmp2.append(i)

        return [tmp1, tmp2]


nums1 = [1,2,3]
nums2 = [2,4,6]
execute = Solution()
print(execute.findDifference(nums1, nums2))

"""
2215. Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1_map = Counter(nums1)
        nums2_map = Counter(nums2)

        print(nums1_map, nums2_map)

        for i in range(len(nums1_map)):
            if nums1_map[i] in nums2_map:
                pass
            else:


"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 0
        second = 1
        triplet = 0

        while triplet < 2 and second < len(nums) - 1:
            print(nums[first], nums[second])
            if nums[first] < nums[second]:
                triplet += 1
                second += 1
                first += 1
            else:
                first += 1
                second = first + 1

        print(triplet)

        return True if triplet >= 2 else False


nums = [2,1,5,0,4,6]
execute = Solution()
print(execute.increasingTriplet())

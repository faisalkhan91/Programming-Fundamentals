"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        In this solution we use two pointers, one slow and one fast, the fast pointer iterates through the loop and when
        a non-zero number is encountered it is swapped with the slow pointer (i.e. 0), the slow pointer is incremented
        to keep track of the start of the 0's in the array.
        """

        slow = 0
        fast = 0
        length = len(nums)

        while fast < length:  # Keep searching until we reach the end of the array.
            if nums[fast] != 0:  # If we encounter a non-zero number, swap it with 0.
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1

        print(nums)


nums = [0,1,0,3,12]
execute = Solution()
execute.moveZeroes(nums)

"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            l = right - left
            current_area = l * h

            if max_area < current_area:
                max_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [2,3,4,5,18,17,6]
execute = Solution()
execute.maxArea(height)

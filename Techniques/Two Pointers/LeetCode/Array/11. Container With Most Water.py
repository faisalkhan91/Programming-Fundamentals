"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxArea(self, height) -> int:
        """
        In this solution, Two Pointer technique is used to track the heights of the container. We have a pointer on the
        left and a pointer on the right, they are initialized on the opposite sides. Over here, greedy algorithm method
        is utilized to calculate the area of the container. Right pointer is moved by default while left pointer is
        moved when the height on the left is less than the right. Each iteration stores the maximum height.

        Time Complexity: O(n), Space Complexity: O(1)

        :param height: List
        :return: max_area
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        # Check a long as left and right don't overlap.
        while left < right:
            h = min(height[left], height[right])
            l = right - left
            current_area = l * h

            # Store the current area if it is greater than previous max area.
            if max_area < current_area:
                max_area = current_area

            # If the left height is less than right height iterate from the left.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [2,3,4,5,18,17,6]
execute = Solution()
print(execute.maxArea(height))

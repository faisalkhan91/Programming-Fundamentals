"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        """
        In this solution pointers are used to iterate through the array. A left pointer is used to check if the left
        adjacent plot condition is met and similarly a right pointer to check if the right adjacent condition is met. If
        both the conditions are true we calculate the current plot as eligible plot. Once we have the number of eligible
        plots we compare it to the n given plots and return true if n is not greater than eligible plots.
        :param flowerbed:
        :param n:
        :return: Boolean
        """

        left, right = -1, 1  # Left and right pointer, left is left of the first element.
        plot = 0  # Current element.
        eligible_plots = 0  # Number of eligible plots.
        check_left, check_right = False, False  # Markers to check the left and right conditions.
        length = len(flowerbed)

        while right <= length:
            if flowerbed[plot] == 0:  # If the plot is empty.
                if left >= 0 and flowerbed[left] == 0:
                    check_left = True
                elif left == -1:  # If there is no left element.
                    check_left = True

                if right <= length - 1 and flowerbed[right] == 0:
                    check_right = True
                elif right > length - 1:  # if there is no right element.
                    check_right = True

                if check_left and check_right:  # If both left and right are True.
                    eligible_plots += 1
                    flowerbed[plot] = 1
            left += 1
            right += 1
            plot += 1
            check_left = False
            check_right = False

        return True if n <= eligible_plots else False


flowerbed = [0,0,1,0,1]
n = 1
execute = Solution()
print(execute.canPlaceFlowers(flowerbed, n))

############################################################################

# This solution fails with edge cases.
#
# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     eligible_empty = 0
#     for plot in range(len(flowerbed)):
#         if flowerbed[plot] == 0 and flowerbed[plot + 1] != 1:
#             if flowerbed[plot - 1] != 1:
#                 flowerbed[plot] = 1
#                 eligible_empty += 1
#
#     if n <= eligible_empty:
#         return True
#     return False

# This solution faces in the edge case [1,0,0,0,1,0,0], and has a lot of nested if statements.
#
# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     eligible_empty = 0
#
#     for plot in range(len(flowerbed)):
#         print("Plot: ", flowerbed[plot])
#         if flowerbed[plot] == 0 and flowerbed[plot + 1] == 0:
#             print("empty Plot: ", flowerbed[plot])
#             if flowerbed[plot - 1] == 0 or plot == 0:
#                 eligible_empty += 1
#                 flowerbed[plot] = 1
#
#     print(eligible_empty)
#     if n <= eligible_empty:
#         return True

# This solution looks too complicated.
#
# def is_eligible(self, p, bed):
#     if p == 0 and bed[p + 1] == 0:
#         return True
#     elif p == len(bed) - 1 and bed[p - 1] == 0:
#         return True
#     elif bed[p + 1] == 0 and bed[p - 1] == 0:
#         return True
#
#     return False
#
#
# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     if len(flowerbed) == 1 and flowerbed[0] == 0:
#         return True
#
#     eligible_plots = 0
#
#     for plot in range(len(flowerbed)):
#         if flowerbed[plot] == 0:
#             if self.is_eligible(plot, flowerbed):
#                 eligible_plots += 1
#                 flowerbed[plot] = 1
#
#     return True if n <= eligible_plots else False

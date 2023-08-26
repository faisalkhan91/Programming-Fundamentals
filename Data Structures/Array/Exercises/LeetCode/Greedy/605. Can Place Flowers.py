"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        eligible_empty = 0
        for plot in range(len(flowerbed)):
            if flowerbed[plot] == 0 and flowerbed[plot + 1] != 1:
                if flowerbed[plot - 1] != 1:
                    flowerbed[plot] = 1
                    eligible_empty += 1

        if n <= eligible_empty:
            return True
        return False


flowerbed = [0,0,1,0,1]
n = 1
execute = Solution()
print(execute.canPlaceFlowers(flowerbed, n))

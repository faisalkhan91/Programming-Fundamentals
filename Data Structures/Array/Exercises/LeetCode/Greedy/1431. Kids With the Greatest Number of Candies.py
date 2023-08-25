"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):

        current_max = max(candies)  # Find the current max of the amount of candies each kid has.
        result = []

        for i in range(len(candies)):
            # Greedy algorithm to check if given extraCandies results in candies greater than current_max.
            if candies[i] + extraCandies >= current_max:
                result.append(True)
            else:
                result.append(False)

        return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3
execute = Solution()
print(execute.kidsWithCandies(candies, extraCandies))

"""
1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def largestAltitude(self, gain) -> int:
        """
        This solution uses prefix sum technique, i.e. the altitude is calculated using the formula:
        gain[i + 1] = gain[i + 1] + gain[i]
        This gives the resulting peak altitude at each point, and the max altitude is returned from the list.
        :param gain
        :return: Maximum value of the calculated altitudes.
        """
        gain.insert(0, 0)
        for i in range(len(gain) - 1):
            gain[i + 1] = gain[i + 1] + gain[i]
        return max(gain)

    def largestAltitude_simple(self, gain) -> int:
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
        return max(max(gain), 0)

    def largestAltitude_sort(self, gain) -> int:
        """
        Same as above, just sorting technique is used instead of max.
        :param gain:
        :return:
        """
        gain.insert(0, 0)
        for i in range(len(gain) - 1):
            gain[i + 1] = gain[i + 1] + gain[i]
        gain.sort(reverse=True)
        return gain[0]


gain = [-5,1,5,0,-7]
execute = Solution()
print(execute.largestAltitude(gain))

"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This is using recursion but won't succeed as for higher numbers it exceeds memory limit.
        :param n:
        :return:
        """
        ways_to_climb = set()
        steps = []
        m = 0

        def routes(n, m):
            if m > n:
                ways_to_climb.add(tuple(steps))
                return ways_to_climb

            steps.append(m)
            routes(n, m + 1)
            routes(n, m + 2)

        routes(n, m)
        return len(ways_to_climb)

    class Solution:
        def climbStairs_bottom_up(self, n: int) -> int:
            """
            This is using bottom_up approach, and we build up to the n number by calculating the difference of 1 step
            and 2 step with respect to the previous steps. Time Complexity is O(n) and Space Complexity is O(n).
            :param n:
            :return:
            """
            if n <= 2:
                return n

            ways_to_climb = [0] * (n + 1)
            ways_to_climb[1] = 1
            ways_to_climb[2] = 2

            for i in range(3, n + 1):
                ways_to_climb[i] = ways_to_climb[i - 1] + ways_to_climb[i - 2]

            return ways_to_climb[n]

    def climbStairs_bottom_up_optimized(self, n: int) -> int:
        """
        This is optimized version of the bottom up approach, i.e. non-recursive approach as we are building the ways
        from the start that is 0. In this version we are keeping only track of 2 steps below, and we don't need to store
        the 3rd step below as that is not needed. Time Complexity is O(n) and Space Complexity is O(1) since there are
        only three variables to track of.
        :param n:
        :return:
        """
        if n <= 2:
            return n

        ways_to_climb = 0
        two_below = 1
        one_below = 2

        for i in range(3, n + 1):
            ways_to_climb = one_below + two_below
            two_below = one_below
            one_below = ways_to_climb

        return ways_to_climb


n = 25
execute = Solution()
print(execute.climbStairs(n))
